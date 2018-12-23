# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:54:35 2018

@author: Administrator
"""

#!/usr/bin/env python
#import time
import socket

def checkPort(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = server.connect_ex((ip, port))
    if (res == 0):
        server.close()
        return True
    else:
        server.close()
        return False



# class socket_port():
#     list = []
#     def __init__(self , ip):
#         self.ip = ip
#     """
#     扫描指定端口状态
#     """
#     def get_ip_status(self, port):
#         # global str_port,infor_all,infor_live_ip
#         # # str_port = ""
#         # str_port = ""
#         # infor_all = ""
#         # infor_live_ip = ""
#         # print(12345)
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         res = server.connect_ex((self.ip, port))
#         if(res == 0):
#             print('{0} port {1} is open'.format(self.ip, port))
#             server.close()
#             # infor_all = str(self.ip) + "," + str(port) + "," + str_port
#             return port
#         else:
#             server.close()
#             return None
