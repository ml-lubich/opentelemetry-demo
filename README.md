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
- [Trace flow (sequence)](#trace-flow-sequence)
- [Span lifecycle (state)](#span-lifecycle-state)
- [Run](#run)
- [Layout](#layout)
- [Author](#author)
- [🗺️ Repository map](#️-repository-map)

## Span lifecycle (state)

```mermaid
stateDiagram-v2
    [*] --> CREATED: tracer.start_as_current_span
    CREATED --> ACTIVE: enter context
    ACTIVE --> ATTRIBUTED: span.set_attribute
    ACTIVE --> CHILD_STARTED: nested start_as_current_span
    CHILD_STARTED --> CHILD_ENDED: child .end()
    CHILD_ENDED --> ACTIVE
    ATTRIBUTED --> ACTIVE
    ACTIVE --> ENDED: span.end()
    ENDED --> QUEUED: BatchSpanProcessor.on_end
    QUEUED --> EXPORTED: ConsoleSpanExporter.export
    EXPORTED --> [*]
```

## Trace flow (sequence)

```mermaid
sequenceDiagram
    participant M as main.py
    participant T as tracer_setup
    participant P as TracerProvider
    participant D as demo.py
    participant B as BatchSpanProcessor
    participant E as ConsoleSpanExporter

    M->>T: init_tracer()
    T->>P: register provider + processor
    P->>B: attach BatchSpanProcessor(E)
    M->>D: run demo workflow
    D->>P: start parent span
    D->>P: start child span (attrs)
    D->>P: end child span
    D->>P: end parent span
    P->>B: queue finished spans
    B->>E: export(batch)
    E-->>M: stdout JSON spans
```

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


## 🗺️ Repository map

Top-level layout of `opentelemetry-demo` rendered as a Mermaid mindmap (auto-generated from the on-disk tree).

```mermaid
mindmap
  root((opentelemetry-demo))
    files
      README.md
      main.py
      requirements.txt
```
