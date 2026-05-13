# OpenTelemetry Python Demo

> Minimal OpenTelemetry (traces) demo in Python: one parent span, one
> child span, console export.

```mermaid
flowchart LR
    MAIN["🚀 main.py"]
    INIT{{"🛠 init_tracer()<br/><i>tracer_setup.py</i>"}}
    DEMO["🧪 demo.py<br/>parent + child spans"]
    PROV["🧠 TracerProvider"]
    EXP["📤 ConsoleSpanExporter<br/>(BatchSpanProcessor)"]
    OUT[/"🖥 console output"/]

    MAIN --> INIT --> PROV
    MAIN --> DEMO
    DEMO -- "spans" --> PROV
    PROV --> EXP --> OUT

    classDef io fill:#0e1116,stroke:#2f81f7,stroke-width:1.5px,color:#e6edf3;
    classDef tool fill:#161b22,stroke:#3fb950,stroke-width:1.5px,color:#e6edf3;
    classDef brain fill:#161b22,stroke:#d29922,stroke-width:1.5px,color:#e6edf3;
    classDef out fill:#0e1116,stroke:#a371f7,stroke-width:1.5px,color:#e6edf3;
    class MAIN io;
    class DEMO,EXP tool;
    class INIT,PROV brain;
    class OUT out;
```

## Table of contents

- [Setup](#setup)
- [Run](#run)
- [Layout](#layout)
- [Author](#author)

## Setup

1. Create and activate a virtual environment (recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run

From the repo root:

```bash
python main.py
```

Spans are printed to the console (BatchSpanProcessor + ConsoleSpanExporter).

## Layout

- `tracer_setup.py` – TracerProvider, console exporter, `init_tracer()` / `get_tracer()`
- `demo.py` – Demo workflow (parent/child spans and attributes)
- `main.py` – Entrypoint: init tracer, run demo

## Author

Misha Lubich, michaelle.lubich@gmail.com  
GitHub: https://github.com/ml-lubich
