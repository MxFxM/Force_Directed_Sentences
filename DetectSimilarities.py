from thefuzz import fuzz

lines = []

with open("inputtext.txt", 'r') as textfile:
    for line in textfile:
        lines.append(line)

matrix = []

for line1 in lines:
    scores = []
    for line2 in lines:
        scores.append(fuzz.token_sort_ratio(line1, line2))
    matrix.append(scores)

with open("scores.csv", 'w+') as scorefile:
    for line in matrix:
        for score in line[:-1]:
            scorefile.write(f"{score}, ")
        scorefile.write(f"{line[-1]}")
        scorefile.write("\n")