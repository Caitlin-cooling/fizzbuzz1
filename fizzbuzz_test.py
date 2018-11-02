from fizzbuzz import Fizzbuzz

def test_fizz():
    fizzbuzz = Fizzbuzz()
    assert fizzbuzz.play(3) == "Fizz"

def test_buzz():
    fizzbuzz = Fizzbuzz()
    assert fizzbuzz.play(5) == "Buzz"

def test_fizzbuzz():
    fizzbuzz = Fizzbuzz()
    assert fizzbuzz.play(15) == "Fizzbuzz"
