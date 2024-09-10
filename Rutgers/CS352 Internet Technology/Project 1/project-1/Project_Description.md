This is a simple project intended to get you used to Python, sockets, and the formalities of projects like readme and groups. This will be worth 3 points on your final grade. This exercise will serve as the foundation for the next project. A sample working client code is given to you in Client.py. Your job is to write the corresponding server code. The goal of the server is to get any string sent to it, and switch any letters from lower case to capital. Lastly it should then close gracefully when the client is done sending strings. A sample output and input file has also been provided. As with all projects you may work in groups of up to two, if you would like to be randomly assigned a partner, please fill out the partner link either in class or afterwards.
### How we will test your programs?
As part of your submission, you will turn in one program: Server.py and one ReadMe file (more on this below).

We will be running the two programs on the iLab machines with Python 3 (ideally 3.8). Information about how to use and access the machines will be provided in lecture.

Please do not assume that all programs will run on the same machine or that all connections are made to the local host. We reserve the right to test your programs with local and remote socket connections, for example with Client.py and Server.py each running on a different machine. You are welcome to simplify the initial development and debugging of your project, and get off the ground by running all programs on one machine first. However, you must ensure that the programs can work across multiple machines. Please note that the iLab machines are no longer addressable from the outside, so you must use two different iLab machines for testing.
### Running programs
The programs must work with the following command lines:
    python3 Server.py PORT
    python3 Client.py SERVERADDRESS PORT

An example of this would be:
    python3 Server.py 5444
    python3 Client.py vi.cs.rutgers.edu 5444

By default the client reads from a file called source_strings.txt and writes to a file called results.txt.