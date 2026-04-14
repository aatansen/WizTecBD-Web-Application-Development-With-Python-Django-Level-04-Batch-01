<div align="center">
<h1>Python Variables</h1>
</div>

# Context

- [Context](#context)
  - [Python Variables](#python-variables)
    - [What is a Variable?](#what-is-a-variable)
    - [Why Use Variables?](#why-use-variables)
    - [Variable Declaration in Python](#variable-declaration-in-python)
    - [Rules for Naming Variables](#rules-for-naming-variables)
    - [Valid Variable Names](#valid-variable-names)
    - [Invalid Variable Names](#invalid-variable-names)
    - [Multi-word Variable Naming Styles](#multi-word-variable-naming-styles)
  - [Assigning Multiple Values](#assigning-multiple-values)
    - [Many Values to Multiple Variables](#many-values-to-multiple-variables)
    - [One Value to Multiple Variables](#one-value-to-multiple-variables)
  - [Python Variables Usecases](#python-variables-usecases)
    - [Checking Variable Type](#checking-variable-type)
    - [Type Casting](#type-casting)
    - [Local Variables](#local-variables)
    - [Global Variables](#global-variables)
    - [Using Global Keyword](#using-global-keyword)
    - [Deleting a Variable](#deleting-a-variable)
    - [Common Errors with Variables](#common-errors-with-variables)

## Python Variables

### What is a Variable?

- A variable is a container for storing data values.
- The value of a variable can change during program execution.

---
[⬆️ Go to Context](#context)

### Why Use Variables?

Variables are used to:

- Store data
- Reuse values
- Make programs readable and manageable
- Perform calculations easily

---
[⬆️ Go to Context](#context)

### Variable Declaration in Python

- No need to declare type explicitly
- Python automatically determines the data type based on the assigned value

  ```py
  x = 10
  name = "John"
  price = 99.5
  ```

---
[⬆️ Go to Context](#context)

### Rules for Naming Variables

- Must start with a letter or underscore (_), not a digit
- Can contain:

  - Letters (a-z, A-Z)
  - Numbers (0-9)
  - Underscores (_)
- Case-sensitive (`myVar` and `myvar` are different)
- Cannot use Python reserved keywords
- No strict length limit, but keep names meaningful

---
[⬆️ Go to Context](#context)

### Valid Variable Names

  ```py
  name = "Ali"
  _age = 25
  total_price = 100
  myVar = 10
  ```

---
[⬆️ Go to Context](#context)

### Invalid Variable Names

  ```py
  1name = "Ali"      # starts with digit
  my-name = 10       # hyphen not allowed
  class = "Python"   # reserved keyword
  ```

---
[⬆️ Go to Context](#context)

### Multi-word Variable Naming Styles

- Camel Case

  ```py
  myVariableName
  ```

- Pascal Case

  ```py
  MyVariableName
  ```

- Snake Case

  ```py
  my_variable_name
  ```

---
[⬆️ Go to Context](#context)

## Assigning Multiple Values

### Many Values to Multiple Variables

  ```py
  x, y, z = 1, 2, 3
  ```

- Number of variables must match number of values

---
[⬆️ Go to Context](#context)

### One Value to Multiple Variables

  ```py
  x = y = z = 100
  ```

---
[⬆️ Go to Context](#context)

## Python Variables Usecases

### Checking Variable Type

  ```py
  x = 10
  print(type(x))  # <class 'int'>
  ```

---
[⬆️ Go to Context](#context)

### Type Casting

- Converting one data type to another

  ```py
  x = int("10")
  y = float(5)
  z = str(100)
  ```

---
[⬆️ Go to Context](#context)

### Local Variables

- Defined inside a function
- Accessible only within that function

  ```py
  def my_func():
      x = 10  # local variable
  ```

---
[⬆️ Go to Context](#context)

### Global Variables

- Defined outside a function
- Accessible everywhere in the program

  ```py
  x = 10  # global variable

  def my_func():
      print(x)
  ```

---
[⬆️ Go to Context](#context)

### Using Global Keyword

- Allows modifying global variable inside a function

  ```py
  x = 10

  def my_func():
      global x
      x = 20
  ```

---
[⬆️ Go to Context](#context)

### Deleting a Variable

  ```py
  x = 10
  del x
  ```

---
[⬆️ Go to Context](#context)

### Common Errors with Variables

- Using undefined variable

  ```py
  print(x)  # error if x is not defined
  ```

- Wrong type usage

  ```py
  x = "10"
  y = x + 5  # error
  ```

---
[⬆️ Go to Context](#context)
