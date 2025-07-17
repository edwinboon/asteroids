# 🚀 Asteroids Game

A classic Asteroids-style game built with Python and Pygame. Navigate through space, dodge asteroids, and shoot them to survive!

## 🎮 Game Features

- **Classic Asteroids gameplay** - Control a spaceship in a 2D space environment
- **Asteroid splitting mechanics** - Large asteroids break into smaller pieces when shot
- **Collision detection** - Realistic collision between player, asteroids, and shots
- **Smooth 60 FPS gameplay** - Responsive controls and fluid movement
- **Space physics simulation** - Momentum-based movement system

## 🕹️ How to Play

- **Move**: Use arrow keys or WASD to control your spaceship
- **Shoot**: Press spacebar to fire shots at asteroids
- **Objective**: Survive as long as possible by avoiding and destroying asteroids
- **Game Over**: The game ends when your ship collides with an asteroid

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- uv (Ultra-fast Python package manager)

### Setup

1. Install uv if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone this repository:

```bash
git clone <your-repo-url>
cd asteroids-game
```

3. Create a virtual environment and install dependencies:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv add pygame
```

4. Run the game:

```bash
python main.py
```

### Alternative Installation (using uv run)

You can also run the game directly without activating the virtual environment:

```bash
uv run python main.py
```

## 📁 Project Structure

```
asteroids-game/
├── main.py           # Main game loop and initialization
├── player.py         # Player spaceship class
├── asteroid.py       # Asteroid objects and behavior
├── asteroidfield.py  # Asteroid spawning system
├── shot.py           # Projectile mechanics
├── constants.py      # Game configuration and settings
├── pyproject.toml    # Project dependencies (uv)
└── README.md         # This file
```

## 🎯 Game Mechanics

### Player Ship

- Rotates smoothly with user input
- Momentum-based movement (thrust to accelerate)
- Can fire projectiles to destroy asteroids

### Asteroids

- Spawn at screen edges and move across the field
- Split into smaller asteroids when hit
- Collision detection with player and shots

### Shooting System

- Limited or unlimited ammo (configurable)
- Projectiles have realistic physics
- Shots destroy asteroids on contact

## ⚙️ Configuration

Game settings can be modified in `constants.py`:

- Screen dimensions (width/height)
- Game speed and physics parameters
- Asteroid spawn rates
- Player ship characteristics

## 🚀 Future Enhancements

- [ ] Score system
- [ ] Multiple lives
- [ ] Power-ups and upgrades
- [ ] Sound effects and music
- [ ] High score leaderboard
- [ ] Different asteroid types
- [ ] Particle effects
- [ ] Menu system

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make sure you have uv installed and dependencies set up (`uv sync`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎮 Screenshots

_(Add screenshots of your game in action here)_

## 🐛 Known Issues

- Game exits immediately on collision (no restart option)
- No pause functionality
- No save/load game state

## 👨‍💻 Developer

Created by **edwinboon** - _2025_

---

_Enjoy playing and feel free to contribute to make this game even better!_ 🌟
