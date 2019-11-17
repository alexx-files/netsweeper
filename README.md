### netsweeper
Python class to allow programmers to create easily your own net sweeper scripts. The examples added to the package already are net sweepers that can be used and improved

> Requires Ping3 https://github.com/kyan001/ping3 (Downloaded automaticaly)
> Tested under Linux and Windows

## Installation

```shell
pip install netsweeper  # install nesweeper
```
## Usage
    # Verbose Mode
    ```
    from netsweeper import NetSweeper
    scan = NetSweeper('192.168.0.0/24', 100, 1)
    scan.verbose_run()
    ```
    # No Interaction Mode
    ```
    from netsweeper import NetSweeper
    scan = NetSweeper('192.168.0.0/24', 100, 1)
    scan.run()
    ```

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
        scan_results (READ ONLY)
            dictionary: store results of network scan
            Structure:
                Key: IP Address in integer format (Interger format is easier to sort IP addresses than string)
                Value: Turple of four values:
                    (str:ip address,
                     boolean: Host up=True Host down=False,
                     float: ping delay time (return the value of ping_timeout argument when the ping timeout,
                     str: The IP address hostname)
        down_hosts (READ/WRITE)
            boolean: define if return or not the not found hosts
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
        packetcount (READ/WRITE)
            int: define the number of icmp packets send to the destination host

Uses the ping() function from the library ping3 developed by kai@kyan001.com https://github.com/kyan001/ping3
