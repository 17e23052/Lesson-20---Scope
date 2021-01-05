def change_direction(d):
  print(f"Current direction: {direction}")
  print("Enter new direction")
  d = input()
  return d

def change_speed(s):
  print(f"Current speed: {speed}")
  print("Enter new speed")
  s = input()
  return s

speed = 10
direction = "North"

d = change_direction(direction)
s = change_speed(speed)

print(f"New direction: {d}")
print(f"New speed: {s}")
