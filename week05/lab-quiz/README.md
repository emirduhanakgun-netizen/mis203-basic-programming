# Week 5 Lab: Reusable Shipping Quote

## Test and Change
- **Test:** I tested the discount threshold with `assert get_discount_rate(100) == 0.10`.
- **Change:** At first I wrote `subtotal > 100`, so exactly 100 was not getting the discount. I changed it to `subtotal >= 100`.

## Print vs Return
- `return` gives the value back so we can use it in other variables and calculations.
- `print` only prints text on the console and cannot be used in further code.