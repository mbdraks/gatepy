gatepy - FortiGate Automation using REST API
=====

gatepy is a python script designed to easier the FortiGate administration using his REST API, some use cases would include mass object creation, processing CSV files to quickly create URL lists and more. Feel free to suggest new use cases at the Issues section.


Usage
----- 
```sh
./gatepy.py <FortiGate IP Address> <Optional VDOM, defaults to root if not specified>
```

Prerequisites
----

* Change credentials on login section
* Install python dependencies (requests)
* Configure FGT accordingly (this version is unable to issue https requests)

```sh
config system interface
    edit <port>
        append allowaccess http
    
config system global
    set admin-https-redirect disable
```

Environment
-----

Tested on:
* Mac OS X
* python 2.7.6
* requests 2.5.3
* FortiOS 5.2.3
