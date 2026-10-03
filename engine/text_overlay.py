"""Randează textul de pe ecran (cu emoji color) ca PNG transparent 1080x1920, pentru ffmpeg overlay.
Rulare: python3 engine/text_overlay.py "text" out.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
SIZE = 62

def is_emoji(ch):
    return ord(ch) > 0x2600

def render(text, out, y=250):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    f = ImageFont.truetype(FONT, SIZE)
    ef = ImageFont.truetype(EMOJI, 109)
    lines = text.split("\\n")
    for i, line in enumerate(lines):
        parts, widths = [], []
        for ch in line:
            if ch == "️": continue
            if is_emoji(ch):
                e = Image.new("RGBA", (136, 128), (0, 0, 0, 0))
                ImageDraw.Draw(e).text((0, 0), ch, font=ef, embedded_color=True)
                e = e.crop(e.getbbox() or (0, 0, 1, 1)).resize((SIZE, SIZE), Image.LANCZOS)
                parts.append(("e", e)); widths.append(SIZE + 6)
            else:
                parts.append(("t", ch)); widths.append(f.getlength(ch))
        x = (W - sum(widths)) / 2; yy = y + i * int(SIZE * 1.3)
        d = ImageDraw.Draw(img)
        for (k, v), w in zip(parts, widths):
            if k == "t":
                d.text((x, yy), v, font=f, fill="white", stroke_width=5, stroke_fill="black")
            else:
                img.alpha_composite(v, (int(x), yy + 4))
            x += w
    img.save(out)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2])
