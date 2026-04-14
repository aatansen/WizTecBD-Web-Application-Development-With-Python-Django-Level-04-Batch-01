<div align="center">
<h1>Python Function,Tuple,Set</h1>
</div>

# Context

- [Context](#context)
  - [Python Function](#python-function)
    - [Introduction to Functions](#introduction-to-functions)
      - [Key Points](#key-points)
    - [Why Use Functions?](#why-use-functions)
    - [Types of Functions](#types-of-functions)
    - [Creating a Function](#creating-a-function)
    - [Calling a Function](#calling-a-function)
    - [Function Parameters](#function-parameters)
    - [Function with Default Parameters](#function-with-default-parameters)
    - [Function with Multiple Parameters](#function-with-multiple-parameters)
    - [Function Arguments](#function-arguments)
      - [Number of Arguments Rule](#number-of-arguments-rule)
    - [Keyword Arguments](#keyword-arguments)
    - [Default Argument Values](#default-argument-values)
    - [Arbitrary Arguments (\*args)](#arbitrary-arguments-args)
    - [Arbitrary Keyword Arguments (\*\*kwargs)](#arbitrary-keyword-arguments-kwargs)
    - [Return Statement](#return-statement)
    - [Pass Statement](#pass-statement)
  - [Python Tuple](#python-tuple)
    - [Key Features of Tuple](#key-features-of-tuple)
    - [Creating a Tuple](#creating-a-tuple)
    - [Single Element Tuple](#single-element-tuple)
    - [Access Tuple Elements](#access-tuple-elements)
    - [Tuple Immutability](#tuple-immutability)
    - [Tuple Length](#tuple-length)
    - [Loop Through Tuple](#loop-through-tuple)
    - [Tuple Methods](#tuple-methods)
      - [count()](#count)
      - [index()](#index)
    - [Why Use Tuples?](#why-use-tuples)
  - [Python Set](#python-set)
    - [Key Features of Set](#key-features-of-set)
    - [Creating a Set](#creating-a-set)
    - [Duplicate Values in Set](#duplicate-values-in-set)
    - [Access Set Items](#access-set-items)
    - [Add Items to Set](#add-items-to-set)
      - [add()](#add)
      - [update()](#update)
    - [Remove Items from Set](#remove-items-from-set)
      - [remove()](#remove)
      - [discard()](#discard)
      - [pop()](#pop)
      - [clear()](#clear)
    - [Set Operations](#set-operations)
      - [Union](#union)
      - [Intersection](#intersection)
      - [Difference](#difference)
      - [Symmetric Difference](#symmetric-difference)
    - [Why Use Sets?](#why-use-sets)

## Python Function

### Introduction to Functions

- A function is a reusable block of code that performs a specific task.
- Functions help reduce code duplication and improve organization.

#### Key Points

- Runs only when called
- Can take inputs (parameters)
- Can return output (result)

---
[⬆️ Go to Context](#context)

### Why Use Functions?

- Avoid code repetition
- Improve readability
- Make debugging easier
- Reuse logic multiple times
- Organize large programs

---
[⬆️ Go to Context](#context)

### Types of Functions

- Built-in functions (e.g., `print()`, `len()`, `type()`)
- User-defined functions

---
[⬆️ Go to Context](#context)

### Creating a Function

- Use the `def` keyword

  ```py
  def greet():
      print("Hello World")
  ```

---
[⬆️ Go to Context](#context)

### Calling a Function

  ```py
  greet()
  ```

---
[⬆️ Go to Context](#context)

### Function Parameters

- Parameters are variables defined inside function parentheses

```py id="wq7m2x"
def greet(name):
    print("Hello", name)
```

---
[⬆️ Go to Context](#context)

### Function with Default Parameters

- Default values are used if no argument is provided

  ```py
  def greet(name="Guest"):
      print("Hello", name)
  ```

---
[⬆️ Go to Context](#context)

### Function with Multiple Parameters

  ```py
  def add(a, b):
      print(a + b)
  ```

---
[⬆️ Go to Context](#context)

### Function Arguments

- Arguments are actual values passed to a function
- Can be multiple, separated by commas

---
[⬆️ Go to Context](#context)

#### Number of Arguments Rule

- Must match function definition
- Too few or too many arguments cause errors

---
[⬆️ Go to Context](#context)

### Keyword Arguments

- Arguments passed using `key=value` format
- Order does not matter

  ```py
  def student(name, age):
      print(name, age)

  student(age=20, name="Ali")
  ```

---
[⬆️ Go to Context](#context)

### Default Argument Values

- Can combine default and normal parameters

  ```py
  def student(name, age=18):
      print(name, age)
  ```

---
[⬆️ Go to Context](#context)

### Arbitrary Arguments (*args)

- Used when number of arguments is unknown
- Stored as a tuple

  ```py
  def add(*numbers):
      print(numbers)
  ```

---
[⬆️ Go to Context](#context)

### Arbitrary Keyword Arguments (**kwargs)

- Used when unknown keyword arguments are passed
- Stored as a dictionary

  ```py
  def student(**info):
      print(info)
  ```

---
[⬆️ Go to Context](#context)

### Return Statement

- Used to return a value from a function

  ```py
  def add(a, b):
      return a + b
  ```

---
[⬆️ Go to Context](#context)

### Pass Statement

- Placeholder for future code
- Prevents errors in empty functions

  ```py
  def future_function():
      pass
  ```

---
[⬆️ Go to Context](#context)

## Python Tuple

- A tuple is an ordered, immutable collection of items in Python.
- Tuples are similar to lists, but they **cannot be changed after creation**.

---
[⬆️ Go to Context](#context)

### Key Features of Tuple

- Ordered (items have a defined order)
- Immutable (cannot be modified)
- Allows duplicate values
- Can store multiple data types

---
[⬆️ Go to Context](#context)

### Creating a Tuple

```python
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.5, True)
```

---
[⬆️ Go to Context](#context)

### Single Element Tuple

- Must include a comma

```python
t = (10,)
```

---
[⬆️ Go to Context](#context)

### Access Tuple Elements

```python
t = (10, 20, 30)

print(t[0])   # 10
print(t[-1])  # 30
```

---
[⬆️ Go to Context](#context)

### Tuple Immutability

```python
t = (1, 2, 3)
# t[0] = 10  ❌ Not allowed
```

---
[⬆️ Go to Context](#context)

### Tuple Length

```python
t = (1, 2, 3)
print(len(t))
```

---
[⬆️ Go to Context](#context)

### Loop Through Tuple

```python
t = (1, 2, 3)

for item in t:
    print(item)
```

---
[⬆️ Go to Context](#context)

### Tuple Methods

#### count()

```python
t = (1, 2, 2, 3)
print(t.count(2))
```

#### index()

```python
t = (10, 20, 30)
print(t.index(20))
```

---
[⬆️ Go to Context](#context)

### Why Use Tuples?

- Data should not change
- Faster than lists
- Safer for fixed data

---
[⬆️ Go to Context](#context)

## Python Set

- A set is an unordered collection of unique items.
- Sets do not allow duplicate values.

---
[⬆️ Go to Context](#context)

### Key Features of Set

- Unordered
- No duplicate values
- Mutable (can add/remove items)
- Cannot be indexed

---
[⬆️ Go to Context](#context)

### Creating a Set

```python
s = {1, 2, 3}
names = {"Ali", "Rahim", "Karim"}
```

---
[⬆️ Go to Context](#context)

### Duplicate Values in Set

```python
s = {1, 2, 2, 3}
print(s)  # {1, 2, 3}
```

---
[⬆️ Go to Context](#context)

### Access Set Items

- Cannot access by index
- Use loop instead

```python
s = {10, 20, 30}

for item in s:
    print(item)
```

---
[⬆️ Go to Context](#context)

### Add Items to Set

#### add()

```python
s = {1, 2}
s.add(3)
```

---
[⬆️ Go to Context](#context)

#### update()

```python
s = {1, 2}
s.update([3, 4])
```

---
[⬆️ Go to Context](#context)

### Remove Items from Set

#### remove()

```python
s = {1, 2, 3}
s.remove(2)
```

- Raises error if item not found

---
[⬆️ Go to Context](#context)

#### discard()

```python
s.discard(10)
```

- No error if item not found

---
[⬆️ Go to Context](#context)

#### pop()

```python
s.pop()
```

- Removes random item

---
[⬆️ Go to Context](#context)

#### clear()

```python
s.clear()
```

---
[⬆️ Go to Context](#context)

### Set Operations

#### Union

```python
a = {1, 2}
b = {3, 4}

print(a | b)
```

---
[⬆️ Go to Context](#context)

#### Intersection

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)
```

---
[⬆️ Go to Context](#context)

#### Difference

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a - b)
```

---
[⬆️ Go to Context](#context)

#### Symmetric Difference

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a ^ b)
```

---
[⬆️ Go to Context](#context)

### Why Use Sets?

- Remove duplicates automatically
- Fast membership testing
- Useful for mathematical operations

---
[⬆️ Go to Context](#context)
