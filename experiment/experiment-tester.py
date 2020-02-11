# Imports
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pyvisa
import scipy as sp

import experiment as exp

in_address = "USB0::0x0483::0x7540::SPD30GB3150177::INSTR"
out_address = "USB0::0x0957::0x17A6::MY54351085::0::INSTR"

v = np.linspace(0, 1, 11)
'''
    TODO:
    Need to make it so you can get every possible instrument state and then measure,
    Right now you can only change one device at a time.

    Need to make it so multiple commands are possible at once with spliting
    the ';' character

    add measurement that distinguishes between BIN and ASCII.
'''

config = {
    0: {
        "address": in_address,
        "init": {
            "CH1:VOLT": 0.1
        },
        "vars": {
            "CH1:VOLT {}": (v,)
        },

        "meas": {
            "BIN  ": "CH1:VOLT?"
        }
    },
}


def main():
    test = exp.Experiment(config)
    print(test.measure())


if __name__ == '__main__':
    print("             ----  Run Main  ----\n")
    main()
    print("\n             ----  End Main  ----")
