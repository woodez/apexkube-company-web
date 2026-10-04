"""Inline SVG line icons (24x24, stroke-based) used throughout the templates."""

from markupsafe import Markup

PATHS = {
    "server": '<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01M11 7.5h6M11 16.5h6"/>',
    "cloud": '<path d="M7 18.5a4.5 4.5 0 0 1-.6-8.96A6 6 0 0 1 18 10a4.25 4.25 0 0 1-.5 8.5Z"/>',
    "bot": '<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 4.5V8M9 13.5h.01M15 13.5h.01M9.5 17h5"/><circle cx="12" cy="3.5" r="1"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5Z"/>',
    "headset": '<path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="14" width="4" height="6" rx="1.5"/><rect x="17" y="14" width="4" height="6" rx="1.5"/>',
    "file-search": '<path d="M13 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h5M13 3l6 6v2M13 3v6h6"/><circle cx="16.5" cy="16.5" r="3"/><path d="m18.7 18.7 2.3 2.3"/>',
    "workflow": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/><path d="M10 6.5h4.5a3 3 0 0 1 3 3V14"/>',
    "trending": '<path d="m3 17 6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
    "book": '<path d="M5 19.5V5a2 2 0 0 1 2-2h12v14H7a2 2 0 0 0-2 2.5Zm0 0A2 2 0 0 0 7 21h12v-4"/>',
    "chart": '<path d="M4 20h16M7 16v-5M12 16V6M17 16v-8"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "arrow-right": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6Z"/><path d="m9 12 2 2 4-4"/>',
    "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6.3 6.3l2.5 2.5M15.2 15.2l2.5 2.5M6.3 17.7l2.5-2.5M15.2 8.8l2.5-2.5"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    "shuffle": '<path d="M4 7h13M14 4l3 3-3 3M20 17H7M10 14l-3 3 3 3"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="m11 12 9-9M16.5 6.5l3 3"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
    "pencil": '<path d="M4 20h4L19 9a2.8 2.8 0 0 0-4-4L4 16Z"/><path d="m13.5 6.5 4 4"/>',
    "code": '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
}


def icon(name: str, cls: str = "") -> Markup:
    """Return an inline SVG icon; decorative, so hidden from screen readers."""
    classes = f"icon icon-{name} {cls}".strip()
    return Markup(
        f'<svg class="{classes}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" '
        f'aria-hidden="true" focusable="false">{PATHS[name]}</svg>'
    )
