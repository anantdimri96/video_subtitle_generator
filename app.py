"""
Streamlit application for generating subtitles from video files.
"""
import streamlit as st

MAX_FILE_SIZE_MB = 20
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

from config import (
    ensure_directories,
    AUDIO_OUTPUT_PATH,
    SRT_OUTPUT_PATH,
    VIDEO_OUTPUT_PATH,
    FFMPEG_PATH,
    WHISPER_MODEL,
    SUPPORTED_VIDEO_FORMATS,
    VIDEO_CODEC,
    AUDIO_CODEC,
    MOV_FLAGS,
)
from src.audio_processor import AudioProcessor
from src.transcription import TranscriptionService
from src.video_processor import VideoProcessor
from src.utils import save_uploaded_file


def main():
    """Main application entry point."""
    st.set_page_config(page_title="Subtitle Generator", layout="centered")
    st.title("🎬 Subtitle Generator")

    ensure_directories()

    try:
        audio_processor = AudioProcessor()
        transcription_service = TranscriptionService(model_name=WHISPER_MODEL)
        video_processor = VideoProcessor(ffmpeg_path=FFMPEG_PATH)
    except FileNotFoundError as e:
        st.error(f"❌ Configuration Error: {str(e)}")
        st.info("💡 Tip: Make sure FFmpeg is installed or available in your environment.")
        st.stop()
    
    uploaded_video = st.file_uploader(
        "Upload a video (max 20 MB)",
        type=SUPPORTED_VIDEO_FORMATS
    )
    
    if uploaded_video:
        if uploaded_video.size > MAX_FILE_SIZE_BYTES:
            st.error("❌ File too large. Maximum allowed size is 20 MB.")
        return

        video_path = save_uploaded_file(uploaded_video, suffix=".mp4")
        
        st.subheader("Original Video")
        st.video(video_path)
        try:
            # Step 1: Extract audio
            with st.spinner("🔊 Extracting audio..."):
                audio_processor.extract_audio(
                    video_path,
                    str(AUDIO_OUTPUT_PATH)
                )
            
            # Step 2: Transcribe audio
            with st.spinner("🧠 Transcribing with Whisper..."):
                transcription_result = transcription_service.transcribe(
                    str(AUDIO_OUTPUT_PATH)
                )
            
            # Step 3: Generate SRT file
            with st.spinner("📝 Generating subtitles..."):
                srt_content = transcription_service.convert_to_srt(
                    transcription_result
                )
                with open(SRT_OUTPUT_PATH, "w", encoding="utf-8") as f:
                    f.write(srt_content)
            
            # Step 4: Burn captions into video
            with st.spinner("🔥 Burning subtitles into video..."):
                video_processor.burn_captions(
                    video_path,
                    str(SRT_OUTPUT_PATH),
                    str(VIDEO_OUTPUT_PATH),
                    video_codec=VIDEO_CODEC,
                    audio_codec=AUDIO_CODEC,
                    mov_flags=MOV_FLAGS,
                )
            
            st.success("✅ Subtitles generated successfully!")
            
            # Display result
            st.subheader("Captioned Video")
            st.video(str(VIDEO_OUTPUT_PATH))
            
            with open(VIDEO_OUTPUT_PATH, "rb") as f:
                st.download_button(
                    "⬇️ Download Captioned Video",
                    f,
                    file_name="captioned_video.mp4",
                    mime="video/mp4"
                )
        
        except ValueError as e:
            st.error(f"❌ Error: {str(e)}")
        except FileNotFoundError as e:
            st.error(f"❌ Configuration Error: {str(e)}")
        except Exception as e:
            st.error(f"❌ Unexpected error: {str(e)}")
            st.exception(e)


if __name__ == "__main__":
    main()
