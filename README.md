<
# Datheon Python Programming Internship

This repository contains projects completed as part of my Datheon Python Programming Internship.

## Task 1: Hangman Word Guessing Game

A command-line game where the player guesses a hidden word one letter at a time.

### Features
- Random word selection from `words.txt`
- Six incorrect attempts allowed
- Displays Hangman drawings
- Tracks guessed letters
- Prevents repeated guesses from reducing attempts
- Validates user input
- Displays win and lose messages

### Run the program
```bash
python hangman.py
```

### What I Learned
Python loops, conditional statements, sets, strings, functions, user input, and file handling.

## Task 2: Investment Portfolio Tracker

Additional Feature:
- Uses the S&P 500 company dataset (constituents.csv).
- Validates stock ticker symbols before accepting transactions.
- Current stock prices are entered manually.

### Features
- Enter stock ticker symbols, buy prices, share quantities, and current prices
- Calculate total invested amount
- Calculate current portfolio value
- Calculate profit or loss and percentage gain or loss
- Save results to a CSV file

### Run the program
```bash
python portfolio.py
```

**Note:** Current stock prices are entered manually.

## Technologies Used
- Python 3
- Dictionaries and loops
- Input validation
- File handling
- CSV module

## Project Files
- `hangman.py` — Hangman game logic
- `words.txt` — Word list
- `portfolio.py` — Portfolio tracker
- `portfolio_summary.csv` — Portfolio summary
- `README.md` — Project documentation

## Author
Madiha

## Task 3: Desktop File Organizer

**Description:**

Developed a Python utility to automatically organize files into categorized folders based on their file extensions.

**Features:**
- Automatically detects file extensions.
- Creates Documents, Images, Videos, Archives, and Code folders.
- Moves files into their appropriate folders.
- Prevents overwriting files with duplicate names.
- Handles permission and operating-system errors.
- Skips unsupported file types.
- Generates execution summaries.
- Records file movements and errors using Python logging.

**Technologies Used:**
- Python
- os
- shutil
- pathlib
- logging

**How to Run:**
```bash
python organizer.py
```

**Output:** Organized files are placed into category folders, and activity is recorded in `organizer.log`.

## Task 4: Rule-Based Customer Support Chatbot

### Description
A Python-based interactive chatbot that answers frequently asked customer-support questions using keyword matching and regular expressions.

### Features
- Greeting detection
- Business-hours information
- Internship project submission guidance
- Certificate information
- Multiple-intent matching
- Fallback responses for unknown questions
- Empty-input handling
- Clean exit using bye, exit, or quit
- FAQ data loaded from a JSON file
- Error handling for missing or invalid FAQ files

### Technologies Used
- Python 3
- JSON
- Regular Expressions (`re`)
- pathlib

### Files
- `chatbot.py` – Main chatbot application
- `sample_faq.json` – FAQ dataset

### How to Run
```bash
python chatbot.py
```

### Example
```text
You: hello
Bot: Hello! Welcome to customer support. How can I help you?

You: bye
Bot: Thank you for chatting. Goodbye!
```