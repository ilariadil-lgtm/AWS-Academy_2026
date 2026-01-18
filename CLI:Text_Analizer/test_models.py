import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("Checking usable models...")
found = False
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Trying {m.name}...", end=" ", flush=True)
        model = genai.GenerativeModel(m.name)
        try:
            response = model.generate_content("Hi")
            print("SUCCESS!", flush=True)
            found = True
            print(f"\n--- WORKING MODEL FOUND: {m.name} ---")
            break
        except Exception as e:
            print(f"Failed ({str(e)[:50]}...)", flush=True)
            time.sleep(1)

if not found:
    print("\nNo working models found. Please check your API Quota and Billing settings.")
