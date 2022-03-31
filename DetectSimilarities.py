from thefuzz import fuzz

lines = []

with open("inputtext.txt", 'r') as textfile:
    for line in textfile:
        lines.append(line)

matrix = []

for line1 in lines:
    scores = []
    for line2 in lines:
        tokenscore = fuzz.token_sort_ratio(line1, line2) / 100
        ratioscore = fuzz.ratio(line1, line2) / 100
        score = (tokenscore + ratioscore) / 2
        scores.append(score)
    matrix.append(scores)

with open("scores.csv", 'w+') as scorefile:
    for line in matrix:
        for score in line[:-1]:
            scorefile.write(f"{score}, ")
        scorefile.write(f"{line[-1]}")
        scorefile.write("\n")