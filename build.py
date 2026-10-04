"""Build the ApexKube static site into dist/.

Usage (with the venv active):
    python build.py
"""

import shutil
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape

from content import site
from content.icons import icon
from content.touch_icon import render_png

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
STATIC = ROOT / "static"
DIST = ROOT / "dist"

PAGES = [
    {
        "template": "index.html",
        "active": "home",
        "title": None,
        "description": site.SITE["description"],
        "cta": True,
    },
    {
        "template": "services.html",
        "active": "services",
        "title": "Services",
        "description": "Private open-source LLMs, hosted LLM integration, agent harnesses and AI strategy for SMEs.",
        "cta": True,
    },
    {
        "template": "solutions.html",
        "active": "solutions",
        "title": "Solutions",
        "description": "Real-world AI use cases for small and medium-sized businesses — support, documents, back office, sales and more.",
        "cta": True,
    },
    {
        "template": "about.html",
        "active": "about",
        "title": "About & Contact",
        "description": "Who ApexKube is, how we work, and how to start a conversation about AI for your business.",
        "cta": False,
    },
]


def build() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(STATIC, DIST)
    (DIST / "img" / "apple-touch-icon.png").write_bytes(render_png(180))

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["icon"] = icon
    context = {name: getattr(site, name) for name in dir(site) if name.isupper()}
    context["year"] = date.today().year

    for page in PAGES:
        html = env.get_template(page["template"]).render(**context, page=page)
        (DIST / page["template"]).write_text(html, encoding="utf-8")
        print(f"built {page['template']}")
    print(f"done -> {DIST}")


if __name__ == "__main__":
    build()
