"""
Configuration settings for the subtitle generator application.
"""
import os
import shutil
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio"
SRT_DIR = BASE_DIR / "srt"
VIDEOS_DIR = BASE_DIR / "videos"

# File paths
AUDIO_OUTPUT_PATH = AUDIO_DIR / "processed_audio.wav"
SRT_OUTPUT_PATH = SRT_DIR / "output.srt"
VIDEO_OUTPUT_PATH = VIDEOS_DIR / "captioned_video.mp4"


def find_ffmpeg_path() -> str:
    """
    Find FFmpeg executable path.
    Tries: environment variable -> system PATH -> imageio-ffmpeg -> default local path.
    
    Returns:
        Path to ffmpeg executable
    """
    # Check environment variable first
    env_path = os.getenv("FFMPEG_PATH")
    if env_path and Path(env_path).exists():
        return env_path
    
    # Check if ffmpeg is in system PATH
    ffmpeg_in_path = shutil.which("ffmpeg")
    if ffmpeg_in_path:
        return ffmpeg_in_path
    
    # Try imageio-ffmpeg (works on Streamlit Cloud and provides bundled ffmpeg)
    try:
        import imageio_ffmpeg
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        if ffmpeg_exe and Path(ffmpeg_exe).exists():
            return ffmpeg_exe
    except (ImportError, Exception):
        pass
    
    # If nothing found, return "ffmpeg" and let subprocess handle it
    # This will work if ffmpeg is in system PATH
    return "ffmpeg"


# FFmpeg configuration
FFMPEG_PATH = find_ffmpeg_path()

# Whisper model configuration
WHISPER_MODEL = "base"

# Video processing settings
VIDEO_CODEC = "libx264"
AUDIO_CODEC = "aac"
MOV_FLAGS = "+faststart"

# Supported video formats
SUPPORTED_VIDEO_FORMATS = ["mp4", "mov", "avi", "mkv"]


def ensure_directories():
    """Create necessary directories if they don't exist."""
    AUDIO_DIR.mkdir(exist_ok=True)
    SRT_DIR.mkdir(exist_ok=True)
    VIDEOS_DIR.mkdir(exist_ok=True)
