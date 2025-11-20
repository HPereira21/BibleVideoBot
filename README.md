[![English](https://img.shields.io/badge/lang-English-blue.svg)](README.md)
[![Português](https://img.shields.io/badge/lingua-Português-green.svg)](README_PT.md)
# BibleVideoBot (AI-Powered Bible Verse Video Generator)

Generate fully automated Bible-based devotional videos using AI. Just type a verse like **"John 3:16"** or **"Salmos 23:1"**, and the bot will:

1. **Fetch the verse** automatically (Portuguese or English)
2. **Generate a calming devotional script** using the OpenAI API
3. **Create a full video** with voice-over, background video, and on-screen text
4. (Optional) **Upload it to YouTube** automatically

This project is ideal for WhatsApp/Instagram/YouTube prayer channels.

---

## 📁 Project Structure

```
BibleVideoBot/
│
├── assets/               # Background videos, music, images
├── output/               # Final exported videos
├── temp/                 # Temporary files
│
├── main.py               # Entry point
├── video_engine.py       # Handles video generation
├── uploader.py           # Handles YouTube upload
├── script_generator.py   # NEW — Fetches verse & generates devotional script
└── requirements.txt      # Dependencies
```

---

## ⚙️ Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/BibleVideoBot.git
cd BibleVideoBot
```

### 2. Install Python 3.10+ (Windows Instructions Below!)

Download here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Edit `script_generator.py` and replace:

```
OPENAI_KEY = "YOUR_OPENAI_API_KEY_HERE"
```

with your real key from:
**[https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)**

---

## 🪶 Windows Setup Instructions (COMPLETE)

Follow these steps carefully.

### ✅ Step 1 — Install Python

1. Download from [https://python.org/downloads](https://python.org/downloads)
2. **IMPORTANT:** Check the box **“Add Python to PATH”**
3. Install

### ✅ Step 2 — Install FFmpeg (REQUIRED)

Video generation needs FFmpeg.

1. Download FFmpeg (Windows build):
   [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)

2. Extract the `.zip` (e.g., to `C:\ffmpeg`)

3. Add to PATH:

   * Press **Win + R**, type: `sysdm.cpl`
   * Go to **Advanced → Environment Variables**
   * In *System Variables*, select **Path** → Edit
   * Add:

     ```
     C:\ffmpeg\bin
     ```

4. Test:

```
ffmpeg -version
```

If it prints version info → OK.

### ✅ Step 3 — Install Requirements

```
pip install -r requirements.txt
```

### ✅ Step 4 — Add Your OpenAI Key

Edit `script_generator.py` as explained above.

### Optional: Install Microsoft Edge TTS (Voices)

Windows has built-in voices automatically. No extra steps usually needed.

---

## ▶️ Running the Bot

Run:

```
python main.py
```

1. Choose the language/voice
2. Enter a Bible verse reference:

   * `Salmos 91:1`
   * `John 3:16`
3. The bot will:

   * Fetch the verse
   * Generate a calming devotional script using AI
   * Synthesize voice-over
   * Add background video
   * Produce the final MP4

Output will be saved in:

```
output/
```

Then you may be asked:

```
Upload to YouTube? (y/n)
```

If yes, it will upload automatically.

---

## 💵 Costs

* **Bible API** → Free
* **OpenAI API** → Extremely cheap

  * `gpt-4o-mini` costs around **$0.01 per 20–40 videos**
* **Voices (Edge TTS)** → Free on Windows

---

## ✨ Features

* Multi-language (PT-BR & EN)
* AI-written devotional scripts
* Auto-generated video with text overlays
* Auto-upload to YouTube
* Clean & modular architecture

---

## 📌 Notes

* Ensure background videos and music exist in `assets/`
* YouTube uploads require authentication (first run will guide you)

---

## 📜 License

MIT — free to use, modify, and distribute.
