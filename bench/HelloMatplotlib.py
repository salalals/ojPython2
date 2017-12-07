#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

x = range(100)
y = map(lambda x: x * x - 2 * x + 1, x)
plt.plot(x, y)
plt.show()
