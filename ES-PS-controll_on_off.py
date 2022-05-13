import ea_psu_controller
import time
# more information on https://pypi.org/project/ea-psu-controller/

ps_com_port = 'COM13'
out_voltage = 0


ps_name = ea_psu_controller.PsuEA.PSU_DEVICE_LIST_WIN

ps_name = "PS 2042-10B"
print(f'Power Supply name: {ps_name}')

print(f'Connecting to  {ps_com_port}')
# ps = ea_psu_controller.PsuEA(ps_name)
ps = ea_psu_controller.PsuEA(comport=ps_com_port)
txt = ps.get_device_description()
print(f'Connected to  {txt}')
time.sleep(0.5)

try:
    print(f'Switching remote control on')
    ps.remote_on()
    time.sleep(0.5)
    print(f'Setting voltage to {out_voltage} V')
    ps.set_voltage(out_voltage)
    time.sleep(0.5)


    print(f'Turning on output')
    ps.output_on()
    Vout_high = 15
    Vout_low = 1
    vout = Vout_low
    Nreps = 1000
    ONtime = 2
    OFFtime = 1
    for x in range(0, Nreps):

        ps.set_voltage(Vout_high)
        time.sleep(ONtime)
        print(f"Counter: {x}, Voltage: {round(ps.get_voltage(),3)}, Current: {round(ps.get_current(),3)}")
        ps.set_voltage(Vout_low)
        time.sleep(OFFtime)


    time.sleep(2)
    ps.output_off()
    ps.close()



except Exception as e:
    print(e)
    print(f'close connection...')
    print("close remote control ")
    ps.remote_off()
    print("close connection ")
    ps.close(remote=False, output=False)
