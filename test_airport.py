import unittest

from airport import Airport
from plane import Plane

class TestAirportClass(unittest.TestCase):

    def test_plane_object_gets_name(self):
      jfk = Airport()
      boeing = Plane("Boeing")
      jfk.dock(boeing)
      self.assertEqual(jfk.docked[0].get_name(), "Boeing")
    
    def test_dock_plane_inserts_plane(self):
      jfk = Airport()
      jfk.dock("Plane")
      self.assertEqual(jfk.docked[0], "Plane")

    def test_dock_plane_takes_more_than_one_plane(self):
      stn = Airport()
      stn.dock("Plane")
      stn.dock("Another Plane")
      self.assertEqual(len(stn.docked), 2)

    def test_takeoff_removes_plane_from_docked(self):
      jfk = Airport()
      jfk.dock("Plane")
      jfk.takeoff()
      self.assertEqual(len(jfk.docked), 0)

    def test_specific_plane_to_takeoff(self):
      jfk = Airport()
      jfk.dock("Plane A")
      jfk.dock("Plane B")
      jfk.takeoff("Plane A")
      self.assertEqual(jfk.docked[0], "Plane B")


if __name__ == "__main__":
    unittest.main()