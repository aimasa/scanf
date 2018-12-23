#coding:utf-8
#Author:se55i0n
import requests

import pymysql

import socket
import pymongo
import binascii
from plugins.config import *
def info():
    return None

def poc(ip, port):
	global dict_result
	for pwd in passwd:
		# print(pwd)
		try:
			dict_result = {
				"info": "不存在mysql弱口令",
				"result": False
			}
			pwd = pwd.replace('{user}', 'root')
			# mysql=pymysql.install_as_MySQLdb()
			conn = pymysql.connect(ip, 'root', pwd, 'mysql')
			# print u'{}[+] {}:3306  Mysql存在弱口令: root  {}{}'.format(G, ip, pwd, W)
			conn.close()
			return {
				"info": "存在mysql弱口令" + pwd,
				"result": True
			}
			# conn.close()

		except Exception as e:
			print(e)


	return dict_result