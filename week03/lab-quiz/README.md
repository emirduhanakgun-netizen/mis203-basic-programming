# Week 03 Lab - Order Approval Policy

This program checks customer orders based on available stock and applies a 10% discount for members who spend at least 500 TRY.

## Boundary Test Table

| Test Case | Order Amount (TRY) | Available Stock | Requested Quantity | Member? | Expected Status | Final Price |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Below 500** | 490 | 10 | 2 | yes | Approved | 490.00 |
| **Exactly 500** | 500 | 10 | 1 | yes | Approved | 450.00 |
| **Above 500** | 600 | 10 | 3 | yes | Approved | 540.00 |
| **Not a Member** | 550 | 10 | 2 | no | Approved | 550.00 |
| **Not Enough Stock** | 300 | 2 | 5 | yes | Rejected | None |

## Notes
* **Test Run:** Tested with 500 TRY and member set to "yes" to make sure the boundary condition (>= 500) gives the discount correctly.
* **Changed After Testing:** I added a check for 0 or negative quantities so the code shows an invalid quantity message.