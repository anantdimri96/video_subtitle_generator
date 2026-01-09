"""
Audio extraction and processing utilities.
"""
from moviepy import VideoFileClip
from pathlib import Path


class AudioProcessor:
    """Handles audio extraction from video files."""
    
    @staticmethod
    def extract_audio(video_path: str, output_audio_path: str) -> None:
        """
        Extract audio from video using MoviePy.
        
        Args:
            video_path: Path to the input video file
            output_audio_path: Path where the extracted audio will be saved
            
        Raises:
            ValueError: If the video has no audio track
        """
        video = VideoFileClip(video_path)
        
        try:
            if video.audio is None:
                raise ValueError("Uploaded video has no audio track")
            
            video.audio.write_audiofile(output_audio_path)
        finally:
            video.close()
