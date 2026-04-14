<div align="center">
<h1>Python Input - Output</h1>
</div>

# Context

- [Context](#context)
  - [Python Input - Output](#python-input---output)
  - [Introduction](#introduction)
  - [Output in Python](#output-in-python)
    - [print() Function](#print-function)
    - [Printing Variables](#printing-variables)
    - [Printing Single Value](#printing-single-value)
    - [Printing Multiple Values](#printing-multiple-values)
  - [Formatting Output](#formatting-output)
    - [Using Comma (,)](#using-comma-)
    - [Using f-strings](#using-f-strings)
    - [Using format() Method](#using-format-method)
    - [Using % Operator](#using--operator)
  - [Input in Python](#input-in-python)
    - [input() Function](#input-function)
    - [Important Note](#important-note)
    - [Type Conversion with Input](#type-conversion-with-input)
    - [Integer Input](#integer-input)
    - [Float Input](#float-input)
  - [Taking Multiple Inputs](#taking-multiple-inputs)
    - [Using Multiple input() Calls](#using-multiple-input-calls)
    - [Using split()](#using-split)

## Python Input - Output

## Introduction

- Input and Output (I/O) are essential parts of programming.
- **Input**: Taking data from the user
- **Output**: Displaying results to the user
- Python provides simple and powerful functions for handling I/O.

---
[⬆️ Go to Context](#context)

## Output in Python

### print() Function

- Used to display output on the screen

  ```py
  print("Hello World")
  ```

---
[⬆️ Go to Context](#context)

### Printing Variables

### Printing Single Value

  ```py
  name = "Ali"
  print(name)
  ```

### Printing Multiple Values

  ```py
  name = "Ali"
  age = 25
  print(name, age)
  ```

---
[⬆️ Go to Context](#context)

## Formatting Output

### Using Comma (,)

- Automatically adds space between values

  ```py
  name = "Ali"
  age = 25
  print("Name:", name, "Age:", age)
  ```

---
[⬆️ Go to Context](#context)

### Using f-strings

  ```py
  name = "Ali"
  age = 25
  print(f"Name: {name}, Age: {age}")
  ```

---
[⬆️ Go to Context](#context)

### Using format() Method

  ```py
  name = "Ali"
  age = 25
  print("Name: {}, Age: {}".format(name, age))
  ```

---
[⬆️ Go to Context](#context)

### Using % Operator

  ```py
  name = "Ali"
  age = 25
  print("Name: %s, Age: %d" % (name, age))
  ```

---
[⬆️ Go to Context](#context)

## Input in Python

### input() Function

- Used to take input from the user

  ```py
  name = input("Enter your name: ")
  print(name)
  ```

---
[⬆️ Go to Context](#context)

### Important Note

> [!NOTE]
>
> - `input()` always returns data as **string**

---
[⬆️ Go to Context](#context)

### Type Conversion with Input

- Required when performing calculations

### Integer Input

  ```py
  age = int(input("Enter age: "))
  ```

### Float Input

  ```py
  price = float(input("Enter price: "))
  ```

---
[⬆️ Go to Context](#context)

## Taking Multiple Inputs

### Using Multiple input() Calls

  ```py
  name = input("Enter name: ")
  age = int(input("Enter age: "))
  ```

---
[⬆️ Go to Context](#context)

### Using split()

  ```py
  name, age = input("Enter name and age: ").split()
  age = int(age)
  ```

---
[⬆️ Go to Context](#context)
