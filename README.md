# 🐍 Snake Game — Built with Python & Pygame



# Overview

A fully functional Snake game built from scratch using Pygame.
This project is less about just building a game and more about mastering the logic behind it — movement, collisions, and real-time updates.🎮

# Tech Stack
Python
Pygame
Random / Time modules

# Features
🎯 Dynamic snake movement
🍎 Random fruit generation
📈 Score tracking system
💀 Collision detection (walls & self)
⏱️ Real-time game loop
🧾 Game over screen
🎹 Controls

# Key	Action
⬆️	Move Up
⬇️	Move Down
⬅️	Move Left
➡️	Move Right

# How It Works (Behind the Scenes)
The snake is stored as a list of coordinates
Each frame:
A new head is added based on direction
The tail is removed (unless fruit is eaten)
Collision checks run every frame:
Boundary check
Self-collision check
Game runs inside a continuous game loop controlled by FPS

# What I Learned 
How a game loop actually works in practice
Handling real-time keyboard input
Structuring logic for movement & growth
Writing clean collision detection
Debugging logic issues (this humbled me fr 😅)
🚀 Future Improvements
🔊 Sound effects & background music
🧠 Smarter difficulty scaling
🏆 High score saving system
⏸️ Pause / Resume feature
🎨 UI improvements (menus, restart button)
🌐 Convert to web version (Pyodide / JS)
▶️ Getting Started
1. Clone the repo
git clone https://github.com/your-username/snake-game.git
cd snake-game
2. Install dependencies
pip install pygame
3. Run the game
python snake.py

# Preview📸 



# Final Thoughts

This project was mainly about understanding the core logic of games, not just building one.
Simple idea, but implementing it cleanly? That’s where the real learning happened.
