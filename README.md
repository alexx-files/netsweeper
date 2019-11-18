# netsweeper
[![GitHub contributors](https://img.shields.io/github/contributors/alexx-files/netsweeper.svg)](https://github.com/alexx-files/netsweeper/graphs/contributors/)

Python class to allow programmers to easily create your own net sweeper scripts. The examples provided already
are net sweepers that can be used and improved.

> Requires Ping3 https://github.com/kyan001/ping3 (Downloaded automaticaly)\
> Tested under Linux and Windows

## Installation

```shell
pip install netsweeper  # install netsweeper
```
## Usage

#### No Interaction Mode
```
from netsweeper import NetSweeper
scan = NetSweeper('192.168.0.0/24', 100, 1)
scan.run()
```
The scan results are stored in the 'results' property as a dictionary.
The 'results' property is read only and have the following structure:
```
Key: IP Address in integer format (Interger format is easier to sort IP addresses than string)
Value: Tuple of four values:
  (str:ip address,
  boolean: Host up=True Host down=False,
  float: ping delay time # return the value of ping_timeout argument when the ping timeout,
  str: The IP address hostname)
```

#### Verbose Mode
```
from netsweeper import NetSweeper
scan = NetSweeper('192.168.0.0/24', 100, 1)
scan.verbose_run()
```

The results are printed in the Python console:

```
Scanning the network: 192.168.0.0/24

192.168.0.1   True      4ms	router
192.168.0.10  True      4ms	WindowsLaptop1
192.168.0.25  True    341ms	Cellphone
192.168.0.43  True    210ms	WindowsLaptop1
192.168.0.121 True     10ms	Printer

Elapsed time: 6.83 seconds
Found 5 hosts up in the network 192.168.0.0/24.
```
#### Properties
```
networkaddress (READ/WRITE)
    str: define network address to be scanned
num_threads (READ/WRITE)
    int: define number of ping threads
timeout (READ/WRITE)
    int: define delay time until timeout
results (READ ONLY)
    dictionary: store network scan results
    Structure:
        Key: int IP Address (Interger is easier to sort IP addresses than string)
        Value: Turple of four values:
            (str:ip address,
             boolean: Host up=True Host down=False,
             float: ping delay time (return the value of ping_timeout argument when the ping timeout,
             str: The IP address hostname)

Optional parameters can be set to change the scan behavior:
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
    int: define the number of tries to send before timeout
```

## Examples

### example_verbose.py
```
This example show the simpler way to use netsweeper to scan a network. Only three parameters are passed 
and the results are printed in the Python console.
```

### example_verbose_custom_params.py
```
This example show the optional parameters for ping and icmp packet.
```

### example.py
```
This is more complex example. It show how to run netsweeper with no interaction and how to interact with 
scan results stored in the property 'results'.
```
