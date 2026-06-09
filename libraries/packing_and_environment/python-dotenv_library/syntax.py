from dotenv import load_dotenv
import os

def main() -> None:
    load_dotenv()
    print(os.getenv("TEST_VAR", 8080))
    print(os.getenv("PORT", 8080))

if __name__ == "__main__":
    main()
