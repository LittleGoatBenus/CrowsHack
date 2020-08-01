import nmap3

nmap = nmap3.Nmap()
nmapT = nmap3.NmapScanTechniques()


print("""

       Join the CrowsNest Discord : https://discord.gg/B5vJbSC
 ▄████▄   ██▀███   ▒█████   █     █░ ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
▒██▀ ▀█  ▓██ ▒ ██▒▒██▒  ██▒▓█░ █ ░█░▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒
▒▓█    ▄ ▓██ ░▄█ ▒▒██░  ██▒▒█░ █ ░█ ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░
▒▓▓▄ ▄██▒▒██▀▀█▄  ▒██   ██░░█░ █ ░█ ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄
▒ ▓███▀ ░░██▓ ▒██▒░ ████▓▒░░░██▒██▓ ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ░▒ ▒  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▓░▒ ▒   ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ░  ▒     ░▒ ░ ▒░  ░ ▒ ▒░   ▒ ░ ░   ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
░          ░░   ░ ░ ░ ░ ▒    ░   ░   ░  ░░ ░  ░   ▒   ░        ░ ░░ ░
░ ░         ░         ░ ░      ░     ░  ░  ░      ░  ░░ ░      ░  ░
░creator: LittleGoatBenus                                       ░



""")
opt = input("""
1. Nmap scanner




""")


if opt == '1':
    print("""
                                ___.-------.___
                            _.-' ___.--;--.___ `-._
                        .-' _.-'  /  .+.  \  `-._ `-.
                      .' .-'      |-|-o-|-|      `-. `.
                     (_ <O__      \  `+'  /      __O> _)
                       `--._``-..__`._|_.'__..-''_.--'
                             ``--._________.--''

  """)
    print(nmap.nmap_version())

    print("\n This is an automated nmap scanner created by LittleGoatBenus")

    ip_a = input("IP/Host: ")

    TypeSc = input("""
 1. Top port scan       6. TCP scan
 2. OS detection        7. UDP scan
 3. Service Version     8. Firewall detection
 4. ping scan           9. workinprogress
 5. SYN ACK scan        10.workinprogress     15. All scan

""")

    if TypeSc == '1':
        res = nmap.scan_top_ports(ip_a)
        print("please wait...")
        print(res)

    elif TypeSc == '2':
        osres = nmap.nmap_os_detection(ip_a)
        print("please wait...")
        print(osres)

    elif TypeSc == 3:
        serres = nmap.nmap_version_detection(ip_a)
        print("please wait...")
        print(serres)

    elif TypeSc == 4:
        pingres = nmapT.nmap_ping_scan(ip_a)
        print("please wait...")
        print(pingres)

    elif TypeSc == 5:
        synres = nmapT.nmap_syn_scan(ip_a)
        print("please wait...")
        print(synres)

    elif TypeSc == 6:
        tcpres = nmapT.namp_tcp_scan(ip_a)
        print("please wait...")
        print(tcpres)

    elif TypeSc == 7:
        udpres = nmapT.nmap_udp_scan(ip_a)
        print("please wait...")
        print(udpres)

    elif Typesc == 8:
        fireres = nmap.nmap_detect_firewall(ip_a)
        print("please wait...")
        print(fireres)

    elif TypeSc == 15:
        osres = nmap.nmap_os_detection(ip_a)
        serres = nmap.nmap_version_detection(ip_a)
        synres = nmapT.nmap_syn_scan(ip_a)
        Ares = nmap.port_scan(ip_a, args='-Sv -sS -A -O -T4')
        print("please wait...")
        print(osres,serres,synres)
