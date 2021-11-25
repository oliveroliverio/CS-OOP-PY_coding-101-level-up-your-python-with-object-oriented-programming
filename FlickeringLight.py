class Light:
  def __init__(self, sync=None):
    # call parent constructor
    # what was the parent class of light?
    super().__init__()
    self.on = False
    self.sync = sync
  def isOn(self):
    return self.on
  def toggle(self):
    self.on = not self.on


class OldLight(Light):
  def __init__(self, sync=None):
    # call parent constructor
    super().__init__(sync=sync)
    self.on = False
    self.sync = sync
    self.flicker = False

  def toggle(self):
    # call parent method with super
    super().toggle()
    if self.on:
      self.flicker = not self.flicker


# test
light = OldLight()
print(light.flicker)
light.toggle()
print(light.flicker)