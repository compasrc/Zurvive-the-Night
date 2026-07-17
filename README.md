# ZURVIVE THE NIGHT

This project is a 2D top-down zombie shooter focused on wave-based survival and dynamic gameplay. Players fight through five increasingly difficult waves of enemies, ending in a final boss battle.

The game features procedurally generated obstacles, creating a unique playfield each run and encouraging adaptability. Players can choose between three distinct weapon types—balanced, rapid fire, and heavy cannon—each offering different trade-offs in speed, damage, and ammo capacity.

Throughout the game, collectible power-ups such as health, ammo, shields, damage boosts, and fire rate enhancements spawn randomly, providing strategic advantages and increasing survivability.

The project is built using a modular Python architecture, with separate systems for enemy management, player control, rendering, and game logic, making the codebase scalable and maintainable.

## Mission Statement:

Our goal with Zurvive the Night is to create a fast-paced, replayable zombie survival game that challenges players through dynamic gameplay and procedural design. We aim to build a clean, modular codebase that is easy to extend while delivering an engaging and polished player experience.

## Development Overview:

During this project, we expanded and improved the base game by adding a full enemy wave-based system, final boss, and multiple weapon types with distinct mechanics. We implemented procedurally generated obstacles to increase replayability and added power-ups to create more dynamic gameplay.

We also improved the user interface with a title screen, pause menu, and improved HUD. Additionally, we refined player movement, fixed gameplay bugs (such as player drift and early wave damage issues), and enhanced visuals with sprite animations and sound effects.

Some features we considered but did not fully implement include additional enemy types, more advanced boss mechanics, infinite waves, a slower difficulty ramp, and settings options (mute, volume, keybinds, etc.).

## Features/Changes Made:

- Wave-based enemy system with increasing difficulty
- Final boss battle on wave 5
- Procedurally generated obstacles for unique gameplay
- Three weapon types with distinct playstyles:
    - Balanced – moderate speed, fire rate, and damage
    - Rapid Fire – high speed and fire rate, low damage
    - Heavy Cannon – high damage, slower movement and fire rate
- Randomly spawning power-ups:
    - Health
    - Ammo
    - Shield
    - Damage boost
    - Fire rate boost
    - Sprite-based animations using sprite sheets

## Testing Procedure:

We used manual testing to verify the game. Each test includes actions and expected results.

### Movement
Action: Move using WASD or arrow keys  
Expected: Player moves in the correct direction smoothly

### Shooting
Action: Press Space  
Expected: Player shoots and ammo decreases

### Reload
Action: Press R  
Expected: Ammo refills and player cannot shoot while reloading

### Weapon Switching
Action: Press 1, 2, 3  
Expected: Weapon changes and stats update

### Enemies & Waves
Action: Play through waves  
Expected: Enemies increase and get harder each wave and boss appears on wave 5

### Collision
Action: Touch enemies or obstacles  
Expected: Player takes damage from enemies and cannot pass through obstacles

### Power-Ups
Action: Collect power-ups  
Expected: Effects apply correctly (health, ammo, shield, damage, fire rate)

### Game Controls
Action: Press P/Esc, Enter, Ctrl+R  
Expected: Pause/resume works, game starts, and resets properly

### Debug
Action: Press I, F1  
Expected: Invincibility toggles and debug overlay appears

## How to Run

You can run the game in two ways:

### Option A: Run a Prebuilt Windows Executable (No Install Required)

This option only works if a prebuilt release zip is provided separately (for example, in GitHub Releases or a shared download link).

1. Download and extract the shared build folder zip.
2. Open dist/CallOfZombieDuty.
3. Double-click CallOfZombieDuty.exe.

You do not need Python, pygame, or an IDE for this option.

Note: The executable is not stored in this source repository by default.

### Option B: Run from Source Code

1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Install dependency:
    - python -m pip install pygame
4. Start the game:
    - python main.py

If your system uses py instead of python, run these instead:
- py -m pip install pygame
- py main.py

## Technologies Used:

- Python
- Pygame

## Controls
- Arrow keys / `WASD`: move (top-down)
- `Space`: shoot projectile
- `R`: reload
- `1` / `2` / `3`: weapon choice (Balanced / Rapid Fire / Heavy Cannon)
- `P` / `Esc`: pause / resume
- Left Mouse Click: interact with UI (pause menu, title screen)
- `Enter`: start game (from title screen)
- `C`: cycle control scheme (WASD / arrows)
- `Ctrl` + `R`: reset game
- `I`: invincibilty for debug
- `F1`: toggle debug overlay

## Authors/Contributions:

- Quinn Hasselgren
    - Wave/Enemy System
    - Power-ups
    - Obstacles
    - Title Screen/Pause Menu
    - Playfield design with tombstones as obstacles
    - Got rid of previous bounds and feel presets
    - Main Menu/Level Music, Sound effects
    - Weapon section of HUD
    - Rebalanced weapons
    - Rethemed menu messages
- Ryan Compas
    - Fixed player drift
    - Graphics/animations (enemy/player sprites, movement, idle, death, weapon)
    - Fixed missing sprites/sounds/music in the packaged Windows build
    - Added a shared asset-path resolver for source and PyInstaller runs
    - Updated build spec and verified assets are bundled in release output
- Khumoyun Abdulpattoev
    - Damage
    - Health bar
    - Weapon mechanics (more ammo with each wave and more power for the Boss fight)
    - Fixed damage issue in first wave
    - HUD Design
    - Death/victory animations

## Tombstone PNG Credit:

- tombstone1.png: https://www.shutterstock.com/image-vector/gravestone-pixel-art-set-objects-tombstone-2683992699
- tombstone2.png: https://www.shutterstock.com/image-vector/gravestone-pixel-art-set-objects-tombstone-2683992699
- tombstone3.png: https://www.shutterstock.com/image-vector/gravestone-pixel-art-set-objects-tombstone-2683992699
- tombstone4.png: https://www.shutterstock.com/image-vector/gravestone-pixel-art-set-objects-tombstone-2683992699
- tombstone5.png: https://www.shutterstock.com/image-vector/gravestone-pixel-art-set-objects-tombstone-2683992699

## Sound Effect Credits (Royalty-Free):

- main_music.mp3: https://pixabay.com/music/mystery-electro-zombies-371569/
- level_music.mp3: https://pixabay.com/music/fantasy-dreamy-childrens-plagued-bastion-survival-undead-haven-477915/
- boss_zombie.mp3: https://pixabay.com/sound-effects/horror-zombie-3-106344/
- zombie_death.mp3: https://pixabay.com/sound-effects/zombie-15965/
- death.mp3: https://pixabay.com/sound-effects/horror-male-death-sound-128357/
- powerup.mp3: https://pixabay.com/sound-effects/film-special-effects-video-game-power-up-sound-effect-384657/
- assault-rifle.mp3: https://pixabay.com/sound-effects/film-special-effects-single-pistol-gunshot-42-40781/
- hurt.mp3: https://pixabay.com/sound-effects/film-special-effects-retro-hurt-2-236675/

## Sprite Sheets and Animations
- Zombie assets courtesy of Kadodey: https://kadodey.itch.io/zombie-sprite
- Player assets courtesy of TheLazyStone: https://thelazystone.itch.io/post-apocalypse-pixel-art-asset-pack
