import os
import random
import textwrap
import edge_tts
from moviepy.editor import *
from moviepy.config import change_settings

# CONFIG
# change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"})
ASSETS_DIR = "assets"
TEMP_DIR = "temp"
VIDEO_SIZE = (1080, 1920)

# Voice Dictionary
VOICES = {
    "pt": "pt-BR-AntonioNeural",     # Brazilian Male (Calm)
    "pt-fem": "pt-BR-FranciscaNeural", # Brazilian Female
    "en": "en-US-ChristopherNeural", # US Male
    "en-fem": "en-US-JennyNeural"    # US Female
}

async def generate_voice(text, lang_code, filename):
    voice = VOICES.get(lang_code, "pt-BR-AntonioNeural") # Default to PT-BR
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

def create_video_file(verse_text, verse_ref, lang_code, output_path):
    os.makedirs(TEMP_DIR, exist_ok=True)
    
    # 1. Audio Generation
    print("... Generating Audio")
    voice_path = os.path.join(TEMP_DIR, "voice.mp3")
    # Add reference to speech? 
    spoken_text = f"{verse_text}... {verse_ref}"
    
    # We must run the async function from a sync context here
    import asyncio
    asyncio.run(generate_voice(spoken_text, lang_code, voice_path))
    
    voice_clip = AudioFileClip(voice_path)
    duration = voice_clip.duration + 2.5

    # 2. Background
    print("... Selecting Background")
    bg_files = [f for f in os.listdir(f"{ASSETS_DIR}/backgrounds") if f.endswith(('.jpg', '.png'))]
    bg_clip = ImageClip(os.path.join(ASSETS_DIR, "backgrounds", random.choice(bg_files)))
    bg_clip = bg_clip.resize(height=VIDEO_SIZE[1]).crop(x1=bg_clip.w/2 - VIDEO_SIZE[0]/2, width=VIDEO_SIZE[0], height=VIDEO_SIZE[1])
    bg_clip = bg_clip.fl_image(lambda image: 0.6 * image) # Darken
    bg_clip = bg_clip.set_duration(duration)

    # 3. Text
    print("... creating Text Overlay")
    # Widen the text wrap slightly for longer scripts, or reduce font size
    wrapper = textwrap.TextWrapper(width=35) 
    txt_string = "\n".join(wrapper.wrap(verse_text)) # Note: verse_text here is now the full script
    
    # Reduce font size slightly to 50 or 60 to fit the reflection text
    txt_clip = TextClip(txt_string, fontsize=55, color='white', font='Arial-Bold', 
                        size=(VIDEO_SIZE[0]-100, None), method='caption', align='center')
    
    # Portuguese text styling
    txt_clip = TextClip(txt_string, fontsize=70, color='white', font='Arial-Bold', 
                        size=(VIDEO_SIZE[0]-100, None), method='caption', align='center')
    txt_clip = txt_clip.set_position('center').set_duration(duration)

    ref_clip = TextClip(verse_ref, fontsize=50, color='#f1c40f', font='Arial-Bold')
    ref_clip = ref_clip.set_position(('center', VIDEO_SIZE[1] - 400)).set_duration(duration)

    # 4. Music
    music_files = [f for f in os.listdir(f"{ASSETS_DIR}/music") if f.endswith('.mp3')]
    if music_files:
        music_path = os.path.join(ASSETS_DIR, "music", random.choice(music_files))
        music_clip = AudioFileClip(music_path)
        if music_clip.duration < duration:
            music_clip = afx.audio_loop(music_clip, duration=duration)
        else:
            music_clip = music_clip.subclip(0, duration)
        
        music_clip = music_clip.volumex(0.15)
        final_audio = CompositeAudioClip([music_clip, voice_clip])
    else:
        final_audio = voice_clip

    # 5. Export
    final = CompositeVideoClip([bg_clip, txt_clip, ref_clip])
    final = final.set_audio(final_audio).set_duration(duration)
    
    final.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac')
    return output_path