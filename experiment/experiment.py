import numpy as np
import scipy as sp
import matplotlib as plt
import matplotlib.pyplot as plt
import pyvisa
import time


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

        # Initilazation
        # Input
        input_devices = config["input"]
        for i, dev_conf in input_devices.items():
            address = dev_conf["address"]

            device = rm.open_resource(address)
            # Try to connect to device
            try:
                # Set read and write termination so the instruments will know when to start and stop read/write
                device.read_termination = '\n'
                device.write_termination = '\n'

                device.write("*IDN?")
                time.sleep(0.1)  # Sleep timeout for old instruments
                print("* Connected successfully to ", device.read(), "!!")
            except pyvisa.VisaIOError:
                print("Couln't connect to device with VISA address", address, "check that it is properly"
                "connected. You can use the list_devices.py script to check all available devices")
            print("Do some stuff")

        result = 0
        return result

    def make_file(self):
        pass
