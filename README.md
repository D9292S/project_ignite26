# IGNITE - Week 1 Python Projects

[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)

Welcome to the IGNITE Week 1 repository containing simple interactive Python scripts.

## Project Directory Structure

```
IGNITE/
├── week1/
│   ├── week_1_1.py      # KBC (Kaun Banega Crorepati) Game
│   └── week_1_2.py      # Birthday Days Calculator
├── .gitignore           # Python Gitignore file
└── README.md            # Project description
```

---

## 1. KBC Game (`week1/week_1_1.py`)

A command-line trivia game modeled after **Kaun Banega Crorepati** (Who Wants to Be a Millionaire).

### Features
* **5 Questions**: Multiple-choice trivia questions with increasing prize money.
* **Prize Money Progression**: Starts at Rs. 1,000 up to Rs. 100,000.
* **Score Tracking**: Tracks correct answers.
* **50-50 Lifeline**: A one-time lifeline that randomly eliminates two incorrect options, leaving the correct option and one remaining incorrect option.
* **Safe Walk Away**: If you answer incorrectly, the game ends, and you take home the prize money won from your last correct answer.

### How to Run
```bash
python week1/week_1_1.py
```

---

## 2. Birthday Days Calculator (`week1/week_1_2.py`)

A utility script that calculates the exact number of days remaining until your next birthday.

### Features
* Accepts birthday input in `DD-MM` format.
* Accounts for leap years (handling February 29th in non-leap years by resolving to March 1st).
* Tells you if it's your birthday today!

### How to Run
```bash
python week1/week_1_2.py
```
