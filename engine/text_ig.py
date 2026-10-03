"""Text în stil Instagram/TikTok (alb, umbră moale, fără contur) cu emoji color, PNG 1080x1920.
Rulare: python3 engine/text_ig.py "linia 1\nlinia 2" out.png [y]
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
SIZE = 68

def layout(line, f):
    parts = []
    for ch in line:
        if ch == "️": continue
        parts.append(("e", ch) if ord(ch) > 0x2600 else ("t", ch))
    return parts

def render(text, out, y=200):
    f = ImageFont.truetype(FONT, SIZE); ef = ImageFont.truetype(EMOJI, 109)
    txt = Image.new("RGBA", (W, H), (0, 0, 0, 0)); emo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    for i, line in enumerate(text.split("\\n")):
        parts = layout(line, f)
        widths = [SIZE * 1.08 if k == "e" else f.getlength(v) for k, v in parts]
        x = (W - sum(widths)) / 2; yy = y + i * int(SIZE * 1.18)
        for (k, v), w in zip(parts, widths):
            if k == "t":
                d.text((x, yy), v, font=f, fill="white", stroke_width=2, stroke_fill=(40,40,40))
            else:
                e = Image.new("RGBA", (136, 128), (0, 0, 0, 0)); ImageDraw.Draw(e).text((0, 0), v, font=ef, embedded_color=True)
                e = e.crop(e.getbbox()).resize((int(SIZE * 0.98), int(SIZE * 0.98)), Image.LANCZOS)
                emo.alpha_composite(e, (int(x + 2), yy + 3))
            x += w
    # umbră moale ca în Instagram
    a = txt.split()[3]
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sh.putalpha(a.point(lambda p: int(p * 0.55)))
    sh = sh.filter(ImageFilter.GaussianBlur(3))
    base = Image.new("RGBA", (W, H), (0, 0, 0, 0)); base.alpha_composite(sh, (0, 2)); base.alpha_composite(txt); base.alpha_composite(emo)
    base.save(out)

if __name__ == "__main__":
    render(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 200)
