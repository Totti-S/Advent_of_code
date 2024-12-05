# Advent_of_code

Here is my repo for all solutions I have crafted for all years. All are done using python.

This has been good learning experience. At first (2022) the challange was to not use any imports in.
2023 I did the same thing, but only limiting myself to not use external libraries. 2024 It's basically
free to use whatever I please, but I am still not using numpy (Written in day5), although it would help.
Don't feel like it.  

While 2023 year was ongoing, i started to make quality of life improvements, how my code works:
    - Made script that makes me set of text templates for data, tests and the python script file.
    - Automatic data parses: Ability to get data in a list and convert everything to integer if need be.

Utilities 2024:
    - Small snippets of over and over used codes to own `helper_funs.py` file
    - Test framework: If test files have something in them, will automatically test and compares to
                      User given expected values. This warns the user if the script dosen't work as intended.
                      Works by capturing print and finding silver and gold values from prints.
    - 2D grids are coming some day: Made my own class implementation. Works with tuples as well


## What I have learned over the year with python
- Learned to use regex
- Made a test framework
- I knew how to make this, but first time implemented plenty of dunder methods to a class
- I think I used "deque" in a puzzle
- Day 7 2022: Although not proper file tree like in os, made basically simple one in this puzzle
- Day 11 2022: Little Mod related math