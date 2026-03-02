import os
import glob
from rembg import remove
from PIL import Image

output_dir = "c:/Users/Lenovo/work2/images/"
os.makedirs(output_dir, exist_ok=True)

brain_dir = "C:/Users/Lenovo/.gemini/antigravity/brain/a6c4b507-d69d-4360-98c8-7c57ddf3bef7/"
files = glob.glob(brain_dir + "sneaker_real_*.png")
print(f"Found {len(files)} files to process.")
for f in files:
    filename = os.path.basename(f)
    # Simplify the name for the HTML: e.g. sneaker_real_1-removebg-preview.png
    parts = filename.split('_')
    # Name format is usually something like sneaker_real_1_12345678.png
    base_id = parts[2] if len(parts) > 2 else "x"
    out_name = f"sneaker_real_{base_id}-removebg-preview.png"
    out_path = os.path.join(output_dir, out_name)
    print(f"Processing {filename} -> {out_name}")
    try:
        input_image = Image.open(f)
        output_image = remove(input_image)
        output_image.save(out_path)
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Error on {filename}: {e}")
