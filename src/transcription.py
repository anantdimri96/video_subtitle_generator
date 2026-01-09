"""
Audio transcription and subtitle generation.
"""
import whisper
import srt
from datetime import timedelta
from typing import Dict, Any
import streamlit as st


class TranscriptionService:
    """Handles audio transcription and SRT generation."""
    
    def __init__(self, model_name: str = "base"):
        """
        Initialize the transcription service.
        
        Args:
            model_name: Whisper model to use (e.g., "base", "small", "medium")
        """
        self.model_name = model_name
        self._model = None
    
    @st.cache_resource
    def _load_model(_self):
        """
        Load Whisper model (cached for Streamlit).
        Note: _self is used instead of self to work with @st.cache_resource
        """
        return whisper.load_model(_self.model_name)
    
    def transcribe(self, audio_path: str) -> Dict[str, Any]:
        """
        Transcribe audio file using Whisper.
        
        Args:
            audio_path: Path to the audio file to transcribe
            
        Returns:
            Transcription result dictionary from Whisper
        """
        if self._model is None:
            self._model = self._load_model()
        return self._model.transcribe(audio_path)
    
    @staticmethod
    def convert_to_srt(transcription_result: Dict[str, Any]) -> str:
        """
        Convert Whisper transcription segments to SRT format.
        
        Args:
            transcription_result: Result dictionary from Whisper transcription
            
        Returns:
            SRT formatted string
        """
        subs = []
        
        for i, segment in enumerate(transcription_result["segments"], start=1):
            subs.append(
                srt.Subtitle(
                    index=i,
                    start=timedelta(seconds=segment["start"]),
                    end=timedelta(seconds=segment["end"]),
                    content=segment["text"].strip()
                )
            )
        
        return srt.compose(subs)
