
🧮 Arithmetic Formatter

A lightweight Python utility that transforms addition and subtraction expressions into a clean, right-aligned, vertical and side-by-side layout, with an optional switch to include computed results.
---

📌 Objective

Implement the function:

arithmetic_arranger(problems, show_answers=False)

This function:
- Takes a list of strings representing arithmetic problems.
- Formats them vertically and side-by-side.
- Optionally displays the solutions.

---

✨ Example Usage

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

Output:
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

With results:
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

Output:
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474

---

⚠️ Validation Rules

The function returns meaningful error messages if the input is invalid:

- ❌ More than 5 problems:  
  Error: Too many problems.

- ❌ Invalid operator (only + or - are allowed):  
  Error: Operator must be '+' or '-'.

- ❌ Non-digit characters in operands:  
  Error: Numbers must only contain digits.

- ❌ Operand length greater than 4 digits:  
  Error: Numbers cannot be more than four digits.

---

🛠️ Formatting Requirements

- Numbers must be right-aligned.
- There must be four spaces between problems.
- Each problem must include a line of dashes (-) matching the width of the problem.
- The operator must be on the same line as the second operand, with appropriate spacing.
