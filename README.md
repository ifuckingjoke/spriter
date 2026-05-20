<div align="center">

# Spriter

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/spriter.svg?style=for-the-badge)](https://pypi.org/project/spriter)

**Spriter** is a command-line tool for efficiently extracting and cropping sprites from sprite sheets.

</div>

---

## About

Spriter is a Python CLI utility designed to simplify the process of extracting individual sprites from sprite sheets. Whether you're working with game assets, animations, or icon sets, Spriter provides an intuitive and efficient way to crop sprites based on coordinates or metadata.

## Features

- **Batch sprite extraction** from sprite sheet images
- **Flexible coordinate input** (manual coordinates, CSV metadata, JSON configuration)
- **Multiple output formats** support
- **Customizable output naming** and organization
- **Command-line interface** for easy automation and scripting
- **Fast processing** with minimal dependencies

## Installation

### Via pip (Recommended)

```bash
pip install spriter
```

### From source

```bash
git clone https://github.com/ifuckingjoke/spriter.git
cd spriter
pip install -e .
```

### Requirements

- Python 3.7 or higher
- Pillow (PIL) for image processing

## Quick Start

### Basic Usage

Extract a single sprite from a sprite sheet:

```bash
spriter crop -i spritesheet.png -o output/ -x 0 -y 0 -w 32 -h 32
```

### Using a Configuration File

Create a `sprites.json` configuration file:

```json
{
  "spritesheet": "spritesheet.png",
  "output_dir": "output/",
  "sprites": [
    {"name": "sprite_1", "x": 0, "y": 0, "width": 32, "height": 32},
    {"name": "sprite_2", "x": 32, "y": 0, "width": 32, "height": 32},
    {"name": "sprite_3", "x": 64, "y": 0, "width": 32, "height": 32}
  ]
}
```

Then run:

```bash
spriter crop --config sprites.json
```

### Using CSV Metadata

Create a `sprites.csv` file:

```csv
name,x,y,width,height
sprite_1,0,0,32,32
sprite_2,32,0,32,32
sprite_3,64,0,32,32
```

Extract sprites:

```bash
spriter crop -i spritesheet.png -o output/ --csv sprites.csv
```

## Usage and Options

### Global Options

```
-v, --version          Show version information and exit
-h, --help             Show help message and exit
```

### crop Command

```bash
spriter crop [OPTIONS]

Options:
  -i, --input FILE           Path to input sprite sheet (required if not in config)
  -o, --output DIR           Output directory for cropped sprites (default: ./output)
  -x, --x-offset INT         X coordinate of sprite (0-based)
  -y, --y-offset INT         Y coordinate of sprite (0-based)
  -w, --width INT            Width of sprite in pixels
  -h, --height INT           Height of sprite in pixels
  -n, --name TEXT            Output filename for single sprite
  --config FILE              Configuration file (JSON or YAML)
  --csv FILE                 CSV file with sprite coordinates
  --format TEXT              Output format (png, jpg, bmp; default: png)
  --quality INT              JPEG quality (1-100; default: 95)
  --padding INT              Add padding around sprites (default: 0)
  --background COLOR         Background color for transparency (hex or name)
  --prefix TEXT              Prefix for output filenames
  --suffix TEXT              Suffix for output filenames
  --preserve-names           Use names from config instead of auto-naming
```

### Examples

**Extract a single sprite:**
```bash
spriter crop -i sheet.png -x 10 -y 20 -w 50 -h 50 -n my_sprite.png -o sprites/
```

**Extract all sprites from CSV with custom settings:**
```bash
spriter crop -i sheet.png -o sprites/ --csv metadata.csv --format jpg --quality 85
```

**Add padding and prefix to all outputs:**
```bash
spriter crop --config config.json --padding 2 --prefix "game_"
```

**Extract with background color:**
```bash
spriter crop -i sheet.png --csv sprites.csv -o output/ --background "#FF00FF"
```

## Configuration File Formats

### JSON Configuration

```json
{
  "spritesheet": "path/to/spritesheet.png",
  "output_dir": "path/to/output",
  "output_format": "png",
  "options": {
    "quality": 95,
    "padding": 0,
    "prefix": "",
    "suffix": ""
  },
  "sprites": [
    {
      "name": "character_idle",
      "x": 0,
      "y": 0,
      "width": 32,
      "height": 32
    },
    {
      "name": "character_run",
      "x": 32,
      "y": 0,
      "width": 32,
      "height": 32
    }
  ]
}
```

### CSV Format

```csv
name,x,y,width,height
sprite_1,0,0,32,32
sprite_2,32,0,32,32
sprite_3,0,32,32,32
sprite_4,32,32,32,32
```

## Python API

You can also use Spriter as a Python library:

```python
from spriter import Spriter

# Initialize Spriter
spriter = Spriter('spritesheet.png')

# Crop a single sprite
spriter.crop(x=0, y=0, width=32, height=32, output='sprite.png')

# Crop multiple sprites from config
spriter.crop_from_config('config.json', output_dir='sprites/')

# Crop from CSV
spriter.crop_from_csv('metadata.csv', output_dir='sprites/')
```

## Supported Image Formats

**Input:** PNG, JPEG, BMP, GIF, TIFF
**Output:** PNG (default), JPEG, BMP, GIF, TIFF

## Performance Tips

- For large sprite sheets, consider splitting them into sections
- Use PNG format for lossless output (recommended for game assets)
- Adjust JPEG quality based on your needs (higher quality = larger file size)
- Batch multiple sprites in a single configuration file for faster processing

## Troubleshooting

### "Sprite out of bounds"
Ensure your x, y, width, and height coordinates are within the sprite sheet dimensions.

### "Unsupported image format"
Verify the input file is in a supported format (PNG, JPEG, BMP, GIF, TIFF).

### "Output directory not found"
The tool will attempt to create the output directory. Ensure you have write permissions.

### Memory issues with large files
Process the sprite sheet in sections or reduce image quality settings.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📖 [Documentation](https://github.com/ifuckingjoke/spriter/wiki)
- 🐛 [Issue Tracker](https://github.com/ifuckingjoke/spriter/issues)
- 💬 [Discussions](https://github.com/ifuckingjoke/spriter/discussions)

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes in each release.

## Related Projects

- [Texture Packer](https://www.codeandweb.com/texturepacker) - Professional sprite sheet creator
- [ImageMagick](https://imagemagick.org) - General-purpose image manipulation
- [PIL/Pillow](https://python-pillow.org) - Python Imaging Library

---

<div align="center">

Made with ❤️ by [ifuckingjoke](https://github.com/ifuckingjoke)

</div>
