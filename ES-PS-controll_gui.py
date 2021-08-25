import ea_psu_controller
import time

import tkinter
from tkinter import messagebox

ps_com_port = 'COM8'
out_voltage = 0


ps_name = ea_psu_controller.PsuEA.PSU_DEVICE_LIST_WIN
print(f'Power Supply name: {ps_name}')

print(f'Connecting to  {ps_com_port}')
psu = ea_psu_controller.PsuEA(comport=ps_com_port)
txt = psu.get_device_description()
print(f'Connected to  {txt}')
time.sleep(0.5)
psu.remote_on()

root = tkinter.Tk()
root.title(f'Control panel for {txt}, on {ps_com_port}')
frame = tkinter.Frame(root)
frame.pack()

ps_volt_val = tkinter.StringVar()
ps_volt_val.set("00.00")



def ps_on():
    print(f'Switching out on')
    psu.output_on()

def ps_off():
    print(f'Switching out off')
    psu.output_off()

def ps_off_on():
    print(f'Switching out off')
    psu.output_off()
    time.sleep(8)
    psu.output_on()
    time.sleep(1)

def ps_set_12V():
    psu.set_voltage(12)

def ps_set_V():
    volt = ps_volt_val.get()
    psu.set_voltage(float(volt))




button_on = tkinter.Button(frame,
                   text="ON",
                   fg="red",
                   width=25,
                   height=2,
                   command=ps_on)
button_on.pack(side=tkinter.LEFT)

button_off = tkinter.Button(frame,
                   text="OFF",
                   fg="red",
                   width=25,
                   height=2,
                   command=ps_off)

button_off.pack(side=tkinter.LEFT)

button_off_on = tkinter.Button(frame,
                   text="OFF_ON",
                   fg="red",
                   width=25,
                   height=2,
                   command=ps_off_on)

button_off_on.pack(side=tkinter.LEFT)


button_set12V = tkinter.Button(frame,
                   text="Set12V",
                   fg="red",
                   width=25,
                   height=2,
                   command=ps_set_12V())

button_set12V.pack(side=tkinter.LEFT)

ps_set_voltage = tkinter.Entry(root, width=20,  textvariable=ps_volt_val)
ps_set_voltage.pack(side=tkinter.BOTTOM)
button_set_V = tkinter.Button(frame,
                   text="Set",
                   fg="red",
                   width=25,
                   height=2,
                   command=ps_set_V)

button_set_V.pack(side=tkinter.BOTTOM)

root.mainloop()
# more information on https://pypi.org/project/ea-psu-controller/


try:
    while True:
        cmd = input("Enter command:")
        if cmd == "on":
            print(f'Switching out on')
            psu.output_on()
            time.sleep(0.5)
        if cmd == "off":
            print(f'Switching out Off')
            psu.output_off()
            time.sleep(0.5)
        if cmd == "toggle":
            print(f'Switching out Off')
            psu.output_off()
            wait_time = 10
            print(f"wait for: {wait_time}")
            time.sleep(wait_time)
            print(f'Switching out ON')
            psu.output_on()
            time.sleep(wait_time)
        if cmd.isdigit():
            print(f'Setting voltage to {cmd} V')
            psu.set_voltage(int(cmd))



except Exception as e:
    print(e)
    print(f'close connection...')
    print("close remote control ")
    psu.remote_off()
    print("close connection ")
    psu.close(remote=False, output=False)
