import subprocess
import optparse

"""
    This program is to show the option of how to use the program and also 
    what to run during the CLI purpose 
"""

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface ", dest="interface", help="interface to change its mac address")
    parser.add_option("-m", "--mac ", dest="newMacAddress", help="New Mac Address")
    (options, arguments) = parser.parse_args()
    if options.interface:
        parser.error("[-] Please specify an interface, use -h, --help for more info")
    elif options.newMacAddress:
        parser.error("[-] Please specify a New Mac Address, use -h, --help for more info")
    return options

def change_macAddress(interface, macAddress):
    print("[+] Changed the Mac Address for " + interface + "to ", + macAddress)

    # using the list to take in arguments is becasuse 
    # we dont want the user to input malicious code 
    # during the input system
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", macAddress])
    subprocess.call(["ifconfig", interface, "up"])

# parser = optparse.OptionParser()

# parser.add_option("-i", "--interface ", dest=" interface", help="interface to change its mac address")
# parser.add_option("-m", "--mac ", dest=" newMacAddress", help="New Mac Address")

# (options, arguments) = parser.parse_args()

# raw_input = python 2.7
# input = = python 3, be vary of chosing 
# interface = options.interface
# macAddress = options.newMacAddress

if __name__ == "__main__":
    options = get_arguments()
    change_macAddress(options.interface, options.newMacAddress)
    
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    print(ifconfig_result)
