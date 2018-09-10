# gatepy - FortiGate Automation using REST API

gatepy ultimate goal is to be a python script to facilitate the FortiGate administration using REST API, some use cases would include mass object creation, processing CSV files to quickly create URL lists and more. Feel free to suggest new use cases at the Issues section.

The first releases will be in various use cases of self-contained scripts, after we have enough maturity the idea is to pack it all in a single tool that will call whatever auxiliar script is needed, but also give the option to use the task script regardless of a master script to control it.

## How To Use

To clone and run the examples you'll need:
* [Docker](https://www.docker.com/get-started)
* [Git](https://git-scm.com)
* [Python3](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)

From your command line:

```bash
# Pull and start docker image
$ docker pull ubuntu:18.04
$ docker run --name=gatepy_dev -it ubuntu:18.04

# Install packages
$ apt update
$ apt install git python3 python3-pip python-dev libssl-dev libffi-dev vim

# Clone this repository
$ git clone https://github.com/barbosm/gatepy

# Go into the repository
$ cd gatepy

# Install dependencies
$ pip3 install -r requirements.txt

# Edit _host to your FG details (IP and credentials)
$ vim examples/_host

# Load environment variables
$ source examples/_host

# Run the examples
$ python3 examples/monitor_system_status.py
```


## Prerequisites

* Change IP and credentials on _host file
* Install python dependencies


## Documentation
* [Module Reference](https://gatepy.readthedocs.io/en/latest/reference.html)


## Environment

Tested on:
* Mac OS X 10.10
* python 3.5.2
* FortiOS 6.0
* fortiosapi 0.9.91

It should work on different environments, just keep in mind the versions above.
