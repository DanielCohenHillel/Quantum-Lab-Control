import numpy as np
import scipy as sp
import matplotlib as plt
import matplotlib.pyplot as plt
import pyvisa
import time
from itertools import product


class Experiment:
    """
    Class used to represent a scanner object, to create a meaurement,
    simply enter the input space and a dictionary that sets up all the
    instrument and call the measure() function

    ...

    Attributes
    ----------
    :param dictionary config:
        Configuration of the experiment, what instruments are the input,
        what instrument measure the outputs and what the outputs are.
        See config docomentation
    """
    # TODO: Rewrite the docomentation, add config docomentation
    def __init__(self, config):
        self.config = config

    def _check_inputs(self):
        """
        Checks that all the inputs given are of correct form and format
        """
        pass

    def measure(self):
        """
        Does the measurment according to the configuration of the objects
        and returns the results of the measurement
        :return list(ndarray):
            Returns the result of the measurments
        """
        config = self.config

        # Setup resource manager to manage all the instrument and their connections
        rm = pyvisa.ResourceManager()

        # TODO: Maybe combine the input and output initilization
        # Initilazation
        for i, dev_conf in config.items():
            address = dev_conf["address"]

            device = rm.open_resource(address)
            # Try to connect to device
            try:
                # Set read and write termination so the instruments will know when to start and stop read/write
                device.read_termination = '\n'
                device.write_termination = '\n'

                device.write("*IDN?")
                time.sleep(0.1) 
                print("* Connected successfully to ", device.read(), "!!")
            except pyvisa.VisaIOError:
                print("Couln't connect to device with VISA address", address, "check that it is properly"
                "connected. You can use the list_devices.py script to check all available devices")
                return 1

            try:
                # Initilize
                for key, value in dev_conf["init"].items():
                    # print(command + " "+ str(value))
                    command = key + " " + str(value)
                    device.write(command)
                    time.sleep(0.1)
            except pyvisa.VisaIOError:
                print("There was an error when initilizing the instruments")

            # Run system change 
            # Run measurement
            for keyy, val in dev_conf["meas"].items():
                for key, values in dev_conf["vars"].items():
                    var_combinations = list(product(*values))
                    # print(var_combinations)
                    for combination in var_combinations:
                        # print(combination)
                        command = key.format(*combination)
                        print(command)
                        device.write(command)
                        time.sleep(0.1) # TODO: Maybe need to change the delay to wait for the device to finish

                        # for v in value:
                        # command = key
                        # print(command)
                        # device.write(val)
                        time.sleep(0.1) # TODO: Maybe need to change the delay to wait for the device to finish
                        # print(device.read())

        
        print("Do some stuff")
        result = 0
        return result

    def make_file(self):
        pass
