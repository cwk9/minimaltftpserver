# minimaltftpserver
A minimal TFTP server in Python 3.

Created to help upgrade firmware on network and embedded systems. 

The script will accept a directory as a commandline parameter. If none is provided it will use the current working directory.
eg. sudo python3 minimaltftpserver.py /home/username/Downloads

You will need the tftpy library as its not included in python by default. It can be installed with the command "python3 -m pip install tftpy" on Linux. Your OS may not allow you to listen on the standard TFTP port of 69 as an unprivileged user. You can use the sudo command or change the port in the scrip itself by modifing the serverport variable to work around this. By default the script will listen on all ip addresses but you can also change that with serverip variable. To exit the program use CTRL+C
