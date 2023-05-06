import sys
import socket
import threading
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

# Get scan options from the user
try:
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    threads = int(input("Enter number of threads to use: "))
except ValueError:
    print("Invalid input for port range or number of threads.")
    sys.exit()

if start_port < 0 or end_port < start_port:
    print("Invalid port range.")
    sys.exit()

if threads < 0:
    print("Invalid number of threads.")
    sys.exit()

# Add a pretty banner
# Add a pretty banner
print("\033[94m" + "-" * 60 + "\033[0m")
print("\033[94m" + " ___         ___                                      " + "\033[0m")
print("\033[94m" + "(  _ \      (  _ \                                    " + "\033[0m")
print("\033[94m" + "| |_) )_   _| (_(_)  ___   _ _  ___   ___    __  _ __ " + "\033[0m")
print("\033[94m" + "|  __/( ) ( )\__ \ / ___)/ _  )  _  \  _  \/ __ \  __)" + "\033[0m")
print("\033[94m" + "| |   | (_) | )_) | (___( (_| | ( ) | ( ) |  ___/ |   " + "\033[0m")
print("\033[94m" + "(_)    \__  |\____)\____)\__ _)_) (_)_) (_)\____)_)   " + "\033[0m")
print("\033[94m" + "      ( )_| |                                         " + "\033[0m")
print("\033[94m" + "       \___/                                          " + "\033[0m")
print("\033[94m" + "    PyScan - Port Scanner - By KamiKaramazov" + "\033[0m")
print("\033[94m" + "-" * 60 + "\033[0m")
print("\033[93m" + "Scanning target: " + target + "\033[0m")
print("\033[93m" + "Time started: " + str(datetime.now()) + "\033[0m")
print("\033[94m" + "-" * 60 + "\033[0m")

# Define a function to handle port scanning for each thread
def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = 0.01
    s.settimeout(timeout)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service_name = socket.getservbyport(port)
            except:
                service_name = "unknown"
            print(f"Port {port} ({service_name}) is open")
    except socket.error:
        pass
    finally:
        s.close()

# Scan the ports using multiple threads
for i in range(threads):
    t = threading.Thread(target=lambda: [scan_port(port) for port in range(start_port+i, end_port+1, threads)])
    t.start()

# Wait for all threads to finish
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

# Add a pretty banner to indicate the end of the scan
print("-" * 50)
print("Time completed: " + str(datetime.now()))
print("Scan completed!")
