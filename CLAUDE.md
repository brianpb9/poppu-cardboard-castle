# Poppu Cardboard Castle — CLAUDE.md

## Game Overview
**Poppu Cardboard Castle** is a creative builder game for kids 3-7. Three phases per level:
1. **BUILD** — Drag cardboard pieces onto a template to construct a castle
2. **DECORATE** — Free-form decoration with paint, stickers, flags
3. **PLAY** — Poppu enters the castle, candies fall, tap to collect (20s timer)

## Visual Style
- **Cardboard texture**: brown kraft paper with visible corrugation, tape strips, crayon marks
- **Crayon colors**: wax-textured, slightly rough, kid-drawn aesthetic (red, blue, yellow, green, purple)
- **Nostalgic 2000s flash game style**: chunky UI, playful fonts, bouncy animations
- **Background**: craft table / construction paper backdrop
- **NO SVG/CSS art** — all visual elements are illustrated PNG assets (Higgsfield gpt_image_2)

## Characters (Poppu World IP)
- **Poppu**: cream fox (#F6EAD6), mint ears/tail, explorer hat, green backpack, gold star compass, pink cheeks — appears in PLAY phase
- **Peeky**: yellow chick — tutorial guide in BUILD phase
- **Puffy**: cloud sheep — sticker in DECORATE phase

## Game Structure: 3 Phases × 10 Levels

### Phase 1: BUILD (drag-drop)
- Template outline of castle shown on screen (dotted line silhouette)
- Pieces at bottom: boxes, triangles, cylinders, cones (4-8 pieces per level)
- Drag piece from tray to template position
- Snap-to-grid with tolerance
- If piece tilted >15° → funny collapse animation (pieces scatter + wobble)
- Progress bar: X/8 pieces placed
- Level themes (10 levels):
  1. Tiny Hut (3 pieces) — tutorial
  2. Watchtower (4 pieces)
  3. Cottage (5 pieces)  
  4. Farmhouse (5 pieces)
  5. Twin Towers (6 pieces)
  6. Bridge Gate (6 pieces)
  7. Grand Hall (7 pieces)
  8. Spiral Tower (7 pieces)
  9. Fortress (8 pieces)
  10. Royal Castle (8 pieces)

### Phase 2: DECORATE (free-form)
- Castle built in Phase 1 remains on screen
- Tools: paintbrush (4 colors), sticker tray (8 stickers), flag pole, banner
- Tap color → tap castle area to paint
- Drag sticker from tray to surface
- No right/wrong — child-directed creativity
- "Done" button → save decorated castle → proceed

### Phase 3: PLAY (20s candy collection)
- Poppu enters the decorated castle
- Candies fall from ceiling (lollipops, gummies, chocolates)
- Tap to collect (+1 point each)
- Sparkle + score popup on tap
- 20 second timer with visual countdown
- Score: X/XX candies collected
- Star rating: 1★ (5+), 2★ (10+), 3★ (15+)

## Audio
- **Web Audio API** — generate all sounds programmatically (no audio files)
- BUILD: cardboard rustle, snap-into-place chime, collapse crash
- DECORATE: brush stroke, sticker peel, happy chime on done
- PLAY: candy drop, collect pop, countdown tick (last 5s), celebration fanfare
- Background: soft lo-fi toy piano loop

## Technical Requirements
- **Single index.html** — everything inline (CSS + JS)
- **Vanilla JS** — no frameworks, no build tools
- **Canvas 2D** — all rendering via Canvas API
- **Asset manifest + procedural fallback**: try load Image PNG → onerror use procedural placeholder
- **Mobile-first**: touch events + mouse fallback, responsive canvas
- **localStorage**: save decorated castle screenshots, high scores, star collection
- **No fail state**: no timer pressure in BUILD/DECORATE, no losing in PLAY
- **Monetization hooks**: ad break trigger between levels (after level 3 and 7), IAP "Unlock All" button (UI only, no payment integration)

## Asset List (Higgsfield gpt_image_2)
All assets should have cardboard texture + crayon color aesthetic.

### Backgrounds (3 total)
1. `bg-craft-table.jpg` — craft table with scissors, tape, crayons scattered
2. `bg-play-room.jpg` — cozy playroom, toy chest in corner
3. `bg-celebration.jpg` — confetti + bunting for level complete

### Cardboard Pieces (20+ total)
- `piece-box-brown.png`, `piece-box-red.png`, `piece-box-blue.png`
- `piece-triangle-yellow.png`, `piece-triangle-green.png`
- `piece-cylinder-purple.png`, `piece-cylinder-orange.png`
- `piece-cone-pink.png`, `piece-cone-teal.png`
- `piece-arch-brown.png`, `piece-wall-brown.png`
- `piece-roof-triangle.png`, `piece-tower-cylinder.png`
- `piece-flag-pole.png`, `piece-door-arch.png`

### Characters
- `poppu-play.png` — Poppu excited, arms up (reference: poppu-official-reference-sheet.png)
- `peeky-tutorial.png` — Peeky pointing/waving
- `puffy-sticker.png` — Puffy cloud sheep sticker

### Stickers (8)
- `sticker-star.png`, `sticker-heart.png`, `sticker-flower.png`
- `sticker-puffy.png` (Puffy character), `sticker-crown.png`
- `sticker-rainbow.png`, `sticker-butterfly.png`, `sticker-sun.png`

### UI Elements
- `ui-piece-tray.png` — tray background for piece selection
- `ui-button-done.png` — "Done" button
- `ui-star-filled.png`, `ui-star-empty.png`
- `ui-timer-bg.png` — timer background
- `candy-lollipop.png`, `candy-gummy.png`, `candy-chocolate.png`
- `particle-sparkle.png` — sparkle particle for collect effect

### Template Outlines
- Per level: `template-lvl1.png` through `template-lvl10.png` — dotted outlines showing piece placement

## Game States
```
START_SCREEN → LEVEL_SELECT → BUILD_PHASE → DECORATE_PHASE → PLAY_PHASE → RESULT_SCREEN
                                                                                    ↓
                                                                           LEVEL_SELECT (next)
```

## Quality Bar
- **Target**: 9/10 Studio Review Board verdict
- **Benchmark**: Toca Boca / Sago Mini
- **Non-negotiable**: No procedural canvas art, all illustrated PNG, smooth 60fps, toddler-friendly touch targets (min 60px)
- **Polished animation**: ease-in-out transitions, bounce on snap, particles on collect
- **No bugs**: test all drag-drop edge cases, touch + mouse, rapid tapping

## Build Priority
1. Phase 1 BUILD engine (drag-drop + physics collapse) — scaffold with procedural fallbacks
2. Phase 2 DECORATE engine (paint + stickers) — scaffold with procedural fallbacks
3. Phase 3 PLAY engine (candy drop + collect + timer)
4. All 3 phases wired together in game loop
5. 10 levels with unique templates
6. Asset manifest → Higgsfield art pipeline
7. Polish: animations, particles, audio, UI
8. Mobile testing, localStorage, monetization hooks
