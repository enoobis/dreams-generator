from PIL import Image, ImageDraw
import random

# Define image size
width = 800
height = 800

# Create black image
img = Image.new('RGB', (width, height), color='black')
draw = ImageDraw.Draw(img)

# Define number of grey areas and their size range
num_grey_areas = 10
min_grey_size = 50
max_grey_size = 200

# Generate random grey areas
for i in range(num_grey_areas):
    # Generate random position and size for grey area
    x = random.randint(0, width - max_grey_size)
    y = random.randint(0, height - max_grey_size)
    size = random.randint(min_grey_size, max_grey_size)
    # Generate random polygon for grey area
    num_vertices = random.randint(10, 50)
    vertices = []
    for j in range(num_vertices):
        vertex_x = random.randint(x, x + size)
        vertex_y = random.randint(y, y + size)
        vertices.append((vertex_x, vertex_y))
    grey_color = (128, 128, 128)
    draw.polygon(vertices, fill=grey_color)

    # Generate random color for pixels within grey area
    colors = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255)]
    for x_coord in range(x, x+size):
        for y_coord in range(y, y+size):
            if img.getpixel((x_coord, y_coord)) == grey_color:
                if random.random() < 0.5:
                    pixel_color = colors[random.randint(0, len(colors)-1)]
                    draw.point((x_coord, y_coord), fill=pixel_color)

# Add random white pixels to the whole picture
white_prob = 0.01
for x_coord in range(width):
    for y_coord in range(height):
        if random.random() < white_prob:
            draw.point((x_coord, y_coord), fill=(255, 255, 255))

# Save image
img.save('random_image.png')