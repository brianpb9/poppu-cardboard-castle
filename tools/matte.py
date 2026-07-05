#!/usr/bin/env python3
"""Border flood-fill matting: removes the solid white background from a sprite
while preserving interior white/cream regions (e.g. Poppu's body). Free, local.

Usage: matte.py IN.png OUT.png [--thresh 236] [--pad 24] [--trim]
"""
import sys, collections
from PIL import Image, ImageFilter

def matte(src, dst, thresh=236, feather=0.6, trim=True, pad=16):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    px = im.load()
    # alpha starts fully opaque
    alpha = [255] * (w * h)
    def is_bg(r, g, b):
        # near-white AND low saturation (so pale-cream stays if it has hue,
        # but pure white bg goes). White bg from the model is ~248-255.
        return r >= thresh and g >= thresh and b >= thresh and \
               (max(r, g, b) - min(r, g, b)) <= 14
    # BFS flood from every border pixel that is background
    q = collections.deque()
    visited = bytearray(w * h)
    def push(x, y):
        i = y * w + x
        if not visited[i]:
            r, g, b = px[x, y]
            if is_bg(r, g, b):
                visited[i] = 1
                alpha[i] = 0
                q.append((x, y))
    for x in range(w):
        push(x, 0); push(x, h - 1)
    for y in range(h):
        push(0, y); push(w - 1, y)
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h:
                push(nx, ny)
    a = Image.frombytes("L", (w, h), bytes(alpha))
    # feather the alpha edge slightly to kill jaggies + 1px erode to kill halo
    a = a.filter(ImageFilter.MinFilter(3))          # erode 1px -> removes white fringe
    if feather:
        a = a.filter(ImageFilter.GaussianBlur(feather))
    out = im.convert("RGBA")
    out.putalpha(a)
    if trim:
        bbox = out.getbbox()
        if bbox:
            l, t, r, b = bbox
            l = max(0, l - pad); t = max(0, t - pad)
            r = min(w, r + pad); b = min(h, b + pad)
            out = out.crop((l, t, r, b))
    out.save(dst)
    return out.size

if __name__ == "__main__":
    args = sys.argv[1:]
    src, dst = args[0], args[1]
    thresh = 236; pad = 16; trim = True
    if "--thresh" in args: thresh = int(args[args.index("--thresh")+1])
    if "--pad" in args: pad = int(args[args.index("--pad")+1])
    if "--no-trim" in args: trim = False
    print(matte(src, dst, thresh=thresh, pad=pad, trim=trim))
