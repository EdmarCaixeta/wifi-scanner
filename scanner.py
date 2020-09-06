import pandas as pd

from os.path import exists
from wifi import Cell, Scheme
from get_nic import getnic

ssid = []
mac_address = []
dbm_signal = []

if __name__ == "__main__":
    try:
        networks = Cell.all(str(getnic.interfaces()[2]))
    except:
        print("Unavailable or incorrect wireless interface. Please inform the correct one:")
        interface = input()
        networks = Cell.all(interface)
    
    print("__________________Wifi Networks Scanner__________________")

    for network in networks:
            ssid.append(network.ssid)
            mac_address.append(network.address)
            dbm_signal.append(str(network.signal) + "dB")

    data_frame = pd.DataFrame({'SSID' : ssid, 'Signal' : dbm_signal, 
                                'MAC ADDRESS' : mac_address})
    
    if exists("./output.csv"):
        print("Wifi status appended to output.csv file located at program folder")
        data_frame.to_csv("output.csv", mode='a')
    else:
        print("Output.csv file created at program folder")
        data_frame.to_csv("output.csv", mode='w')
            

    print(data_frame)
        