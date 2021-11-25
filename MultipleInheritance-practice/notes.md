# [Python - Object Oriented Programming | Multiple Inheritance](https://www.youtube.com/watch?v=uYu4hCjYDhY)

- create initial classes
```python

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Dancer:
  def __init__(self, style):
    self.style =style

class Student:
  pass

# test
John = Student()
print(John.age)
```
- running this gives error
- `AttributeError: 'Student' object has no attribute 'age'`