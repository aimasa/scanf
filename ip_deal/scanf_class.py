# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:13:45 2018

@author: Administrator
"""
from data_conver.list_ip import ip_list as IPLIST


def getIPsFromRange(iprange):
    args_ip = iprange
    march_str = '-'
    if (args_ip.find(march_str) > 0):
        ip_list = args_ip.split('-')
        ip_list_range = []
        ip_list_range.append(ip_list[0])
        ip_list_range.append(ip_list[(len(ip_list)) - 1])
        ip_list_range = IPLIST.iplist(ip_list_range[0], ip_list_range[1])
        return ip_list_range
    else:
        ip_list = []
        ip_list.append(args_ip)
        return ip_list


# class scanf_ping(object):
#     def __init__(self, ip_address):
#         self.ip_address = ip_address
# #        self.port_address=port_address
#
# #    def get_system():
# #       getsystem=platform.system()
# #       if(getsystem=="Windows"):
# #           return 'n'
# #       else:
# #           return 'c'
#
# #    def commend_str():
# #        commendargs=sys.argv[1:]
# #        args="".join(commendargs)
# #        return args
#
#     def get_ip(self):
#         """
#         对输入的ip范围值进行处理
#         :return: 需要扫描的ip
#         """
#         args_ip = self.ip_address
#         march_str = '-'
#         if(len(args_ip) == 0):
#             ip_list = ['10.10.9.1']
#             #print(len(ip_list))
#             return ip_list
#         if(args_ip.find(march_str)>0):
#             ip_list = args_ip.split('-')
#             ip_list_range = []
#             ip_list_range.append(ip_list[0])
#             ip_list_range.append(ip_list[(len(ip_list))-1])
#             print(ip_list_range)
#             return ip_list_range
#         else:
#             ip_list = []
#             ip_list.append(args_ip)
#             return ip_list
#
# #    def ping_ip(ip):
# ##        ips=[]
# #        cmd=["ping", "-{op}".format(op=scanf_ping.get_system()),
# #           "1", ip]
# #        output=os.popen(" ".join(cmd)).readlines()
# #        flag=False
# #        for line in list(output):
# #            #print(str(line).upper().find("TTL"))
# #            #print(line)
# #            if not line:
# #                continue
# #            if str(line).upper().find("TTL") >=0:
# #                flag=True
# #                break
# #        if(flag):
# #            print(ip," is live")
# ##            port.get_ip()
# #            port.run_port_status(ip)
# #        else:
# #            print(ip," is dead")
#
# #        return ips
#