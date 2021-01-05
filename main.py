def change_colour(c):
  print(f"Your current colour is {colour}")
  print("What would you like to change it to?")
  c = input()
  return c

colour = "Red"
c = change_colour(colour)
print(f"Your current colour is {c}")