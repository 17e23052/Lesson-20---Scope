def increase_score(score):
  if answer == "Yes":
    score = score + 1
  return score


score = 0
answer = "Yes"
score = increase_score(score)
print(score)