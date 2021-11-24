class IceCream:
  def __init__(self):
    super().__init__()
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
    super().__init__()
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
  # instead of this:
  # iceCream = IceCream()
  # self.add(iceCream, scoops)
  # Do this to call the parent class method "order." Note, the IceCreamTruck order method instantiates an IceCream object automatically and returns it
  iceCream = super().order(scoops)
  # call the iceCream add method to add scoops
  iceCream.add(1)

# test
truck = DeluxeIceCreamTruck()
iceCream = truck.order(2)
iceCream.scoops
truck.soldass