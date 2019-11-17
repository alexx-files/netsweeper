### netsweeper
Python class to allow programmers to create easily your own net sweeper scripts. The examples added to the package already are net sweepers that can be used and improved

> Requires Ping3 https://github.com/kyan001/ping3 (Downloaded automaticaly)
> Tested under Linux and Windows

## Installation

```shell
pip install netsweeper  # install nesweeper
```
## Usage
```
# Verbose Mode
from netsweeper import NetSweeper
scan = NetSweeper('192.168.0.0/24', 100, 1)
scan.verbose_run()
```

```
# No Interaction Mode
    from netsweeper import NetSweeper
scan = NetSweeper('192.168.0.0/24', 100, 1)
scan.run()
```
