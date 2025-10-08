"""
This class is going to encapsulate all the work necessary to make an ICMP request and get its reply.
(It may expand, that is why we are starting it as a class.)
"""
import socket 

class  Ping:
    
    def __init__(self,ip_address:str):
        #check the ipaddress format
        if (self.check_ip_address(ip_address)):
            self.ip_address=ip_address  
        
    def check_ip_address(self,address)->bool:
        #we are only checking for ipv4 for now so = 32B or 4 segments of 8B values 0-255 (2^8) serparated by .
        segments=address.split(".") #make an array with the numbers only

        for segment in segments:
                if int(segment) > 255 or int(segment)< 0:
                    print("invalid input, aborting")
                    return False
        return True
    
    def get_host_ip()-> str:
        host_ip = socket.gethostbyname(socket.gethostname) #get the hostname of the machine where the socket is running (local machine) then get the ip address
        return host_ip
    
        