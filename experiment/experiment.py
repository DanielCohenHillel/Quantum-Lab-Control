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
                print("\n\n* Connected successfully to ", device.read(), "\n")
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

        # Run measurement
        # com, variables = dev_conf["vars"]

        # var_combinations = list(product(*variables))
        # for combination in var_combinations:
        #     command = com.format(*combination)
        #     print(command)
        #     # device.write(command)
        #     # TODO: Maybe need to change the delay to wait for the device to finish
        #     time.sleep(0.01)

        # print("Do some stuff")
        # result = 0
        # return result

        # print("USB0::0x0483::0x7540::SPD30GB3150177::INSTR" == rm.list_opened_resources()[0].resource_name)
        open_resources = rm.list_opened_resources()
        open_resources_address = [resource.resource_name for resource in open_resources]

        # print(open_resources_address)
        states = []
        # states_values = []
        address_state = []
        device_state = []


        for i, dev_conf in config.items():
            # print(dev_conf)
            voltages = []
            for com, value in dev_conf["vars"].items():
                # print(value)
                # print(list(product(*value)))
                state_com = []
                for v in product(*value):
                    voltages.append(v[0])
                    state_com.append(com.format(*v))
                    # states_values.append(v)
                states.append(state_com)
                address_state.append(dev_conf.get("address"))
                
                # TODO: Change this to exeption
                print("Instument isn't connected " + dev_conf["address"]) if (not dev_conf["address"] in open_resources_address) else print("Nice")
                dev_index = None
                for k in range(len(open_resources)):
                    if open_resources[k].resource_name == dev_conf["address"]:
                        dev_index = k
                # print(dev_index)
                device_state.append(open_resources[dev_index])
        # print(voltages)
        # print(states_values)
        full_States = list(product(*states))

        measured_test = []
        for state in full_States:
            print("\nSet State\n---------")
            for i, command in enumerate(state):
                print(command, "-"*(40 - len(command)) +
                      "> ", address_state[i])
                # TODO: Add here device write command
                # print(command)
                device_state[i].write(str(command))


                # rm.list_opened_resources()[0].write(str(command))
                time.sleep(0.01)
                # print(rm.list_opened_resources()[0].read())
                # print(i)

            print("\nMeaure\n-------")
            for i, dev_conf in config.items():
                for tran_type, command in dev_conf["meas"].items():
                    com_str = tran_type + " || " + command
                    print(com_str,
                          "-"*(40 - len(com_str)) + "> ", address_state[i])
                    # TODO: Add measure command here
                    # print(i)
                    device_state[i].write(str(command))
                    time.sleep(0.01)
                    measured_test.append(float(device_state[i].read()))
                    print(measured_test[len(measured_test)-1])
                    time.sleep(0.01)
                # for i, dev_conf in config.items():
        print(len(voltages))
        print(measured_test)
        plt.plot(voltages, measured_test)
        plt.show()

        return 0


    def make_file(self):
        pass
