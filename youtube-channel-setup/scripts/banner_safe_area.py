#!/usr/bin/env python3
"""Banner safe-area checker for YouTube channel art.

Overlays the YouTube crop zones on a 2560x1440 channel banner so the
owner can see exactly what survives on each device before uploading it.

YouTube channel art facts (current YouTube layout):
  - Design size: 2560 x 1440 pixels (the only size to design at).
  - Desktop shows a 2560 x 423 strip from the middle of the banner.
  - Tablet shows a 1855 x 423 strip from the middle.
  - Mobile shows a 1546 x 423 strip from the center.
  - TV shows the whole 2560 x 1440 image.
  - Safe area (shows on every device): 1546 x 423, centered.
    All text and logos must sit inside the safe area, or they will be
    cut off on desktop and mobile.

Usage:
    python3 banner_safe_area.py banner.png [checked-banner.png]

The script saves a copy of the banner with the zones drawn on it and
prints a text report of what each zone covers. If Pillow is not
installed it prints the install command and still prints the report.

Needs: Pillow (pip install pillow)
"""

import sys
from pathlib import Path

# Banner design size — YouTube channel art.
BANNER_W = 2560
BANNER_H = 1440

# Crop zones: (label, width, height). Every zone is centered on the
# banner; the visible strip is the middle band of the image.
ZONES = [
    ("TV (full image)", BANNER_W, BANNER_H),
    ("Desktop strip", BANNER_W, 423),
    ("Tablet strip", 1855, 423),
    ("Mobile strip", 1546, 423),
    ("SAFE AREA (all devices)", 1546, 423),
]


def zone_rect(width: int, height: int) -> tuple:
    """Centered rectangle for a zone, as (left, top, right, bottom)."""
    left = (BANNER_W - width) // 2
    top = (BANNER_H - height) // 2
    return (left, top, left + width, top + height)


def print_report(image_path: Path) -> None:
    print(f"Banner: {image_path}")
    print(f"Design size: {BANNER_W} x {BANNER_H}")
    print()
    print("Crop zones (all centered on the banner):")
    for label, width, height in ZONES:
        left, top, right, bottom = zone_rect(width, height)
        print(f"  {label:<26} {width} x {height}  "
              f"— x {left}..{right}, y {top}..{bottom}")
    print()
    print("Rules:")
    print("  - All text and logos must sit inside the SAFE AREA")
    print("    (1546 x 423, centered: x 507..2053, y 508..931).")
    print("  - Text outside the safe area is cut off on desktop and mobile.")
    print("  - Characters in the middle 423-pixel band show on every device;")
    print("    characters near the top or bottom edges show on TV only.")
    print()
    print("Known live example: the Bunny Sounds banner title text was")
    print("placed outside the safe area and is cut off on desktop, while")
    print("the characters in the middle band still show. Do not repeat it.")


def draw_zones(image_path: Path, output_path: Path) -> bool:
    """Draw the crop zones onto the banner and save it. Returns True on success."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow is not installed. Install it to draw the zones:")
        print("    pip install pillow")
        print("The text report above still applies — check the banner")
        print("against the safe area (x 507..2053, y 508..931) by hand.")
        return False

    try:
        image = Image.open(image_path).convert("RGB")
    except OSError as exc:
        print(f"Could not open {image_path}: {exc}")
        return False

    if image.size != (BANNER_W, BANNER_H):
        print(f"WARNING: this image is {image.size[0]} x {image.size[1]}, "
              f"not {BANNER_W} x {BANNER_H}.")
        print("YouTube channel art must be 2560 x 1440. Resize it first,")
        print("then run this script again — the zones below are drawn for")
        print("a 2560 x 1440 image and will not line up on another size.")
        return False

    draw = ImageDraw.Draw(image, "RGBA")
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 42)
    except OSError:
        font = ImageFont.load_default()

    # Zone colors: outline + translucent fill, safe area drawn last (on top).
    colors = {
        "Desktop strip": (255, 165, 0, 255),        # orange
        "Tablet strip": (0, 170, 255, 255),         # blue
        "Mobile strip": (255, 0, 0, 255),           # red
        "SAFE AREA (all devices)": (0, 200, 0, 255),  # green
    }
    for label, width, height in ZONES:
        if label == "TV (full image)":
            continue
        color = colors[label]
        rect = zone_rect(width, height)
        draw.rectangle(rect, outline=color, width=6)
        draw.rectangle(rect, fill=color[:3] + (18,))
        draw.text((rect[0] + 12, rect[1] + 10), label, fill=color, font=font)

    image.save(output_path)
    print(f"Checked banner saved to: {output_path}")
    print("Green = safe area (shows everywhere). Red = mobile strip.")
    print("Blue = tablet strip. Orange = desktop strip.")
    return True


def main(argv: list) -> int:
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(argv) >= 2 else 1

    image_path = Path(argv[1])
    if not image_path.is_file():
        print(f"File not found: {image_path}")
        return 1

    output_path = Path(argv[2]) if len(argv) > 2 else Path(
        f"{image_path.stem}-checked{image_path.suffix}"
    )

    print_report(image_path)
    draw_zones(image_path, output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
