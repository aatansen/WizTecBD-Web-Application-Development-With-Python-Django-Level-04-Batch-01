<div align="center">
<h1>Python Loops</h1>
</div>

# Context

- [Context](#context)
  - [Python Loops](#python-loops)
  - [Introduction](#introduction)
  - [Why Use Loop?](#why-use-loop)
  - [Types of Loops](#types-of-loops)
  - [Python for Loop](#python-for-loop)
    - [for Loop with range()](#for-loop-with-range)
    - [Loop Through a String](#loop-through-a-string)
    - [Loop Through a List](#loop-through-a-list)
    - [Loop Through a Dictionary](#loop-through-a-dictionary)
      - [a) Loop Through Keys](#a-loop-through-keys)
      - [b) Loop Through Values](#b-loop-through-values)
      - [c) Loop Through Key-Value Pairs](#c-loop-through-key-value-pairs)
  - [Loop Control Statements](#loop-control-statements)
    - [break Statement](#break-statement)
    - [continue Statement](#continue-statement)
  - [Practice Tasks](#practice-tasks)

## Python Loops

## Introduction

- A loop is used to execute a block of code repeatedly:

  - While a condition is true
  - Or for a fixed number of times
- Helps reduce code repetition and improve efficiency

---
[⬆️ Go to Context](#context)

## Why Use Loop?

- Repeat tasks automatically
- Process multiple items in a sequence
- Reduce code duplication
- Perform calculations on large datasets

---
[⬆️ Go to Context](#context)

## Types of Loops

- for loop
- while loop

---
[⬆️ Go to Context](#context)

## Python for Loop

- Used to iterate over a sequence:

  - list
  - tuple
  - string
  - range

  ```py
  for i in range(5):
      print(i)
  ```

---
[⬆️ Go to Context](#context)

### for Loop with range()

- `range()` generates a sequence of numbers

  ```py
  for i in range(1, 6):
      print(i)
  ```

---
[⬆️ Go to Context](#context)

### Loop Through a String

  ```py
  text = "Python"

  for char in text:
      print(char)
  ```

---
[⬆️ Go to Context](#context)

### Loop Through a List

  ```py
  numbers = [1, 2, 3, 4]

  for num in numbers:
      print(num)
  ```

---
[⬆️ Go to Context](#context)

### Loop Through a Dictionary

#### a) Loop Through Keys

  ```py
  data = {"name": "Ali", "age": 25}

  for key in data:
      print(key)
  ```

---
[⬆️ Go to Context](#context)

#### b) Loop Through Values

  ```py
  for value in data.values():
      print(value)
  ```

---
[⬆️ Go to Context](#context)

#### c) Loop Through Key-Value Pairs

  ```py
  for key, value in data.items():
      print(key, value)
  ```

---
[⬆️ Go to Context](#context)

## Loop Control Statements

### break Statement

- Terminates the loop immediately

  ```py
  for i in range(10):
      if i == 5:
          break
      print(i)
  ```

---
[⬆️ Go to Context](#context)

### continue Statement

- Skips current iteration and moves to next

  ```py
  for i in range(5):
      if i == 2:
          continue
      print(i)
  ```

---
[⬆️ Go to Context](#context)

## Practice Tasks

- Print odd or even numbers from a list
- Print positive or negative numbers from a list
- Print odd or even numbers from 1 to 20 using `range()`
- Find sum of all numbers in a list
- Count odd and even numbers from 1 to 20
- Find the largest number in a list
- Print multiplication table of 5
- Separate odd and even numbers from a list

---
[⬆️ Go to Context](#context)
