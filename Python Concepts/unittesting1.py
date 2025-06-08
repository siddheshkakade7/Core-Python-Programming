# import unittest
# class MytTest(unittest.TestCase):
#     def test_addition(self):
#          result = 2 + 2
#          self.assertEqual(result, 4)

import unittest
class MyTestFixture(unittest.TestCase):
    # Setup method - runs before each test method
    def setUp(self):
        print("in set up")
        # Initialize resources or perform setup actions
        self.data = [1, 2, 3, 4, 5]

    # Teardown method - runs after each test method
    def tearDown(self):
        print("in teardown")
        # Clean up resources or perform teardown actions
        self.data = None

# Test method 1
    def test_list_length(self):
        print("test_list_length")
        self.assertEqual(len(self.data), 5, "Length should be 5")

    # Test method 2
    def test_list_contains_element(self):
        print("test_list_contains_element")
        self.assertIn(3, self.data, "List should contain 3")




