from random import randint


class Die:  # Die class (die.py) – has two attributes: the number of sides of the die and the value of the rolled die.
  # 1. __init__(self, sides=6) – assigns the number of sides from the value passed in. Set value to 0 or to the returned value of roll().
  # 2. roll(self) – generate a random number between 1 and the number of sides and assign it to the Die’s value. Return the value.
  # 3. __str__(self) – return the Die’s value as a string.
  # 4. __lt__(self, other) – return true if the value of self is less than the value of other.
  # 5. __eq__(self, other) – return true if both the values of self and other are equal.
  # 6. __sub__(self, other) – return the difference between the value of self and the value
  # of other.
  # Die(parameter = default value)
  def __init__(self, sides=6):
    self.sides = sides
    self.value = self.roll()

  def roll(self):
    self.value = randint(1, self.sides)
    return self.value

  def __str__(self):
    return str(self.value)

  def __lt__(self, other):
    if self.value < other.value:
      return True
    else:
      return False

  def __eq__(self, other):
    if self.value == other.value:
        return True
    else:
        return False

  def __sub__(self, other):
    return (self.value - other.value)
