#!/usr/bin/env python3

from PIL import Image
import os, argparse, cv2


def mk_out(args):
    os.makedirs(args, exist_ok=True)

def cmd_grid(args):

    img = Image.open(args.input)
    w, h = img.size

    mk_out(args.output)

    i = 0
    for y in range(0, h, args.height):
        for x in range(0, w, args.width):
            box = (
                x,
                y,
                min(x + args.width, w),
                min(y + args.height, h)
            )
            sprite = img.crop(box)

            sprite.save(f"{args.output}/sprite_{i}.png")
            i += 1

            print(f"Saved {i} sprite from {args.output}")

def cmd_slice(args):
    img = cv2.imread(args.input, cv2.IMREAD_UNCHANGED)

    mk_out(args.output)

    if img is None:
        raise ValueError("Failed to load image")

    if img.shape[2] < 4:
        raise ValueError("Image has no alpha channel")

    alpha = img[:, :, 3]

    _, thresh = cv2.threshold(alpha, 1, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[1], reverse=True)

    count = 0

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        if w * h < args.min_area:
            continue

        x1 = max(x - args.padding, 0)
        y1 = max(y - args.padding, 0)
        x2 = min(x + w + args.padding, img.shape[1])
        y2 = min(y + h + args.padding, img.shape[0])

        sprite = img[y1:y2, x1:x2]

        out_path = os.path.join(args.output, f"sprite_{count}.png")
        cv2.imwrite(out_path, sprite)

        count += 1

        print(f"Saved {count} sprite from {args.output}")


def main():
    parser = argparse.ArgumentParser(prog="spriter")
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # --- GRID ---
    grid = subparsers.add_parser("grid", help="Slice by fixed grid")
    grid.add_argument("input")
    grid.add_argument("-o", "--output", default=os.path.expanduser("~/"))
    grid.add_argument( "--width", type=int, required=True)
    grid.add_argument( "--height", type=int, required=True)
    grid.set_defaults(func=cmd_grid)

    # --- SLICE ---
    slice_ = subparsers.add_parser("slice", help="Auto detect sprites")
    slice_.add_argument("input")
    slice_.add_argument("-o", "--output", default=os.path.expanduser("~/"))
    slice_.add_argument("--min-area", type=int, default=100, help="Minimum sprite area")
    slice_.add_argument("--padding", type=int, default=0, help="Padding around sprite")
    slice_.set_defaults(func=cmd_slice)

    args = parser.parse_args()
    args.func(args)

    if not hasattr(args, "func"):
        parser.print_help()
        return

if __name__ == "__main__":
    main()


