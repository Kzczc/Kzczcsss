from PIL import Image
import os

def conservative_resize(path, target_size_mb=3.5):
    if not os.path.exists(path):
        print(f"Skipping {path}: Not found")
        return

    try:
        file_size_mb = os.path.getsize(path) / (1024 * 1024)
        if file_size_mb <= target_size_mb:
            print(f"Skipping {path}: Already {file_size_mb:.2f} MB (<= {target_size_mb} MB)")
            return

        print(f"Processing {path}...")
        print(f"Original: {file_size_mb:.2f} MB")
        
        img = Image.open(path)
        
        # Calculate resize ratio based on file size (rough estimate)
        # Square root because area is w*h
        scale_factor = (target_size_mb / file_size_mb) ** 0.5
        # Don't scale down too aggressively in one go, cap at 0.8 to be safe if close
        # But here 25MB -> 4MB needs significant scaling.
        
        # Let's just target a generous resolution like 2000px width (very safe for retina)
        # 2000px width PNG is usually around 2-4MB depending on complexity
        
        target_width = 2000
        
        if img.width > target_width:
            ratio = target_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
        
        # Save with high quality
        if path.lower().endswith('.jpg') or path.lower().endswith('.jpeg'):
            img.save(path, quality=98, optimize=True)
        else:
            # PNG compression level 1 (fastest, less compression) to 9 (slowest, best compression)
            # Default is 6. optimize=True tries to find best strategy.
            img.save(path, optimize=True)
            
        new_size_mb = os.path.getsize(path) / (1024 * 1024)
        print(f"Done: {path} -> {new_size_mb:.2f} MB")

    except Exception as e:
        print(f"Error {path}: {e}")

files = [
    "images/Kc.png",
    "images/Kc_head.jpg",
    "images/apple-touch-icon.png",
    "images/favicon-192x192.png",
    "images/favicon-32x32.png",
    "images/favicon-512x512.png"
]

for f in files:
    conservative_resize(f)

