from PIL import Image
import os

# Set the paths for input and output folders
input_folder = '2d_masks'
output_folder = '2d_masks_jpg'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate over all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.tif') or filename.lower().endswith('.tiff'):
        # Construct the full file path
        file_path = os.path.join(input_folder, filename)
        
        # Open the image file
        with Image.open(file_path) as img:
            # Convert the image to RGB (if not already)
            img = img.convert('RGB')
            
            # Define the output file path
            output_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
            
            # Save the image in JPEG format
            img.save(output_file_path, 'JPEG')

print("Conversion completed!")
