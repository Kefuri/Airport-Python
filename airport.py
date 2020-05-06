class Airport():
  def __init__(self):
    self.docked = []

  def dock(self, plane):
    self.docked.append(plane)

  def takeoff(self, plane = None):
    if plane != None:
      self.docked.remove(plane)
    else:
      self.docked.pop()