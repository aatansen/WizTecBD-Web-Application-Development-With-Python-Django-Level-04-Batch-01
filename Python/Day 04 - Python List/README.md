<div align="center">
<h1>Python List</h1>
</div>

# Context

- [Context](#context)
  - [Python List](#python-list)
  - [Introduction to Python List](#introduction-to-python-list)
  - [Why Use Lists?](#why-use-lists)
  - [Creating a List](#creating-a-list)
  - [Accessing List Elements](#accessing-list-elements)
  - [Negative Indexing](#negative-indexing)
  - [Changing List Items](#changing-list-items)
  - [List Length](#list-length)
  - [Adding Elements to a List](#adding-elements-to-a-list)
    - [append(item)](#appenditem)
    - [insert(index, item)](#insertindex-item)
    - [extend(list)](#extendlist)
  - [Removing Elements from a List](#removing-elements-from-a-list)
    - [remove(item)](#removeitem)
    - [pop(\[index\])](#popindex)
    - [clear()](#clear)
    - [del Keyword](#del-keyword)
  - [Looping Through a List](#looping-through-a-list)
  - [Useful List Methods](#useful-list-methods)
    - [count()](#count)
    - [copy()](#copy)

## Python List

## Introduction to Python List

- A **list** is a built-in data structure used to store multiple items in a single variable.
- Lists are:

  - Ordered
  - Mutable (can be changed)
  - Allow duplicate values

  ```py
  student_list = ["rohim", 100, True, "Korim", 5.5]
  ```

---
[⬆️ Go to Context](#context)

## Why Use Lists?

- Store multiple values in one variable
- Access elements using index
- Modify, add, or remove elements
- Perform operations on collections of data

---
[⬆️ Go to Context](#context)

## Creating a List

- Lists are created using square brackets `[ ]`

  ```py
  numbers = [1, 2, 3, 4]
  names = ["Ali", "Rahim", "Karim"]
  ```

---
[⬆️ Go to Context](#context)

## Accessing List Elements

- Index starts from **0**

  ```py
  names = ["Ali", "Rahim", "Karim"]

  print(names[0])  # Ali
  print(names[1])  # Rahim
  ```

---
[⬆️ Go to Context](#context)

## Negative Indexing

- Access elements from the end

  ```py
  names = ["Ali", "Rahim", "Karim"]

  print(names[-1])  # Karim
  print(names[-2])  # Rahim
  ```

---
[⬆️ Go to Context](#context)

## Changing List Items

- Lists are mutable

  ```py
  names = ["Ali", "Rahim", "Karim"]
  names[1] = "Hasan"
  ```

---
[⬆️ Go to Context](#context)

## List Length

- Use `len()` function

  ```py
  numbers = [1, 2, 3, 4]
  print(len(numbers))  # 4
  ```

---
[⬆️ Go to Context](#context)

## Adding Elements to a List

### append(item)

- Adds item to the end

  ```py
  numbers = [1, 2]
  numbers.append(3)
  ```

---
[⬆️ Go to Context](#context)

### insert(index, item)

- Inserts item at specific position

  ```py
  numbers = [1, 3]
  numbers.insert(1, 2)
  ```

---
[⬆️ Go to Context](#context)

### extend(list)

- Adds elements of another list

  ```py
  a = [1, 2]
  b = [3, 4]

  a.extend(b)
  ```

---
[⬆️ Go to Context](#context)

## Removing Elements from a List

### remove(item)

- Removes first occurrence of value

  ```py
  numbers = [1, 2, 3, 2]
  numbers.remove(2)
  ```

---
[⬆️ Go to Context](#context)

### pop([index])

- Removes element at given index
- Default: removes last item

  ```py
  numbers = [1, 2, 3]
  numbers.pop()     # removes last
  numbers.pop(0)    # removes index 0
  ```

---
[⬆️ Go to Context](#context)

### clear()

- Removes all elements

  ```py
  numbers = [1, 2, 3]
  numbers.clear()
  ```

---
[⬆️ Go to Context](#context)

### del Keyword

- Deletes specific item or entire list

  ```py
  numbers = [1, 2, 3]
  del numbers[1]

  del numbers
  ```

---
[⬆️ Go to Context](#context)

## Looping Through a List

  ```py
  numbers = [1, 2, 3]

  for num in numbers:
      print(num)
  ```

---
[⬆️ Go to Context](#context)

## Useful List Methods

### count()

- Returns number of occurrences

  ```py
  numbers = [1, 2, 2, 3]
  print(numbers.count(2))  # 2
  ```

---
[⬆️ Go to Context](#context)

### copy()

- Creates a copy of the list

  ```py
  numbers = [1, 2, 3]
  new_list = numbers.copy()
  ```

---
[⬆️ Go to Context](#context)
