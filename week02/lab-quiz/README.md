# Lab 02 - Purchase Quote

This program calculates the final total for two items, including subtotal, tax, and delivery fee.

## Why convert input() before arithmetic?
The `input()` function returns data as a string. In Python, you cannot perform mathematical calculations on strings. For example, multiplying a string repeats the text instead of doing math (`"5" * 2` becomes `"55"`). We must convert inputs using `int()` for quantities and `float()` for money values to calculate prices correctly.

## Test Results and Improvements
- **Test:** Ran the program with 2 x 50 TRY and 1 x 80 TRY, 20 TRY delivery fee, and 10% tax. The output was 218.00 TRY, matching the expected total.
- **Change:** Added `:.2f` formatting to currency outputs so numbers always display with two decimal places.

## Stretch Task
- **Error:** Entering letters for quantity causes a `ValueError` because text cannot be converted into an integer.
- **Improvement:** In a future version, this can be handled using a `try-except` block inside a loop to keep prompting the user until a valid number is entered.
