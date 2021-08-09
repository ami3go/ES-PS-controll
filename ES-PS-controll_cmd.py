import ea_psu_controller
import time
# more information on https://pypi.org/project/ea-psu-controller/

ps_com_port = 'COM9'
out_voltage = 0


ps_name = ea_psu_controller.PsuEA.PSU_DEVICE_LIST_WIN
print(f'Power Supply name: {ps_name}')

print(f'Connecting to  {ps_com_port}')
psu = ea_psu_controller.PsuEA(comport=ps_com_port)
txt = psu.get_device_description()
print(f'Connected to  {txt}')
time.sleep(0.5)
psu.remote_on()

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
