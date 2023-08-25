# ArithmeticFormatter

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
<pre>
  235
+  52
-----
</pre>
This program converts a list of strings that are arithmetic problems to problems arranged vertically and side-by-side. The function should optionally take a second argument.

## Example
Function Call:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```
## Output:

<pre>
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
</pre>

When the second argument is set to **True**, the answers should be displayed.

## Function Call:
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```
## Output:

<pre>
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
</pre>
## Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.