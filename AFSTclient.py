# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2018/03/06"

from TCP_connecter import *

import os
import sys
import time
import socket
from multiprocessing import Queue

class AFSTclient:
    def __init__(self, server_ip = '119.23.239.27', server_port = 9999):
        self.q_recv = Queue(maxsize = 10)
        self.tcp_conn = TcpConnecter(self.q_recv, server_ip, server_port)
        self.tcp_conn.start()
        try:
            recv = self.q_recv.get(block=True, timeout=1800)
            if recv[0] == 1:
                print(recv[1])
            else:
                print("error 1")
                os.system('pause')
                sys.exit(1)
        except Exception as e:
            print(e)
            print("----------ERROR1: 连接服务器失败，请关闭程序，稍后再试----------")
            self.tcp_conn.end_thread()
            os.system('pause')
            sys.exit(1)