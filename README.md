# PyScanner
A Python-based port scanner that allows you to use multiple threads to search a given IP address for open ports. Simply specify the starting and terminating port numbers, as well as the number of threads to utilize.
- IP address of the target host
- Starting and ending port range to scan
- Number of threads to use for scanning

## Installation
```sh
git clone https://github.com/KamiKaramazov/PyScanner.git
```

## Usage
```sh
cd PyScanner
python PyScanner.py <ip>
```
The tool will request the user to input the starting and finishing port ranges, as well as the number of scanning threads. When the scan is finished, a list of open ports with their related service names (if available) will be shown.



