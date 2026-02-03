from openinference.instrumentation.agno import AgnoInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor
from phoenix.otel import register


def setup_observability():
    """
    Sets up OpenTelemetry tracing and exports traces to a local Arize Phoenix server.
    """
    # Register the Phoenix exporter
    # This acts as the OTLP exporter to send traces to the Phoenix server (default: http://localhost:6006)
    register()

    # Instrument Agno
    AgnoInstrumentor().instrument()

    # Instrument OpenAI (optional, but recommended if using OpenAI models)
    OpenAIInstrumentor().instrument()
