import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Network Diagnostics API")
    parser.add_argument(
        "--host",
        help="Host to bind to",
        default="127.0.0.1",
    )
    parser.add_argument(
        "--port",
        help="Port to bind to",
        type=int,
        default=8000,
    )
    parser.add_argument(
        "--log-level",
        help="Log level",
        default="info",
    )
    return parser.parse_args()
