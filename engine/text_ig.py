"""Text în stil Instagram/TikTok (alb, umbră moale) cu emoji de iPhone (assets/emoji-apple), PNG 1080x1920.
Rulare: python3 engine/text_ig.py "linia 1\nlinia 2" out.png [y]
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W, H = 1080, 1920
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
SIZE = 68

APPLE = os.path.join(os.path.dirname(__file__), "..", "assets", "emoji-apple")

def layout(line, f):
    """Grupează emoji-urile (inclusiv ZWJ, FE0F, ton de piele) într-un singur element."""
    parts = []
    for ch in line:
        o = ord(ch)
        joiner = o in (0x200D, 0xFE0F) or 0x1F3FB <= o <= 0x1F3FF
        if parts and parts[-1][0] == "e" and (joiner or parts[-1][1].endswith("\u200d")):
            parts[-1] = ("e", parts[-1][1] + ch)
        elif o > 0x2600 and not joiner:
            parts.append(("e", ch))
        elif not joiner:
            parts.append(("t", ch))
    return parts

def apple_emoji(seq):
    """Emoji de iPhone (PNG Apple) dacă există; altfel None."""
    cps = [f"{ord(c):x}" for c in seq]
    for cand in ("-".join(cps), "-".join(c for c in cps if c != "fe0f")):
        fp = os.path.join(APPLE, cand + ".png")
        if os.path.exists(fp):
            return Image.open(fp).convert("RGBA")
    return None

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
                e = apple_emoji(v)
                if e is None:
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
