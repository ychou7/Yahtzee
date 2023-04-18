from player import Player

print("-Yahtzee-")
player = Player()
while True:
  player.roll_dice()
  print(player)
  #case1: 3 of kind, print You got 3 of a kind
  # object.method()
  if player.has_three_of_a_kind():
    print("You got 3 of a kind!")

  #case2: series, print you got a series of 3!
  elif player.has_series():
    print("You got a series of 3!")

  #case3: pair, print you got a pair!
  elif player.has_pair():
    print("You got a pair!")
  #else: nothing,abs print Awww. Too bad.
  else:
    print("Aww. Too Bad.")
  # Score = 0
  print(f"Score = {player.player_points}")
  # ask user for play again
  while True:
    reply = input("Play again? (Y/N): ")
    if reply != "y" and reply != "n":
      print("Invalid input - should be a 'Yes' or 'No'.")
    else:
      break

  if reply == "n":
    print("Game Over.")
    print(f"Final Score = {player.player_points}")
    break
