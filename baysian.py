import daft
import pymc3
import matplotlib.pyplot as plt
import matplotlib as mlp
import numpy as np
#import ggplot
import pandas as pd

COLORS = ["#348ABD", "#A60628", "#7A68A6"]

pgm = daft.PGM([9, 4], origin=[1, 0.5])
pgm.add_node(daft.Node('r', 'rain', 3, 4, aspect=2))
pgm.add_node(daft.Node('s', 'sprinkler', 9, 4, aspect=3))
pgm.add_node(daft.Node('w', 'grass wet', 6, 2, aspect=4, observed=True))
pgm.add_edge('r', 's')
pgm.add_edge('r', 'w')
pgm.add_edge('s', 'w')
pgm.render()
pgm.figure.savefig("sprinkler.png", dpi=500)