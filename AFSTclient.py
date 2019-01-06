# _*_ coding:utf-8 _*_
__author__ = "WDdeBWT"
__date__ = "2018/03/06"

from TCP_connecter import *

import os
import sys
import csv
import time
import socket
import hashlib
from multiprocessing import Queue

class AFSTclient:
    def __init__(self):
        self.OF_list = []
        self.NF_list = []
        self.cache_path = 'AFST_cache/imf.csv'
        if not os.path.exists('AFST_cache'):
            os.mkdir('AFST_cache')
        if os.path.exists('AFST_cache/imf.csv'):
            with open('AFST_cache/imf.csv') as r:
                reader = csv.reader(r)
                for row in reader:
                    self.OF_list.append(row)
        write_list = [['Name', 'Type', 'Time', 'MD5']]
        with open('AFST_cache/imf.csv', 'w', newline="") as w:
            writer = csv.writer(w)
            for line in write_list:
                writer.writerow(line)

    # def get_connection(self, server_ip = '119.23.239.27', server_port = 9999):
    #     self.q_recv = Queue(maxsize = 10)
    #     self.tcp_conn = TcpConnecter(self.q_recv, server_ip, server_port)
    #     self.tcp_conn.start()
    #     try:
    #         recv = self.q_recv.get(block=True, timeout=1800)
    #         if recv[0] == 1:
    #             print(recv[1])
    #         else:
    #             print("error 1")
    #             os.system('pause')
    #             sys.exit(1)
    #     except Exception as e:
    #         print(e)
    #         print("----------ERROR1: 连接服务器失败，请关闭程序，稍后再试----------")
    #         self.tcp_conn.end_thread()
    #         os.system('pause')
    #         sys.exit(1)
    
    def get_new_file_list(self):
        crt_path = os.getcwd()
        with open('AFST_cache/imf.csv', 'a', newline="") as a:
            writer = csv.writer(a)
            for root, dirs, files in os.walk(os.getcwd()):
                # root当前路径, dirs当前路径下子目录, files当前路径下子文件
                root = root.replace(crt_path, '')
                if root[1:] == 'AFST_cache':
                    continue
                if not root == '':
                    one_line = [root[1:], 'folder', '', '']
                    writer.writerow(one_line)
                    self.NF_list.append(one_line)
                for one_file in files:
                    one_path = (root + '\\' + one_file)[1:]
                    md5_value = hashlib.md5()
                    with open(one_path,'rb') as f:
                        md5_value.update(f.read())
                    m_time = os.path.getmtime(one_path)
                    md5_code = md5_value.hexdigest()
                    one_line = [one_path, 'file', str(int(m_time)), md5_code]
                    writer.writerow(one_line)
                    self.NF_list.append(one_line)
    
    def commit_all_file(self):
        pass
    
    def commit_one_file(self):
        pass
    
    def get_history_edition(self):
        pass

afst = AFSTclient()
afst.get_new_file_list()