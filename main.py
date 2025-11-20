import os
import asyncio
import script_generator
import video_engine
import uploader

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("========================================")
    print("   AUTO BIBLE VIDEO BOT (AI POWERED)    ")
    print("========================================")

    # 1. Settings
    print("\nSelect Language:")
    print("1. Portuguese (Brazil) - Male")
    print("2. Portuguese (Brazil) - Female")
    print("3. English - Male")
    choice = input("Choice [1]: ") or "1"
    
    lang_map = {"1": "pt", "2": "pt-fem", "3": "en"}
    selected_lang = lang_map.get(choice, "pt")
    
    # Map to language code for the Verse API (pt or en)
    api_lang = "en" if selected_lang == "en" else "pt"

    # 2. Input Reference Only
    print("\nEnter Bible Reference (e.g., 'John 3:16' or 'Salmos 23:1'):")
    ref_input = input("> ")

    try:
        # A. Fetch Verse
        print(f"\n... Searching Bible for {ref_input}...")
        verse_text, verse_ref = script_generator.get_bible_verse(ref_input, api_lang)
        print(f"   Found: {verse_text[:50]}...")

        # B. Generate Script
        print("... Writing Script with AI...")
        full_script = script_generator.generate_devotional_script(verse_text, verse_ref, api_lang)
        print("\n--- SCRIPT GENERATED ---")
        print(full_script)
        print("------------------------\n")

        # C. Create Video
        clean_ref = verse_ref.replace(":", "-").replace(" ", "_")
        filename = f"{clean_ref}.mp4"
        output_path = os.path.join(OUTPUT_DIR, filename)

        print("... Generating Video Engine...")
        # Pass the FULL SCRIPT to the video engine instead of just the verse
        video_engine.create_video_file(full_script, verse_ref, selected_lang, output_path)
        
        print(f"\n DONE! Video saved: {output_path}")

    except Exception as e:
        print(f"\nERROR: {e}")
        return

    # 3. Upload?
    if input("\nUpload to YouTube? (y/n): ").lower() == 'y':
        title = f"{verse_ref} - Night Prayer #shorts"
        desc = f"{full_script}\n\n#bible #prayer #night"
        try:
            uploader.upload_to_youtube(output_path, title, desc, ["bible", "prayer", "sleep"])
        except Exception as e:
            print(f"Upload error: {e}")

if __name__ == "__main__":
    main()