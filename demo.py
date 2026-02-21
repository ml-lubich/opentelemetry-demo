"""
Demo workflow: create parent and child spans with attributes.
Single responsibility: run the demo trace workflow.
"""
import time
from tracer_setup import get_tracer


def run_demo() -> None:
    """Run a short demo with a parent span and a nested child span."""
    tracer = get_tracer("opentelemetry-demo")
    with tracer.start_as_current_span("parent") as parent_span:
        parent_span.set_attribute("demo.step", "parent")
        time.sleep(0.1)
        with tracer.start_as_current_span("child") as child_span:
            child_span.set_attribute("demo.step", "child")
            time.sleep(0.05)
        time.sleep(0.05)
