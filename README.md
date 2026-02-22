# sigma-capstone-project

## Sigma Capstone Project: Hangman
A short program to run a game of Hangman in the terminal. This version features dynamic ASCII art.

## 🚀 Features
- **TUI:** text-based user interface
- **Visuals:** hand-drawn ASCII hangman stages that update as lives are lost
- **Validation:** built-in validation and prevention for double guessing
- **Difficulties:** choice of 3 difficult modes - easy (10 lives), medium (8 lives), hard (6 lives)
- **Word selection:** choice of word length from 5 to 14 letters, from a list of 5000 most common english words
- **Stats:** displays (every turn) game difficulty, correctly guessed letters, current state of hangman & all previously guessed letters 
- **Infinite replays**

NB: words list includes some words <5 letters long. This can be edited in the main logic if desired.

## 🛠 Installation
1. Clone the repo: "git clone [this repo](https://github.com/timkoh97/sigma-capstone-project.git)"
2. Navigate to the folder: "cd sigma-capstone-project"
3. Ensure Python 3.9+ is installed

## 🎮 How to play
Run the script using Python in the terminal:
"python3 hangman.py"
- choose a length of word to guess
- the game will choose a random word of that length
- choose a difficulty
- type one letter to guess (as prompted)
- try to guess the word before the hangman is fully constructed

## 💻 Technologies Used
Python 3.12 - game logic
Git / GitHub - version control, feature branching

## 🔮 Future Improvements
- **Scores:** Saves scores in each play session
- **Hint System:** Allow users to spend a "life" to reveal a letter.

## 👥 Contributors
Tim Koh

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Acknowledgements
The word list used in this project was provided by [Michael_Wehar](https://github.com/MichaelWehar). 
* Data Source: [Public-Domain-Word-Lists](https://github.com/MichaelWehar/Public-Domain-Word-Lists)
