# 3D Reconstruction from 2D Segmentation Images

## Overview

This project provides tools for visualizing 3D objects reconstructed from 2D segmentation images and for converting image formats. It also includes instructions for running the `im2mesh` tool on custom datasets.

![Project GIF](assets/3D-Lungs.gif)

## Basic Requirements

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Visualization of 3D Objects

To visualize 3D objects, use the script `visualize_3d.py`. Ensure that you specify the path to the correct `.stl` file.

```bash
python visualize_3d.py --file path/to/your/file.stl
```

## Image Format Conversion

To convert images from `.tif` to `.jpg`, use the script `convert_to_jpg.py`. Provide the path to the folder containing `.tif` images and specify the desired output folder.

```bash
python convert_to_jpg.py --input-folder path/to/tif/folder --output-folder path/to/output/folder
```

## Running `im2mesh` on Custom Datasets

Instructions for running `im2mesh` are available in the notebook provided. Note that `im2mesh` currently does not support macOS and is only compatible with Windows 10.

Which is why a local .py file was not provided to run it locally, but you can simply run it on google colab.