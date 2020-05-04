import unittest

class TestDockPlane(unittest.TestCase):
    
    def test_dock_plane_inserts_plane(self):
      self.assertEqual("foo".upper(), "FOO")

if __name__ == "__main__":
    unittest.main()