#input: hostname port1,port2,...,portn 
#translate hostname to ipv4 addr
#socket connection to (ipv4,port)
#send garbage, read banner results

import optparse
from socket import *
parser = optparse.OptionParser('usage %prog -H'+\
                               '<target hostname> -p <target port>')
parser.add_option('-H',dest='tgtHost',type='string',help='specify the target hostname eg: example.com')
parser.add_option('-p',dest='tgtPort',type='int',help='specify the target ports to be scanned')

(options,args) = parser.parse_args()# making a touple that holds the values of the options defined and CLI args
tgtHost = options.tgtHost
tgtPort = options.tgtPort

if (tgtHost == None or tgtPort == None):
        print(parser.usage)
        exit(0)

#checking for multiple port input

#resolve the hostname to ip addr
try:
        connskt= socket(AF_INET, SOCK_STREAM)
except:
        print("AHHHHHHHH what are you doing you twat")