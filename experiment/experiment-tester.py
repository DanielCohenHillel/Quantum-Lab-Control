import pyvisa
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import experiment as exp

in_address = "USB0::0x0483::0x7540::SPD30GB3150177::INSTR"
out_address = "USB0::0x0957::0x17A6::MY54351085::0::INSTR"

v = np.linspace(0, 1, 10)

config = {
    "input":{
        0:{
            "address": in_address,
            "config":{
                "CH1:VOLT": 0.0
            },
            "variables":{
                "CH1:VOLT": v
            }
        }
    },
    "output": {
        0:{
            "address": out_address,
            "config": {
                "conf_command": "command"
            },
            "variables":{
                "command": "command_var"
            }
 
        }
    }
}


def main():
    test = exp.Experiment(config)
    print(test.measure())

if __name__ == '__main__':
    print("             ----  Run Main  ----\n")
    main()
    print("\n             ----  End Main  ----")
