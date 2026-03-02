import os
import glob
from PIL import Image

output_dir = "c:/Users/Lenovo/work2/images/"
files = glob.glob(output_dir + "sneaker_real_*-removebg-preview.png")

print(f"Found {len(files)} files to process for edge cleanup.")
for f in files:
    try:
        img = Image.open(f).convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # item is (R, G, B, A)
            # If the pixel is mostly white/light gray and somewhat transparent (the halo),
            # or if it's very bright near the edge, we make it fully transparent or reduce opacity.
            
            # Simple approach: If alpha is between 1 and 200, it's an edge pixel.
            # We can aggressively trim semi-transparent pixels to remove the halo.
            if item[3] > 0 and item[3] < 220:
                newData.append((255, 255, 255, 0)) # Make it fully transparent
            else:
                newData.append(item)
                
        img.putdata(newData)
        
        # Save back to the same path
        img.save(f, "PNG")
        print(f"Cleaned edges and saved: {f}")
    except Exception as e:
        print(f"Error on {f}: {e}")
