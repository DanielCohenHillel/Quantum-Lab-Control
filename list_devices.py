import numpy as np
import scipy as sp
import pyvisa
import visa
import time

# Open the default visa resource manager
rm = pyvisa.ResourceManager()
# List of all instruments
instruments = np.array(rm.list_resources())

# Print all connected visa devices and if they're reachable
print("             All Resources")
print("             -------------")
for ins in instruments:
    # Open the instrument to talk to it
    instrument = rm.open_resource(ins)
    # Try to communicate with the instrument and get it's name
    try:
        # Set read and write termination so the instruments will know when to start and stop read/write
        instrument.read_termination = '\n'
        instrument.write_termination = '\n'

        instrument.write("*IDN?")
        time.sleep(1)  # Sleep timeout for old instruments
        # idn = instrument.read()
        print("*", str(ins), "   is ", str(instrument.read()), "\n")
    except visa.VisaIOError:
        # Failed to connect
        print("* No connection to ", instrument, "\n")