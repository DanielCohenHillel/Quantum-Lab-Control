# Lab_Control
Instrument control library for Prof. Nadav Katz's lab

How it works
----------
An experiment could be simply defined with a *config dictionary* and an *experiment object*.
First create a config dictionary(as explained below), then, initilize an experiment object with that config.

The Config
---------
The config is the most important part of the setup, you set the input and output instruments, the experiment itself and everything else.

A config dictionaty is of the form
```py
config = {
    # List of input instruments
    "input":{
        0:{
            # The visa address of the first instrument
            "address": address,
            # The initial configuration of the instrument
            "config":{
                "Command 1": Command1,
                "Command 2": Command2,
            },
            # List of variables that change between each measurement
            "variables":{
                "Variable 1": v1,
                "variable 2": v2    
            }
        },
        
        1:{
            ...
        }
    },
    # List of output instruments
    "output": {
        0:{
            # The visa address of the first instrument
            "address": address,
            # The initial configuration of the instrument
            "config":{
                "Command 1": Command1,
                "Command 2": Command2,
            },
            # List of measured data
            "measurements":{
                0: "measured element 1",
                1: "measured element 2"
            }
        },

        1:{
            ...
        }
    }
}
```

Some explenation of the structure

* **input** - list of all the input instruments
    * **device** - The input device, can set as many of these as you want
        * **address** - The VISA address of the instrument
        * **config** - the initial configuration of the instrument, this are things like dc offsets that don't change, and more
            * **commands** - These are the command to set up the initial configuration
        * **variables** - A list of the variables that change with the experiment
            * **Variable** - The command that set's up the variable followed by an ndarray of the experiment variables

* **output** - list of all the output instruments
    * **device** - The measurement device, can set as many of these as you want
        * **address** - The VISA address of the instrument
        * **config** - the initial configuration of the instrument, this are things like oscilloscope time window
            * **commands** - These are the command to set up the initial configuration
        * **variables** - A list of the variables that change with the experiment
            * **Variable** - The command that set's up the variable followed by an ndarray of the experiment variables


Example
-------
```py
import numpy as np
from experiment import Experiment

# Addresses of power supply and oscilloscope
in_address = "USB0::0x0483::0x7540::SPD30GB3150177::INSTR"
out_address = "USB0::0x0957::0x17A6::MY54351085::0::INSTR"

# Measure over different voltages between 0 and 1 volt
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

# Create an experiment object with my experiment
my_experiment = Experiment(config)

# Do the experiment and measure the results into the result variable
result = my_experiment.measure()
```
<!-- TODO: Change output in config>