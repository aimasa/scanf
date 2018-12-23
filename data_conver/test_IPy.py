 # -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:35:50 2018

@author: Administrator
"""


class func_bin():
#十进制0~255转化为二进制,补0到8位
    def dec2bin80(string_num):
        num = int(string_num)
        mid = []
        while True:
            if num == 0: break
            num,rem = divmod(num, 2)
            mid.append(rem)

        result = ''.join([str(x) for x in mid[::-1]])
        length = len(result)
        if length < 8:
            result = '0' * (8 - length) + result
        return result


#十进制0~255转化为二进制,补0到32位
    def dec2bin320(string_num):
        num = int(string_num)
        mid = []
        while True:
            if num == 0: break
            num,rem = divmod(num, 2)
            mid.append(rem)

        result = ''.join([str(x) for x in mid[::-1]])
        length = len(result)
        if length < 32:
            result = '0' * (32 - length) + result
        return result

#二进制转换为十进制
    def bin2dec(string_num):
        return str(int(string_num, 2))

#ip列表生成



#iplist('2.168.255.254','2.169.1.10')

