# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:57:06 2018

@author: Administrator
"""
import os
import platform


def get_system():
    getsystem = platform.system()
    if (getsystem == "Windows"):
        return 'n'
    else:
        return 'c'

def ping_ip(ip):
    dict_infor_temp = {}
    list_all_infor = []

    cmd = ["ping", "-{op}".format(op=get_system()),
           "1", ip]
    output = os.popen(" ".join(cmd)).readlines()
    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >= 0:
            flag = True
            break

    return flag

# class command_ping():
#     def __init__(self):
#         pass
# #        pass
#
#     def get_system(self):
#         getsystem = platform.system()
#         if(getsystem == "Windows"):
#             return 'n'
#         else:
#             return 'c'
#
#     def ping_ip(self, ip):
#         # count = my_Enum()
#         # global count_hosts, dict_all_hosts_tmp
#         dict_infor_temp = {}
#         list_all_infor = []
#
#         cmd = ["ping", "-{op}".format(op=self.get_system()),
#            "1", ip]
#         output = os.popen(" ".join(cmd)).readlines()
#         flag = False
#         for line in list(output):
#             if not line:
#                 continue
#             if str(line).upper().find("TTL") >= 0:
#                 flag = True
#                 break
#
#         if(flag):
#             # count_hosts = count.addCount()
#             # print(count_hosts)
#             # print(ip, " is live")
#             # port_num = port_live(ip, self.start_port, self.end_port)
#             # dict_all_hosts_tmp = port_num.run_port_status()
#             return ip
#         # dict_infor_temp["numberOfHosts"] = str(count_hosts)
#         # dict_infor_temp.update(dict_all_hosts_tmp)
#         # return dict_infor_temp
