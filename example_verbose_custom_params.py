from netsweeper import NetSweeper

scan = NetSweeper('192.168.100.0/24', 100, 1)
"""
Where: 
    '192.168.100.0/24': Network to be scanned.
    100: Number of simultaneos ping threads. More threads equals to fast scans, but more errors in unreliable networks.
    1: delay time to timeout. Lower values equals to fast scans, but more timeouts in unreliable networks.
    To simpler example see example_verbose.py
"""

scan.return_down_hosts = True  # Return not found hosts
scan.return_unit = 'ms'  # return the reply delay time in miliseconds. Verbose mode only work in miliseconds.
scan.src_addr = '192.168.100.101'  # set the source IP address
scan.packet_ttl = 32  # set icmp packet time to live
scan.icmp_seq = 0  # set icmp packet sequence
scan.payload_size = 56  # set icmp packet payload size
scan.packetcount = 3  # set the number of tries until timeout. Increase the scan time.

scan.verbose_run()  # scan the network in verbose mode. The results are printed in Python console.

# The scan results are stored in the property 'results' and can be manipulated as did in the example.py
# See documentation for more information about 'results' structure.
