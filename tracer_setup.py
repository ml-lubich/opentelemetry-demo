"""
OpenTelemetry tracer setup: provider, console exporter, and tracer access.
Single responsibility: configure and expose the global tracer.
"""
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import Resource


def init_tracer(service_name: str = "opentelemetry-demo") -> None:
    """Initialize the global TracerProvider with console export."""
    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(provider)


def get_tracer(name: str, version: str = "0.1.0"):
    """Return a tracer for the given name and version."""
    return trace.get_tracer(name, version)
