# Poppu Cardboard Castle — UPGRADE BRIEF v1 → v2
## Task: GAME-1ED823 | Target: 8.5+ | Previous: 4.88

---

## WHY REBUILDING
Lex QC rejected v1 at **4.88/10** (threshold: 8.5). Three critical failures:

| Category | v1 Score | v2 Target |
|----------|---------|-----------|
| visual_polish | 7.0 → needs to hit 9.0 |
| stability | 4.5 → 9.0 |
| gameplay_depth | 4.5 → 9.0 |
| reward_loop | 4.5 → 9.0 |
| mobile_readiness | 4.5 → 9.0 |
| brand_fit | 4.5 → 9.0 |

**Root causes:**
1. **PROCEDURAL ART = BANNED.** v1 used all canvas procedural drawing (boxes, triangles, crayon lines). HDRV Studio OS PR-022/PR-023: ALL game objects MUST be illustrated PNG from Higgsfield gpt_image_2. No exceptions.
2. **Only 3/10 levels built.** v1 shipped scaffold (levels 1-3). Need all 10.
3. **Level 1 star-gating bug.** Level 1 required 1★ to unlock but player starts at 0★. Deadlock. MUST fix: Level 1 always unlocked.

---

## JANGAN DILAKUKAN
- ❌ JANGAN gunakan canvas procedural drawing untuk game objects (boxes, triangles, crayons)
- ❌ JANGAN pakai SVG atau CSS untuk art
- ❌ JANGAN gate Level 1 di belakang star requirement
- ❌ JANGAN kirim tanpa Higgsfield assets
- ❌ JANGAN skip QA — test semua 10 level end-to-end

---

## WHAT TO BUILD

### PHASE 0: Art Pipeline (Higgsfield gpt_image_2)
Generate ALL assets first, then build game code. Asset manifest + procedural fallback architecture (same pattern as Poppu Garden Whisper):

**Backgrounds (3):**
- `bg-craft-table.webp` — craft table with scissors, tape rolls, crayon box scattered, warm overhead light
- `bg-play-room.webp` — cozy playroom, toy chest in corner, window with sunlight
- `bg-celebration.webp` — confetti, bunting flags, "YOU DID IT!" feel

**Cardboard Pieces (12 types × variants):**
- `piece-box-brown.png`, `piece-box-red.png`, `piece-box-blue.png` — cardboard boxes with tape strips, corrugated edge visible
- `piece-triangle-yellow.png`, `piece-triangle-green.png` — triangle roof pieces, crayon-colored
- `piece-cylinder-purple.png`, `piece-cylinder-orange.png` — cylinder tower pieces, rolled cardboard look
- `piece-cone-pink.png`, `piece-cone-teal.png` — cone roof pieces
- `piece-arch-brown.png` — door archway piece
- `piece-wall-brown.png` — wall panel with window cutout

**Characters (3):**
- `poppu-play.png` — Poppu excited, arms up, jumping pose. Reference: `/Users/isjen/HDRV/01_HDRV-AI-Gaming-Studio-OS/assets/reference-sheets/poppu/poppu-official-reference-sheet.png`. Cream (#F6EAD6), mint ears/tail, brown explorer hat, green backpack, gold star compass, pink cheeks.
- `peeky-tutorial.png` — Peeky yellow chick, pointing/waving, cute expression
- `puffy-sticker.png` — Puffy cloud sheep, fluffy, round, sticker-style outline

**Stickers (8):**
- `sticker-star.png`, `sticker-heart.png`, `sticker-flower.png`, `sticker-puffy.png`, `sticker-crown.png`, `sticker-rainbow.png`, `sticker-butterfly.png`, `sticker-sun.png`
- All with white stroke outline + drop shadow (sticker look)

**Candies (4 types):**
- `candy-lollipop.png` — spiral lollipop, red+white swirl
- `candy-gummy.png` — colorful gummy bear
- `candy-chocolate.png` — chocolate square with wrapper
- `candy-star.png` — star-shaped candy

**UI Elements:**
- `ui-btn-done.png` — "Done!" button, crayon-style
- `ui-btn-next.png` — "Next →" button
- `ui-star-filled.png`, `ui-star-empty.png` — gold stars
- `ui-timer-bg.png` — timer bar background
- `ui-piece-tray.png` — wooden tray for piece selection
- `particle-sparkle.png` — sparkle for collect effects

**Template Outlines (10):**
- `template-lvl1.png` through `template-lvl10.png`
- Dotted-line silhouettes showing piece placement for each level
- Level 1: simple hut (3 pieces)
- Level 10: royal castle (8 pieces)

### PHASE 1: Game Engine (rebuild with assets)
Reuse v1's proven architecture:
- 720×1280 virtual coordinate system (responsive scaling)
- Touch + mouse input mapped to design space
- Canvas 2D with `ctx.drawImage()` for all assets
- Asset manifest + procedural fallback for every object
- Web Audio API for all sounds (no audio files)
- localStorage for progress/stars/stickers

### PHASE 2: BUILD Phase (10 levels)
**Must fix: drag-drop snap tolerance**
- Template outline always visible (dotted line from template PNG)
- Pieces in scrollable tray at bottom
- Drag from tray → snap to nearest template position (tolerance: 40px)
- If piece tilted >15° from correct rotation → funny collapse animation
- Progress counter: "X/8 pieces"

**Levels:**
1. Tiny Hut (3 pieces) — tutorial with Peeky
2. Watchtower (4 pieces)
3. Cottage (5 pieces)
4. Farmhouse (5 pieces, different shape)
5. Twin Towers (6 pieces)
6. Bridge Gate (6 pieces)
7. Grand Hall (7 pieces)
8. Spiral Tower (7 pieces)
9. Fortress (8 pieces)
10. Royal Castle (8 pieces)

### PHASE 3: DECORATE Phase
- Built castle from Phase 2 persists on screen
- Paint: 6 crayon colors (tap color → tap area to paint). Paint applies as tinted overlay on pieces.
- Stickers: 8 stickers in tray (drag to place on castle)
- Flag pole: tap to add flag to highest tower
- "Done" button → save decorated state → proceed to PLAY

### PHASE 4: PLAY Phase
- Poppu enters the decorated castle (appears at door)
- Candies fall from above castle: lollipops, gummies, chocolates, star candies
- Physics: gentle gravity, slight bounce on castle pieces
- Tap candy to collect → sparkle particle + "+1" popup + chime
- 20-second timer with visual countdown bar
- Score: X candies collected
- Star rating: ★ (5+), ★★ (10+), ★★★ (15+)

### PHASE 5: Polish & Systems
- **Level Select**: winding path, 10 nodes. Locked=grey, completed=color with stars shown
- **Level 1 ALWAYS UNLOCKED** (critical fix)
- **Sticker Book**: collected stickers viewable in menu
- **Star counter**: "X/30 stars" on level select
- **Celebration screen**: confetti + Poppu dancing on 3★
- **Monetization hooks**: ad-break prompt after levels 3 and 7 (UI only), "Unlock All" button (decorative)
- **Smooth 60fps** with requestAnimationFrame
- **Touch targets ≥ 60px**
- **Cardboard/crayon aesthetic** maintained throughout

---

## TARGET SCORE
**8.5+ Review Board WIN vs Toca Boca / Sago Mini**

Key metrics:
- Visual Language: Higgsfield illustrated → 9.0
- Gameplay Feel: drag-drop snap + collapse physics → 9.0
- Density: 10 levels × 3 phases = 30 distinct experiences → 9.0
- Character: Poppu + Peeky + Puffy, all illustrated → 9.0
- Polish: particles, animation, audio, celebration → 8.5+

---

## BUILD INSTRUCTIONS FOR CLAUDE CODE

1. Read CLAUDE.md for full game spec (already in project folder)
2. Read this UPGRADE_BRIEF.md for v2 changes
3. **Phase A — Validate 2:** Generate 2 test assets (one cardboard box, one Poppu pose) to validate gpt_image_2 style. If any issues, adjust prompts.
4. **Phase B — Batch Assets:** Generate ALL assets (backgrounds, pieces, characters, stickers, candies, UI, templates). Use 4-slot Higgsfield queue. Self-key checkerboards locally. Remove backgrounds for characters. Compress backgrounds to WebP q90.
5. **Phase C — Build Game:** Rewrite index.html with asset manifest + procedural fallback architecture. All 10 levels. Fix Level 1 gating. Build all 3 phases per level.
6. **Phase D — QA:** Test all levels end-to-end. Verify no JS errors. Verify touch + mouse. Verify 60fps.
7. **Phase E — Report:** List all generated assets, confirm 10 levels complete, confirm Level 1 unlocked.

Go.
