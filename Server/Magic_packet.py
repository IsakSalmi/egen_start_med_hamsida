from wakeonlan import send_magic_packet
import Config as Config
MAC_ADR = Config.MAC
IP = Config.IP

def Magic_packet():
    send_magic_packet(MAC_ADR, ip_address=IP)
    print("det funkar")