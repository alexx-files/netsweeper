from netsweeper import NetSweeper

scan = NetSweeper('192.168.100.0/24', 100, 1)
"""
Where: 
    '192.168.100.0/24': Network, IP Range or IP address to be scanned. Accept a txt file name with IP address list.
    100: Number of simultaneos ping threads.
    1: delay time to timeout.
    For more scan options see example_verbose_custom_params.py
"""

# Use one of the next four lines to define which ports will be scanned.
# scan.scanports = 'TCPLOWPORTS'
# scan.scanports = 'TCPHIGHPORTS'
# scan.scanports = 'ALLPORTS'
scan.scanports = [21, 22, 53, 80, 135, 139, 443, 445, 902, 912]


scan.return_down_hosts = False  # Define if ICMP down host will be returned.
scan.scan_down_host_ports = False  # Define if the ICMP down host ports will be scanned.
scan.max_ports_scan_threads = 100  # Define the number of ports to be scanned simultaneously per host

scan.verbose_run()  # scan the network in verbose mode. The results are printed in Python console.

# The scan results are stored in the 'results' property and can be manipulated as did in the example.py
# See README.md for more information about 'results' structure.
