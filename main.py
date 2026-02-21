"""
Entrypoint: initialize tracing and run the demo.
"""
from tracer_setup import init_tracer
from demo import run_demo


def main() -> None:
    init_tracer()
    run_demo()


if __name__ == "__main__":
    main()
