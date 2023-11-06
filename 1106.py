""" import getpass

pw = input("Pass :")
print(pw)

# pw = getpass.getpass("Pass : ")
 """
 
 #해시알고리즘
 
""" import hashlib
 
target = "hello"
# target = "hi"
# target = "world"
# target = "python"
# target = "1234567890"

hl = hashlib.sha256()
target = "hello"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())
 """

#keccak256

""" import Crypto.Hash.keccak as kek

target = "to be or not to be, that is a question!"
# target = "hi"
# target = "world"
# target = "python"
# target = "1234567890"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest)
 """
#입력키 변환

""" import getpass
import hashlib
pw =getpass.getpass("Pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest)
print(hl.hexdigest())

#암호 파일 저장

import hashlib
import os

def pwInsert():
    if os.path.exists('pw.txt') :
        pw = input('insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True
    
if pwInsert():
    pw = input('new pass :')
    with open ('pw.txt', 'w') as fp :
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password") """
    
#시스템 정보

""" import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps)
     """
#웹페이지 읽기

""" import urllib.request as ur

url = 'https://www.google.com'
#url= "https://www.daum.net"

res = urllib.request.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
    
#print(web.decode('utf-8))
print(web)
 """
#웹정보 읽기 2

""" import http.client as hc

# url = 'https://www.google.com'
url = "www.google.com"
#conn = http.client.HTTPSConnection(url)
conn = hc.HTTPSconnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulrp.html", "wb") as fp:
    fp.write(r.read)
    
conn.close()

print(r) """

#웹정보 읽기 3

""" import requests
url = "https://www.google.com"
res = requests.get(url)
web = res.content

with open("ulrp.html", "wb") as fp:
    fp.write(web) """

#싱글 스레드

""" import time
def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
for i in range(3) :
    counter(f"num{i}")
    
print("single end",end- start)
 """
 
 #멀티 스레드
""" import time
import threading as td

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

start= time.time()
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time()

print("multi end", end- start) """

#병렬처리
""" import time
import multiprocessing as mp

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

process1 = mp.Process(target=counter, args=("1num",))
process2 = mp.Process(target=counter, args=("2num",))
process3 = mp.Process(target=counter, args=("3num",))

start= time.time()
process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()

end = time.time()

print("proc-end", end-start) """

#main 실행

""" def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    #run()
    main()
     """