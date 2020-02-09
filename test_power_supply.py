import pyvisa
import time

# def slow_query(inst, command):
#     """
#     Slow query is query for slow, old devices. If a device is too slow for the computer you need to wait before
#     reading from the instrument after writing to it

#     :param instrument inst:
#         The instrument to query
#     :param string command:
#         The command to query to the device
#     """
#     inst.write(command)
#     time.sleep(0.1)  # Sleep timeout for old instruments
#     return inst.read()

rm = pyvisa.ResourceManager()

ins = "USB0::0x0483::0x7540::SPD30GB3150177::INSTR"
print(type(rm.list_resources()[0]))
instrument = rm.open_resource(ins)
# Try to communicate with the instrument and get it's name
try:
    # Set read and write termination so the instruments will know when to start and stop read/write
    instrument.read_termination = '\n'
    instrument.write_termination = '\n'

    # print("*", ins, "   is ", slow_query(instrument, "*IDN?"))

    instrument.write("*IDN?")
    time.sleep(0.1)  # Sleep timeout for old instruments
    # idn = instrument.read()
    print("*", str(ins), "   is ", str(instrument.read()), "\n")
    
    print("\n--- Successfull connection! ---\n")
except pyvisa.VisaIOError:
    # Failed to connect
    print("* No connection to ", instrument, "\n")
    
instrument.write("CH1:VOLT 0.4321")
time.sleep(0.1)
instrument.write("CH1:VOLT?")
time.sleep(0.1)
print("\n Voltage:", instrument.read())
time.sleep(0.1)
instrument.write("CH1:VOLT 0.1234")
time.sleep(0.1)
instrument.write("CH1:VOLT?")
time.sleep(0.1)
print("\n Voltage:", instrument.read())
