# more information on https://pypi.org/project/ea-psu-controller/
# installation: pip3 install ea_psu_controller
"""

    EA PS power supply control script
    Simple ON/ OFF cycling to check device durability.

"""

import ea_psu_controller
import time
import datetime
import Logging_class as logclass

folder = r"C:\Users\achestni\Desktop\PycharmProjects\Libraries\ES-PS-controll\chcm_log"
file_name = "log.txt"
logger = logclass.txt_logger()
logger.set_folder(folder)
logger.set_file_name(file_name)
logger.init("chcm_cycling")



# please define your COM port
# USB\VID_232E&PID_0010\

def get_time():
    time_var = datetime.datetime.now()
    return time_var.strftime("%y-%m-%d %H:%M:%S")

ps_com_port = 'COM13'

ps_name = ea_psu_controller.PsuEA.PSU_DEVICE_LIST_WIN

ps_name = "PS 2042-10B"
print(f'Power Supply name: {ps_name}')

print(f'Connecting to  {ps_com_port}')
ps = ea_psu_controller.PsuEA(comport=ps_com_port)
print(f'Connected to  {ps.get_device_description()}')
time.sleep(0.5)

# initial voltage of power supply
out_voltage = 0


try:
    print(f'Switching remote control on')
    ps.remote_on()
    time.sleep(0.5)
    print(f'Setting voltage to {out_voltage} V')
    ps.set_voltage(out_voltage)
    ps.set_ocp(1.5)
    time.sleep(0.5)


    print(f'Turning on output')
    ps.output_on()

    Vout_high = 13.5  # Set a HIGH voltage

    Vout_low = 1  # Set LOW voltage , Set 0 for Switch off

    Nreps = 1000000  # number of cycles, Better to use for cycle to prevent software stuck

    ONtime = 10  # on time in seconds

    OFFtime = 10  # off time in seconds

    vout = Vout_low

    """
    ***** Cycling start ***** 
    """

    for x in range(0, Nreps):
        chcm_current = []
        ps.set_voltage(Vout_high)

        for samples in range(50):
            chcm_current.append(round(ps.get_current(), 3))
            time.sleep(0.2)
        logger.print_and_log(f"Cnt, {x}, V, {round(ps.get_voltage(), 3)}, Cur, {chcm_current} ")
        # print(f"{get_time()}, Cnt, {x}, V, {round(ps.get_voltage(), 3)}, Cur: {chcm_current} ")
        ps.set_voltage(Vout_low)
        time.sleep(OFFtime)

    # disconnect and stop communication
    time.sleep(2)
    ps.output_off()
    ps.close()


# in case something got wrong
except Exception as e:
    print("*"*50)
    print(e)
    print(f'close connection...')
    print("close remote control ")
    print("close connection ")
    print("*"*50)
    ps.set_voltage(0)
    ps.output_off()
    ps.remote_off()
    ps.close(remote=False, output=False)
