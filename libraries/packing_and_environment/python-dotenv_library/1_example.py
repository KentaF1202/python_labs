import os
import pytest
from io import StringIO
from dotenv import load_dotenv

# Service to be tested
def initialize_service():
    """Simulates initializing a connection using environment variables."""
    api_key = os.environ.get("API_KEY")
    env_state = os.environ.get("ENVIRONMENT", "development")
    
    if not api_key:
        raise ValueError("CRITICAL: API_KEY is missing from the environment!")
        
    return f"Service started in [{env_state}] mode with key: {api_key[:4]}..."


@pytest.fixture
def mock_env():
    """
    Fixture to stream a fake .env file into memory for a single test,
    and cleanly wipe it out after the test finishes.
    """
    # 1. Take a snapshot of the environment BEFORE the test runs
    old_env = dict(os.environ)
    
    # 2. Define our mock environment configuration stream
    mock_dotenv_content = (
        "API_KEY=mocked_secret_test_token_12345\n"
        "ENVIRONMENT=testing\n"
        "DATABASE_URL=sqlite:///:memory:"
    )
    stream = StringIO(mock_dotenv_content)
    
    # 3. Stream it straight into os.environ (forcing override)
    load_dotenv(stream=stream, override=True)
    
    # Yield control to the actual test function
    yield 
    
    # 4. TEARDOWN: Wipe the changes and restore the OS memory state exactly as it was
    os.environ.clear()
    os.environ.update(old_env)


def test_initialize_service_with_mock_stream(mock_env):
    """Test that our application correctly reads the streamed configuration."""
    # Act: Run the application logic
    result = initialize_service()
    
    # Assert: Verify it bound correctly to our streamed variables
    assert os.environ.get("ENVIRONMENT") == "testing"
    assert "mocked_secret_test_token_12345" in os.environ.get("API_KEY")
    assert "started in [testing] mode" in result


def test_initialize_service_missing_token(mock_env):
    """Test that our system safely errors out if a key is missing from the stream."""
    # Modify the stream state by manually knocking out the key for this isolated run
    if "API_KEY" in os.environ:
        del os.environ["API_KEY"]
        
    # Assert that the app throws the correct ValueError
    with pytest.raises(ValueError, match="CRITICAL: API_KEY is missing"):
        initialize_service()