from script.redis_unauth import redis_unauth
from port_description.redis_detail import detail_description

def checkWarn(ip_num,port_num):
    list_Warn = []
    if(port_num==6379):
        redis = redis_unauth(ip_num, port_num)
        result = redis.poc()
        return {
            "plugin": "redis",
            "description": "redis未授权访问",
            "result": result
        }

# class  port_scanf():
#
#     def __init__(self, ip_number, port_number):
#         self.port_number = port_number
#         self.ip_number = ip_number
#
#     def port_scanf_detail(self):
#         """
#         对指定port端口进行相应的脆弱性扫描
#         :return: dict{
#                     "port": ?,
#                     "numberofWarning": ?,
#                     "warning": ?
#                 }
#         """
#         list_infor_port = []
#
#         if(self.port_number == 6379):
#             """
#             判断redis是否未授权访问
#             """
#             numberofwarning = 0
#             dict_port_detail = {}
#             dict_port_detail["port"] = self.port_number
#             redis = redis_unauth(self.ip_number, self.port_number)
#             result = redis.poc()
#             list_warning = []
#             if(result):
#                 numberofwarning = numberofwarning + 1
#                 description = detail_description()
#                 list_warning.append(description.redis_description())
#             dict_port_detail["numberofWarning"] = numberofwarning
#             dict_port_detail["warning"] = list_warning
#             # list_infor_port.append(dict_port_detail)
#             return dict_port_detail
#         dict_port_detail = {}
#         dict_port_detail["port"] = self.port_number
#         dict_port_detail["numberofWarning"] = 0
#         dict_port_detail["warning"] = []
#         # list_infor_port.append(dict_port_detail)
#         return  dict_port_detail