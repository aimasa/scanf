# from ip_deal.task_thread import task_create
# from port_deal.run_port import port_live
# from port_deal.port_detail import port_scanf
# class scanf_ip_port():
#     def __init__(self, ips_all, start_port, end_port):
#         self.ips_all = ips_all
#         self.start_port = start_port
#         self.end_port = end_port
#         self.progress = 0
#
#     def ports_live(self):
#         """
#         扫描ip得出的结果去扫描port得出的结果去扫描脆弱性
#         :return:
#         {
#             "numberofHosts": 1,
#             "numberofPorts": 1,
#             "hosts": [
#                 {
#                     "host": ?,
#                     "numberofPort": ?,
#                     "ports": [
#                         {
#                             "port": ?,
#                             "numberofWarning": ?,
#                             "warning": ?
#                         }
#                     ]
#                 }
#             ]
#         }
#         """
#         ips_live = []
#         progress = 0
#         host_live = {}
#         # ports_live = []
#         task = task_create(self.ips_all)
#         """
#         扫描ip得到存活的ip
#         """
#         ips_live = task.ip_result()
#         # dict_host = {}
#         list_hosts = []
#         numberofPorts = 0
#         numberofHosts = len(ips_live)
#         # print(ips_live)
#         numberofWarnings = 0
#         for i in ips_live:
#             numberofWarning_ip = 0
#             # print(i)
#             dict_host = {}
#             has_port_live = []
#             ports_scanf = port_live(i, self.start_port, self.end_port)
#             has_port_live = ports_scanf.run_port_status()
#             """
#             对存活的ip扫描想要扫描的端口得到存活的端口
#             """
#             # print("活的端口", has_port_live)
#             dict_host["host"] = i
#             dict_host["numberofPort"] = len(has_port_live)
#             numberofPorts = numberofPorts + len(has_port_live)
#             list_infor = []
#             # dict_host["ports"]=has_port_live
#             # host_live.append(dict_host)
#             for port in has_port_live:
#                 print(port)
#                 """
#                 看存活的端口对应的应用有没有安全隐患
#                 """
#                 scanf_tmp = port_scanf(i, port)
#                 infor_tmp=scanf_tmp.port_scanf_detail()
#                 numberofWarning_ip=numberofWarning_ip + infor_tmp["numberofWarning"]
#                 list_infor.append(infor_tmp)
#             dict_host["numberofWarnings"] = numberofWarning_ip
#             dict_host["ports"] = list_infor
#
#             list_hosts.append(dict_host)
#             numberofWarnings = numberofWarnings + numberofWarning_ip
#
#             # print(list_hosts)
#         host_live["numberofHosts"] = numberofHosts
#         host_live["numberofPorts"] = numberofPorts
#         host_live["numberofWarninga"] = numberofWarnings
#         host_live["hosts"] = list_hosts
#         return host_live


