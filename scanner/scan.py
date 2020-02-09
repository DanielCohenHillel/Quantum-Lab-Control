import numpy as np
import scipy as sp
import matplotlib as plt
import matplotlib.pyplot as plt
import pyvisa


class Scan:
    """
    Class used to represent a scanner object, to create a meaurement,
    simply enter the input space and a dictionary that sets up all the
    instrument and call the measure() function

    ...

    Attributes
    ----------
    :param list(ndarray) inputs:
        The input space of measurment, the measurment will sets the
        instruments to output whatever you put in the inputs for every
        possible input combination
    :param dictionary config:
        Configuration of the instruments, what instruments are the input,
        what instrument measure the outputs and what the outputs are.
        See config docomentation
    """
    # TODO: Rewrite the docomentation, add config docomentation
    def __init__(self, inputs, config):
        pass

    def measure():
        """
        Does the measurment according to the configuration of the objects
        and returns the results of the measurement
        :return list(ndarray):
            Returns the result of the measurments
        """
        pass

    def make_file():
        pass


def main():
    pass


if __name__ == '__main__':
    print("             ----  Run Main  ----\n")
    main()
    print("\n             ----  End Main  ----")
