import re

def check_ip_address(ip):
    if re.match(r'^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
, ip):
        return "IPv4"
    
    elif re.match(r'^\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b$', ip):
        return "IPv6"

    else:
        return "Bukan IP Address"

n = int(input())

for _ in range(n):
    input_str = input().strip()
    result = check_ip_address(input_str)
    print(result)
