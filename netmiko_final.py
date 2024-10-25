from netmiko import ConnectHandler
from pprint import pprint

device_ip = "10.0.15.181"
username = "admin"
password = "cisco"

device_params = {
    "device_type": "cisco_ios",
    "ip": device_ip,
    "username": username,
    "password": password,
}


def gigabit_status():
    ans = ""
    with ConnectHandler(**device_params) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("", use_textfsm=True)
        for status in result:
            if status["interface"] == "GigabitEthernet0/0":
                status = status["status"].lower()
                if status == "up":
                    up += 1
                elif status == "down":
                    down += 1
                elif status == "administratively down":
                    admin_down += 1
        ans = f"Interface GigabitEthernet0/0: {up} up, {down} down, {admin_down} administratively down"
        pprint(ans)
        return ans
