from die import Die


class Player:

  # Player class (player.py) – has two attributes: a list of 3 Die objects and the player’s points.
  # 1. __init__(self) – constructs and sorts the list of three Die objects and initializes the
  # player’s points to 0.
  # 2. get_points(self) – returns the player’s points.
  # 3. roll_dice(self) – calls roll on each of the Die objects in the dice list and sorts the list.
  # 4. has_pair(self) – returns true if two dice in the list have the same value (uses ==).
  # Increments points by 1.
  # 5. has_three_of_a_kind(self) – returns true if all three dice in the list have the same
  # value (uses ==). Increments points by 3.
  # 6. has_series(self) – returns true if the values of each of the dice in the list are in a
  # sequence (ex. 1,2,3 or 2,3,4 or 3,4,5 or 4,5,6) (uses -). Increments points by 2.
  # 7. __str__(self) – returns a string in the format: “D1=2, D2=4, D3=6”.

  def __init__(self):
    self.die_objects = list()
    self.player_points = 0
    for i in range(3):
      self.die_objects.append(Die())

    self.die_objects.sort()

  def get_points(self):
    return self.player_points

  def roll_dice(self):
    for die in self.die_objects:
      die.roll()
    self.die_objects.sort()

  def has_pair(self):
    d1, d2, d3 = self.die_objects
    # 3 same
    if d1 == d2 and d2 == d3 and d3 == d1:
      return False
    # 3 not same
    if d1 != d2 and d2 != d3 and d3 != d1:
      return False

    self.player_points += 1
    return True

  def has_three_of_a_kind(self):
    d1, d2, d3 = self.die_objects
    if d1 == d2 and d2 == d3 and d3 == d1:
        self.player_points += 3
        return True
    else:
        return False

  def has_series(self):
    d1, d2, d3 = self.die_objects
    if d2 - d1 == 1 and d3 - d2 == 1:
        self.player_points += 2
        return True
    else: 
        return False
 # returns a string in the format: “D1=2, D2=4, D3=6”.
  # example: f"D1 = {variable}, D2 = {varialbe}"
  def __str__(self):
    d1, d2, d3 = self.die_objects
    return f"D1 = {d1}, D2 = {d2}, D3 = {d3}"
      
