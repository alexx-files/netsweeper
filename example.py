from netsweeper import NetSweeper

scan = NetSweeper('192.168.100.0/24', 100, 1)
"""
Where: 
    '192.168.100.0/24': Network, IP Range or IP address to be scanned.
    100: Number of simultaneos ping threads. More threads equals to fast scans, but more errors in unreliable networks.
    1: delay time to timeout. Lower values equals to fast scans, but more timeouts in unreliable networks.
    For simpler example see example_verbose.py
"""

scan.return_down_hosts = False  # Do not return not found hosts. Not necessary as the default value is already False
scan.return_unit = 'ms'  # return the reply delay time in miliseconds. Verbose mode only work in miliseconds.
scan.src_addr = '192.168.100.101'  # set the source IP address
scan.packet_ttl = 32  # set icmp packet time to live
scan.icmp_seq = 0  # set icmp packet sequence
scan.payload_size = 56  # set icmp packet payload size
scan.retrycount = 3  # set the number of tries until timeout. Increase the scan time.

scan.run()  # scan the network. The results are stored in the 'results' property.

# The scan results are stored in the 'results' property and can be manipulated as following.
# See README.md for more information about 'results' structure.

for key in sorted(scan.results.keys()):  # interact with sorted property 'results'
    print(f'IP Address: {scan.results[key][0]:<16s}', end='')  # print the IP Address. No \n at the end of the line.
    print(f'{scan.results[key][2]:>4.0f}', end='')  # print delay time in miliseconds.
    if scan.results[key][1]:  # print the status of the host according to boolean value
        print(f'Host UP'.center(11), end='')   # print Host UP
    else:
        print(f'Host DOWN'.center(11), end='')  # print Host DOWN
    print(f'Hostname: {scan.results[key][3]}')  # print the hostname
