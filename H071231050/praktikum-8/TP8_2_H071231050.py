import re
def ipv4 (ip) :
    IPv4 = r'^((25[0-5]|2[0-4]\d|1\d{2}|[0-9]{2}|[0-9])\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[0-9]{2}|[0-9])$'
    return re.match (IPv4,ip)
def ipv6 (ip) :
    IPv6 = r'^([a-f0-9]{1,4}:){7}[a-f0-9]{1,4}$'
    return re.match (IPv6, ip)
jumlah = int(input ("berapa kali perulangan : "))
text = []
for i in range(jumlah) :
    text.append(input(f"masukkan IP Addres ke {i + 1} : "))
    
for ip in text :
    if ipv4(ip) :
        print ("IPv4")
    elif ipv6 (ip) :
        print ("IPv6")
    else :
        print ("Bukan IP Address ")

# This line has trailing whitespace
# 121.203.197.20
# 2001:0db8:0000:0000:0000:ff00:0042:8329