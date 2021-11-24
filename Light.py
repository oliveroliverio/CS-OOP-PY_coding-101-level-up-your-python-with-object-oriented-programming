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