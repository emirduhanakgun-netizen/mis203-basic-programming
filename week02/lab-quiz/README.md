# Lab 02 - Purchase Quote Program

This program calculates a two-item purchase quote by taking item names, quantities, unit prices, delivery fee, and tax percentage from the user.

## Acceptance Checks & Conceptual Questions

### Why `input()` must be converted before arithmetic?
The `input()` function in Python always captures user data as a `string` (text). In Python, arithmetic operations behave differently or fail on strings:
- Multiplying a string duplicates text (e.g., `'10' * 2 = '1010'`).
- Adding strings concatenates them rather than summing numerical values.

Therefore, explicit type conversion using `int()` for quantities and `float()` for monetary values is necessary to perform mathematical calculations.

## Testing & Changes

- **Test Run:** Tested with Item 1 (2 x 50 TRY), Item 2 (1 x 80 TRY), Delivery (20 TRY), and Tax (10%). Subtotal was calculated as 180.00 TRY, Tax as 18.00 TRY, resulting in an expected final total of 218.00 TRY.
- **Change Made After Testing:** Formatted all monetary outputs using `:.2f` to ensure values consistently print with exactly two decimal places (e.g., `218.00 TRY` instead of `218.0 TRY`).

## Stretch Task: Error Handling

- **Error Observed:** Entering non-numeric characters (e.g., letters) for the quantity input raises a `ValueError: invalid literal for int() with base 10: ...` and terminates the program execution.
- **Handling in Later Versions:** This can be handled gracefully by enclosing user inputs inside a `try-except ValueError` block combined with a `while` loop, reprompting the user until valid numeric input is provided.
  
