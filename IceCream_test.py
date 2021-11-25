class IceCream:
  def __init__(self):
    self.scoops = 6
    self.scoopMax = 10
    print(f"initial scoops = {self.scoops}")

  def eat(self, scoops):
    if self.scoops < scoops:
      print("no more ice cream left")
    else:
      self.scoops -= scoops
      print(f"eating {scoops} scoops of icecream")
      print(f"You have {self.scoops} left")

  def add(self, scoops):
    if (self.scoops + scoops > self.scoopMax):
      self.scoops = 0
      print(f"adding {scoops} scoops")
      print(f"you know have zero scoops because you dropped it")
    else:
      self.scoops += scoops
      print(f"adding {scoops} scoops")
      print(f"you know have {self.scoops} scoops")

# intantiate and check
iceCream = IceCream()
iceCream.eat(2)
iceCream.add(4)
