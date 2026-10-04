"""Build the site and serve dist/ on your local network for preview.

Usage (with the venv active):
    python serve.py [port]

Open the printed network URL on an iPhone connected to the same Wi-Fi.
"""

import functools
import http.server
import socket
import sys

from build import DIST, build


def lan_ip() -> str:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No packets are sent; this just picks the outbound interface.
        sock.connect(("10.255.255.255", 1))
        return sock.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        sock.close()


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    build()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIST)
    with http.server.ThreadingHTTPServer(("0.0.0.0", port), handler) as server:
        print(f"\nLocal:   http://localhost:{port}")
        print(f"Network: http://{lan_ip()}:{port}   <- open this on your iPhone")
        print("Ctrl+C to stop.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
