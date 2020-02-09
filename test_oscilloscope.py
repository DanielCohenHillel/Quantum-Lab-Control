import pyvisa
import numpy as np
import time
import matplotlib as mpl
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager()
ins = "USB0::0x0957::0x17A6::MY54351085::0::INSTR"
instrument = rm.open_resource(ins)
# Try to communicate with the instrument and get it's name
try:
    # Set read and write termination so the instruments will know when to start and stop read/write
    instrument.read_termination = '\n'
    instrument.write_termination = '\n'

    instrument.write("*IDN?")
    time.sleep(0.1)  # Sleep timeout for old instruments
    print("*", str(ins), "   is ", str(instrument.read()), "\n")
    
    print("\n--- Successfull connection! ---\n")
except pyvisa.VisaIOError:
    # Failed to connect
    print("* No connection to ", instrument, "\n")

instrument.write(":ACQ:TYPE AVER")
instrument.write(":ACQ:COMP 100")
instrument.write(":ACQ:COUN 8")
instrument.write(":DIG CHAN4")
instrument.write(":WAV:SOUR CHAN4")
instrument.write(":WAV:FORM BYTE")
instrument.write(":WAV:POIN 1000")
v = instrument.query_binary_values(":WAV:DATA?")
v = np.array(v)
print(len(v))
x = np.linspace(0, 1, len(v))
plt.plot(x,v)
plt.show()