<div align="center">
<h1>Python Conditional Statements</h1>
</div>

# Context

- [Context](#context)
  - [Python Conditional Statements](#python-conditional-statements)
  - [Introduction](#introduction)
  - [Why Conditional Statements are Important](#why-conditional-statements-are-important)
  - [Types of Conditional Statements](#types-of-conditional-statements)
    - [if Statement](#if-statement)
    - [if-else Statement](#if-else-statement)
    - [if-elif-else Statement](#if-elif-else-statement)
    - [Nested if Statement](#nested-if-statement)
  - [Short-hand if](#short-hand-if)
  - [Short-hand if-else](#short-hand-if-else)
  - [Logical Keywords in Conditions](#logical-keywords-in-conditions)
    - [and](#and)
    - [or](#or)
    - [not](#not)

## Python Conditional Statements

## Introduction

- Conditional statements are used for **decision-making** in programs.
- They allow execution of different code blocks based on conditions (**True / False**).
- Conditions are evaluated using:

  - Comparison operators
  - Logical operators

---
[⬆️ Go to Context](#context)

## Why Conditional Statements are Important

- Make decisions in programs
- Control the flow of execution
- Execute code selectively
- Handle different situations dynamically

---
[⬆️ Go to Context](#context)

## Types of Conditional Statements

- if statement
- if-else statement
- if-elif-else statement
- Nested if statement
- Short-hand if (one-line if)
- Short-hand if-else (conditional expression)

---
[⬆️ Go to Context](#context)

### if Statement

- Executes code only if condition is **True**

  ```py
  x = 10

  if x > 5:
      print("x is greater than 5")
  ```

---
[⬆️ Go to Context](#context)

### if-else Statement

- Executes one block if condition is **True**, another if **False**

  ```py
  x = 3

  if x > 5:
      print("x is greater than 5")
  else:
      print("x is not greater than 5")
  ```

---
[⬆️ Go to Context](#context)

### if-elif-else Statement

- Used to check multiple conditions sequentially

  ```py
  x = 10

  if x < 5:
      print("Less than 5")
  elif x == 10:
      print("Equal to 10")
  else:
      print("Greater than 5 but not 10")
  ```

---
[⬆️ Go to Context](#context)

### Nested if Statement

- An `if` statement inside another `if`

  ```py
  x = 10

  if x > 5:
      if x < 20:
          print("x is between 5 and 20")
  ```

---
[⬆️ Go to Context](#context)

## Short-hand if

- One-line if statement

  ```py
  x = 10

  if x > 5: print("x is greater than 5")
  ```

---
[⬆️ Go to Context](#context)

## Short-hand if-else

- One-line if-else

  ```py
  x = 10

  print("Greater") if x > 5 else print("Smaller")
  ```

---
[⬆️ Go to Context](#context)

## Logical Keywords in Conditions

### and

- Returns True if **both conditions are True**

  ```py
  x = 10

  if x > 5 and x < 20:
      print("x is between 5 and 20")
  ```

---
[⬆️ Go to Context](#context)

### or

- Returns True if **at least one condition is True**

  ```py
  x = 3

  if x < 5 or x > 10:
      print("Condition satisfied")
  ```

---
[⬆️ Go to Context](#context)

### not

- Reverses the result

  ```py
  x = 3

  if not x > 5:
      print("x is not greater than 5")
  ```

---
[⬆️ Go to Context](#context)
