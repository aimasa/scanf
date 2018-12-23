import pymongo
import socket
def info():
    return None


def poc(ip, port):
	try:
		conn = pymongo.MongoClient(ip, port)
		dbname = conn.list_database_names()
		print(ip, "存在MongoDB未授权")
		myCol = conn["site"]
	# conn.close()
		return {
			"info": "存在MongoDB未授权",
			"result": True
		}
	except Exception as e:
		print(e)
	finally:
		conn.close()
	return {
			"info": "不存在MongoDB未授权",
			"result": False
		}