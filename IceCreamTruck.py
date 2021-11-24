class IceCream:
  maxScoops = 6
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

# Test
truck = IceCreamTruck()
iceCream1 = truck.order(3)
iceCream1.eat(2)
truck.add(iceCream1, 1)
print(truck.scoopsSold)