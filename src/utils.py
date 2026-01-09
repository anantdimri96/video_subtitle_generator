"""
General utility functions.
"""
import tempfile
from pathlib import Path


def save_uploaded_file(uploaded_file, suffix: str = ".mp4") -> str:
    """
    Save an uploaded file (e.g., from Streamlit) to a temporary file.
    
    Args:
        uploaded_file: File-like object from Streamlit file uploader
        suffix: File extension suffix (e.g., ".mp4", ".wav")
        
    Returns:
        Path to the saved temporary file
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getbuffer())
        return tmp.name


def ensure_directory(path: Path) -> None:
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        path: Path to the directory
    """
    path.mkdir(parents=True, exist_ok=True)
