import os
import time
import subprocess
import platform



# Muto Framework laptop
hostnameLT = 'LT-MUTO-STAN'
responseLT = subprocess.run('ping -4 -a -n 1 ' + str(hostnameLT), stdout=subprocess.PIPE, shell=True)
outputLT = responseLT.stdout.decode('utf8')
time.sleep(3)
# print(responseLT)
responseLT.returncode 
if "Destination host unreachable." not in outputLT and responseLT.returncode == 0:
    print(hostnameLT, '\033[96m Muto Laptop \033[96m', '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameLT, '\033[96m Muto Laptop \033[96m', '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(responseLT.returncode)

time.sleep(1)

# Used to be Dom Castillo PC
hostnameDCAST = 'DT-dcastillo-std'
responseDCAST = subprocess.run("ping -4 -a -n 1 " + hostnameDCAST, stdout=subprocess.PIPE, shell=True)
output = responseDCAST.stdout.decode('utf8')
time.sleep(3)
# print(responseDCAST)
responseDCAST.returncode 
if "Destination host unreachable." not in output and responseDCAST.returncode == 0:
    print(hostnameDCAST, '\033[96m Doms Old PC \033[96m', '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameDCAST, '\033[96m Doms Old PC \033[96m', '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(responseDCAST.returncode)

time.sleep(1)

# Ed's PC
hostnameES = 'DT-ES-Extract'
responseES = subprocess.run("ping -4 -a -n 1 " + hostnameES, stdout=subprocess.PIPE, shell=True)
outputES = responseES.stdout.decode('utf8')
time.sleep(3)
# print(responseES)
responseES.returncode 
if "Destination host unreachable." not in outputES and responseES.returncode == 0:
    print(hostnameES, '\033[96m EDs PC \033[96m', '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameES, '\033[96m EDs PC \033[96m', '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(responseES.returncode)

time.sleep(1)

# Netappa Home, ITSup, Fieldword,HRdata,Sanstor Drives
hostname0 = 'netappa'
response0 = subprocess.run("ping -4 -a -n 1 " + hostname0, stdout=subprocess.PIPE, shell=True)
outputa = response0.stdout.decode('utf8')
time.sleep(3)
response0.returncode 
if "Destination host unreachable." not in outputa and response0.returncode == 0:
    print(hostname0, '\033[96m Sanstor \033[96m', '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostname0, '\033[96m Sanstor \033[96m', '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(response0.returncode)

time.sleep(1)

# G: working drive & Library Drives
hostname1 = 'netappb'
response1 = subprocess.run("ping -4 -a -n 1 " + hostname1, stdout=subprocess.PIPE, shell=True)
outputb = response1.stdout.decode('utf8')
time.sleep(3)
response1.returncode 
if "Destination host unreachable." not in outputb and response1.returncode == 0:
    print(hostname1, '\033[96m G: and L: \033[96m', '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostname1, '\033[96m G: and L: \033[96m', '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(response1.returncode)

time.sleep(1)

# DNS failover
hostnameDNSb = '66.188.38.58'
response2 = subprocess.run("ping -4 -a -n 1 " + hostnameDNSb, stdout=subprocess.PIPE, shell=True)
outputDNSb = response2.stdout.decode('utf8')
time.sleep(3)
response2.returncode 
if "Destination host unreachable." not in outputDNSb and response2.returncode == 0:
    print(hostnameDNSb, '\033[96m Backup VPN host \033[96m', '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameDNSb, '\033[96m Backup VPN host \033[96m','\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(response2.returncode)

time.sleep(1)

# DC1
hostnameDC1 = 'ssi-dc1'
responseDC1 = subprocess.run("ping -4 -a -n 1 " + hostnameDC1, stdout=subprocess.PIPE, shell=True)
outputDC1 = responseDC1.stdout.decode('utf8')
time.sleep(3)
responseDC1.returncode 
if "Destination host unreachable." not in outputDC1 and responseDC1.returncode == 0:
    print(hostnameDC1, '\033[96m Domain Controller 1 \033[96m', '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameDC1, '\033[96m Domain Controller 1 \033[96m', '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(responseDC1.returncode)

time.sleep(1)

# DC2
hostnameDC2 = 'ssi-dc2'
responseDC2 = subprocess.run("ping -4 -a -n 1 " + hostnameDC2, stdout=subprocess.PIPE, shell=True)
outputDC2 = responseDC2.stdout.decode('utf8')
time.sleep(3)
responseDC2.returncode 
if "Destination host unreachable." not in outputDC2 and responseDC2.returncode == 0:
    print(hostnameDC2, '\033[96m Domain Controller 2 \033[96m', '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameDC2, '\033[96m Domain Controller 2 \033[96m', '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(responseDC2.returncode)

time.sleep(1)