# Font Rasterizer

Font Rasterizer is a Python script that automates the process of creating bitmap fonts from TrueType font files (`.ttf`). 

It uses the `fontbm` executable to generate `.png` texture atlases and corresponding `.fnt` descriptor files at various sizes and colors.

## Requirements

- Python 3.x
- `fontbm` executable

## Installation

1. Ensure that you have Python 3.x installed on your system.
2. Place the `fontbm` executable in the root of the project directory.

## Usage

1. Place all your `.ttf` font files in the `fonts-in` directory.
2. Open a terminal in the project directory.
3. Run the script with `python font_rasterizer.py`.

## Configuration

You can configure the script by editing the `font_rasterizer.py` file:

- `font_names`: List the filenames of the `.ttf` fonts you want to rasterize.
- `font_sizes`: Specify the sizes (in pixels) at which you want to rasterize the fonts.
- `color_map`: Define the colors in which you want the fonts rasterized. Map the color names to their corresponding RGB string values.

## Output

The rasterized font files will be output to the `fonts-out` directory. Each font will have its own `.png` texture atlas and a `.fnt` file. The files will be named in the following format:

```
FontName-Size-Color.png
FontName-Size-Color.fnt
```

For example, `Ubuntu-Regular-32px-white.png` and `Ubuntu-Regular-32px-white.fnt`.

## Notes

- The `--color` parameter uses RGB values to define the color of the font glyphs. Ensure that the `color_map` in the script maps to valid RGB strings.
- The script will run the `fontbm` command for each combination of font name, size, and color defined in the configuration.

## Author

FunkPd

## Acknowledgements

- [fontbm](https://github.com/vladimirgamalyan/fontbm) for the bitmap font generation tool.