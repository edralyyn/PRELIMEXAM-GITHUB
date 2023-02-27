import unittest

def temperature(x):

    return ((x - 32)*(5/9))

class converted(unittest.TestCase):
    def test(self):

        self.assertEqual(temperature(0),1)

if __name__ == '__main__':

    unittest.main()