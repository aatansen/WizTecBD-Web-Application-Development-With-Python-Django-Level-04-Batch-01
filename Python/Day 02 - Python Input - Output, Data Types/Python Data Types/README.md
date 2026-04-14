<div align="center">
<h1>Python Data Types</h1>
</div>

# Context

- [Context](#context)
  - [Python Data Types](#python-data-types)
    - [Introduction](#introduction)
    - [Why Data Types are Important](#why-data-types-are-important)
  - [Common Data Types in Python](#common-data-types-in-python)
  - [Mutable vs Immutable Data Types](#mutable-vs-immutable-data-types)
    - [Mutable Data Types](#mutable-data-types)
    - [Immutable Data Types](#immutable-data-types)
  - [Checking Data Types](#checking-data-types)
  - [Type Conversion (Type Casting)](#type-conversion-type-casting)

## Python Data Types

### Introduction

- Data types define the type of value a variable can store.
- Python is a **dynamically typed** language:

  - No need to declare data types explicitly
  - Python automatically assigns the data type based on the value

---
[⬆️ Go to Context](#context)

### Why Data Types are Important

- Define what kind of data a variable holds
- Determine which operations can be performed
- Help prevent errors in programs
- Improve program readability and logic

---
[⬆️ Go to Context](#context)

## Common Data Types in Python

| Data Type | Example                  |
| --------- | ------------------------ |
| `int`     | 10                       |
| `float`   | 10.5                     |
| `str`     | "Hello"                  |
| `bool`    | True / False             |
| `list`    | [1, 2, 3]                |
| `tuple`   | (1, 2, 3)                |
| `dict`    | {"name": "John"}         |
| `set`     | {"red", "green", "blue"} |

---
[⬆️ Go to Context](#context)

## Mutable vs Immutable Data Types

### Mutable Data Types

- Can be changed after creation

  - list

  - dict

  - set

---
[⬆️ Go to Context](#context)

### Immutable Data Types

- Cannot be changed after creation

  - `int`

  - `float`

  - `bool`

  - `tuple`

  - `str`

---
[⬆️ Go to Context](#context)

## Checking Data Types

- Use `type()` function

  ```py
  x = 10
  print(type(x))  # <class 'int'>
  ````

---
[⬆️ Go to Context](#context)

## Type Conversion (Type Casting)

- Converting one data type to another

  ```py
  x = int("10")
  y = float(5)
  z = str(100)
  ```

---
[⬆️ Go to Context](#context)
