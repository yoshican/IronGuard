# test_ironguard.py
"""
Tests for IronGuard module.
"""

import unittest
from ironguard import IronGuard

class TestIronGuard(unittest.TestCase):
    """Test cases for IronGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IronGuard()
        self.assertIsInstance(instance, IronGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IronGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
