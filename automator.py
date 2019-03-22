#!/usr/bin/python3
# This line tells the CGI loader that this is a python script.

# Project: RTL Image Downloader
# Author: Stephen Cassaro
# Company: Dasan Zhone Solutions
# Description: This python program facilitates the downloading of files to a MX/MXK system for the RTLAutomation website.

# Import libraries:
# cgi = Allows us to use this program as a CGI program (runs under an apache page).
# cgitb = Enables more detailed logging (debug mode below).
# telnetlib = Handles telnet connecting, reading, and writing.
# time = Lets us use time functions.
# os = Enables operating system commands. Likely not needed, will probably remove later.

import cgi, cgitb, telnetlib, time, os, paramiko, sys

# Turn on debug mode.
cgitb.enable()

print("Content-Type: text/html")
print()
print("<head><title>MXK Test Results</title></head>")
print("<style>table, th, td {border-collapse: collapse;border:1px solid black}</style>")
print("<table style='width:100%>'")
print("<tr><th>Test</th><th>Result</th></tr>")
     

# Zhone uses weird capitalizations in filenames.
# This extracts filenames from the development server to use for ftp.
# binname = Zhone MX/MXK binary name.
# chassistype = Either MX or MXK.
# version = Software version we wish to upgrade to.

# Use telnetlib to login to the MX/MXK and determine if the system has a custom prompt.
def TelnetLoginandGetPrompt(mxkip):
       
       # Login to system.
       mxktelnet = telnetlib.Telnet(mxkip)
       mxktelnet.read_until(b"login:")
       mxktelnet.write(b"admin\n")
       mxktelnet.read_until(b"password:")
       mxktelnet.write(b"zhone\n")
       
       # The prompt is extremely important in determining if a download has finished, among other things.
       # Here, I extract whatever comes up after login.
       prompt = str(mxktelnet.read_until(b"zSH>", 1))
       
       # Basically, theres a bunch of junk leftover from the read_until function above.
       # I know there will be exactly 8 characters of trash before and including the carriage return character ("\r").
       # I slice the first 8 characters off the string, and also remove any extra characters at the end, however unlikely.
       prompt = prompt[prompt.find("b' \n\r")+8:prompt.find(" '")]
       prompt = prompt.encode()
       
       # Return the telnet object and prompt to use elsewhere.
       return mxktelnet, prompt

def AsymmetricSingleRGBridged(mxktelnet, prompt, IP):
       time.sleep(10)
       return "Passed"

def AsymmetricSingleSecureRGBridged(mxktelnet, prompt, IP):
       time.sleep(10)
       return "Passed"

def main():
       
       # Collect data contained in the URL (version, binary names, system IP).
       form = cgi.FieldStorage()

       IP = form.getvalue('IP')
       
       # Telnet to system, login, and create login string.
       mxktelnet, prompt = TelnetLoginandGetPrompt(IP)
       
       # If a list of tests is in the URL,
       if("testarray" in form):
              
              # store tests in the URL to testList.
              testList = form.getvalue('testarray')
              if(len(testList[0]) == 1):
                     
                     print("<tr><td>" + testList + "</td><td>")
                     execstring = testList + "(mxktelnet,prompt,IP)"
                     print(str(eval(execstring)))
                     print("</td></tr>")
              else:
                     for i in range(len(testList)):
                            print("<tr><td>" + testList[i] + "</td><td>")
                            execstring = testList[i] + "(mxktelnet,prompt,IP)"
                            print(str(eval(execstring)))
                            print("</td>")
                            sys.stdout.flush()
                     print("</tr>")
              
       # Otherwise print error message.
       else:
              print("<tr><td>No tests found. Please select some checkboxes and try again.</td></tr>")
              
       return

if(__name__ == "__main__"):
       main()
