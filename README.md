# ESM-Simulator
Ingest ESM logs into Panorama without having an ESM installed


This project consists of the following files:

* esm_background.py: Python script that builds and sends ESM logs to the specified Panorama
* hashes.txt: Contains hashes used to build ESM logs
* machines.txt: Contains hostnames used to build ESM logs
* mappings.xml: Contains a UserID payload which is used to build ESM logs



## How it works:
1. esm_background.py reads in the contents of the other three files and builds lists based on the contents. One list is build for users, one for hostnames, and one for hashes.
2. Every 30 minutes (1800 seconds) esm_background chooses a random entry from each of the lists and uses those to create a log file.
3. The log file is sent to Panorama on the configured port using TCP.


## Configuration:

1. Modify the sendLog function to reflect the correct IP address and port of your log collector:

`def sendLog(c_hash, c_user, machine):
        logstring = "<134> 1 {0} WIN-CAURRM4ONJ2 - - - {4},Traps Agent,3.4.1.15678,Threat,Prevention Event,{1},{2},New prevention event. Prevention Key: 1acabebe-833a-41e4-80a9-421923443eb9,6,Wildfire,myapp.exe,{3},[\"ContentVersion\"],,,".format(genTStamp(), machine, c_user, c_hash, genTime())
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('10.3.4.48', 23001))  <====== Modify these to match your environment.
        sock.send(logstring)
        print "Sent:\n\n" + logstring`
        
        
