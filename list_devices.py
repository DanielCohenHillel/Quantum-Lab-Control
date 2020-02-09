import pyvisa
import time

# Open the default visa resource manager
rm = pyvisa.ResourceManager()
# List of all instruments
instruments = rm.list_resources()

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
        time.sleep(0.1)  # Sleep timeout for old instruments
        # idn = instrument.read()
        print("*", str(ins), "   is ", str(instrument.read()), "\n")
    except pyvisa.VisaIOError:
        # Failed to connect
        print("* No connection to ", instrument, "\n")