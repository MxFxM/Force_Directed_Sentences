# other imports
import matplotlib.pyplot as plt
import numpy as np

# import the package
import forcelayout as fl

# Need a dataset to visualise
dataset = None
with open("scores.csv", encoding='utf8') as scorefile:
    dataset = np.loadtxt(
        scorefile,
        delimiter=',',
    )

names = []
with open("inputtext.txt", 'r') as textfile:
    for line in textfile:
        names.append(line)

def annotate_points(node, i):
    return names[i]

# Need to use the brute force algorithm on a dataset this small
# (not recommended for larger datasets)
layout = fl.draw_spring_layout_animated(dataset=dataset,
                                        algorithm=fl.SpringForce,
                                        annotate=annotate_points)

plt.show()