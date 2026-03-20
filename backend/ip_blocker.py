import os

def block_ip(ip):
    print("Blocking IP:",ip)

    cmd=f'netsh advfirewall firewall add rule name="Block {ip}" dir=in action=block remoteip={ip}'

    os.system(cmd)