""" #모듈화

import mod.utils as mu

my_list = ['apple', 'banana', 'cherry']
print(mu.rd_int(1, 100))
print(mu.rd_list(my_list))
print(mu.rd_rd())
print(mu.rd_nmvar()) """

""" #datetime 이용 함수

from datetime import datetime as dt

#현재 시간 출력
print(dt.now())

#특정 시간대의 현재시간 출력
from pytz import all_timezone
# tz = timezone('Asia/Seoul')
tz = timezone('UTC')
print("timezon : ", dt.now(tz))

import mod.utils as mu
# import datetime as dt

#print (dt.now())
dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

mu.cvt_str2time(dtnow)

#문자열을 날짜로 변환
date_string = '2021-07-28'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

#날짜를 문자열로 변환
date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string) """

#os 모듈 확인

""" import os

#현재 작업 디렉토리 출력
print(os.getcwd())

#디렉토리 변경
os.chdir('../')

#변경된 디렉토리 출력
print(os.getcwd())

#파일 목록 출력 
print(os.listdir())

#디렉토리 생성
os.mkdir('new_directory')
print(os.listdir())

#디렉토리 삭제
os.rmdir('new_directory')
print(os.listdir())

import mod.utils as mu
import os
print(mu.get_curdir()) 
    
pname = "python"
mu.os_mkdir(pname) 
print(os.listdor())

os.rmdir(pname)
print(os.listdir()) """

#stack

st = []

#스택에 값 넣기
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

#스택의 상태 확인
print(st) # [1, 2, 3]

#스택에서 값 빼기
top = st.pop()
print(top) #3
print(st) #
print(len(st)) #


#append, pop, 이용한 queue

#빈 큐 생성
queue = []

#큐에 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

#큐의 상태 확인
print(queue) #[1, 2, 3]

#큐에서 값 빼기
front = queue.pop(0)
print(front) #1
print(queue) # [2, 3]
print(len(queue))

#enqueue/ dequeue

qlist = []

def enqueue (qlist, data) :
    qlist.append(data)
    
def dequeue(qlist) :
    data = qlist[0]
    del qlist[0]
    return data

enqueue (qlist,1)
print(qlist)    

enqueue (qlist,2)
print(qlist)   

enqueue (qlist,3)
print(qlist)   