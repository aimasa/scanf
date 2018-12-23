import socket
def info():
    return None

def poc(ip, port):
    #    url = host2IP(url)  # 自动判断输入格式,并将URL转为IP
    url=ip
    #    port = int(url.split(':')[-1]) if ':' in url else 6379  # 不指定端口则为默认端口
    payload = '\x2a\x31\x0d\x0a\x24\x34\x0d\x0a\x69\x6e\x66\x6f\x0d\x0a'
    s = socket.socket()
    socket.setdefaulttimeout(10)
    try:
        host = url.split(':')[0]
        s.connect((host, port))
        s.send(payload.encode())
        recvdata = s.recv(1024).decode()
        s.close()
        if recvdata and 'redis_version' in recvdata:
            return {
                "info": "存在redis未授权",
                "result": True
            }
    except Exception as e:
        print("出错了", e);
        pass
    return {
        "info": "安全",
        "result": False
    }