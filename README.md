# 01 - introduction.mp4
# 02 - project.mp4
# 03 - concept-oop-paradigm.mp4
# 04 - practice-ice-cream.mp4

### Create ice cream class
![](img/2021-11-24-09-22-49.png)

```python
class IceCream:
  pass
```

### instantiate

```python
ice = Ice()
```
### Add methods to class
![](img/2021-11-24-09-25-02.png)

```python
class IceCream
  def eat(self):
    print("yum")
```
### add constructor
code that's run when object is instantiated

![](img/2021-11-24-09-27-25.png)

```python
class IceCream
  def __init__(self):
    print("created ice cream!")

  def eat(self):
    print("yum")

# instantiate
iceCream = IceCream()
```

### Add attributes
Note, self refers to current instance instance
![](img/2021-11-24-09-31-27.png)
```python
class IceCream
  def __init__(self):
    self.scoops = 3

  def eat(self):
    print("yum")

# instantiate
iceCream = IceCream()
# check attributes
iceCream.scoops
```

### change eat method to take in another parameter
```python
class IceCream:
  def __init__(self):
    self.scoops = 6

  def eat(self, scoops):
    # self.scoops = self.scoops - scoops
    # cleaner way
    self.scoops -= scoops
    print("yumyum")

iceCream = IceCream()
print(iceCream.scoops)
iceCream.eat(2)
print(iceCream.scoops)
```

### Add more methods and account for running out of iceCream

```python
class IceCream:
  def __init__(self):
    self.scoops = 6
    self.scoopMax = 7

  def eat(self, scoops):
    if self.scoops < scoops:
      print("no more ice cream left")
    else:
      self.scoops -= scoops
      print("yumyum")

  def add(self, scoops):
    if self.scoops > self.scoopMax:
      print("too many scoops")
    else:
      self.scoops += scoops
      print("yay more scoops")

# I don't think the above works, but I'll figure that out later
# intantiate and check
iceCream = IceCream()
iceCream.eat(10)
print(iceCream.scoops)
```

# 05 - bonus-practice-light-switch.mp4

### Instantiate lightswitch class to off initially
```python
class Light:
  def __init__(self):
    self.on = False
```

### Create toggle method that switches from off to on and vice versa
```python
class Light:
  def __init__(self):
    self.on = False
  def toggle(self):
    self.on = not self.on
```

### Test it
```python
class Light:
  def __init__(self):
    self.on = False
  def isOn(self):
    return self.on
  def toggle(self):
    self.on = not self.on

light = Light()
# see if light's off initially
light.isOn()
# toggle it on
light.toggle()
# see if light's on
light.isOn()
# toggle it back off
light.toggle()
light.isOn()
```




# 06 - bonus-mystery-sync-ed-lights.mp4
# 07 - concept-abstraction.mp4
![](img/2021-11-24-10-08-27.png)
- encapsulation hides info from users
- users can't modify the scoop max or initial scoops
- abstraction also removes redundancy
- imagine two different instances of IceCream: iceCreamTruck vs iceCreamCone.  Maintaining this would be a nightmare

![](img/2021-11-24-10-11-24.png)
- but you still only want one copy of the scoop adding code
- Tip: check for redundant code.  If you're copying/pasting, you're doing it wrong
- Encapsulation hides/restricts information
- Abstraction means you don't have to worry about how the eat method works
# 08 - practice-ice-cream-truck.mp4
Continuing from ice cream code and adding max

```python
class IceCream:
  maxScoops = 3
  def __init__(self):
    self.scoops = 2

  def eat(self, scoops):
    if self.scoops < scoops:
      print("no more ice cream left")
    else:
      self.scoops -= scoops
      print("yumyum")

  def add(self, scoops):
    self.scoops += scoops
    if self.scoops > self.maxScoops:
      self.scoops = 0
      print("Too many scoops, dropped ice cream.. :(")

# I don't think the above works, but I'll figure that out later
# intantiate and check
iceCream = IceCream()
iceCream.eat(10)
print(iceCream.scoops)
```

### Add IceCreamTruck class
- instantiating another class within this class
- give the add method a paramter that takes in instantiated iceCream objects and adds scoops to it
```python
class IceCreamTruck:
  def __init__(self):
    self.sold = 0

  def order(self, scoops):
    # instantiate IceCream class
    iceCream = IceCream()
    iceCream.add(scoops)
    return iceCream

  def add(self, iceCream, scoops):
    iceCream.add(scoops)

```



# 09 - bonus-practice-sync-ed-lights.mp4
# 10 - concept-inheritance.mp4
# 11 - practice-deluxe-ice-cream-truck.mp4
# 12 - bonus-practice-flickering-light.mp4
# 13 - bonus-mystery-mro.mp4.
# 14 - concept-inheritance.mp4
# 15 - practice-melting-ice-cream.mp4
# 16 - bonus-practice-timed-lights.mp4
# 17 - bonus-mystery-fragile-base-case.mp4
# 18 - conclusion.mp4
