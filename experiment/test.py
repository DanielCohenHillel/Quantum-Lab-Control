import pyvisa
import time

adr = "USB0::0x0483::0x7540::SPD30GB3150177::INSTR"

rm = pyvisa.ResourceManager()

inst = rm.open_resource(adr)
inst.read_termination = '\n'
inst.write_termination = '\n'

inst.write("*IDN?")
time.sleep(0.1)
print(inst.read(), "\n\n")

inst.write('CURV?')
time.sleep(0.1)
data = inst.read_raw()
print(data)