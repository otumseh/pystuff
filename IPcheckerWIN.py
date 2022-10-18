"""
This program checks external and internal IPs and other info for Windows
"""

# import requests
# import dfwinreg
# import sys
# import os
# import socket
import subprocess
import socket
import platform
import cpuinfo
import psutil
import netifaces
from requests import get

# info using cpuinfo
# cputype = cpuinfo.get_cpu_info()
cputype = cpuinfo.get_cpu_info()['brand_raw']

# use subprocess with grep (linux)
# cpu_sockets = int(subprocess.check_output('cat /proc/cpuinfo | grep "physical id" | '
#                                           'sort -u | wc -l', shell=True))

# use subprocess with wmic Win32_VideoController (Windows)
GPUgetname = subprocess.check_output("wmic path Win32_VideoController get name", shell=True, text=True)
result = " ".join(line.strip() for line in GPUgetname.splitlines())
StripRes = result.replace("Name", "")
MoreStripRes = StripRes.strip()
MoreStripRes1 = MoreStripRes.replace("'", '')

GPUgetDriver = subprocess.check_output("wmic path Win32_VideoController get DriverVersion", shell=True, text=True)
resultDriver = " ".join(line.strip() for line in GPUgetDriver.splitlines())
StripDriver = resultDriver.replace("DriverVersion", "")
MoreStripDriver = StripDriver.strip()
MoreStripDriver1 = MoreStripDriver.replace("'", '')

GPUgetDriverDate = subprocess.check_output("wmic path Win32_VideoController get DriverDate", shell=True, text=True)
resultDriverDate = " ".join(line.strip() for line in GPUgetDriverDate.splitlines())
StripDriverDate = resultDriverDate.replace("DriverDate", "")
MoreStripDriverDate = StripDriverDate.strip()
MoreStripDriverDate1 = MoreStripDriverDate.replace("'", '')
FormatDate = MoreStripDriverDate1[0:8]

GPUgetRes = subprocess.check_output("wmic path Win32_VideoController get VideoModeDescription", shell=True, text=True)
resultRes = " ".join(line.strip() for line in GPUgetRes.splitlines())
StripResRes = resultRes.replace("VideoModeDescription", "")
MoreStripResRes = StripResRes.strip()
MoreStripRes1Res = MoreStripResRes.replace("'", '')

GPUgetMaxRefr = subprocess.check_output("wmic path Win32_VideoController get MaxRefreshRate", shell=True, text=True)
resultRefr = " ".join(line.strip() for line in GPUgetMaxRefr.splitlines())
StripRefr = resultRefr.replace("MaxRefreshRate", "")
MoreStripRefr = StripRefr.strip()
MoreStripRefr1 = MoreStripRefr.replace("'", '')

GPUgetMinRefr = subprocess.check_output("wmic path Win32_VideoController get MinRefreshRate", shell=True, text=True)
resultMin = " ".join(line.strip() for line in GPUgetMinRefr.splitlines())
StripMinRefr = resultMin.replace("MinRefreshRate", "")
MoreStripMinRefr = StripMinRefr.strip()
MoreStripMinRefr1 = MoreStripMinRefr.replace("'", '')

GPUgetCurRefr = subprocess.check_output("wmic path Win32_VideoController get CurrentRefreshRate", shell=True, text=True)
resultCur = " ".join(line.strip() for line in GPUgetCurRefr.splitlines())
StripCur = resultCur.replace("CurrentRefreshRate", "")
MoreStripCur = StripCur.strip()
MoreStripCur1 = MoreStripCur.replace("'", '')

# info using os
# cpudie = os.cpu_count()
# DeskTop = os.environ.get('DESKTOP_SESSION')

# info using sys
cpu1 = platform.processor()
# winver = sys.getwindowsversion()

# info using psutil
cpucount = psutil.cpu_count()
cpucountphys = int(cpucount / 2)
cpu2 = psutil.cpu_freq()
cpu2max = psutil.cpu_freq().max
cpu2min = psutil.cpu_freq().min
cpu2current = psutil.cpu_freq().current
format_cpu2current = "{:.2f}".format(cpu2current)
cpu3 = psutil.cpu_stats()
cpu3ctx_sw = psutil.cpu_stats().ctx_switches
cpu3interrupts = psutil.cpu_stats().interrupts
cpu3sft_intpts = psutil.cpu_stats().soft_interrupts
cpu3syscalls = psutil.cpu_stats().syscalls
# boot1 = psutil.boot_time()
user = psutil.users()
# net1 = psutil.net_if_addrs()
mem = psutil.virtual_memory()
memTotal = psutil.virtual_memory().total / (1024 ** 3)
format_memtotal = "{:.2f}".format(memTotal)
memAvail = psutil.virtual_memory().available / (1024 ** 3)
format_memAvail = "{:.2f}".format(memAvail)
memUsed = psutil.virtual_memory().used / (1024 ** 3)
format_memUsed = "{:.2f}".format(memUsed)
memPerc = psutil.virtual_memory().percent

# info using platform
nameCPU = platform.processor()
name = platform.uname()
nameOSbase = platform.uname().system
nameNode = platform.uname().node
nameOSrelease = platform.uname().release
nameOS = platform.uname().version

# Gets external IP with get
ip = get('https://api.ipify.org', timeout=5).text

# Gets internal IP with socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

# Gets gateway with netifaces
gws = netifaces.gateways()
# print(gws)
DomName = socket.gethostbyaddr(s.getsockname()[0])


# print POB
print("")
print("CPU:", cputype)
print("CPU architecture:", cpu1)
# print("CPU count:", cpu_sockets)
print("Logical cores:", cpucount)
print("Physical cores:", cpucountphys)
# print(cpu2)
print("CPU Max Frequency:", cpu2max, "MHz")
print("CPU Min Frequency:", cpu2min, "MHz")
print("CPU Current Frequency:", format_cpu2current, "MHz")
# print(cpu3)
# print("ctx_switches:", cpu3ctx_sw)
# print("interrupts:", cpu3interrupts)
# print("soft_interrupts:", cpu3sft_intpts)
# print("sys_calls:", cpu3syscalls)
print("")
# print(mem)
print("Total System Memory:", format_memtotal, "GB")
print("Total Available Memory:", format_memAvail, "GB")
print("Total Used Memory:", format_memUsed, "GB")
print("Percentage Used:", memPerc, "%")
print("")
# print(subprocess.check_output("wmic path Win32_VideoController", shell=True, text=True))
print("Graphics Card:", MoreStripRes1)
print("Driver Version:", MoreStripDriver1)
print("Driver Date:", FormatDate)
print("Resolution and Color:", MoreStripRes1Res)
print("Maximum Refresh Rate:", MoreStripRefr1, "Hz")
print("Minimum Refresh Rate:", MoreStripMinRefr1, "Hz")
print("Current Refresh Rate:", MoreStripCur1, "Hz")
print("")
# print(boot1)
# print(user[0])
print("Username:", user[0].name)
# print("Terminal:", user[0].terminal)
# print("Host:", user[0].host)
# print("PID:", user[0].pid)
print("")
# print(name)
print("Base OS:", nameOSbase)
print("Desktop Name:", nameNode)
print("Win Ver:", nameOSrelease)
print("Version and Build:", nameOS)
# print("DE:", DeskTop)
# print(winver)
print("")

# print(net1)
print("External IP: ", ip)
print("Internal IP: ", s.getsockname()[0])
print("Gateway IP:  ", gws['default'][netifaces.AF_INET][0])
# print(DomName[0])
print("The domain name for " + s.getsockname()[0] + " is", DomName[0])
s.close()
