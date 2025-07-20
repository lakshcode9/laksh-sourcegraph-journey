from scapy.all import ARP, Ether, srp, IP, ICMP, sr1
import socket
def arp_scan(subnet="192.168.56.0/24"):
    print(f"[*] Scanning subnet: {subnet}")
    arp = ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]
    hosts = [received.psrc for sent, received in result]
             
    print(f"[+] Found {len(hosts)} active hosts.")
    return hosts
def scan_ports(ip, ports=range(1, 1025)):
    print(f"\n[*] Scanning ports on {ip}")
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ip, port))
            open_ports.append(port)
            sock.close()
        except Exception:
            pass
    return open_ports

def guess_os(ip):
    pkt = IP(dst=ip)/ICMP()
    reply = sr1(pkt, timeout=1, verbose=0)
    if reply:
        ttl = reply.ttl
        if ttl >= 128:
            return "Windows"
        elif ttl >= 64:
            return "Linux"
    return "Unknown"

def main():
    subnet = "192.168.56.0/24"
    hosts = arp_scan(subnet)
    
    for ip in hosts:
        ports = scan_ports(ip)
        os_guess = guess_os(ip)
        print(f"\n[+] {ip} - OS: {os_guess}")
        print(f" Open Ports: {ports if ports else 'none'}")

if __name__ == "__main__":
    main()