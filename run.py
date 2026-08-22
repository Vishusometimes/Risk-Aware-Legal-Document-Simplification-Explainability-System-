import sys
sys.path.append("src")

from src.pipeline import process_document
from src.risk_model import train_model


if __name__ == "__main__":

    # Train model
    train_model()

    # Test input
    text = """
    You must not share your password.
    We may update the policy anytime.
    This app is free to use.
    """

    results = process_document(text)

    for r in results:
        print("\n----------------------")
        print("Original:", r["original"])
        print("Risk:", r["risk"])
        print("Simplified:", r["simplified"])
        print("RPS:", r["rps"])
        print("Explanation:", r["explanation"])