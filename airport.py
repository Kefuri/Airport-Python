class Airport():
  def __init__(self):
    self.docked = []

  def dock(self, plane):
    self.__checkAlreadyDocked(plane)
    self.docked.append(plane)

  def takeoff(self, plane = None):
    if plane != None:
      self.docked.remove(plane)
    else:
      self.docked.pop()
  
  def __checkAlreadyDocked(self, plane):
    if plane in self.docked:
      raise ValueError("Plane is already docked!")
