import os
import glob
from PIL import Image, ImageEnhance

image_dir = "c:/Users/Lenovo/work2/images/"
files = glob.glob(image_dir + "sneaker_real_*-removebg-preview.png")

print(f"Found {len(files)} images to enhance.")

for f in files:
    try:
        img = Image.open(f)
        
        # 1. Enhance Sharpness to bring out details
        enhancer_sharp = ImageEnhance.Sharpness(img)
        img_sharp = enhancer_sharp.enhance(1.8)  # Increase sharpness
        
        # 2. Enhance Contrast to make details pop
        enhancer_contrast = ImageEnhance.Contrast(img_sharp)
        img_contrast = enhancer_contrast.enhance(1.15)  # Increase contrast
        
        # 3. Slightly reduce brightness if they are too blown out
        enhancer_brightness = ImageEnhance.Brightness(img_contrast)
        img_final = enhancer_brightness.enhance(0.85)  # Darken slightly
        
        # Save back to the same file
        img_final.save(f)
        print(f"Enhanced and saved: {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
