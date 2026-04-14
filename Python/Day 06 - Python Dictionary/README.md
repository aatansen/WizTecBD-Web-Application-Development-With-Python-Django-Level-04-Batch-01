<div align="center">
<h1>Python Dictionary</h1>
</div>

# Context

- [Context](#context)
  - [Python Dictionary](#python-dictionary)
  - [Introduction to Python Dictionary](#introduction-to-python-dictionary)
  - [Why Use Dictionaries?](#why-use-dictionaries)
  - [Creating a Dictionary](#creating-a-dictionary)
  - [Accessing Dictionary Elements](#accessing-dictionary-elements)
  - [Adding Items](#adding-items)
  - [Modifying Items](#modifying-items)
  - [Dictionary Length](#dictionary-length)
  - [Removing Dictionary Items](#removing-dictionary-items)
  - [Using del](#using-del)
    - [pop() Method](#pop-method)
    - [clear() Method](#clear-method)
  - [Useful Dictionary Methods](#useful-dictionary-methods)
    - [get()](#get)
    - [items()](#items)
    - [keys()](#keys)
    - [values()](#values)
    - [copy()](#copy)
  - [Iterating Through a Dictionary](#iterating-through-a-dictionary)
    - [Loop Through Keys](#loop-through-keys)
    - [Loop Through Values](#loop-through-values)
    - [Loop Through Key-Value Pairs](#loop-through-key-value-pairs)
  - [Nested Dictionary](#nested-dictionary)

## Python Dictionary

## Introduction to Python Dictionary

- A **dictionary** is a collection of data stored in **key–value pairs**.
- Characteristics:

  - Unordered
  - Mutable (changeable)
  - Do not allow duplicate keys
- Commonly used to represent real-world structured data

---
[⬆️ Go to Context](#context)

## Why Use Dictionaries?

- Store data with meaningful keys
- Access values quickly using keys
- Represent structured data (e.g., student, product, user)
- Map relationships between data

---
[⬆️ Go to Context](#context)

## Creating a Dictionary

- Use curly braces `{}` with key–value pairs

  ```py
  student = {
      "name": "Ali",
      "age": 25,
      "marks": 90
  }
  ```

---
[⬆️ Go to Context](#context)

## Accessing Dictionary Elements

- Access values using keys

  ```py
  print(student["name"])  # Ali
  ```

---

## Adding Items

  ```py
  student["city"] = "Dhaka"
  ```

---
[⬆️ Go to Context](#context)

## Modifying Items

  ```py
  student["age"] = 26
  ```

---
[⬆️ Go to Context](#context)

## Dictionary Length

- Use `len()`

  ```py
  print(len(student))
  ```

---
[⬆️ Go to Context](#context)

## Removing Dictionary Items

## Using del

  ```py
  del student["age"]
  ```

---
[⬆️ Go to Context](#context)

### pop() Method

- Removes and returns value by key

  ```py
  student.pop("marks")
  ```

- If key not found → error (unless default provided)

---
[⬆️ Go to Context](#context)

### clear() Method

- Removes all items

  ```py
  student.clear()
  ```

---
[⬆️ Go to Context](#context)

## Useful Dictionary Methods

### get()

- Returns value for a key
- Returns `None` if key not found

  ```py
  student.get("name")
  ```

---
[⬆️ Go to Context](#context)

### items()

- Returns key-value pairs

  ```py
  student.items()
  ```

---
[⬆️ Go to Context](#context)

### keys()

- Returns all keys

  ```py
  student.keys()
  ```

---
[⬆️ Go to Context](#context)

### values()

- Returns all values

  ```py
  student.values()
  ```

---
[⬆️ Go to Context](#context)

### copy()

- Returns a copy of dictionary

  ```py
  new_student = student.copy()
  ```

---
[⬆️ Go to Context](#context)

## Iterating Through a Dictionary

### Loop Through Keys

  ```py
  for key in student:
      print(key)
  ```

---
[⬆️ Go to Context](#context)

### Loop Through Values

  ```py
  for value in student.values():
      print(value)
  ```

---
[⬆️ Go to Context](#context)

### Loop Through Key-Value Pairs

  ```py
  for key, value in student.items():
      print(key, value)
  ```

---
[⬆️ Go to Context](#context)

## Nested Dictionary

- Dictionary inside another dictionary

  ```py
  students = {
      "student1": {"name": "Ali", "age": 25},
      "student2": {"name": "Rahim", "age": 22}
  }
  ```

---
[⬆️ Go to Context](#context)
