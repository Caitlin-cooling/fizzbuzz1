# Fizzbuzz
class Fizzbuzz:
    def play(self, number):
        if number % 15 == 0:
            return "Fizzbuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return number
