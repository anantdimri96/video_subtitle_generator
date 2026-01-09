"""
Video processing and caption burning utilities.
"""
import subprocess
import shutil
from pathlib import Path


class VideoProcessor:
    """Handles video processing and caption burning."""
    
    def __init__(self, ffmpeg_path: str):
        """
        Initialize the video processor.
        
        Args:
            ffmpeg_path: Path to the ffmpeg executable or "ffmpeg" to use system PATH
            
        Raises:
            FileNotFoundError: If ffmpeg cannot be found
        """
        self.ffmpeg_path = ffmpeg_path
        
        # If it's "ffmpeg", check if it's available in system PATH
        if ffmpeg_path == "ffmpeg":
            ffmpeg_in_path = shutil.which("ffmpeg")
            if ffmpeg_in_path:
                self.ffmpeg_path = ffmpeg_in_path
            else:
                raise FileNotFoundError(
                    "FFmpeg not found in system PATH. "
                    "Please install FFmpeg or ensure it's available in your environment. "
                    "On Streamlit Cloud, imageio-ffmpeg should provide FFmpeg automatically."
                )
        else:
            # Check if the specified path exists
            path = Path(ffmpeg_path)
            if not path.exists():
                # Try to find ffmpeg in system PATH as fallback
                ffmpeg_in_path = shutil.which("ffmpeg")
                if ffmpeg_in_path:
                    self.ffmpeg_path = ffmpeg_in_path
                else:
                    raise FileNotFoundError(
                        f"FFmpeg not found at {ffmpeg_path} and not in system PATH. "
                        "Please install FFmpeg or set the correct path."
                    )
    
    def burn_captions(
        self,
        video_path: str,
        srt_path: str,
        output_path: str,
        video_codec: str = "libx264",
        audio_codec: str = "aac",
        mov_flags: str = "+faststart"
    ) -> None:
        """
        Burn subtitles into video using ffmpeg.
        
        Args:
            video_path: Path to the input video file
            srt_path: Path to the SRT subtitle file
            output_path: Path where the output video will be saved
            video_codec: Video codec to use
            audio_codec: Audio codec to use
            mov_flags: MOV flags for browser compatibility
            
        Raises:
            subprocess.CalledProcessError: If ffmpeg command fails
        """
        command = [
            self.ffmpeg_path,
            "-y",  # Overwrite output file if it exists
            "-i", video_path,
            "-vf", f"subtitles={srt_path}",
            "-c:v", video_codec,
            "-c:a", audio_codec,
            "-movflags", mov_flags,
            output_path
        ]
        
        subprocess.run(command, check=True, capture_output=True)
