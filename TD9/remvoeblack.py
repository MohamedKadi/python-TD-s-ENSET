from PIL import Image

# Input / Output images
input_path = r"C:\Users\moham\Desktop\learning projects\python\TD9\input.png"
output_path = r"C:\Users\moham\Desktop\learning projects\python\TD9\output1.png"

# How close to black a pixel must be to remove it (0 = remove only pure black, higher = remove dark tones)
BLACK_THRESHOLD = 20   # Try 20–40 depending on how dark the "black" is

# Open image and convert to RGBA
img = Image.open(input_path).convert("RGBA")
pixels = img.load()

width, height = img.size

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]

        # Check if the pixel is near black
        if r < BLACK_THRESHOLD and g < BLACK_THRESHOLD and b < BLACK_THRESHOLD:
            # Make the pixel transparent (remove it)
            pixels[x, y] = (0, 0, 0, 0)

img.save(output_path, "PNG")
print("Done! Saved:", output_path)
