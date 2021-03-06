from netsweeper import NetSweeper

scan = NetSweeper('192.168.100.0/24', 10, 1)
"""
Where: 
    '192.168.100.0/24': Network, IP Range or IP address to be scanned. Accept a txt file name with IP address list.
    100: Number of simultaneos ping threads.
    1: delay time to timeout.
    For more scan options see example_verbose_custom_params.py
"""

scan.verbose_run()  # scan the network in verbose mode. The results are printed in Python console.

# The scan results are stored in the 'results' property and can be manipulated as did in the example.py
# See README.md for more information about 'results' structure.
