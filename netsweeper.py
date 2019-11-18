#!/usr/bin/env python

"""Python class to allow programmers to create easily your own net sweeper scripts."""
from __future__ import print_function

from ipaddress import ip_address, ip_network
from ping3 import ping
from socket import gethostbyaddr
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter


class NetSweeper:
    """
    Class to allow the creation of Netsweeper programs in Python
    Functions:
    __init__:
        (Constructor)
        Args:
            networkaddress: str: define network address to be scanned
            num_threads:    int: define number of ping thread
            timeout:        int: define delay time until timeout (Default value 1)

        Methods:
            run():
                Run the scan in the network and store the results in the property scan_results.
            run_verbose():
                Run the scan in the network, store the results in the property scan_results amd show the results
                formated in Python console.

        Properties:
            networkaddress (READ/WRITE)
                str: define network address to be scanned
            num_threads (READ/WRITE)
                int: define number of ping threads
            timeout (READ/WRITE)
                int: define delay time until timeout
            results (READ ONLY)
                dictionary: store results of network scan
                Structure:
                    Key: int IP Address (Interger is easier to sort IP addresses than string)
                    Value: Turple of four values:
                        (str:ip address,
                         boolean: Host up=True Host down=False,
                         float: ping delay time (return the value of ping_timeout argument when the ping timeout,
                         str: The IP address hostname)
            down_hosts (READ/WRITE)
                boolean: define if return or not the not found hosts. Default = False
            return_unit (READ/WRITE)
                str: define the return unit for reply time (s) secs or (ms) mili secs
            src_addr (READ/WRITE)
                str: define ping source address
            packet_ttl (READ/WRITE)
                int: define icmp packet time to live
            icmp_seq (READ/WRITE)
                int: define icmp packet sequence
            payload_size (READ/WRITE)
                int: define icmp packet payload size
            retrycount (READ/WRITE)
                int: define the number of retries to send before timeout

    Uses the ping() function from the library ping3 developed by kai@kyan001.com https://github.com/kyan001/ping3"""

    def __init__(self, networkaddress, num_threads, timeout=1):
        self._networkaddress = networkaddress  # str: define network address to be scanned
        self._num_threads = num_threads  # int: define number of ping threads
        self._timeout = timeout  # int: define delay time until timeout
        self._scan_results = {}  # dct: results of network scan
        self._return_down_hosts = False  # boo: define if return or not the not found hosts
        self._return_unit = 's'  # str: define the return unit for reply time (s) secs or (ms) mili secs
        self._src_addr = None  # str: define ping source address
        self._packet_ttl = 64  # int: define icmp packet time to live
        self._icmp_seq = 0  # int: define icmp packet sequence
        self._payload_size = 56  # int: define icmp packet payload size
        self._retrycount = 1  # int: define the number of tries to send before timeout

    ########################################################################################################################
    #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  GETTERS AND SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    ########################################################################################################################

    @property
    def return_unit(self):
        return self._return_unit

    @return_unit.setter
    def return_unit(self, return_unit):
        self._return_unit = return_unit

    @property
    def retrycount(self):
        return self._retrycount

    @retrycount.setter
    def retrycount(self, retrycount):
        self._retrycount = retrycount

    @property
    def payload_size(self):
        return self._payload_size

    @payload_size.setter
    def payload_size(self, payload_size):
        self._payload_size = payload_size

    @property
    def icmp_seq(self):
        return self._icmp_seq

    @icmp_seq.setter
    def icmp_seq(self, icmp_seq):
        self._icmp_seq = icmp_seq

    @property
    def src_addr(self):
        return self._src_addr

    @src_addr.setter
    def src_addr(self, src_addr):
        self._src_addr = src_addr

    @property
    def packet_ttl(self):
        return self._packet_ttl

    @packet_ttl.setter
    def packet_ttl(self, packet_ttl):
        self._packet_ttl = packet_ttl

    @property
    def return_down_hosts(self):
        return self._return_down_hosts

    @return_down_hosts.setter
    def return_down_hosts(self, return_down_hosts):
        self._return_down_hosts = return_down_hosts

    @property
    def results(self):
        return self._scan_results

    @property
    def networkaddress(self):
        return self._networkaddress

    @networkaddress.setter
    def networkaddress(self, networkaddress):
        self._networkaddress = ip_network(networkaddress)

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = int(timeout)

    @property
    def num_threads(self):
        return self._num_threads

    @num_threads.setter
    def num_threads(self, num_threads):
        self._num_threads = num_threads

    def _gethostname(self, ipaddress):
        try:
            data = gethostbyaddr(ipaddress)
            return repr(data[0])
        except Exception:
            return 'Hostname not found'

    ########################################################################################################################
    #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  INTERNAL FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    ########################################################################################################################

    def _ping_address(self, ipaddress, ping_timeout):
        """Ping an IP address
        Args:
            ipaddress:      str: IP address to ping
            ping_timeout:   int: Ping timeout in seconds
        Returns:
            Tuple:
                (str:ip address,
                 boolean: Host up=True Host down=False,
                 float: ping delay time (return the value of ping_timeout argument when the ping timeout,
                 str: The IP address hostname)"""

        ipaddress = str(ipaddress)
        ping_ip = 0
        for _ in range(self._retrycount):
            ping_ip = ping(dest_addr=ipaddress, timeout=ping_timeout, unit=self._return_unit, src_addr=self._src_addr,
                           ttl=self._packet_ttl, seq=self._icmp_seq, size=self._payload_size)
            if type(ping_ip) == float:
                break
        if type(ping_ip) == float:
            return ipaddress.replace("'", ""), True, ping_ip, self._gethostname(ipaddress).replace("'", "")
        else:
            return ipaddress, False, ping_timeout * 1000, ''

    ########################################################################################################################
    #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  CLASS METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    ########################################################################################################################

    def run(self):
        """Execute the network scan using threads. The results are stored in the property 'results'.
        See properties documentation for more details."""
        self._scan_results.clear()  # Clear results of previous scans
        networkaddresslist = list(ip_network(self._networkaddress).hosts())  # convert from string to networkaddress
        timeout_list = []
        for _ in networkaddresslist:  # create a list with timeout value in all positions
            timeout_list.append(self._timeout)
            # necessary because all args of function _ping_address must be iterators
            # when using threads

        with ThreadPoolExecutor(max_workers=self._num_threads) as executor:
            threadsresults = executor.map(self._ping_address, networkaddresslist, timeout_list)
            for result in threadsresults:
                if self._return_down_hosts:
                    self._scan_results[ip_address(result[0])] = result
                else:
                    if result[1]:
                        self._scan_results[ip_address(result[0])] = result

    def verbose_run(self):
        """Execute the network scan using threads. The results are stored in the property 'results'.
        See properties documentation for more details.
        Show the results formatted in the Python console"""
        start = perf_counter()
        # print(f'\nScanning the network: {self._networkaddress}\n')
        print('\nNetSweeper version 0.2.6')
        print('Scanning the network: {}\n'.format(self._networkaddress))
        self.return_unit = 'ms'
        self.run()
        for key in sorted(self.results.keys()):
            if self.results[key][2] <= 100:
                # print(
                # f'{self.results[key][0]:<16s}{str(self.results[key][1]):<7s}\033[32m{self.results[key][2]:>4.0f}ms'
                # f'\033['f'0m\t{self.results[key][3]}')
                print('{:<16s} {}\t \033[32m{:.0f}ms\033[0m\t{}'.format(self.results[key][0], str(self.results[key][1]),
                                                           self.results[key][2], self.results[key][3]))
            elif self.results[key][2] <= 500:
                #print(
                #    f'{self.results[key][0]:<16s}{str(self.results[key][1]):<7}\033[33m{self.results[key][2]:>4.0f}ms'
                #    f'\033['f'0m\t{self.results[key][3]}')
                print('{:<16s} {}\t \033[33m{:.0f}ms\033[0m\t{}'.format(self.results[key][0], str(self.results[key][1]),
                                                           self.results[key][2], self.results[key][3]))
            else:
                #print(
                #    f'{self.results[key][0]:<16s}{str(self.results[key][1]):<7}\033[31m{self.results[key][2]:>4.0f}ms'
                #    f'\033['f'0m\t{self.results[key][3]}')
                print('{:<16s} {}\t \033[31m{:.0f}ms\033[0m\t{}'.format(self.results[key][0], str(self.results[key][1]), self.results[key][2], self.results[key][3]))
        end = perf_counter()
        print('\nElapsed time: {} seconds'.format(round(end - start, 2)))
        hosts_up = 0
        for result in self.results:
            if self.results[result][1]:
                hosts_up += 1
        print('Found {} hosts up in the network {}.'.format(hosts_up, self._networkaddress))
