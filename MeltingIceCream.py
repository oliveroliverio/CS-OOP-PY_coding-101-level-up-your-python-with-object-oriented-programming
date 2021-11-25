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

class IceCreamTruck:
  def __init__(self):
    self.scoopsSold = 0

  def order(self, scoops):
    # instantiate IceCream class
    iceCream = IceCream()
    self.add(iceCream, scoops)
    return iceCream

  def add(self, iceCream, scoops):
    iceCream.add(scoops)
    self.scoopsSold += scoops

class DeluxeIceCreamTruck(IceCreamTruck):
  def order(self, scoops):
    iceCream = super().order(scoops)
    iceCream.add(1)
    return iceCream

class Drinkable:
  # make constructor with initial cup value zero
  def __init__(self):
    self.cups = 0
  # create add method that adds variable number of cups to drink
  def add(self, cups):
    self.cups+= cups
  # create drink method that subtracts cups from drink
  def drink(self, cups):
    self.cups -= cups

class Lemonade(Drinkable):
  pass

# create MeltingIceCream class that inherits from IceCream, then Drinkable (order matters)
# IceCreams add method takes precedence over the Drinkable add method
class MeltingIceCream(IceCream, Drinkable):
  # add elapse method that updates scoop number of unmelted icecream and cups of melted icecream over time.
  # takes timeElapsed as argument
  def elapse(self, timeElapsed):
    # compute no. of icecreams melted (amount of time elapsed) or no of scoops left, whatever's smaller
    melted = min(timeElapsed, self.scoops)
    # subtract number of melted scoops from total number of scoops (inherited from IceCream)
    self.scoops -= melted
    # add number of melted scoops to cups (inherited from Drinkable) of melted iceCream
  self.cups += melted

# test
iceCream = MeltingIceCream()
print(f"Initially cups of icecream = {iceCream.scoops}")
iceCream.add(3)
print(f"added 3 scoops, total number now {iceCream.scoops}")
iceCream.elapse(2)
print(f"2 minutes have passed, 2 scoops melted and formed two cups")
print(f"There are now {iceCream.scoops} of icecream, and {iceCream.cups} of melted icecream")

# getting error: AttributeError: 'MeltingIceCream' object has no attribute 'cups'
# looked at [this](https://stackoverflow.com/questions/10268603/python-class-inheritance-attributeerror-subclass-object-has-no-attribute)
# rewritten