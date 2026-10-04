"""Site copy and structured content.

Edit text here rather than in the HTML templates. Every UPPERCASE name in this
module is passed to the templates by build.py.
"""

SITE = {
    "name": "ApexKube",
    "domain": "www.apexkube.xyz",
    "url": "https://www.apexkube.xyz",
    "email": "hello@apexkube.xyz",
    "tagline": "AI enablement for growing businesses",
    "description": (
        "ApexKube helps small and medium-sized businesses put AI to work — "
        "private open-source LLMs, hosted models, and agents that plug into "
        "the tools you already use."
    ),
}

NAV = [
    {"key": "home", "label": "Home", "href": "index.html"},
    {"key": "services", "label": "Services", "href": "services.html"},
    {"key": "solutions", "label": "Solutions", "href": "solutions.html"},
    {"key": "about", "label": "About", "href": "about.html"},
]

HERO_POINTS = [
    "Local or hosted LLMs",
    "Your data, your control",
    "Agents that take action",
    "No vendor lock-in",
]

SERVICES = [
    {
        "id": "local-llm",
        "icon": "server",
        "title": "Private, local LLMs",
        "summary": (
            "Run open-source models such as Llama, Mistral, Qwen and Gemma on "
            "your own hardware or private cloud. Your data never leaves your "
            "control."
        ),
        "points": [
            "Model selection and benchmarking against your real workload",
            "Hardware sizing — from a single GPU workstation to an on-prem server",
            "Secure deployment with Ollama, vLLM or llama.cpp",
            "Retrieval (RAG) over your own documents and data",
            "Ongoing model updates and quality evaluations",
        ],
        "best_for": "Sensitive or regulated data, predictable costs, offline sites.",
    },
    {
        "id": "hosted-llm",
        "icon": "cloud",
        "title": "Hosted LLM integration",
        "summary": (
            "Tap into frontier models from leading providers through secure, "
            "governed integrations — with no infrastructure to manage."
        ),
        "points": [
            "Provider selection and cost modelling",
            "Secure gateway with key management and usage limits",
            "Prompt design, guardrails and automated evaluation",
            "Data-handling settings aligned to your compliance needs",
            "Hybrid routing: hosted for heavy reasoning, local for sensitive data",
        ],
        "best_for": "Fast time-to-value, top-tier reasoning, variable workloads.",
    },
    {
        "id": "agents",
        "icon": "bot",
        "title": "Agents & agent harnesses",
        "summary": (
            "We wrap your existing applications in an agent layer, so an LLM can "
            "read, reason and take action inside the tools you already use."
        ),
        "points": [
            "Custom connectors for your CRM, ERP, inbox, databases and APIs",
            "A harness with permissions, approvals and full audit logs",
            "Human-in-the-loop checkpoints for high-impact actions",
            "Model-agnostic — swap local or hosted LLMs without a rebuild",
            "Monitoring, tracing and continuous improvement",
        ],
        "best_for": "Repetitive, multi-step work that spans several systems.",
    },
    {
        "id": "enablement",
        "icon": "compass",
        "title": "AI strategy & enablement",
        "summary": (
            "Practical guidance and hands-on training, so your team knows where "
            "AI pays off and how to use it safely."
        ),
        "points": [
            "AI readiness assessment and opportunity mapping",
            "A roadmap ranked by return on investment",
            "Staff workshops and prompt playbooks",
            "AI usage policy and governance",
        ],
        "best_for": "Teams getting started, or scaling beyond experiments.",
    },
]

HARNESS_LAYERS = [
    {
        "icon": "workflow",
        "title": "Your business apps",
        "text": "The systems you already run stay exactly where they are.",
        "chips": ["CRM", "ERP", "Email", "Databases", "Documents", "APIs"],
    },
    {
        "icon": "shield",
        "title": "ApexKube agent harness",
        "text": "The control layer that lets AI act safely on your behalf.",
        "chips": ["Tool connectors", "Permissions", "Human approval", "Audit log", "Monitoring"],
        "core": True,
    },
    {
        "icon": "spark",
        "title": "The LLM — your choice",
        "text": "Plug in the model that fits your privacy, cost and quality needs.",
        "chips": ["Local open-source", "Hosted frontier", "Hybrid routing"],
    },
]

PROCESS = [
    {
        "icon": "search",
        "title": "Discover",
        "text": "We map your workflows, data and goals to find where AI will deliver the most value.",
    },
    {
        "icon": "pencil",
        "title": "Design",
        "text": "We choose the right model and architecture — local, hosted or hybrid — and agree success measures.",
    },
    {
        "icon": "code",
        "title": "Build & pilot",
        "text": "We build a working pilot on your real data, test it with your team and refine it.",
    },
    {
        "icon": "trending",
        "title": "Scale & support",
        "text": "We roll out, train your people and keep improving — with monitoring you can see.",
    },
]

COMPARISON = [
    ("Data privacy", "Stays on your infrastructure", "Governed by provider terms"),
    ("Upfront cost", "Hardware investment", "None — pay as you go"),
    ("Running cost", "Predictable and fixed", "Scales with usage"),
    ("Model capability", "Strong and improving fast", "Frontier-level reasoning"),
    ("Setup time", "Days to weeks", "Hours to days"),
    ("Works offline", "Yes", "No"),
]

FAQS = [
    {
        "q": "Do I need expensive hardware to run a local LLM?",
        "a": (
            "Not always. Many business tasks run well on a single modern GPU "
            "workstation. We size hardware to your workload, and we'll tell you "
            "when a hosted model is the better deal."
        ),
    },
    {
        "q": "Will my data be used to train someone else's model?",
        "a": (
            "With local models, your data never leaves your environment. With "
            "hosted models, we configure business-grade plans and settings that "
            "keep your data out of provider training, and we document exactly "
            "where it flows."
        ),
    },
    {
        "q": "Can an agent take actions without anyone checking?",
        "a": (
            "Only if you want it to. Our harness lets you decide which actions "
            "run automatically and which need a person to approve — and every "
            "action is logged."
        ),
    },
    {
        "q": "We're not technical. Can we still do this?",
        "a": (
            "Yes. That's who we built ApexKube for. We handle the engineering, "
            "train your team in plain language and hand over documentation so "
            "you're never dependent on us."
        ),
    },
]

SOLUTIONS = [
    {
        "icon": "headset",
        "tag": "Retail & e-commerce",
        "title": "Customer support agent",
        "problem": "Staff spend hours answering the same order, delivery and returns questions.",
        "solution": (
            "An agent connected to your order system and help articles answers "
            "customers around the clock, and hands complex cases to a person "
            "with the full context."
        ),
        "outcome": "Faster replies for customers, and more time for your team's harder cases.",
    },
    {
        "icon": "file-search",
        "tag": "Professional services",
        "title": "Private document Q&A",
        "problem": "Answers are buried in contracts, policies and manuals that nobody has time to search.",
        "solution": (
            "A local LLM with retrieval over your files answers questions in plain "
            "English and cites the exact source — without documents leaving your "
            "network."
        ),
        "outcome": "Answers in seconds, with sensitive files kept in-house.",
    },
    {
        "icon": "workflow",
        "tag": "Finance & admin",
        "title": "Back-office automation",
        "problem": "Invoices, purchase orders and data entry eat into every week.",
        "solution": (
            "An agent reads incoming documents, extracts and checks the details, "
            "posts them to your accounting system and flags exceptions for "
            "approval."
        ),
        "outcome": "Less manual keying, fewer errors and a clear audit trail.",
    },
    {
        "icon": "trending",
        "tag": "B2B sales",
        "title": "Sales & CRM assistant",
        "problem": "Follow-ups slip and the CRM is always out of date.",
        "solution": (
            "An assistant drafts follow-up emails, updates CRM records from "
            "meeting notes and prepares account briefings before every call."
        ),
        "outcome": "A cleaner pipeline, and reps who spend more time selling.",
    },
    {
        "icon": "book",
        "tag": "Any team",
        "title": "Internal knowledge assistant",
        "problem": "The same HR, IT and process questions interrupt people all day.",
        "solution": (
            "A chat assistant in Slack or Teams answers from your wiki and "
            "handbooks, and knows when to route a question to a human."
        ),
        "outcome": "Fewer interruptions, and faster onboarding for new starters.",
    },
    {
        "icon": "chart",
        "tag": "Operations",
        "title": "Reporting & insights",
        "problem": "Getting a simple answer from your data means waiting on a spreadsheet expert.",
        "solution": (
            "Ask questions of your data in plain English. The agent queries your "
            "systems, builds the summary and delivers weekly reports "
            "automatically."
        ),
        "outcome": "Decisions based on current numbers, not last month's.",
    },
]

VALUES = [
    {
        "icon": "target",
        "title": "Practical first",
        "text": "We start with a business problem, not a technology. If AI isn't the answer, we'll say so.",
    },
    {
        "icon": "shield",
        "title": "Private by design",
        "text": "Your data is treated as yours. We design for least access, clear data flows and full audit trails.",
    },
    {
        "icon": "shuffle",
        "title": "Vendor-neutral",
        "text": "Open-source or hosted, we recommend what fits your needs — never what locks you in.",
    },
    {
        "icon": "key",
        "title": "Built to be owned",
        "text": "Documentation, training and handover come as standard, so your team stays in control.",
    },
]
