# netsweeper
Python class to allow programmers to create easily your own net sweeper scripts. The examples added to the package already are net sweepers that can be used and improved

> Requires Ping3 https://github.com/kyan001/ping3 (Downloaded automaticaly)\
> Tested under Linux and Windows

## Installation

```shell
pip install netsweeper  # install nesweeper
```
## Usage

#### Verbose Mode
```
from netsweeper import NetSweeper
scan = NetSweeper('192.168.0.0/24', 100, 1)
scan.verbose_run()
```

The results are printed in the Python console:

```
Scanning the network: 192.168.100.0/24

192.168.0.1   True      4ms	router
192.168.0.10  True      4ms	WindowsLaptop1
192.168.0.25  True    341ms	Cellphone
192.168.0.43  True    210ms	WindowsLaptop1
192.168.0.121 True     10ms	Printer

Elapsed time: 6.83 seconds
Found 5 hosts up in the network 192.168.0.0/24.
```


#### No Interaction Mode
```
from netsweeper import NetSweeper
scan = NetSweeper('192.168.0.0/24', 100, 1)
scan.run()
```
A dictionary is stored in the property 'results' with the scan results.
The property 'results' is read only and have the following structure:
```
Key: IP Address in integer format (Interger format is easier to sort IP addresses than string)
Value: Turple of four values:
  (str:ip address,
  boolean: Host up=True Host down=False,
  float: ping delay time (return the value of ping_timeout argument when the ping timeout,
  str: The IP address hostname)
```
## Examples

```
from netsweeper import NetSweeper

scan = NetSweeper('192.168.100.0/24', 100, 1)
"""
Where: 
    '192.168.100.0/24': Network to be scanned.
    100: Number of simultaneos ping threads. More threads equals to fast scans, but more errors in unreliable networks.
    1: delay time to timeout. Lower values equals to fast scans, but more timeouts in unreliable networks.
    To simpler example see example_verbose.py
"""

scan.return_down_hosts = False  # Do not return not found hosts. Not necessary as the default value is already False
scan.return_unit = 'ms'  # return the reply delay time in miliseconds. Verbose mode only work in miliseconds.
scan.src_addr = '192.168.100.101'  # set the source IP address
scan.packet_ttl = 32  # set icmp packet time to live
scan.icmp_seq = 0  # set icmp packet sequence
scan.payload_size = 56  # set icmp packet payload size
scan.packetcount = 3  # set the number of tries until timeout. Increase the scan time.

scan.run()  # scan the network in verbose mode. The results are printed in Python console.

# The scan results are stored in the property 'results' and can be manipulated as following.
# See documentation for more information about 'results' structure.

for key in sorted(scan.results.keys()):  # interact with sorted property 'results'
    print(f'IP Address: {scan.results[key][0]:<16s}', end='')  # print the IP Address. No \n at the end of the line.
    print(f'{scan.results[key][2]:>4.0f}', end='')  # print delay time in miliseconds.
    if scan.results[key][1]:  # print the status of the host according to boolean value
        print(f'Host UP'.center(11), end='')   # print Host UP
    else:
        print(f'Host DOWN'.center(11), end='')  # print Host DOWN
    print(f'Hostname: {scan.results[key][3]}')  # print the hostname
```
