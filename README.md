# Asteroids Game

A simple "Asteroids" game written in Python using the Pygame library. In this game, you control a spaceship that can rotate, shoot bullets, and avoid colliding with asteroids. When a bullet hits an asteroid, the asteroid may split into two smaller ones until it reaches a minimum size and is then destroyed. If an asteroid collides with the spaceship, the game ends. When all asteroids are cleared, you win the game.

## Features

- **Spaceship Control:**  
  Use the **A/D** keys to rotate and the **Spacebar** to shoot. A cooldown timer prevents shooting too frequently.

- **Asteroids:**  
  Asteroids spawn randomly at the edges of the screen and move toward the center. When hit by a bullet, an asteroid splits into two smaller ones if its size is above a defined minimum.

- **Scoring System:**  
  Points are awarded for destroying asteroids and are displayed in the top left corner of the screen.

- **Game Over and Victory:**  
  The game ends with a "Game Over!" message if an asteroid collides with your spaceship. If all asteroids are destroyed, you win.

## Project Structure

- **main.py** — The main file containing the game loop.
- **constants.py** — Contains global constants (screen dimensions, asteroid parameters, shooting speed, etc.).
- **circleshape.py** — Base class for circular objects (used for collision detection).
- **player.py** — Defines the Player class, handling ship control and shooting.
- **asteroid.py** — Defines the Asteroid class, responsible for rendering, movement, and splitting.
- **asteroidfield.py** — Manages asteroid spawning.
- **shot.py** — Defines the Shot class for bullets, inheriting from CircleShape.

## Requirements

- Python 3.x
- Pygame  
  Install via pip: