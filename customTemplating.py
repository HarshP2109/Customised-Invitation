import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from truncateDirectory import deleteFiles
import os

def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height

def create_personalized_invitation_simple(image_path, csv_file, output_dir, font_path, font_size, font_color, y_coordinate):

    # To Delete Files from folder
    deleteFiles("personalized_invitations")
    
    # Load CSV file with names
    df = pd.read_csv(csv_file)
    
    # Open the base invitation image
    img = Image.open(image_path).convert("RGB")
    image_width, image_height = img.size
    draw = ImageDraw.Draw(img)
    
    # Load the font
    font = ImageFont.truetype(font_path, font_size)
    font_color = tuple(int(font_color[i:i+2], 16) for i in (0, 2, 4))  # Convert hex color to RGB

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each name in the CSV
    for index, row in df.iterrows():
        name = row[0]  # Assuming the name is in the first column

        # Calculate text width and set X-coordinate to center text horizontally
        text_width, text_height = textsize(name, font=font)
        x_coordinate = (image_width - text_width) // 2  # Center horizontally

        # Draw the name on the image
        img_copy = img.copy()  # Create a copy to avoid overwriting
        draw_copy = ImageDraw.Draw(img_copy)
        draw_copy.text((x_coordinate, y_coordinate), name, font=font, fill=font_color)

        # Save the image with the name from CSV
        output_path = os.path.join(output_dir, f"{name}.jpg")
        img_copy.save(output_path)

# Example usage with known coordinates
image_path = "template.png"
csv_file = "words.csv"
output_dir = "personalized_invitations"
font_path = "Alice-Regular.ttf"
font_size = 80
font_color = "20520c"
y_coordinate = 548  # Keep Y fixed

create_personalized_invitation_simple(image_path, csv_file, output_dir, font_path, font_size, font_color, y_coordinate)
