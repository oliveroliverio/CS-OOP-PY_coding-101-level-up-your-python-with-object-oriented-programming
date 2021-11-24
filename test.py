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