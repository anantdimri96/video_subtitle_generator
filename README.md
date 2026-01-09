# 🎬 Auto Caption Generator 🧠

Tired of **bad subtitles ruining your videos**? I was too. So I built **Auto Caption Generator** — a lightweight AI web app that **auto-generates perfectly synced captions** and burns them into your videos.  

🔗 **Try it live:** [Click here](https://video-caption-generator-anant.streamlit.app/)

https://github.com/user-attachments/assets/e8cb4e96-6990-48df-9684-8052ac079e4f



---

## 🤯 The Problem
Tired of bad subtitles ruining your videos? So was I. That’s why I built Auto Caption Generator — a lightweight AI web app that automatically generates and burns subtitles into your videos, in perfect sync.

Subtitles matter: accessibility, comprehension, global audiences.  
But most tools are:  
- 💸 Expensive  
- 🤯 Clunky  
- 🐢 Slow  
- 😩 Out of sync  

Frustrating, right? I wanted **something simple and reliable**.  

---

## 💡 The Solution

**Auto Caption Generator** does it all:  
1. Upload a short video  
2. AI transcription (Whisper)  
3. Time-aligned subtitles (SRT)  
4. Burn captions directly into video  
5. Preview & download  

No manual syncing. No extra tools. Just working subtitles.  

---

## ⚙️ How It Works

Video Upload
->
Audio Extraction (MoviePy)
->
Speech-to-Text (OpenAI Whisper)
->
Timestamped Segments
->
SRT Generation
->
Subtitle Burn-in (ffmpeg)
->
Browser Playback + Download


---

## 🧠 AI & Product Decisions

From an **AI Product Manager perspective**, this project involved several deliberate tradeoffs:

### Model Choice
- **Whisper (base)** was chosen to balance:
  - Transcription accuracy
  - Latency
  - CPU-only inference (no GPU dependency)

### Infrastructure Constraints
- Deployed on **Streamlit Community Cloud (free tier)**
- CPU-only environment → influenced model size and upload limits
- File size capped at **10 MB** to ensure reliability and predictable performance

### UX Decisions
- Immediate validation for file size
- In-browser video playback for instant feedback
- Minimal UI to reduce cognitive load
- Downloadable output for real-world usability

---

## 📹 Product Demo (Screen Recording)

> _Add a short screen recording here to demonstrate the full flow._

**Suggested format:**
- Upload video
- Processing states
- Captioned output playback


---

## 🛠 Tech Stack

- **Frontend / App Framework:** Streamlit
- **Speech-to-Text:** OpenAI Whisper
- **Video Processing:** MoviePy, ffmpeg
- **Subtitle Formatting:** srt
- **Deployment:** GitHub + Streamlit Community Cloud

---

## ⚠️ Known Limitations

- CPU-only inference → slower for longer videos
- Optimized for short-form content
- Single-language transcription (English by default)
- Not designed for batch processing (yet)

These limitations are intentional, aligned with free-tier constraints and product simplicity.

---

## 🔮 Future Improvements

If evolving this into a more production-grade AI product:
- Language selection & multilingual subtitles
- Subtitle styling (font, size, color, positioning)
- Async processing with progress indicators
- Batch uploads
- User authentication & history
- Cost-aware scaling strategies

---

## 👤 About the Builder

Built by **Anant Dimri** — a AI Product manager with experience across AI SaaS, infrastructure, and growth systems.

This project reflects how I approach AI products:
- Start with a real user pain
- Ship end-to-end
- Respect system constraints
- Optimize for clarity, reliability, and usability

---

## 🔗 Links

- **Live App:** https://video-caption-generator-anant.streamlit.app/
- **GitHub Repo:** You are already here!!
- **LinkedIn:** https://www.linkedin.com/in/anant-dimri96/

---

*Feedback, ideas, and suggestions are welcome.*

