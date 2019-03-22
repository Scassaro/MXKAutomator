#!/usr/bin/env python3

import telnetlib, time, cgi, cgitb, re, sys, datetime, logging
from printlog import setuplog, printandlog
from bankdict import determineZPERF, determineSuper
cgitb.enable()

print("Content-Type: text/html", "|")
print()

def TelnettoMXKLoginandProvision(mxkip):
    mxktelnet = telnetlib.Telnet(mxkip)
    mxktelnet.read_until(b"login:")
    mxktelnet.write(b"admin\n")
    mxktelnet.read_until(b"password:")
    mxktelnet.write(b"zhone\n")
    mxktelnet.read_until(b">")
    mxktelnet.write(b"setline 0 \n")
    mxktelnet.read_until(b">")
    mxktelnet.write(b"bridge add 1-5-[1-20]-0/eth downlink-data vlan 3604 tagged eth 1 rg-bridged \r")
    mxktelnet.read_until(b">")
    return mxktelnet

def TelnettoZPERF(zperfip):
    zperftelnet = telnetlib.Telnet(zperfip)
    zperftelnet.read_until(b"login: ")
    zperftelnet.write(b"tpelham\r")
    zperftelnet.read_until(b"Password: ")
    zperftelnet.write(b"zhone\r")
    zperftelnet.read_until(b":~$ ")
    return zperftelnet

def main():
    logfile = 'asymsingrgbridged' + str(datetime.datetime.now().time()) + '.txt'
    print(logfile + " ")
    setuplog(logfile)
    printandlog("Test in progress...")
    
    form = cgi.FieldStorage()
    mxktelnet = TelnettoMXKLoginandProvision(form.getvalue('MXKIP'))
    
    # CPE Status
    mxktelnet.write(b"cpe status 5 \n")
    mxktelnet.read_until(b"[no]")
    mxktelnet.write(b"yes \n")
    if(mxktelnet.read_until(b">").decode('ascii').count("Active") == 40):
        printandlog("PASSED - ONU/CPE status complete")
    else:
        printandlog("FAILED - ONU/CPE status incomplete")

    # Anazlyze bridge-add data
    mxktelnet.write(b"bridge show slot 5 vlan 3604 \n")
    if(mxktelnet.read_until(b">").decode('ascii').count(" 3604 ") == 21):
        printandlog("PASSED - All bridges created")
    else:
        printandlog("FAILED - Some bridges not created")
        
    # Telnet into ZPERF
    zperftelnet = TelnettoZPERF(determineZPERF(form.getvalue('BankNum')))

    # Verify bank traffic lane    
    zperftelnet.write(b"fping -i 10 < /home/tpelham/bank104 \r")
    
    if(zperftelnet.read_until(b":~$ ").decode('ascii').count("alive") == 20):
        printandlog("PASSED - ZNID bank is alive")
    else:
        printandlog("FAILED - All ZNIDs do not ping")
        
    # Start ZPERF traffic
    zperftelnet.write(b"./devbank104 & \r")
    zperftelnet.read_until(b":~$ ")
    
    # Buffer - Give traffic time to run up
    time.sleep(8)

    # Start, stop, and store data traffic
    zperftelnet.write(b"ifstat -i eth5 -b -q 1 1 \r")
    trafficdata = zperftelnet.read_until(b":~$ ").decode('ascii').split()
    trafficspeed = float(trafficdata[trafficdata.index("out")+1])
    if(trafficspeed > 800000):
        printandlog("PASSED - Traffic speed is " + str(trafficspeed) + " Kbps")
    else:
        printandlog("FAILED - Traffic speed is not 1GB")
    
    # Kill ZPERF traffic
    zperftelnet.write(b"killbank 104 \r")
    
    # Verify MAC/IP addresses exist on MXK
    mxktelnet.write(b"bridge show slot 5 vlan 3604 \n")    
    bridgeshowdata = mxktelnet.read_until(b">").decode('ascii')
    if(len(re.findall("((\d|([a-f]|[A-F])){2}:){5}(\d|([a-f]|[A-F])){2}", bridgeshowdata)) == 20):
        printandlog("PASSED - MAC addresses present")
    else:
        printandlog("FAILED - Not all MAC addresses present")

    if(len(re.findall("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", bridgeshowdata)) == 20):
        printandlog("PASSED - IP addresses present")
    else:
        printandlog("FAILED - Not all IP addresses present")

    printandlog("Test completed. ")
    mxktelnet.close()
    zperftelnet.close()
    return
    
if(__name__ == "__main__"):
    main()
    
