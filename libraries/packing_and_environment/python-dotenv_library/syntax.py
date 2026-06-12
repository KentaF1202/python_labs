from dotenv import load_dotenv
import os

# # load_dotenv():
# Not override existing environment variables (override=False).
# Pass override=True to override existing variables.

# # To configure the development environment, add a `.env` in the root directory of
# your project:
# ```
# .
# ├── .env
# └── foo.py
# ```
# Look for a .env file in the same directory as the Python script (or higher up the directory tree).
# Read each key-value pair and add it to os.environ.


# # dotenv_values()
# ```python
# import os
# from dotenv import dotenv_values

# config = {
#     **dotenv_values(".env.shared"),  # load shared development variables
#     **dotenv_values(".env.secret"),  # load sensitive variables
#     **os.environ,  # override loaded values with environment variables
# }
# ```

# import os
# from io import StringIO
# from dotenv import load_dotenv

# def test_database_connection_fallback():
#     # Force a test configuration entirely in memory
#     test_env = StringIO("DATABASE_URL=sqlite:///:memory:\nDEBUG=True")
#     load_dotenv(stream=test_env, override=True)
    
#     assert os.environ.get("DEBUG") == "True"

def main() -> None:
    load_dotenv()
    print(os.getenv("TEST_VAR", 8080))
    print(os.getenv("PORT", 8080))

if __name__ == "__main__":
    main()
