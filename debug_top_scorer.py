scores = {}
while True:
    entry = input("Enter player and score as 'name score' (or type 'stop' to finish):\n")
    if entry.lower() == "stop":
        break
    name, score = entry.split()
    score = int(score)
    if name in scores:
        scores[name] += score
    else:
        scores[name] = score
if len(scores) == 0:
    print("No scores recorded.")
else:
    top_name = ""
    top_score = 0 
    for player, points in scores.items():
        if points > top_score:
            top_score = points
            top_name = player
    print("Top scorer:", top_name, "with", top_score, "points.")