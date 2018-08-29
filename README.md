gatepy - FortiGate Automation using REST API
=====

gatepy ultimate goal is to be a python script to facilitate the FortiGate administration using REST API, some use cases would include mass object creation, processing CSV files to quickly create URL lists and more. Feel free to suggest new use cases at the Issues section.

The first releases will be in various use cases of self-contained scripts, after we have enough maturity the idea is to pack it all in a single tool that will call whatever auxiliar script is needed, but also give the option to use the task script regardless of a master script to control it.

Usage
-----

Each case will have usage instructions in the same file


Prerequisites
----

* Change credentials on login section
* Install python dependencies

Environment
-----

Tested on:
* Mac OS X 10.10
* python 3.5.2
* FortiOS 6.0.0
* fortiosapi 0.9.91

It should work on different environments, just keep in mind the versions above.
