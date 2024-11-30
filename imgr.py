from PIL import Image

# Open the image file
image = Image.open("file-Jg111QWhSoLs1KsV6BqusR.webp")

# Resize the image to desired dimensions
image_resized = image.resize((1280, 720))  # Width: 1280, Height: 720

# Save the resized image
image_resized.save("resized_image.jpg")

print("Image resized and saved successfully!")