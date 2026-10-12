# Week 4 Lab: Savings Goal Planner

## Overview
This program calculates monthly savings growth based on user inputs (starting balance, monthly deposit, interest rate, and savings goal). It prints a monthly breakdown and stops early when the target balance is achieved or after 60 months.

## Testing & Adjustments
* **Test Ran:** I tested the simulation with a starting balance of 1000, monthly deposit of 500, interest rate of 1%, and a goal of 3000. It successfully stopped at month 4 with a final balance of 3070.80 and 70.80 total interest earned.
* **Change After Testing:** After testing boundary conditions, I added an initial check before the simulation loop to immediately detect if the starting balance already meets the goal, preventing unnecessary table rows from printing.