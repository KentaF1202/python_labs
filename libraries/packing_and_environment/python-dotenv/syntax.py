# /// script
# dependencies = [
#   "python-dotenv",
# ]
# ///

from dotenv import load_dotenv
import os

if __name__ == "__main__":
    # Loading environment variables from a .env file
    load_dotenv()
    print("Environment variables loaded from .env file.")
    print()
