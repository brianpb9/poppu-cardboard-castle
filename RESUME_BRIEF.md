# RESUME_BRIEF.md — GAME-1ED823 Poppu Cardboard Castle v2
## Auto-generated 2026-07-06 03:32 WIB | Resume at 5am WIB

## STATUS
- Session sebelumnya (cardboard-v2) generate 22 assets + validasi test asset, lalu kena rate limit
- Sekarang 22 assets + 1 FAL Poppu sudah di-matte ke RGBA

## ASSETS SUDAH SIAP (RGBA, siap pakai)
### Backgrounds (WebP, 576×1024):
- assets/bg-craft-table.webp ✅
- assets/bg-play-room.webp ✅
- assets/bg-celebration.webp ✅

### Cardboard Pieces (RGBA, sudah matte):
- assets/piece-box-brown-rgba.png ✅ (771×782)
- assets/piece-triangle-yellow-rgba.png ✅ (896×801)
- assets/piece-cylinder-purple-rgba.png ✅ (459×960)
- assets/piece-cone-pink-rgba.png ✅ (757×848)
- assets/piece-arch-brown-rgba.png ✅ (1010×911)
- assets/piece-wall-brown-rgba.png ✅ (780×802)

### Characters (RGBA):
- assets/peeky-tutorial-rgba.png ✅ (813×860)
- assets/puffy-sticker-rgba.png ✅ (884×852)
- assets/poppu-play-rgba.png ✅ (712×829) — FAL-generated, cream body, brown hat, green backpack, gold compass, pink cheeks, EXCITED JUMPING POSE. Tail tip is cream (should be mint — minor, acceptable for now)

### Combined Sprites (RGB, perlu di-slice atau dipakai sebagai sprite sheet):
- assets/candies-all.png (1024×1024) — 4 candy types in one sheet
- assets/stickers-set1.png (1024×1024) — stickers batch 1
- assets/stickers-set2.png (1024×1024) — stickers batch 2
- assets/ui-set1.png (1024×1024) — UI elements batch 1
- assets/ui-set2.png (1024×1024) — UI elements batch 2

### UI:
- assets/ui-star-empty.png ✅

## ASSETS MASIH MISSING (generate via Higgsfield gpt_image_2):
- piece-box-red.png, piece-box-blue.png — RED/BLUE color variants of existing box
- piece-triangle-green.png — GREEN variant of triangle
- piece-cylinder-orange.png — ORANGE variant of cylinder
- piece-cone-teal.png — TEAL variant of cone

## WHAT TO DO NOW
1. **Phase A — Generate 5 missing piece variants** via Higgsfield (5 credits). Just color variants — use same prompts as existing pieces but change color.
2. **Phase B — Slice sprite sheets** — extract individual candies (4) and stickers (8) from combined sheets using canvas cropping
3. **Phase C — Build complete index.html** with:
   - Asset manifest referencing ALL RGBA assets + combined sheets
   - Procedural fallback for any missing asset
   - All 10 levels (Tiny Hut → Royal Castle)
   - 3 phases: BUILD (drag-drop with snap physics) → DECORATE (paint + stickers) → PLAY (candy collection, 20s timer)
   - Level select screen with star display
   - **Level 1 ALWAYS UNLOCKED** (critical fix from v1 rejection)
   - Web Audio API for all sounds
   - Touch + mouse support
   - localStorage for progress
   - Smooth 60fps, 720×1280 virtual coordinate system
4. **Phase D — QA** — test all 10 levels end-to-end
5. **Phase E — Deploy** — Vercel deploy

## REFERENCE FILES
- CLAUDE.md — full game spec
- UPGRADE_BRIEF.md — v1→v2 upgrade details
- tools/matte.py — border flood-fill matting (preserves interior whites)
- index.html — current v1 (procedural, DO NOT REUSE — needs full rewrite)
- index-v1-backup.html — backup of original v1

## TARGET
8.5+ Review Board WIN vs Toca Boca / Sago Mini
