import ea_psu_controller
import time
import datetime
# more information on https://pypi.org/project/ea-psu-controller/

def get_time_stamp():
    time_var = datetime.datetime.now()
    return time_var.strftime("%y-%m-%d %H:%M:%S")

ps_com_port = 'COM8'
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
    voltage_step = 0.1
    Vout_high = 13.5
    Vout_low = 0
    vout = Vout_low
    Nreps = 100
    step_delay = 0.1
    step_num = round((Vout_high - Vout_low) / voltage_step)
    ramp_up_time = round(step_num * step_delay,3)
    ramp_up_slope = round((Vout_high - Vout_low) / ramp_up_time,3)
    print(f"Ramp up time: {ramp_up_time  } sec")
    print(f"Ramp up slope: {ramp_up_slope} V/sec")
    for x in range(0, Nreps):
        print(get_time_stamp(),"-"*20, "Cycle number: ", x, "-"*50)
        step_delay = 0.05
        step_num = round((Vout_high - Vout_low) / voltage_step)
        ramp_up_time = round(step_num * step_delay, 3)
        ramp_up_slope = round((Vout_high - Vout_low) / ramp_up_time, 3)
        print(f"Ramp up time: {ramp_up_time} sec")
        print(f"Ramp up slope: {ramp_up_slope} V/sec")
        # print(f"Cycle number: {x}")
        print(f"Ramp up voltage from {Vout_low} V to {Vout_high} V with { voltage_step} V increments   ")

        for v in range(round((Vout_high - Vout_low) / voltage_step)):
            ps.set_voltage(vout)
            time.sleep(step_delay)
            vout = round((vout + voltage_step), 3)  # function round should be used
        print("Wait for 10 secs ")
        time.sleep(20)
        ps.set_voltage(0)
        time.sleep(5)
        Vout_low = round(Vout_low + 0.1, 3)
        vout = Vout_low

        # for v in range(round((Vout_high - Vout_low) / voltage_step)):
        #     ps.set_voltage(vout)
        #     time.sleep(step_delay)
        #     vout = round((vout - voltage_step), 3)
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
