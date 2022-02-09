import ifcfg, requests,subprocess



def connectionCheck(ext_domain):
    #Get network information
    interfaces = ifcfg.interfaces()
    result= False
    #Check which network adapter is connected. If Wifi is connected then check connectivity to external domain.
    try:

        if (not interfaces['Ethernet adapter Ethernet']['inet'] and interfaces['Wireless LAN adapter Wi-Fi']['inet']!= None):
            request=requests.get(ext_domain, timeout=3)
            result = True
    except KeyError:
        print("Check Adapter Names")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection")
    return result

def openproc(exe_path):
    #Open vpn client
    try:
        subprocess.Popen(exe_path)
    except FileNotFoundError:
        print("Unable to locate process.")
    


def runsikuli(ide_path, script_path):
    #Run Sikuli script to click "Connect" button.
    sikuli_path=[ide_path,"-r",script_path]
    try:
        subprocess.Popen(sikuli_path, shell=True)
    except FileNotFoundError:
        print("Unable to locate script.")
    



if __name__=='__main__':
    if connectionCheck("https://google.com"):
        openproc("C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpnui.exe")
        runsikuli(<Path to Sikuli IDE>,<Path to Sikuli script>}

