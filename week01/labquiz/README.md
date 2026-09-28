# Week 1 Lab: Student Introduction Card

## Overview
This program collects 5 key pieces of information from the student (Name, Student ID, Department, GitHub Username, Programming Goal) using Python's `input()` function and prints a formatted student introduction card using f-strings.

## Testing & Adjustments
* **Test Ran:** I tested the program with normal inputs as well as an empty input (boundary case) for the `name` field to verify edge-case behavior.
* **Change After Testing:** After the first test run, I adjusted the column spacing and borders in the f-string template to ensure all labels aligned neatly and the output card was clean and easy to read.

## Acceptance & Stretch Task Answers
* **`input()` vs `print()`:**
  * `input()` captures text from the user via the console and stores it as a `string`.
  * `print()` outputs and displays data, variables, or formatted strings onto the terminal.
* **Stretch Task (Empty Name):**
  * When the `name` prompt is left empty, the current program proceeds without error and leaves the `Name:` field blank on the card.
  * *Future Improvement:* A `while` loop or input validation can be implemented to ensure the user does not leave mandatory fields like `name` empty before generating the card.
  * 
