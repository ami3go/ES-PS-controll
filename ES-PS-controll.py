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

try:
    print(f'Switching remote control on')
    psu.remote_on()
    time.sleep(0.5)
    print(f'Setting voltage to {out_voltage} V')
    psu.set_voltage(out_voltage)
    time.sleep(0.5)


    print(f'Turning on output')
    psu.output_on()

    print(psu.get_status())
    for n in range (100):
        out_voltage = 1 + n*0.1
        psu.set_voltage(out_voltage)
        time.sleep(2)
        actual_voltage = psu.get_voltage()
        voltage_error = 100 - (actual_voltage/out_voltage)*100
        print(f"Set Voltage:{out_voltage}, Actual voltage:{actual_voltage}, difference:{voltage_error}")
        time.sleep(3)



except Exception as e:
    print(e)
    print(f'close connection...')
    print("close remote control ")
    psu.remote_off()
    print("close connection ")
    psu.close(remote=False, output=False)
