import numpy.random as rd
import matplotlib.pyplot as plt


def simul_X():
    pile = 0
    for i in range(3):
        x=rd.random()
        if x < 1/3:
            pile += 1
    return pile
