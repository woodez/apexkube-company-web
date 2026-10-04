"""Render the ApexKube cube logo to a PNG for the iPhone home-screen icon.

iOS does not accept SVG apple-touch-icons, so we rasterise the logo's
polygons in pure Python (no image libraries needed).
"""

import struct
import zlib

# Logo geometry in the 64x64 coordinate space of static/img/logo.svg,
# in painting order: (points, RGB colour).
LOGO_POLYGONS = [
    ([(10, 26), (32, 38), (32, 62), (10, 50)], (37, 99, 235)),   # cube, left face
    ([(32, 38), (54, 26), (54, 50), (32, 62)], (91, 33, 182)),   # cube, right face
    ([(32, 2), (10, 26), (32, 38)], (103, 232, 249)),            # apex, left face
    ([(32, 2), (32, 38), (54, 26)], (8, 145, 178)),              # apex, right face
]

BG_TOP = (11, 26, 54)
BG_BOTTOM = (5, 10, 22)
GLOW = (34, 211, 238)


def _inside(x: float, y: float, pts: list[tuple[float, float]]) -> bool:
    hit = False
    j = len(pts) - 1
    for i, (xi, yi) in enumerate(pts):
        xj, yj = pts[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            hit = not hit
        j = i
    return hit


def _mix(a, b, t):
    return tuple(a[k] + (b[k] - a[k]) * t for k in range(3))


def render_png(size: int = 180, samples: int = 3) -> bytes:
    # Fit the logo's content box (x 10..54, y 2..62) to ~66% of the icon height.
    scale = size * 0.66 / 60
    off_x = (size - 44 * scale) / 2 - 10 * scale
    off_y = (size - 60 * scale) / 2 - 2 * scale
    polys = [
        ([(off_x + x * scale, off_y + y * scale) for x, y in pts], colour)
        for pts, colour in LOGO_POLYGONS
    ]
    centre = size / 2

    rows = []
    for py in range(size):
        background = _mix(BG_TOP, BG_BOTTOM, py / size)
        row = bytearray()
        for px in range(size):
            dist = ((px - centre) ** 2 + (py - centre) ** 2) ** 0.5
            bg = _mix(background, GLOW, max(0.0, 1 - dist / (size * 0.6)) * 0.28)
            acc = [0.0, 0.0, 0.0]
            for sy in range(samples):
                for sx in range(samples):
                    x = px + (sx + 0.5) / samples
                    y = py + (sy + 0.5) / samples
                    colour = bg
                    for pts, fill in polys:
                        if _inside(x, y, pts):
                            colour = fill
                    for k in range(3):
                        acc[k] += colour[k]
            n = samples * samples
            row.extend(round(c / n) for c in acc)
        rows.append(row)

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    raw = b"".join(b"\x00" + bytes(row) for row in rows)
    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )
