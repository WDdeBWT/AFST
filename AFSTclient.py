# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2018/03/06"

from TCP_connecter import *

import os
import sys
import csv
import time
import socket
from multiprocessing import Queue

class AFSTclient:
    def __init__(self):
        self.cache_path = 'AFST_cache/imf.csv'
        if not os.path.exists('AFST_cache'):
            os.mkdir('AFST_cache')
        if not os.path.exists('AFST_cache/imf.csv'):
            write_list = [['Name', 'Type', 'Time']]
            with open('AFST_cache/imf.csv', 'w', newline="") as w:
                writer = csv.writer(w)
                for line in write_list:
                    writer.writerow(line)
        else:
            pass

    def get_connection(self, server_ip = '119.23.239.27', server_port = 9999):
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
    
    def get_file_list(self):
        crt_path = os.getcwd()
        with open('AFST_cache/imf.csv', 'a', newline="") as a:
            writer = csv.writer(a)
            for root, dirs, files in os.walk(os.getcwd()):
                root = root.replace(crt_path, '')
                if root == 'AFST_cache':
                    continue
                if not root == '':
                    writer.writerow([root, 'folder', int(time.time())])
                for one_file in files:
                    writer.writerow([root + '\\' + one_file, 'file', int(time.time())])
                # print(root) # 当前目录路径
                # print(dirs) # 当前路径下的所有子目录
                # print(files) # 当前目录下的所有非目录子文件
    
    def commit_all_file(self):
        pass
    
    def commit_one_file(self):
        pass
    
    def get_history_edition(self):
        pass

afst = AFSTclient()
afst.get_file_list()