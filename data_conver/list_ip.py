     # -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 20:27:47 2018

@author: Administrator
"""
from data_conver.test_IPy import func_bin
class ip_list():
    def iplist(string_startip,string_endip):

    #分割IP，然后将其转化为8位的二进制代码
        start = string_startip.split('.')
        start_a = func_bin.dec2bin80(start[0])
        start_b = func_bin.dec2bin80(start[1])
        start_c = func_bin.dec2bin80(start[2])
        start_d = func_bin.dec2bin80(start[3])
        start_bin = start_a + start_b + start_c + start_d
    #将二进制代码转化为十进制
        start_dec = func_bin.bin2dec(start_bin)

        end = string_endip.split('.')
        end_a = func_bin.dec2bin80(end[0])
        end_b = func_bin.dec2bin80(end[1])
        end_c = func_bin.dec2bin80(end[2])
        end_d = func_bin.dec2bin80(end[3])
        end_bin = end_a + end_b + end_c + end_d
    #将二进制代码转化为十进制
        end_dec = func_bin.bin2dec(end_bin)

    #十进制相减，获取两个IP之间有多少个IP
        count = int(end_dec) - int(start_dec)
        address_list=[]
    #生成IP列表
        for i in range(0,count + 1):
        #将十进制IP加一，再转化为二进制（32位补齐）
            plusone_dec = int(start_dec) + i
            plusone_dec = str(plusone_dec)
            address_bin = func_bin.dec2bin320(plusone_dec)
        #分割IP，转化为十进制
            address_a = func_bin.bin2dec(address_bin[0:8])
            address_b = func_bin.bin2dec(address_bin[8:16])
            address_c = func_bin.bin2dec(address_bin[16:24])
            address_d = func_bin.bin2dec(address_bin[24:32])
            address = address_a + '.'+ address_b +'.'+ address_c +'.'+ address_d
            #print("address:",address)
            address_list.append(address)
        #print("address_list",address_list)
        return address_list