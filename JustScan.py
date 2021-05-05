#Whois Scan and Port Scan
import socket, threading
import time
import whois


def connect_tcp(host, port, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((host, port))
        output[port] = 'OPEN'
    except:
        output[port] = ''


def scan_ports(host, delay):
    threads = []        # Runs connect_tcp
    output = {}         # For Output
    for i in range(1000): # Spawns threads to scan ports
        t = threading.Thread(target=connect_tcp, args=(host, i, delay, output))
        threads.append(t)
    for i in range(1000):
        threads[i].start()
    for i in range(1000): # locks main thread until scan completion
        threads[i].join()
    for i in range(1000): # Printing all ports that are OPEN
        if output[i] == 'OPEN':
            print(str(i) + ': ' + output[i])


def main():
    host = input("Host IP or Domain: ")
    try:
        delay = int(input("timeout setting (2 is default): "))
    except ValueError:
        delay = 2
    start_time = time.time()
    whois_result = whois.whois(host)
    print('---PORTS---')
    scan_ports(host, delay)
    print('---WHOIS---')
    print(whois_result)
    end_time = time.time() - start_time
    print('Took '+ str(end_time) + ' seconds')


if __name__ == "__main__":
    main()
