import unittest

from airport import Airport

class TestAirportClass(unittest.TestCase):
    
    def test_dock_plane_inserts_plane(self):
      jfk = Airport()
      jfk.dock("Plane")
      self.assertEqual(jfk.docked[0], "Plane")

    def test_dock_plane_takes_more_than_one_plane(self):
      jfk = Airport()
      jfk.dock("Plane")
      jfk.dock("Another Plane")
      self.assertEqual(len(jfk.docked), 2)

    def test_takeoff_removes_plane_from_docked(self):
      jfk = Airport()
      jfk.dock("Plane")
      jfk.takeoff()
      self.assertEqual(len(jfk.docked), 0)



if __name__ == "__main__":
    unittest.main()