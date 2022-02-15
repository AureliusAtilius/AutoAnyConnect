import ifcfg, requests,subprocess,keyboard,time,win32gui


def windowEnumerationHandler(hwnd, top_windows):
    #Create list of top windows
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def bring_to_front():
    #Take list of top windows, search for Cisco Anyconnect and bring to front.
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "cisco anyconnect secure mobility client" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break

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

def hit_enter():
    #Wait one second then click enter
    bring_to_front()
    time.sleep(1)
    keyboard.press('enter')  


if __name__=='__main__':
    if connectionCheck("https://google.com"):
        openproc("C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpnui.exe")
        hit_enter()

