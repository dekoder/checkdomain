#/usr/bin/env python
#coding:utf-8
import argparse
import sys
import re
import requests
import threading



def banner():
    pass


def parse_args():#命令定义
    parser = argparse.ArgumentParser(description='Example:python checkDomain.py -f alimama.txt -p 80,8080')
    parser.error=parse_error
    parser._optionals.title='OPTIONS'
    parser.add_argument('-p','--port',metavar="",default='80',help='choose a port or ports')
    parser.add_argument('-f','--file',metavar="",default='',help='choose a subdomain txt')
    parser.add_argument('-o','--outfile',metavar="",default='',help='save a file')
    return parser.parse_args()


def parse_error(errormsg):#传参报错
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errormsg)
    sys.exit()


def open_file(filename):#读取域名文件
    try:
        files = open(filename,'r')
    except IOError, e:
        print "could not open file:",e
        sys.exit(1)
    subdomain = []
    for eachline in files:
        print eachline     
        subdomain.append(eachline)
        
    return subdomain


def check_state(i,port,subdomain_ip):#检查主机状态
    url = "http://%s"%(subdomain_ip)

    if '443' in subdomain_ip:
        url = "https://%s"%(subdomain_ip.split(":")[0])
    else:
        url = "http://%s"%(subdomain_ip)
    try:
        r = requests.get(url,timeout=4)
        status = r.status_code
        if status in {200,301}:
            print "\033[91m[Interesting]:{}".format(url)
            intersting.append(url)
    except:
        print "\033[0m[Down]:{}".format(url)


def write(ip,infilename,filename):#写进文件
    filename == ''
    filename = 'out.'+infilename
    file = open(filename,'w')
    for i,this_ip in enumerate(ip):
        file.writelines(this_ip)
    file.close()


def go_threading(nums,port,subdomain_ip):#调用多线程
    global intersting
    intersting = []
    threads = []
    for i in nums:
        t = threading.Thread(target=check_state,args=(i,port,subdomain_ip[i]))
        threads.append(t)
    print '\033[1;32m[STRAT..]\n'
    for i in nums:
        threads[i].start()
    for i in nums:
        threads[i].join()
    print '\n\033[1;32m[DONE..]'


def main(port,infile,outfile): 
    subdomain_ip = open_file(infile)
    subdomain_ip = list(set(subdomain_ip))#去重ip/域名
    nums = range(len(subdomain_ip))
    go_threading(nums,port,subdomain_ip)
    write(intersting,infile,outfile)


if __name__ == '__main__':
    banner()
    args = parse_args()
    port = args.port
    infile = args.file
    outfile = args.outfile
    main(port,infile,outfile)
    
    
