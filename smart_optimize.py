from PIL import Image
import os

def smart_resize(path, target_width=1000):
    if not os.path.exists(path):
        print(f"Skipping {path}: Not found")
        return

    try:
        img = Image.open(path)
        original_size_mb = os.path.getsize(path) / (1024 * 1024)
        
        # If image is smaller than 1MB, skip (unless it's dimensions are huge)
        # But here we know they are 25MB!
        
        if img.width > target_width:
            print(f"Processing {path}...")
            print(f"Original: {img.width}x{img.height}, {original_size_mb:.2f} MB")
            
            ratio = target_width / img.width
            new_height = int(img.height * ratio)
            
            # High quality resize
            img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
            
            # Save
            # Keep original format
            if path.lower().endswith('.jpg') or path.lower().endswith('.jpeg'):
                img.save(path, quality=95, optimize=True)
            else:
                img.save(path, optimize=True)
                
            new_size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"Done: {path} -> {new_size_mb:.2f} MB (Quality preserved)")
        else:
            print(f"{path} width is already small ({img.width}px). optimizing only...")
            if path.lower().endswith('.jpg') or path.lower().endswith('.jpeg'):
                img.save(path, quality=95, optimize=True)
            else:
                img.save(path, optimize=True)

    except Exception as e:
        print(f"Error {path}: {e}")

# List of huge files found
files = [
    "images/Kc.png",
    "images/Kc_head.jpg",
    "images/apple-touch-icon.png",
    "images/favicon-192x192.png",
    "images/favicon-32x32.png",
    "images/favicon-512x512.png"
]

for f in files:
    smart_resize(f)

