# Imports
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pyvisa
import scipy as sp

import experiment as exp

address = "USB0::0x0483::0x7540::SPD30GB3150177::INSTR"

voltages = np.linspace(0, 1, 11)

config = {
    0: {
        "address": address,
        "init": {
            "CH2:VOLT": 0.1
        },
        "vars": {
            "CH1:VOLT {}": (voltages,)
        },

        "meas": {
            "BIN ": "CH1:VOLT?"
        }
    },
}

test = exp.Experiment(config)
test.measure()
