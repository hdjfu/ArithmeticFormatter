
# Arithmetic Formatter

A lightweight Python utility that transforms addition and subtraction expressions into a clean, right-aligned, vertical and side-by-side layout, with an optional switch to include computed results.

---

## Objective

Implement the function:

<pre>
def arithmetic_arranger(problems, show_answers=False):
    ...
</pre>

This function:
- Takes a list of strings representing arithmetic problems.
- Formats them vertically and side-by-side.
- Optionally displays the solutions.

---

## Example Usage

<pre>
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
</pre>

Output:

<pre>
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
</pre>

With results:

<pre>
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
</pre>

Output:

<pre>
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
</pre>

---

## Validation Rules

The function returns meaningful error messages if the input is invalid:

- More than 5 problems:  
  <pre>Error: Too many problems.</pre>

- Invalid operator (only <code>+</code> or <code>-</code> are allowed):  
  <pre>Error: Operator must be '+' or '-'.</pre>

- Non-digit characters in operands:  
  <pre>Error: Numbers must only contain digits.</pre>

- Operand length greater than 4 digits:  
  <pre>Error: Numbers cannot be more than four digits.</pre>

---

## Formatting Requirements

- Numbers must be right-aligned.
- There must be four spaces between problems.
- Each problem must include a line of dashes (<code>-</code>) matching the width of the problem.
- The operator must be on the same line as the second operand, with appropriate spacing.
