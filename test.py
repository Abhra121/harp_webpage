
#!/usr/bin/env python3


import os
#import sys

#p = (sys.argv[1])
#print(p)

#string=""
#s=""

#for word in sys.argv[1:]:
#    string += word + ' '

#print(string)
#s=sys.argv[1]

#import sys

#who = sys.argv[1]

#print ("Hello %s" % who)


#f = open('/home/pi/serialid.txt', 'w')
#ser1 = f.read()
#f.write(who)
#f.close

#f.close()
#print(ser1)
   # ser1=int(ser1)
#os.makedirs("folder")
#print("Hello World");



# Python program to demonstrate
# command line arguments
 
 
import sys
 
# total arguments
n = len(sys.argv)
#print("Total arguments passed:", n)
 
# Arguments passed
#print("\nName of Python script:", sys.argv[0])
 
print("\nAPN Passed:", end = " ")
#print("APN is:\n")

#for i in range(1, n):
#    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
#for i in range(1, n):
#    Sum += int(sys.argv[i])
     
#print("\n\nResult:", Sum)
#print(sys.argv[1])
s=""
s=(sys.argv[1])
s=s+'"'
#print(s)

#f = open('/var/www/html/serialid.txt', 'w')
#f = open('/home/pi/apn.txt', 'w')
#ser1 = f.read()
#f.write(s)
#f.close

with open("/home/pi/apn.txt") as f:
    lines = f.readlines() #read.
#modify.
    lines[1] = 'connect "/usr/sbin/chat -v -f /etc/chatscripts/gprs -T ' +s+  '\n' #you can repla>

with open("/home/pi/apn.txt", "w") as f:
    f.writelines(lines) #write back.


os.popen('sudo cp /home/pi/apn.txt /etc/ppp/peers/rnet')


#print(s)
#print(sys.argv[1])
#print(sys.argv[1])

