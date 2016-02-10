import unittest
import sys
import re
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()

        self.failIf(app.calc(1) != 1)

    def test_two(self):
        app = FizzBuzz()
        output = StringIO()
        app.run(50, output)
#        print output.getvalue().splitlines()[2]
        self.failIf(output.getvalue().splitlines()[0] != "1")
        self.failIf(output.getvalue().splitlines()[5] != "Fizz")
        self.failIf(output.getvalue().splitlines()[9] != "Buzz")
        self.failIf(output.getvalue().splitlines()[14] != "FizzBuzz")   
        self.failIf(output.getvalue().splitlines()[44] != "FizzBuzz")   

    def test_three(self):
        app = FizzBuzz()
        output = StringIO()
        app.run(100, output)
        
        self.failIf(output.getvalue().splitlines().count("Fizz") != 26)
        self.failIf(output.getvalue().splitlines().count("Buzz") != 13)
        self.failIf(output.getvalue().splitlines().count("FizzBuzz") != 6)

    def test_prime(self):
        app = FizzBuzz()
        output = StringIO()
        app.run(100, output)

        lista = output.getvalue().splitlines()
        primecount = ['is a prime' in x for x in lista]
        self.failIf(primecount.count(True) !=25)


    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
