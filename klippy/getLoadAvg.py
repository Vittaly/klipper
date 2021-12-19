import os
def get_avg():
    s= None
    with open('/proc/loadavg', 'r') as f:
        s = f.read()
    retrun [float(x) for x in s.split()[0:3]]

if not hasattr(os, "getloadavg"):
    os.getloadavg = get_avg