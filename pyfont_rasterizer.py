import subprocess
import os

def generate_bitmap_fonts(font_names, font_sizes, color_map, fontbm_path, input_dir, output_dir):
    for font_name in font_names:
        for font_size in font_sizes:
            for color, rgb in color_map.items():
                # Format: FontName-FontSize-Color
                output_file_name = f"{font_name[:-4]}-{font_size}px-{color}"

                command = [
                    fontbm_path,
                    "--font-file", os.path.join(input_dir, font_name),
                    "--output", os.path.join(output_dir, output_file_name),
                    "--font-size", str(font_size),
                    "--color", rgb,
                ]

                subprocess.run(command, check=True)

font_names = [
    "Ubuntu-BoldItalic.ttf",
    "Ubuntu-Italic.ttf",
    "Ubuntu-LightItalic.ttf",
    "Ubuntu-MediumItalic.ttf",
    "Ubuntu-Regular.ttf"
]

font_sizes = [32, 48, 64, 96]

color_map = {
    "white": "255,255,255",
    "black": "0,0,0"
}

fontbm_path = "./fontbm"
input_dir = "./fonts-in"
output_dir = "./fonts-out"

generate_bitmap_fonts(font_names, font_sizes, color_map, fontbm_path, input_dir, output_dir)