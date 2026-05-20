<div align="center">

# Spriter

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/spriter.svg?style=for-the-badge)](https://pypi.org/project/spriter)

**Spriter** is a CLI tool for extracting and cropping sprites from sprite sheets.

</div>

---

## About

Spriter is a lightweight Python command-line utility for extracting individual sprites from sprite sheets. It offers two powerful methods:

1. **Grid-based extraction** - Slice sprite sheets using fixed grid dimensions
2. **Intelligent auto-detection** - Automatically detect sprites using alpha channel analysis

Perfect for game developers, animators, and anyone working with sprite assets.

## Features

- **Grid-based sprite extraction** with fixed width and height
- **Smart sprite detection** using alpha channel analysis and contour detection
- **Automatic sprite padding** support
- **Minimal dependencies** (PIL and OpenCV)
- **Command-line interface** for easy automation

## Installation

### Via pip (Recommended)

```bash
pip install spriter==1.0.0
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
- OpenCV (cv2) for advanced sprite detection

## Quick Start

### Grid-based Extraction

Extract sprites from a sprite sheet using a fixed grid size:

```bash
spriter grid input_sheet.png --width 32 --height 32 -o ./output/
```

This will split the sprite sheet into 32x32 pixel sprites.

### Auto-detection Extraction

Automatically detect and extract sprites based on alpha channel transparency:

```bash
spriter slice input_sheet.png -o ./output/
```

## Usage and Options

### grid Command

Extract sprites using fixed grid dimensions.

```bash
spriter grid INPUT -o OUTPUT --width WIDTH --height HEIGHT
```

**Options:**
- `INPUT` - Path to input sprite sheet (required)
- `-o, --output` - Output directory (default: ~/)
- `--width` - Width of each sprite in pixels (required)
- `--height` - Height of each sprite in pixels (required)

**Example:**
```bash
spriter grid spritesheet.png --width 64 --height 64 -o ./sprites/
```

### slice Command

Automatically detect and extract sprites using alpha channel analysis.

```bash
spriter slice INPUT -o OUTPUT [OPTIONS]
```

**Options:**
- `INPUT` - Path to input sprite sheet with alpha channel (required)
- `-o, --output` - Output directory (default: ~/)
- `--min-area` - Minimum sprite area in pixels to extract (default: 100)
- `--padding` - Padding around each detected sprite in pixels (default: 0)

**Example:**
```bash
spriter slice spritesheet.png -o ./sprites/ --padding 2 --min-area 50
```

## Supported Image Formats

**Input:** PNG, JPEG, BMP, and other OpenCV-supported formats
**Output:** PNG (default)

## Limitations

- JSON and CSV metadata formats are **not supported**
- Output format is fixed to PNG
- No custom naming or prefix options

## Performance Tips

- For large sprite sheets, use the **grid command** for consistent results
- Use the **slice command** for irregular sprite layouts with transparency
- The slice command requires images with an alpha channel (PNG format recommended)
- Use `--min-area` to filter out noise and small artifacts

## Troubleshooting

### "Image has no alpha channel"
The slice command requires images with transparency. Ensure your input is in PNG format with an alpha channel.

### "Failed to load image"
Verify the input file path is correct and the format is supported by OpenCV.

### Output directory not created
The tool will automatically create the output directory if it doesn't exist. Ensure you have write permissions.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details.

For more information about GPL-3.0, visit [https://www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html).

## Support

- 🐛 [Issue Tracker](https://github.com/ifuckingjoke/spriter/issues)
- 💬 [Discussions](https://github.com/ifuckingjoke/spriter/discussions)

---

<div align="center">

Made with ❤️ by [ifuckingjoke](https://github.com/ifuckingjoke)

</div>