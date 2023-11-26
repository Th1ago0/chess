# Python Chess Game

This is a simple command-line chess game implemented in Python. It allows two players to play a standard game of chess on the terminal.

## Features

- Full support for standard chess rules.
- Interactive and user-friendly interface.
- Player vs Player gameplay.
- The game provides error messages and prompts to ensure players make valid moves and impossible moves.
- Online multiplayer mode.

### Screenshot
![Chess board](../media/screenshot.jpg)

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system.

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Th1ago0/chess.git

2. Change your directory:
   ```bash
   cd chess

3. Start the game:
   ```bash
   python3 main.py

## How to use the multiplayer mode

I recommend to use ngrok for the server address

1. Choose the player.
   ```bash
   python3 main.py online p1

Use p1 to player1(server) and p2 to player2(client)

2. Provide the addresses.
   ```bash
   Host: "your host here"
   
   Port: "your port here"

And now you can play the multiplayer mode.

## How to play.

You only need to run the game and follow the chess rules.

- The game is played by two players.
- Each player takes turns to make a move.
- To make a move, enter the source and target squares ex: source = "e2" target = "e4".
- The game enforces standard chess rules, so make sure your moves are legal.

