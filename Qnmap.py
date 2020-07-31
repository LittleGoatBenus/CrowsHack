import nmap

scanner = nmap.PortScanner()
print("Nmap Version: ", scanner.nmap_version())

IP = input("IP: ")
type(IP)

scans = input("""please select the type of scan you wish to perform
                 1. SYN ACK scan 
                 2. OS scan
                 3. UDP scan 
		 4. Complete scan\n""")
print("please wait...")

if scans == '1':
	scanner.scan(IP, '1-1024', '-v -sS')
	print(scanner.scaninfo())
	print("Ip is: ", scanner[IP].state())
	print(scanner[IP].all_protocols())
	print("open ports: ", scanner[IP]['tcp'].keys())

elif scans == '2':
	scanner.scan(IP, '1-1024', '-v -O')
	print(scanner.scaninfo())
	print("Ip is: ", scanner[IP].state())
	print(scanner[IP].all_protocols())
	print("open ports: ", scanner[IP]['tcp'].keys())

elif scans  == '3':
	scanner.scan(IP, '1-1024', '-v -sU')
	print(scanner.scaninfo())
	print("Ip is: ", scanner[IP].state())
	print(scanner[IP].all_protocols())
	print("open ports: ", scanner[IP]['tcp'].keys())
elif scans == '4':
	scanner.scan(IP, '1-1024', '-v -sS -sV -sC -A -O')
	print(scanner.scaninfo())
	print("Ip is: ", scanner[IP].state())
	print(scanner[IP].all_protocols())
	print("open ports: ", scanner[IP]['tcp'].keys())

  
                 
