# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:42:14 2018

@author: Administrator
"""

import json


def store_ip_port(dict_infor):
    with open("test.json", "w", encoding='utf-8') as f:
        # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
        f.write(json.dumps(dict_infor, indent=4,ensure_ascii=False))
class store_infor():
    def __init__(self, dict_infor):
        self.dict_infor = dict_infor

#    def sort_ip(self):
        
    
    def store_ip_port(self):
        with open("test.json", "w", encoding='utf-8') as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
            f.write(json.dumps(self.dict_infor, indent=4))