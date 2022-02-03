import subprocess
from optparse import OptionParser
import re
def get_user_input():
    opt_obje = OptionParser()
    opt_obje.add_option("-i","--interface",dest="interface",help="interface to change")
    opt_obje.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return  opt_obje.parse_args()

def change_mac(inter,new_mac):
    subprocess.run(["ifconfig",inter,"down"])
    subprocess.run(["ifconfig",inter,"hw","ether",new_mac])
    subprocess.run(["ifconfig",inter,"up"])

def control_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig)).group()     # python 2 and python 3 library difference --> str(ifconfig)
    return new_mac

print("Welcome to MacChanger")
(values,key) = get_user_input()
change_mac(values.interface,values.mac_address)
final_mac = control_mac(values.interface)

if final_mac == values.mac_address:
    print(f"Changing the Mac address of interface {values.interface} to {values.mac_address}")
else:
    print("Mac address not changed")