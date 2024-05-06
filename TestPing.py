import os
import time
import subprocess
import platform

# hostnameDCAST = 'DT-dcastillo-std'
# result = subprocess.run("ping -4 -a -n 1 " + hostnameDCAST, stdout=subprocess.PIPE)
# output = result.stdout.decode('utf8')
# print(output)
# if "Destination host unreachable." in output:
#     print("Unreachable")
# else:
#     print("nada")

# Muto Framework laptop
hostnameLT = 'LT-MUTO-STAN'
responseLT = subprocess.run('ping -4 -a -n 1 ' + str(hostnameLT), stdout=subprocess.PIPE, shell=True)
outputLT = responseLT.stdout.decode('utf8')
time.sleep(4)
print(responseLT)
responseLT.returncode 
if "Destination host unreachable." not in outputLT and responseLT.returncode == 0:
    print(hostnameLT, '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameLT, '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(responseLT.returncode)

time.sleep(2)

# Used to be Dom Castillo PC
hostnameDCAST = 'DT-dcastillo-std'
responseDCAST = subprocess.run("ping -4 -a -n 1 " + hostnameDCAST, stdout=subprocess.PIPE, shell=True)
output = responseDCAST.stdout.decode('utf8')
time.sleep(4)
print(responseDCAST)
responseDCAST.returncode 
if "Destination host unreachable." not in output and responseDCAST.returncode == 0:
    print(hostnameDCAST, '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameDCAST, '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(responseDCAST.returncode)

time.sleep(2)

# Netappa Home, ITSup, Fieldword,HRdata,Sanstor Drives
hostname0 = 'netappa'
response0 = subprocess.run("ping -a -n 1 " + hostname0)
time.sleep(4)
response0.returncode 
if response0.returncode == 0:
    print(hostname0, '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostname0, '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(response0.returncode)

time.sleep(2)

# G: working drive & Library Drives
hostname1 = 'netappb'
response1 = subprocess.run("ping -a -n 1 " + hostname1)
time.sleep(4)
response1.returncode 
if response1.returncode == 0:
    print(hostname1, '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostname1, '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(response1.returncode)

time.sleep(2)

# DNS failvoer
hostnameDNSb = '66.188.38.58'
response2 = subprocess.run("ping -a -n 1 " + hostnameDNSb)
time.sleep(4)
response2.returncode 
if response2.returncode == 0:
    print(hostnameDNSb, '\033[1;32m [ **SERVER UP** ] \033[1;m')
else:
    print(hostnameDNSb, '\033[93m [ **SERVER DOWN** ] \033[93m')
print("\033[0m")
print(response2.returncode)