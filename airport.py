class Airport():
  def __init__(self):
    self.docked = []

  def dock(self, plane):
    self.docked.append(plane)