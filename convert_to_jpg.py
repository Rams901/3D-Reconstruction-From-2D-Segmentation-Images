from PIL import Image
import os
import argparse

def convert_images(input_folder, output_folder):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images from .tif to .jpg format.")
    parser.add_argument('--input-folder', type=str, default='2d_masks', 
                        help="Path to the input folder containing .tif images (default: '2d_masks')")
    parser.add_argument('--output-folder', type=str, default='2d_masks_jpg', 
                        help="Path to the output folder for .jpg images (default: '2d_masks_jpg')")
    args = parser.parse_args()
    
    convert_images(args.input_folder, args.output_folder)
