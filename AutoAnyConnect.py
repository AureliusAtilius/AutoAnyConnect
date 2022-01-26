import ifcfg, requests



def connectionCheck():
    
    interfaces = ifcfg.interfaces()
    result= False
    try:

        if (not interfaces['Ethernet adapter Ethernet']['inet'] and interfaces['Wireless LAN adapter Wi-Fi']['inet']!= None):
            request=requests.get("https://karemaircraft.com", timeout=3)
            result = True
    except KeyError:
        print("Check Adapter Names")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection")
    return result

