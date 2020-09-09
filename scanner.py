#TODO: argument parser with the option to not export the data; list rooms to IA project
import pandas as pd

from os.path import exists
from os import getcwd
from wifi import Cell, Scheme
from get_nic import getnic

ssid = []
mac_address = []
dbm_signal = []

def output_operation(data_frame: pd.DataFrame) -> bool:
    """
    This function verifies if output file exists already and change permissions of pandas.DataFrame.to_csv if it's either True or False.
    param data_frame: an existent pandas.DataFrame
    Returns True if output file exists.
    """
    if exists("/home/edmarcaixeta/Documentos/repos/wifi_reporter/output.csv"):
        data_frame.to_csv(r"/home/edmarcaixeta/Documentos/repos/wifi_reporter/output.csv", mode='a')
        return True
    else:
        data_frame.to_csv(r"/home/edmarcaixeta/Documentos/repos/wifi_reporter/output.csv", mode='w') 
        return False

def df_creation(ssid: list, signal: list, mac:list) -> pd.DataFrame:
    """
    This function creates a new pandas.DataFrame by using a new dictionary created by the provided lists.
    param ssid: list of wireless networks ssid.
    param signal: list of wireless networks dB signals.
    param mac: list of wireless networks mac adresses. 
    Returns a new Data Frame.
    """
    data_frame = pd.DataFrame({'SSID' : ssid, 'Signal' : signal, 
                                'MAC ADDRESS' : mac})
    return data_frame

if __name__ == "__main__":
    try:
        #Getnic.interfaces()[2] usually returns the correct interface, but you can change it if not works for you
        interface = str(getnic.interfaces()[2])
        networks = Cell.all(interface)
    except:
        print("Unavailable or incorrect wireless interface. Please inform the correct one:")
        interface = input()
        try:
            networks = Cell.all(interface)
        except:
            print("Please run \"nmcli device status\" command to check your system WiFi interfaces.")
            exit(0)
        
    print("__________________Wifi Networks Scanner__________________")

    for network in networks:
            ssid.append(network.ssid)
            mac_address.append(network.address)
            dbm_signal.append(str(network.signal) + "dB")
    
    df = df_creation(ssid, dbm_signal, mac_address)
    print("WiFi status appended to output.csv file located at program folder") if output_operation(df) else print("output.csv file created at program folder")
               
    print(df)