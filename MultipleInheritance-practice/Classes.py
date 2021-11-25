
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Dancer:
  def __init__(self, style):
    self.style =style

class Student(Human):
  pass

# test
John = Student("John", "23")
print(John.name)