import os

from netmiko import ConnectHandler

user = os.environ["USER"]
password = os.environ["PASSWORD"]

iosv_l2_s1 = {
    "device_type": "juniper",
    "ip": "172.25.240.245",
    "username": user,
    "password": password,
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command("show configuration | display set")
print(output)
