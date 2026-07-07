# Tasks: Arkanoid Implementation

## 1. Project Scaffolding

- [ ] 1.1 Create project directory structure (`src/`, `assets/`, `levels/`, `tests/`)
- [ ] 1.2 Init `pyproject.toml` / `requirements.txt` with dependencies (pygame, pyyaml, requests)
- [ ] 1.3 Create `main.py` with basic Pygame window (event loop, 800×600)

## 2. Core Architecture — Game Loop & State Machine

- [ ] 2.1 Implement `Game` class with state machine (MENU → PLAYING → PAUSED → GAME_OVER)
- [ ] 2.2 Implement `update(dt)` and `draw(screen)` on each entity
- [ ] 2.3 Implement `Paddle` class — keyboard input (←, →), position, width
- [ ] 2.4 Implement `Ball` class — position, velocity, movement, reset after loss

## 3. Physics & Collisions

- [ ] 3.1 Implement AABB collision detection between ball and paddle
- [ ] 3.2 Implement angled reflection on paddle (offset-based)
- [ ] 3.3 Implement ball ↔ brick collision with side detection
- [ ] 3.4 Implement wall bouncing (top, left, right)
- [ ] 3.5 Implement bottom boundary — life loss / game over trigger

## 4. Game Entities — Bricks & Levels

- [ ] 4.1 Implement `Brick` class with `hp`, `max_hp`, color interpolation
- [ ] 4.2 Implement brick types: normal, strong, bonus, indestructible
- [ ] 4.3 Implement level loader from YAML config (`levels/level_01.yaml`)
- [ ] 4.4 Implement level progression — load next level after clear
- [ ] 4.5 Implement transition screen ("LEVEL CLEAR!" for 2 sec)

## 5. Scoring & UI

- [ ] 5.1 Implement score accumulation (per-brick points by type)
- [ ] 5.2 Display score on screen (top-left HUD)
- [ ] 5.3 Display remaining lives as icons
- [ ] 5.4 Implement game-over screen with final score display

## 6. Bonuses & Power-ups

- [ ] 6.1 Implement bonus drop system — falling object from bonus bricks
- [ ] 6.2 Implement `Wide` — paddle width ×1.5 for 10s
- [ ] 6.3 Implement `Slow` — ball speed ×0.7 for 8s
- [ ] 6.4 Implement `Multi` — second ball on screen
- [ ] 6.5 Implement `Sticky` — ball sticks to paddle (launch on space)
- [ ] 6.6 Implement bonus timer tracking — effects expire after duration

## 7. Persistence — Local Leaderboard

- [ ] 7.1 Implement `Leaderboard` class — save/load `leaderboard.json`
- [ ] 7.2 Implement top-10 sorting and display on game-over screen
- [ ] 7.3 Implement name entry (3-char input) after game over
- [ ] 7.4 Handle file corruption gracefully — fallback to empty

## 8. Leaderboard Client — HTTP Integration

- [ ] 8.1 Implement `LeaderboardClient` class with `submit_score()` and `get_top()`
- [ ] 8.2 Implement fallback — local-only mode, no crash on network error
- [ ] 8.3 Configurable server URL via `LEADERBOARD_URL` env / config

## 9. Build & Distribution

- [ ] 9.1 Create `build.sh` / `build.bat` — PyInstaller commands
- [ ] 9.2 Verify Windows build (`.exe` — onefile, windowed)
- [ ] 9.3 Verify Linux build (binary — standalone)
- [ ] 9.4 Add README with build + run instructions

## 10. Polish & Extras

- [ ] 10.1 Add unit tests for core logic (collision, scoring, states)
- [ ] 10.2 Add level difficulty progression (more bricks per level)
- [ ] 10.3 Add visual polish — colours, fonts, transitions