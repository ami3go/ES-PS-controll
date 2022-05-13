import ea_psu_controller
import time
# more information on https://pypi.org/project/ea-psu-controller/

ps_com_port = 'COM5'
out_voltage = 0


ps_name = ea_psu_controller.PsuEA.PSU_DEVICE_LIST_WIN

print(f'Power Supply name: {ps_name}')

print(f'Connecting to  {ps_com_port}')
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
    out = 0.00
    voltage_step = 0.5
    Vout_high = 15
    Vout_low = 1
    vout = Vout_low
    Nreps = 100
    step_delay = 1
    step_num = round((Vout_high - Vout_low) / voltage_step)
    ramp_up_time = step_num * step_delay
    ramp_up_slope = (Vout_high - Vout_low) / ramp_up_time
    print(f"Ramp up time: {ramp_up_time  } sec")
    print(f"Ramp up slope: {ramp_up_slope} V/sec")
    for x in range(0, Nreps):
        print(f"Cycle number: {x}")
        print("Ramp up voltage ")
        for v in range(round((Vout_high - Vout_low) / voltage_step)):
            ps.set_voltage(vout)
            time.sleep(step_delay)
            vout = round((vout + voltage_step), 3)  # function round should be used
        print("Ramp down voltage ")
        for v in range(round((Vout_high - Vout_low) / voltage_step)):
            ps.set_voltage(vout)
            time.sleep(step_delay)
            vout = round((vout - voltage_step), 3)
        # print("Meander")
        # ps.set_voltage(0)
        # time.sleep(2)
        # ps.set_voltage(6.5)
        # time.sleep(2)
        # ps.set_voltage(0)


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
