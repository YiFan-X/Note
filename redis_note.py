redisѧϰ

��һ�������ݣ�

һ��
mysql ��ϵ�����ݿ�
�ǹ�ϵ�����ݿ� redis    mongodb
nosql  ��������sql

���ݳ־û�,���Խ����ݴ洢��������,���ļ���ʽ�洢

redis���ڴ��Ե����ݿ�,��д�Ƿǳ����
ȱ����:�ϵ��ͷ��ڴ�����,redis���ݶ�ʧ,redis���̹ҵ�,���ݶ�ʧ,redis�ṩ�˳־û�����

which����PATH����
[root@bogon src]# echo $PATH
/opt/python36/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/opt/node-v8.6.0-linux-x64/bin:/root/bin


[root@bogon ~]# echo $PATH
/opt/python36/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/opt/node-v8.6.0-linux-x64/bin:/root/bin


redis�İ�װ��ʽ
1.yum  install  redis -y
rpm

Դ�����(��ѡ������ʱ��,ע��ɾ��֮ǰ��yum��װ��)
1.yum remove redis -y 

2.����redis��Դ�����
wget http://download.redis.io/releases/redis-4.0.10.tar.gz

3.��ѹ��Դ���
����������:
#(��redisѹ����,�Ѿ��ṩ����makefile,ֻ��Ҫִ��,����ĵڶ�,������)
# ��Ϊ���ļ�����makefile�ļ�  ���Բ���ִ�� ./confiure

2.ִ��gcc��makeָ��,ִ��makefile�ļ�

make 
3.��ʼ��װ
make install

# ���µ�½һ�»ᷢ���Ѿ����س���PATH
[root@bogon ~]# which redis-server
/usr/local/bin/redis-server

# which����PATH����
[root@bogon src]# echo $PATH
/opt/python36/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/opt/node-v8.6.0-linux-x64/bin:/root/bin

  

4.�ᰲװ�ڵ�ǰ��Դ����е�srcĿ¼,�Ұ������ú���PATH����
ͨ��redis-����tab��ȫ�鿴��������

redis-benchmark  redis-check-rdb  redis-sentinel   
redis-check-aof  redis-cli        redis-server  


[root@bogon src]# pwd
/opt/redis-4.0.10/src
[root@bogon src]# redis-
redis-benchmark  redis-check-rdb  redis-sentinel   
redis-check-aof  redis-cli        redis-server 






5.�ƶ�һ����װ�ɿ���redis���ݿ�
���¹���ͨ�������ļ�����
1.���Ķ˿�
2.��������
3.����redis�İ�ȫ����ģʽ

Ĭ��ֱ������redis-server�������������,Ĭ�϶˿�6379,��û������
redis-cli��¼
[root@bogon ~]# redis-cli
127.0.0.1:6379> ping
PONG


[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING  Makefile   redis.conf       runtest-sentinel  tests
BUGS             deps     MANIFESTO  runtest          sentinel.conf     utils
CONTRIBUTING     INSTALL  README.md  runtest-cluster  src

[root@bogon redis-4.0.10]# vim redis.conf 
[root@bogon redis-4.0.10]# grep -v "^#" redis.conf  | grep  -v  "^$0"  >  ./s20redis.conf
# ��redis.conf���õ���Ϣ�������µ�s20redis.conf��

# �鿴�µ��ļ����Ƿ������
[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING  Makefile   redis.conf       runtest-sentinel  src
BUGS             deps     MANIFESTO  runtest          s20redis.conf     tests
CONTRIBUTING     INSTALL  README.md  runtest-cluster  sentinel.conf     utils
[root@bogon redis-4.0.10]# vim s20redis.conf 



[root@bogon ~]# cd /opt/redis-4.0.10/
[root@bogon redis-4.0.10]# vim s20redis.conf

#ʵ����ֱ��touchһ�� s20redis.conf  ��������Ϣֱ�Ӹ���ճ����ȥ
# vim s20redis.conf ��������
bind 192.168.190.11
protected-mode yes
port 6380
daemonize yes
pidfile /var/run/redis_6379.pid 
loglevel notice 
requirepass 123




redis.conf ��������,�ж��ٲ���,���ж��ٹ���,

bind 192.168.16.142    	#��redis�����ĵ�ַ
protected-mode yes		#����redis�İ�ȫģʽ,������������ſ���Զ�̵�¼
port 6380			 	#ָ��redis�Ķ˿�  
daemonize yes			#��redis���ػ����̷�ʽ�ں�̨����,��ռ�ô���
pidfile /var/run/redis_6379.pid   #��¼redis�Ľ���id�ŵ��ļ�
loglevel notice    		#��־���еȼ� .���ؼ���,���漶��,debug���Խ��.....logging
requirepass haohaio     #����redis������,�� haohaio


# ��������Ժ�
ָ�������ļ���������ʽ
redis-server  s20redis.conf  

[root@bogon redis-4.0.10]# redis-server  s20redis.conf  
11085:C 04 Jul 15:33:45.087 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
11085:C 04 Jul 15:33:45.087 # Redis version=4.0.10, bits=64, commit=00000000, modified=0, pid=11085, just started
11085:C 04 Jul 15:33:45.087 # Configuration loaded


# ��ʾ���õ���Ϣ�Ѿ���������
# ���û����ʾ���� ����Ҫ�����˳��Ự ���µ�¼ ����һ��s20redis.conf  �����˳�
# Ȼ�� redis-server  s20redis.conf  
[root@bogon ~]# netstat -tunlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
     
tcp        0      0 192.168.190.11:6380     0.0.0.0:*               LISTEN      11268/redis-server 




#��ʱ��¼redis������ϲ�����,���ҵ�¼��֮��,������������ſ���ʹ�� 
redis-cli -p 6380 -h 192.168.16.142

redis-cli -p 6380 -h 192.168.190.11

# ע�� ����ʱ�����ĸ�Ŀ¼������
[root@bogon ~]# redis-cli -p 6380 -h 192.168.190.11
192.168.190.11:6380> ping
(error) NOAUTH Authentication required.
# ���ҵ�¼��֮��,������������ſ���ʹ�� 
192.168.190.11:6380> auth 123
OK
192.168.190.11:6380> ping
PONG







����

ѧϰredis����������ʹ��

1.����redis�Ĺ�������
keys *         �鿴����key
type key      �鿴key����
expire key seconds    ����ʱ��
ttl key     �鿴key����ʣ��ʱ��        -2��ʾkey�Ѿ���������
persist     ȡ��key�Ĺ���ʱ��   -1��ʾkey���ڣ�û�й���ʱ��

exists key     �ж�key����    ���ڷ���1    ����0
del keys     ɾ��key    ����ɾ�����
dbsize         ����key������




192.168.190.11:6380> ping
PONG
192.168.190.11:6380> set name ivan
OK
192.168.190.11:6380> get name
"ivan"

192.168.190.11:6380> EXPIRE  name 20
(integer) 1
192.168.190.11:6380> ttl name
(integer) 13
192.168.190.11:6380> ttl name
(integer) 5
192.168.190.11:6380> ttl name
(integer) -2




192.168.190.11:6380> set name xiaobai
OK
192.168.190.11:6380> EXPIRE name 30
(integer) 1
192.168.190.11:6380> ttl name
(integer) 19
192.168.190.11:6380> PERSIST name   # ��ֹ����
(integer) 1
192.168.190.11:6380> ttl name
(integer) -1						# �ظ�Ϊ-1 ��û�й���ʱ��
192.168.190.11:6380> get name
"xiaobai"



192.168.190.11:6380> EXISTS age
(integer) 0
192.168.190.11:6380> set age 18
OK
192.168.190.11:6380> DBSIZE
(integer) 2						#name  age ����keyֵ
192.168.190.11:6380> EXISTS age
(integer) 1
192.168.190.11:6380> EXISTS name
(integer) 1


192.168.190.11:6380> del name age 
(integer) 2
192.168.190.11:6380> keys *
(empty list or set)







2.ѧϰstring���͵Ĳ���
set ��������key
get   ��ȡkey
append  ׷��string
mset   ���ö����ֵ��
mget   ��ȡ�����ֵ��
del  ɾ��key
incr  ����+1
decr  �ݼ�-1

list����,˫�����

dic1={
	'k1':{"k2":"v2"}
}


dic1[k1][k2]


# string

# type name
192.168.190.11:6380> type name
none
# ������ֵΪnone


# set name
192.168.190.11:6380> set name ivan
OK
192.168.190.11:6380> type name
string
#ͨ��set���õľ���string���͵�key -value


# APPEND name
192.168.190.11:6380> APPEND name xiaohai
(integer) 11
192.168.190.11:6380> get name
"ivanxiaohai"


# mset mget
192.168.190.11:6380> mset name2 xiaohei name3 xiaohong
OK
192.168.190.11:6380> DBSIZE
(integer) 3
192.168.190.11:6380> mget name name2 name3
1) "ivanxiaohai"
2) "xiaohei"
3) "xiaohong"



# INCR  �������а� 
# ÿ�μ�1 תΪ�ַ���
192.168.190.11:6380> set dizeng 0
OK
192.168.190.11:6380> get dizeng
"0"
192.168.190.11:6380> INCR dizeng
(integer) 1
192.168.190.11:6380> get dizeng
"1"
192.168.190.11:6380> INCR dizeng
(integer) 2
192.168.190.11:6380> get dizeng
"2"




# list

# LPUSH
192.168.190.11:6380> LPUSH dizeng xiaohuang xiaowang
(error) WRONGTYPE Operation against a key holding the wrong kind of value
# �б�����ֲ�����������ظ�
192.168.190.11:6380> LPUSH paidui xiaohuang  xiaobai 
(integer) 2

192.168.190.11:6380> keys *
1) "name3"
2) "name2"
3) "paidui"
4) "name"
5) "dizeng"

# LRANGE
192.168.190.11:6380> LRANGE paidui 0 -1
1) "xiaobai"
2) "xiaohuang"
192.168.190.11:6380> LPUSH paidui xiaohei
(integer) 3
192.168.190.11:6380> LPUSH paidui xiaohei
(integer) 4
192.168.190.11:6380> LRANGE paidui 0 -1
1) "xiaohei"
2) "xiaohei"
3) "xiaobai"
4) "xiaohuang"

# LTRIM
192.168.190.11:6380> LTRIM paidui 0 1
OK
192.168.190.11:6380> LRANGE paidui 0 -1
1) "xiaohei"
2) "xiaohei"

# LPOP
192.168.190.11:6380> LPOP paidui
"xiaohei"
192.168.190.11:6380> LRANGE paidui 0 -1
1) "xiaohei"




#  sets

#1   sadd/srem   ���/ɾ�� Ԫ��
192.168.190.11:6380> SADD home ivan sail
(integer) 2
192.168.190.11:6380> SMEMBERS home
1) "ivan"
2) "sail"

192.168.190.11:6380> SADD home2 xiaohai xiaobai
(integer) 2
192.168.190.11:6380> SMEMBERS home2
1) "xiaohai"
2) "xiaobai"


#2   sismember   �ж��Ƿ�Ϊset��һ��Ԫ��
# �ж��ڲ��ڼ�����
192.168.190.11:6380> SISMEMBER home xiaohai
(integer) 0
192.168.190.11:6380> SISMEMBER home2 xiaohai
(integer) 1



#3   sdiff             ����һ�����Ϻ��������ϵĲ���
# �鿴�������ϵĲ���
# ��ʾд��ǰ��Ĳ���
192.168.190.11:6380> SDIFF home home2
1) "ivan"
2) "sail"
192.168.190.11:6380> SDIFF home2 home
1) "xiaohai"
2) "xiaobai"


192.168.190.11:6380> SADD home2 sail
(integer) 1
192.168.190.11:6380> SDIFF home home2
1) "ivan"
# ��Ϊhome �� home2 ��һ��ivan




#4    sinter           ���ؼ������ϵĽ���

192.168.190.11:6380> SINTER home home2
1) "sail"

# sunion          ���ؼ������ϵĲ���
192.168.190.11:6380> SUNION home home2
1) "xiaohai"
2) "ivan"
3) "xiaobai"
4) "sail"



# ��ϣ���ݽṹ



192.168.190.11:6380> HSET stu1 name ivan age 18
(integer) 2
192.168.190.11:6380> HGET stu1 name
"ivan"
192.168.190.11:6380> HGET stu1 age
"18"

192.168.190.11:6380> hmget stu1 name age
1) "ivan"
2) "18"


192.168.190.11:6380> HSETNX stu1 name ivan age 15
(error) ERR wrong number of arguments for 'hsetnx' command
192.168.190.11:6380> HSETNX stu2 name ivan age 15
(error) ERR wrong number of arguments for 'hsetnx' command
192.168.190.11:6380> HSETNX stu2 name ivan
(integer) 1


192.168.190.11:6380> HKEYS stu1 
1) "name"
2) "age"
192.168.190.11:6380> HKEYS stu2
1) "name"
















�ڶ��������ݣ���
#redis�ķ�������
#QQȺ  
��ϸ�������


[root@bogon ~]# redis-cli -p 6380 -h 192.168.190.11
192.168.190.11:6380> auth 123
OK
192.168.190.11:6380> PUBLISH python2 hello
(integer) 2
192.168.190.11:6380> PUBLISH python22 hello
(integer) 1


��ͼ


.












�����������ݣ�


# ���⣺
# �ϵ����� �鿴֮ǰ������Ϊ��
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      12761      1  0 17:33 ?        00:00:00 redis-server 192.168.190.11:6380
root      12775  11284  0 17:33 pts/3    00:00:00 grep --color=auto redis
[root@bogon redis-4.0.10]# pkill -9 redis
[root@bogon redis-4.0.10]# redis-server s20redis.conf 
12777:C 04 Jul 17:34:01.018 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
12777:C 04 Jul 17:34:01.018 # Redis version=4.0.10, bits=64, commit=00000000, modified=0, pid=12777, just started
12777:C 04 Jul 17:34:01.018 # Configuration loaded
[root@bogon redis-4.0.10]# redis-cli -p 6380 -h 192.168.190.11 -a 123
Warning: Using a password with '-a' option on the command line interface may not be safe.
192.168.190.11:6380> keys *
(empty list or set)
# ���̶��� ���ݶ�ʧ


�������ķ�ʽ��

#redis�ĳ־û�����
��Ϊaof��rdb����,���忴����





һ�� rdb

����׼��

[root@bogon redis-4.0.10]# ps -ef | grep redis
root      12778      1  0 17:34 ?        00:00:00 redis-server 192.168.190.11:6380
root      12847  11284  0 17:41 pts/3    00:00:00 grep --color=auto redis
[root@bogon redis-4.0.10]# kill -9 12778
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      12858  11284  0 17:41 pts/3    00:00:00 grep --color=auto redis

[root@bogon redis-4.0.10]# touch s20rdb.conf


[root@bogon redis-4.0.10]# vim s20rdb.conf 
1.����һ��rdb��redis�����
	s20rdb.conf��������
	
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
dbfilename  dbmp.rdb 
bind  127.0.0.1
save 900 1       
save 300 10
save 60  10000

# �������
"""
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379              #����־û��ļ��洢λ��
dbfilename  dbmp.rdb        #rdb�־û��ļ�
bind 10.0.0.10  127.0.0.1    #redis�󶨵�ַ
requirepass redhat            #redis��¼����
save 900 1                    #rdb���� ÿ900�� ��1���޸ļ�¼
save 300 10                    #ÿ300��        10���޸ļ�¼
save 60  10000                #ÿ60����        10000�޸ļ�¼

# save 30  1    #ÿ30���Զ�saveһ��
# ����ǿ������Լ����ĵ�
# ע�ⲻ�ܸ�Ϊ1��һ��save  ̫ռ����Դ�� 

"""




		 		
		
2.��������ļ�����redis,֧��rdb�����ݿ�
redis-server s20rdb.conf 

# 1
[root@bogon redis-4.0.10]# redis-server s20rdb.conf

*** FATAL CONFIG FILE ERROR ***
Reading the configuration file, at line 4
>>> 'logfile /data/6379/redis.log'
Can't open the log file: No such file or directory


# 2
# ��Ҫ����һ�� /data/6379
[root@bogon redis-4.0.10]# mkdir -p /data/6379
[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING   INSTALL    README.md   runtest-cluster   s20redis.conf  tests
BUGS             deps      Makefile   redis.conf  runtest-sentinel  sentinel.conf  utils
CONTRIBUTING     dump.rdb  MANIFESTO  runtest     s20rdb.conf       src

[root@bogon redis-4.0.10]# redis-server s20rdb.conf 
# �����ɹ� ���ھͲ��ᱨ����

# 3
[root@bogon redis-4.0.10]# redis-server s20rdb.conf 
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      12932      1  0 17:46 ?        00:00:00 redis-server 127.0.0.1:6379
root      12962  11284  0 17:49 pts/3    00:00:00 grep --color=auto redis

# ��ʱ�Ľ��̾����޸��ļ���� 6379

[root@bogon redis-4.0.10]# cd /data/6379/
[root@bogon 6379]# ls
redis.log




3.��¼redis����key,Ȼ���ֶ�����save,����rdb�����ļ�dbmp.rdb 


[root@bogon 6379]# redis-cli
127.0.0.1:6379> keys *
(empty list or set)
127.0.0.1:6379> set name ivan
OK
127.0.0.1:6379> 
[root@bogon 6379]# ls
redis.log

[root@bogon 6379]# redis-cli
127.0.0.1:6379> keys *
1) "name"
127.0.0.1:6379> set age 18
OK
127.0.0.1:6379> save
OK
127.0.0.1:6379> 
[root@bogon 6379]# ls
dbmp.rdb  redis.log
# ֻ��save�� �Ż�����dbmp.rdb �ļ�


# �ϵ����� �鿴����

[root@bogon 6379]# pkill -9 redis
[root@bogon 6379]# ps -ef | grep redis
root      13149  11284  0 18:03 pts/3    00:00:00 grep --color=auto redis

[root@bogon 6379]# redis-server /opt/redis-4.0.10/s20rdb.conf 
[root@bogon 6379]# redis-cli 
127.0.0.1:6379> keys *
1) "name"
2) "age"
# �鿴 �����˽��� ����Ҳ��

# �鿴 dbmp.rdb�ļ���������� 
127.0.0.1:6379> 
[root@bogon 6379]# ls
dbmp.rdb  redis.log
[root@bogon 6379]# vim dbmp.rdb 

REDIS0008��      redis-ver^F4.0.10��
redis-bits��@��^Ectime???^]]��^Hused-mem?^X^A^L^@��^Laof-preamble��^@t^@?^B^@^@^Cage��^R^@^Dname^Divan??��E^D����X?
~     






����aof



# 1 ׼����
[root@bogon 6379]# cd /opt/redis-4.0.10/
[root@bogon redis-4.0.10]# touch s20aof.conf
[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING   INSTALL    README.md   runtest-cluster   s20rdb.conf    src
BUGS             deps      Makefile   redis.conf  runtest-sentinel  s20redis.conf  tests
CONTRIBUTING     dump.rdb  MANIFESTO  runtest     s20aof.conf       sentinel.conf  utils
[root@bogon redis-4.0.10]# vim s20aof.conf 


# 2 ����s20aof.conf 
[root@bogon redis-4.0.10]# vim s20aof.conf 

#2 s20aof.conf ��������
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
dbfilename  dbmp.rdb
requirepass redhat
save 900 1
save 300 10
save 60  10000
appendonly yes
appendfsync everysec


daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
appendonly yes
appendfsync everysec




# 3
# Ϊ�˲�Ӱ��ʵ��Ч�� �ϵ�֮ǰ�Ľ��̺� 6379�����е��ļ�

[root@bogon redis-4.0.10]# ps -ef | grep redis
root      13169      1  0 18:04 ?        00:00:00 redis-server 127.0.0.1:6379
root      13382  11284  0 18:24 pts/3    00:00:00 grep --color=auto redis
[root@bogon redis-4.0.10]# pkill -9 redis
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      13393  11284  0 18:25 pts/3    00:00:00 grep --color=auto redis
[root@bogon redis-4.0.10]# cd /data/6379/
[root@bogon 6379]# ls
dbmp.rdb  redis.log
[root@bogon 6379]# rm -rf  *
[root@bogon 6379]# ls


# 4 ���������ļ�

[root@bogon 6379]# cd -      # �ص���һ�ε�Ŀ¼ ���������ļ�
/opt/redis-4.0.10
[root@bogon redis-4.0.10]# redis-server s20aof.conf 
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      13437      1  0 18:29 ?        00:00:00 redis-server *:6379
root      13442  11284  0 18:29 pts/3    00:00:00 grep --color=auto redis

# �ص�6379 �鿴���������ļ� �Զ����س������ļ�
[root@bogon redis-4.0.10]# cd -
/data/6379
[root@bogon 6379]# ls
appendonly.aof  redis.log


# 5  ʵ�鿪ʼ
# 
# ����1
[root@bogon ~]# redis-cli
127.0.0.1:6379> auth 123
(error) ERR Client sent AUTH, but no password is set
127.0.0.1:6379> keys *
(empty list or set)

127.0.0.1:6379> set age 18
OK


# ����2
[root@bogon 6379]# tail -f appendonly.aof


*2
$6
SELECT
$1
0
*3
$3
set
$3
age
$2
18



# 6  �鿴����
# �鿴�����ݻ���
[root@bogon 6379]# redis-server /opt/redis-4.0.10/s20aof.conf 
[root@bogon 6379]# redis-cli 
127.0.0.1:6379> keys *
1) "age"
127.0.0.1:6379> 
[root@bogon 6379]# ls
appendonly.aof  redis.log
[root@bogon 6379]# vim appendonly.aof 

*2
$6
SELECT
$1
0
*3
$3
set
$3
age
$2
18
~    


# �������ȼ�

aof �ļ���� rdb��













���Ĳ������ݣ�


#�ڲ�����redis�������,�л�rdb�е�����,��aof�еĲ���
����׼��

1.����һ��rdb��redis�����
	s20rdb.conf��������
		daemonize yes
		port 6379
		logfile /data/6379/redis.log
		dir /data/6379
		dbfilename  dbmp.rdb 
		bind  127.0.0.1
		save 900 1       
		save 300 10
		save 60  10000



[root@bogon 6379]# cd -
/opt/redis-4.0.10

[root@bogon redis-4.0.10]# ps -ef | grep redis
root      13437      1  0 18:29 ?        00:00:02 redis-server *:6379
root      14005  11284  0 19:21 pts/3    00:00:00 grep --color=auto redis

[root@bogon redis-4.0.10]# kill -9 13437

[root@bogon redis-4.0.10]# !ps
ps -ef | grep redis
root      14015  11284  0 19:22 pts/3    00:00:00 grep --color=auto redis

[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING   INSTALL    README.md   runtest-cluster   s20rdb.conf    src
BUGS             deps      Makefile   redis.conf  runtest-sentinel  s20redis.conf  tests
CONTRIBUTING     dump.rdb  MANIFESTO  runtest     s20aof.conf       sentinel.conf  utils

[root@bogon redis-4.0.10]# vim s20rdb.conf 

daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
dbfilename  dbmp.rdb
bind  127.0.0.1
save 900 1
save 300 10
save 60  10000


# ɾ��6379�µ��ļ�
[root@bogon redis-4.0.10]# cd -
/data/6379
[root@bogon 6379]# ls
appendonly.aof  redis.log

[root@bogon 6379]# rm -rf *
[root@bogon 6379]# ls
#�鿴�ļ��Ѿ���ɾ��

		
			
		
		
2.��������ļ�����redis,֧��rdb�����ݿ�
redis-server s20rdb.conf 


[root@bogon 6379]# cd -
/opt/redis-4.0.10
[root@bogon redis-4.0.10]# redis-server s20rdb.conf 

[root@bogon redis-4.0.10]# redis-cli
127.0.0.1:6379> set name  sail
OK
127.0.0.1:6379> set addr shanghai
OK
127.0.0.1:6379> set age 18
OK
127.0.0.1:6379> keys *
1) "addr"
2) "age"
3) "name"
127.0.0.1:6379> save
OK
# �ֶ�����
# �鿴�Ѿ����ļ�
[root@bogon redis-4.0.10]# ls /data/6379/
dbmp.rdb  redis.log


3.��¼redis����key,Ȼ���ֶ�����save,����rdb�����ļ�


4.ͨ����¼redis,��������,�л�Ϊaof�־û���ʽ

[root@bogon redis-4.0.10]# redis-cli
127.0.0.1:6379>  CONFIG set appendonly yes 
OK
127.0.0.1:6379> CONFIG SET save ""
OK


[root@bogon redis-4.0.10]# ls /data/6379/
appendonly.aof  dbmp.rdb  redis.log

# ������appendonly.aof
# �鿴���ݹ�����
[root@bogon redis-4.0.10]# vim /data/6379/appendonly.aof 

*2
$6
SELECT
$1
0
*3
$3
SET
$4
addr
$8
shanghai
*3
$3
SET
$3
age
$2
18
*3
$3
SET
$4
name
$4
sail




5.��4���Ĳ���,��������ʱ��Ч,�����޸������ļ�,��֤�´�����,Ҳ����aof���г־û�



# ԭ���������ļ���Ϣ

[root@bogon redis-4.0.10]# vim s20rdb.conf 
"""
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
dbfilename  dbmp.rdb
bind  127.0.0.1
save 900 1
save 300 10
save 60  10000
"""

# �޸���������ļ���Ϣ
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
bind  127.0.0.1
appendonly yes
appendfsync  always


[root@bogon redis-4.0.10]# vim s20rdb.conf 
# �������ļ���Ϣ
# �鿴������Ϣ
[root@bogon redis-4.0.10]# redis-cli
127.0.0.1:6379> keys *
1) "addr"
2) "age"
3) "name"
127.0.0.1:6379> 

# ��ʼ �ϵ����� �������������ļ�
[root@bogon redis-4.0.10]# pkill -9 redis
[root@bogon redis-4.0.10]# redis-server s20rdb.conf 
[root@bogon redis-4.0.10]# redis-cli 
127.0.0.1:6379> keys *
1) "age"
2) "name"
3) "addr"

127.0.0.1:6379> 
[root@bogon redis-4.0.10]# cd -
/data/6379
[root@bogon 6379]# ls
appendonly.aof  dbmp.rdb  redis.log

# �鿴appendonly.aof �����Ϣ
[root@bogon 6379]# cat appendonly.aof 
*2
$6
SELECT
$1
0
*3
$3
SET
$4
addr
$8
shanghai
*3
$3
SET
$3
age
$2
18
*3
$3
SET
$4
name
$4
sail


#�ڿ������� ��¼redis

[root@bogon ~]# redis-cli
127.0.0.1:6379> 
127.0.0.1:6379> set name123  ican
OK


# ��̬�Ĳ鿴�� ���� �仯�� ��¼����appendonly.aof 
[root@bogon 6379]# tail -f appendonly.aof 
age
$2
18
*3
$3
SET
$4
name
$4
sail




*2
$6
SELECT
$1
0
*3
$3
set
$7
name123
$4
ican






6. ��չ֪ʶ redis�¼�����

save 900 1����ʾ900 ������������� 1 �� key ��ֵ�仯���򱣴�
save 300 10����ʾ300 ������������� 10 �� key ��ֵ�仯���򱣴�
save 60 10000����ʾ60 ������������� 10000 �� key ��ֵ�仯���򱣴�

redis�ǵ��̵߳�,��c��д 








daemonize yes
port 6379
logfile "/data/6379/redis.log"
dir /data/6379
dbfilename dump.rdb
bind 127.0.0.1
save 30 1




���岿�����ݣ�

       
#redis�����Ӹ���



һ�� �����˽�
1.redis��mysql����֧�ֶ�ʵ������,���������ļ�����,����һ�����ݿⵥ����ʵ��



# �������
# ԭ����myredis.conf�ļ���Ϣ
[root@bogon redis-4.0.10]# touch myredis.conf
[root@bogon redis-4.0.10]# vim myredis.conf 

daemonize yes
port 6379
logfile "/data/6379/redis.log"
dir /data/6379
dbfilename dump.rdb
bind 127.0.0.1
save 30 1
          

[root@bogon redis-4.0.10]# sed 's/6379/6380/g'  myredis.conf  > 6380-redis.conf

# ��myredis.conf�ļ������滻  �滻�Ľ��д�뵽 6380-redis.conf ��

# �鿴6380-redis.conf����Ϣ
[root@bogon redis-4.0.10]# cat 6380-redis.conf 
daemonize yes
port 6380
logfile "/data/6380/redis.log"
dir /data/6380
dbfilename dump.rdb
bind 127.0.0.1
save 30 1






2.�ֱ�����2��redisʵ��
 1061  redis-server redis-6379.conf 
 1062  redis-server redis-6380.conf 

 
# ����һ��6380���ļ���
[root@bogon redis-4.0.10]# mkdir -p /data/6380

#�鿴������Ϣ ����һ��redis����Ҳû��
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      14796  11284  0 20:22 pts/3    00:00:00 grep --color=auto redis

# ���� myredis.conf  127.0.0.1:6379
[root@bogon redis-4.0.10]# redis-server myredis.conf 
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      14800      1  0 20:22 ?        00:00:00 redis-server 127.0.0.1:6379
root      14805  11284  0 20:22 pts/3    00:00:00 grep --color=auto redis

# ���� 6380-redis.conf  127.0.0.1:6380
[root@bogon redis-4.0.10]# redis-server 6380-redis.conf 
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      14800      1  0 20:22 ?        00:00:00 redis-server 127.0.0.1:6379
root      14817      1  0 20:22 ?        00:00:00 redis-server 127.0.0.1:6380
root      14822  11284  0 20:22 pts/3    00:00:00 grep --color=auto redis


# �������������� ����֮���Ǹ����


# 6379�� ���ݿ���Ϣ
[root@bogon redis-4.0.10]# redis-cli
127.0.0.1:6379> keys *
(empty list or set)
127.0.0.1:6379> set name ivan
OK
127.0.0.1:6379> set age 18
OK
127.0.0.1:6379> set addr shanghai
OK
127.0.0.1:6379> keys *
1) "age"
2) "addr"
3) "name"
127.0.0.1:6379> 


# 6380�� ���ݿ���Ϣ
[root@bogon ~]# redis-cli -p 6380
127.0.0.1:6380> keys *
(empty list or set)
# ��ʱ 6380 �ǿյ�


# ���������ļ���һ̨���������ж�����ݿ� 
# �������ݿⲻ����  ���Ը���ͬ����Ŀ��






������ʼʵ��

1 ����׼��,һ��6379��redis(master),��һ��6380��redis(slave)

�ֱ�׼��2�������ļ�,��������
redis-6379.conf

port 6379
daemonize yes
pidfile /data/6379/redis.pid
loglevel notice
logfile "/data/6379/redis.log"
dbfilename dump.rdb
dir /data/6379
protected-mode no


redis-6380.conf (��)

port 6380
daemonize yes
pidfile /data/6380/redis.pid
loglevel notice
logfile "/data/6380/redis.log"
dbfilename dump.rdb
dir /data/6380
protected-mode no
slaveof   127.0.0.1  6379


port 6380
daemonize yes
pidfile /data/6380/redis.pid
loglevel notice
logfile "/data/6380/redis.log"
dbfilename dump.rdb
dir /data/6380
protected-mode no
slaveof   127.0.0.1  6379



# ��������
# Ϊ�˱������ ��opt�ﴴ��smredis
[root@bogon redis-4.0.10]# cd /opt/
[root@bogon opt]# mkdir smredis
[root@bogon opt]# cd smredis/
[root@bogon smredis]# ls

[root@bogon smredis]# touch redis-6380.conf
[root@bogon smredis]# vim redis-6380.conf 
port 6380
daemonize yes
pidfile /data/6380/redis.pid
loglevel notice
logfile "/data/6380/redis.log"
dbfilename dump.rdb
dir /data/6380
protected-mode no



# 6380 ������Ϣ�� ֱ��ɾ��
[root@bogon smredis]# ls /data/6380/redis.log 
/data/6380/redis.log
[root@bogon smredis]# rm -rf /data/6380/*



# �� smredis ���� redis-6379.conf  
[root@bogon smredis]# sed 's/6380/6379/g'  redis-6380.conf  >  redis-6379.conf
[root@bogon smredis]# ls
redis-6379.conf  redis-6380.conf
# ���� smredis ������ redis-6379.conf  redis-6380.conf �����ļ�



# ɱ������
[root@bogon smredis]# ps -ef | grep redis
root      14800      1  0 20:22 ?        00:00:01 redis-server 127.0.0.1:6379
root      14817      1  0 20:22 ?        00:00:01 redis-server 127.0.0.1:6380
root      14958  14901  0 20:31 pts/0    00:00:00 redis-cli -p 6380
root      15197  11284  0 20:55 pts/3    00:00:00 grep --color=auto redis
[root@bogon smredis]# pkill -9 redis
[root@bogon smredis]# ps -ef | grep redis
root      15200  11284  0 20:55 pts/3    00:00:00 grep --color=auto redis



# �鿴�ղ����ɵ� redis-6379.conf  ��Ϣ
[root@bogon smredis]# cat redis-6379.conf 
port 6379
daemonize yes
pidfile /data/6379/redis.pid
loglevel notice
logfile "/data/6379/redis.log"
dbfilename dump.rdb
dir /data/6379
protected-mode no



# ��� /data/6379/* ���е�����
[root@bogon smredis]# rm -rf /data/6379/*



# �� redis-6380.conf  �ļ���  ��slaveof
[root@bogon smredis]# vim redis-6380.conf 
port 6380
daemonize yes
pidfile /data/6380/redis.pid
loglevel notice
logfile "/data/6380/redis.log"
dbfilename dump.rdb
dir /data/6380
protected-mode no
slaveof   127.0.0.1  6379






2.�ֱ�����2��redisʵ��
 1061  redis-server redis-6379.conf 
 1062  redis-server redis-6380.conf 

[root@bogon smredis]# redis-server redis-6379.conf 
[root@bogon smredis]# redis-server redis-6380.conf 
[root@bogon smredis]# ps -ef | grep redis
root      15361      1  0 21:01 ?        00:00:01 redis-server *:6379
root      15795      1  0 21:29 ?        00:00:00 redis-server *:6380
root      15801  15646  0 21:29 pts/0    00:00:00 grep --color=auto redis

 
 
 
 
3.��¼���ݿ�,�鿴����֮��Ĺ�ϵ

��¼6379���ݿ�,������������
127.0.0.1:6379> info  replication

[root@bogon smredis]# redis-cli
127.0.0.1:6379> info  replication
# Replication
role:master
connected_slaves:1
slave0:ip=127.0.0.1,port=6380,state=online,offset=196,lag=0
master_replid:bd80df540e6a5e4a235d52db0b36184eb8f93b6f
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:196
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:196





6380���ݿ�鿴���¹�ϵ
[root@s20 smredis]# redis-cli -p 6380  info replication

[root@bogon ~]# redis-cli -p 6380  info replication
# Replication
role:slave
master_host:127.0.0.1
master_port:6379
master_link_status:up
master_last_io_seconds_ago:0
master_sync_in_progress:0
slave_repl_offset:336
slave_priority:100
slave_read_only:1
connected_slaves:0
master_replid:bd80df540e6a5e4a235d52db0b36184eb8f93b6f
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:336
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:336




4.���ݶ�д�鿴
��6379���ǿ��Զ�д��

# ����1   6379
redis-cli -p 6379  set name5  haoxiangxiake

[root@bogon smredis]# redis-cli -p 6379  set name5  zuoyetaiduo
OK
[root@bogon smredis]# redis-cli
127.0.0.1:6379> keys *
1) "name5"



# ����2   6380
redis-cli -p 6380 get name5

[root@bogon ~]# redis-cli -p 6380 get name5
"zuoyetaiduo"
[root@bogon ~]# redis-cli -p 6380  
127.0.0.1:6380> keys *
1) "name5"

127.0.0.1:6380> set name6 buxiangxiezuoye
(error) READONLY You can't write against a read only slave.
# ֻ�ܶ� ����д




5.���Ӹ��ƹ��ϻָ�

# �����һ��6381���ݿ�  Ҳ����Ϊ6379 �Ĵ����ݿ�

# ��/data�ﴴ��һ�� 6381 �ļ�
[root@bogon ~]# cd /data
[root@bogon data]# ls
6379  6380
[root@bogon data]# mkdir 6381
[root@bogon data]# ls
6379  6380  6381



# ����һ�� redis-6381.conf �ļ�
[root@bogon smredis]# sed 's/6380/6381/g'  redis-6380.conf  >  redis-6381.conf
[root@bogon smredis]# ls
��  redis-6379.conf  redis-6380.conf  redis-6381.conf
# �����ļ���Ϣ
[root@bogon smredis]# vim redis-6381.conf 
port 6381
daemonize yes
pidfile /data/6381/redis.pid
loglevel notice
logfile "/data/6381/redis.log"
dbfilename dump.rdb
dir /data/6381
protected-mode no
slaveof   127.0.0.1  6379

# ���� redis-6381.conf
[root@bogon smredis]# redis-server redis-6381.conf 
[root@bogon smredis]# redis-cli -p 6381

127.0.0.1:6381> keys *
1) "name1"
2) "name5"
3) "name2"


# 6379������  6380 6381 �Ǵӿ�


�ӿ��������ν
������˵������ָ�����,���߽��ӿ��л�Ϊ����,��������

	-.ʵ�鲽��
	1.�ֱ����� 6379  6380 6381 �������ݿ�ʵ��,���������ӹ�ϵ
	
	2.ɱ��6379����,��ʱ6380 6381 Ⱥ������
	
	
	[root@bogon smredis]# ps -ef |grep redis
	root      15361      1  0 21:01 ?        00:00:02 redis-server *:6379
	root      15795      1  0 21:29 ?        00:00:00 redis-server *:6380
	root      16106      1  0 21:45 ?        00:00:00 redis-server *:6381
	root      16128  15841  0 21:47 pts/3    00:00:00 redis-cli -p 6381
	root      16160  16045  0 21:50 pts/4    00:00:00 redis-cli -p 6380
	root      16200  15646  0 21:53 pts/0    00:00:00 grep --color=auto redis

	[root@bogon smredis]# kill -9 15361

	[root@bogon smredis]# ps -ef |grep redis
	root      15795      1  0 21:29 ?        00:00:01 redis-server *:6380
	root      16106      1  0 21:45 ?        00:00:00 redis-server *:6381
	root      16128  15841  0 21:47 pts/3    00:00:00 redis-cli -p 6381
	root      16160  16045  0 21:50 pts/4    00:00:00 redis-cli -p 6380
	root      16219  15646  0 21:55 pts/0    00:00:00 grep --color=auto redis



	
	3.ѡ����6381Ϊ�µ�����,��Ҫȥ��6381�Ĵӵ����
	redis-cli -p 6381 slaveof  no one 
	#�鿴��ʱ6381�����
	redis-cli -p 6381 info replication
	
	[root@bogon smredis]# redis-cli -p 6381 slaveof  no one
	OK
	[root@bogon smredis]# redis-cli -p 6381 info replication
	# Replication
	role:master    		#    ��ʱ 6381Ϊ������
	connected_slaves:0
	master_replid:5b91f338a06af956a1050ca0deb5e3ba48925849
	master_replid2:bd80df540e6a5e4a235d52db0b36184eb8f93b6f
	master_repl_offset:2313
	second_repl_offset:2314
	repl_backlog_active:1
	repl_backlog_size:1048576
	repl_backlog_first_byte_offset:1460
	repl_backlog_histlen:854

	
	
	
	

	4.��ʱ��6380�����˸�Ϊ6381
	redis-cli -p 6380 slaveof 127.0.0.1 6381

	# �ȴ���һ������ �������ÿ������ݵı仯
	[root@bogon smredis]# redis-cli -p 6381
	127.0.0.1:6381> set name  zuoyexiebuwanle
	OK

	[root@bogon smredis]# redis-cli -p 6380 slaveof 127.0.0.1 6381
	OK


	[root@bogon smredis]# redis-cli -p 6380 info replication
	# Replication
	role:slave
	master_host:127.0.0.1
	master_port:6381                 # ����Ϊ6381��
	master_link_status:up
	master_last_io_seconds_ago:0
	master_sync_in_progress:0
	slave_repl_offset:2507
	slave_priority:100
	slave_read_only:1
	connected_slaves:0
	master_replid:5b91f338a06af956a1050ca0deb5e3ba48925849
	master_replid2:bd80df540e6a5e4a235d52db0b36184eb8f93b6f
	master_repl_offset:2507
	second_repl_offset:2314
	repl_backlog_active:1
	repl_backlog_size:1048576
	repl_backlog_first_byte_offset:1
	repl_backlog_histlen:2507

	
	# �鿴�� �ղŴ�������һ��������
	[root@bogon smredis]# redis-cli -p 6380
	127.0.0.1:6380> keys *
	1) "name"
	2) "name5"
	3) "name2"
	4) "name1"





	
	
�����������ݣ�	

	
redis���ڱ�,�Զ������ӹ����л�
���ò���

1.����׼��,׼��3��redis���ݿ�ʵ��,�ֱ��� 6379  6380  6381  
	redis-6379.conf     redis-6380.conf    redis-6381.conf 
	
[root@bogon smredis]# cd ..
[root@bogon opt]# mkdir sbredis
[root@bogon opt]# cd sbredis/
[root@bogon sbredis]# vim redis-6379.conf
port 6379
daemonize yes
logfile "6379.log"
dbfilename "dump-6379.rdb"
dir "/var/redis/data/6379"

[root@bogon sbredis]# vim redis-6380.conf
port 6380
daemonize yes
logfile "6380.log"
dbfilename "dump-6380.rdb"
dir "/var/redis/data/6380" 
slaveof 127.0.0.1 6379    

[root@bogon sbredis]# vim redis-6381.conf
port 6381
daemonize yes
logfile "6380.log"
dbfilename "dump-6380.rdb"
dir "/var/redis/data/6381" 
slaveof 127.0.0.1 6379    

# �����ļ�
[root@bogon sbredis]# mkdir -p /var/redis/data/{6379,6380,6381}

# ɱ������
[root@bogon sbredis]# pkill -9 redis
[root@bogon sbredis]# ps -ef | grep redis
root      16528  15646  0 22:26 pts/0    00:00:00 grep --color=auto redis



	
2.�ֱ���������redis���ݿ�ʵ�� 
[root@bogon sbredis]# redis-server redis-6379.conf 
[root@bogon sbredis]# redis-server redis-6380.conf 
[root@bogon sbredis]# redis-server redis-6381.conf 
[root@bogon sbredis]# ps -ef | grep redis
root      16538      1  0 22:27 ?        00:00:00 redis-server *:6379
root      16543      1  0 22:27 ?        00:00:00 redis-server *:6380
root      16549      1  0 22:27 ?        00:00:00 redis-server *:6381
root      16555  15646  0 22:27 pts/0    00:00:00 grep --color=auto redis



# �鿴�����ļ�����Ϣ  ���Ƿ����

[root@bogon sbredis]# redis-cli -p 6379 info replication
# Replication
role:master
connected_slaves:2
slave0:ip=127.0.0.1,port=6380,state=online,offset=84,lag=0
slave1:ip=127.0.0.1,port=6381,state=online,offset=84,lag=1
master_replid:c2d32464eed5e8e4219067530abe0b5fe69341fd
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:84
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:84


[root@bogon sbredis]# redis-cli -p 6380 info replication
# Replication
role:slave
master_host:127.0.0.1
master_port:6379
master_link_status:up
master_last_io_seconds_ago:3
master_sync_in_progress:0
slave_repl_offset:98
slave_priority:100
slave_read_only:1
connected_slaves:0
master_replid:c2d32464eed5e8e4219067530abe0b5fe69341fd
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:98
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:98


[root@bogon sbredis]# redis-cli -p 6381 info replication
# Replication
role:slave
master_host:127.0.0.1
master_port:6379
master_link_status:up
master_last_io_seconds_ago:9
master_sync_in_progress:0
slave_repl_offset:98
slave_priority:100
slave_read_only:1
connected_slaves:0
master_replid:c2d32464eed5e8e4219067530abe0b5fe69341fd
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:98
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:15
repl_backlog_histlen:84


# ������Ϣ �������




3.׼������redis-sentinel�ڱ��������ļ�

redis-sentinel-26379.conf

port 26379  
dir /var/redis/data/26379
logfile "26379.log"

// ��ǰSentinel�ڵ��� 127.0.0.1:6379 ������ڵ�
// 2�����ж����ڵ�ʧ��������Ҫ2��Sentinel�ڵ�ڵ�ͬ��
// mymaster�����ڵ�ı���
sentinel monitor s20master 127.0.0.1   6379  2
// �ڱ������ s20master  

//ÿ��Sentinel�ڵ㶼Ҫ����PING�������ж�Redis���ݽڵ������Sentinel�ڵ��Ƿ�ɴ�������30000����30s��û�лظ������ж����ɴ�
sentinel down-after-milliseconds s20master 30000

//��Sentinel�ڵ㼯�϶����ڵ�����ж����һ��ʱ��Sentinel�쵼�߽ڵ��������ת�Ʋ�����ѡ���µ����ڵ㣬
ԭ���Ĵӽڵ�����µ����ڵ㷢���Ʋ���������ÿ�����µ����ڵ㷢���Ʋ����Ĵӽڵ����Ϊ1
sentinel parallel-syncs s20master 1

//����ת�Ƴ�ʱʱ��Ϊ180000����
sentinel failover-timeout s20master 180000

//���ڱ��ں�̨����
daemonize yes



[root@bogon sbredis]# ls
6379.log  6380.log  redis-6379.conf  redis-6380.conf  redis-6381.conf

[root@bogon sbredis]# touch redis-26379.conf
[root@bogon sbredis]# vim redis-26379.conf 
port 26379  
dir /var/redis/data/26379
logfile "26379.log"
sentinel monitor s20master 127.0.0.1   6379  2
sentinel down-after-milliseconds s20master 30000
sentinel parallel-syncs s20master 1
sentinel failover-timeout s20master 180000
daemonize yes	

# daemonize yes һ��Ҫ��,���ڱ����ں������	
	

	
	
#����26380��26381�������ļ�,�����Ƕ˿ڵĲ�ͬ,���Կ�������	
redis-sentinel-26380.conf
redis-sentinel-26381.conf

#������������
 1119  sed "s/26379/26380/g"  redis-26379.conf > redis-26380.conf
 1121  sed "s/26379/26381/g"  redis-26379.conf > redis-26381.conf

 
[root@bogon sbredis]# sed "s/26379/26380/g"  redis-26379.conf > redis-26380.conf
[root@bogon sbredis]# sed "s/26379/26381/g"  redis-26379.conf > redis-26381.conf
[root@bogon sbredis]# ls
6379.log  redis-26379.conf  redis-26381.conf  redis-6380.conf
6380.log  redis-26380.conf  redis-6379.conf   redis-6381.conf


# �鿴һ��redis-26380.conf ��Ϣ
[root@bogon sbredis]# cat redis-26380.conf 
port 26380  
dir /var/redis/data/26380
logfile "26380.log"
sentinel monitor s20master 127.0.0.1   6379  2
sentinel down-after-milliseconds s20master 30000
sentinel parallel-syncs s20master 1
sentinel failover-timeout s20master 180000
daemonize yes	
 
# daemonize yes һ��Ҫ��,���ڱ����ں������	

 
# �鿴һ��redis-26381.conf ��Ϣ 
[root@bogon sbredis]# cat redis-26381.conf 
port 26381  
dir /var/redis/data/26381
logfile "26381.log"
sentinel monitor s20master 127.0.0.1   6379  2
sentinel down-after-milliseconds s20master 30000
sentinel parallel-syncs s20master 1
sentinel failover-timeout s20master 180000
daemonize yes	

# daemonize yes һ��Ҫ��,���ڱ����ں������	



4.�ֱ����������ڱ�����
(��֤sentinel��������ȷ,����,�������������,�����ļ������ݷ������仯,���Ǹ���!!!!)

#�����ڱ��������ļ���
[root@bogon sbredis]# mkdir -p /var/redis/data/26379
[root@bogon sbredis]# mkdir -p /var/redis/data/26380
[root@bogon sbredis]# mkdir -p /var/redis/data/26381
 
 
 
(��֤sentinel��������ȷ,����,�������������,�����ļ������ݷ������仯,���Ǹ���!!!!) 
(��֤sentinel��������ȷ,����,�������������,�����ļ������ݷ������仯,���Ǹ���!!!!) 
(��֤sentinel��������ȷ,����,�������������,�����ļ������ݷ������仯,���Ǹ���!!!!) 

# daemonize yes һ��Ҫ��,���ڱ����ں������	
# daemonize yes һ��Ҫ��,���ڱ����ں������	
# daemonize yes һ��Ҫ��,���ڱ����ں������	

 
 #�ֱ����������ڱ�
 1134  redis-sentinel redis-26379.conf 
 1137  redis-sentinel redis-26380.conf 
 1138  redis-sentinel redis-26381.conf 

[root@bogon sbredis]# ps -ef | grep redis
root      16538      1  0 22:27 ?        00:00:00 redis-server *:6379
root      16543      1  0 22:27 ?        00:00:00 redis-server *:6380
root      16549      1  0 22:27 ?        00:00:00 redis-server *:6381
root      16755  15646  0 22:45 pts/0    00:00:00 grep --color=auto redis

[root@bogon sbredis]# redis-sentinel redis-26379.conf
[root@bogon sbredis]# redis-sentinel redis-26380.conf 
[root@bogon sbredis]# redis-sentinel redis-26381.conf

[root@bogon sbredis]# ps -ef | grep redis
root      16538      1  0 22:27 ?        00:00:00 redis-server *:6379
root      16543      1  0 22:27 ?        00:00:00 redis-server *:6380
root      16549      1  0 22:27 ?        00:00:00 redis-server *:6381
root      16765      1  0 22:45 ?        00:00:00 redis-sentinel *:26379 [sentinel]
root      16770      1  0 22:46 ?        00:00:00 redis-sentinel *:26380 [sentinel]
root      16775      1  0 22:46 ?        00:00:00 redis-sentinel *:26381 [sentinel]
root      16780  15646  0 22:46 pts/0    00:00:00 grep --color=auto redis


# �����ڱ� �� �������ݿ� �Ѿ�����




 
5.���redis���ڱ�״̬
redis-cli -p 26379 info sentinel
redis-cli -p 26380 info sentinel
redis-cli -p 26381 info sentinel

[root@bogon sbredis]# redis-cli -p 26379 info sentinel
# Sentinel
sentinel_masters:1
sentinel_tilt:0
sentinel_running_scripts:0
sentinel_scripts_queue_length:0
sentinel_simulate_failure_flags:0
master0:name=s20master,status=ok,address=127.0.0.1:6379,slaves=2,sentinels=3

[root@bogon sbredis]# redis-cli -p 26380 info sentinel
# Sentinel
sentinel_masters:1
sentinel_tilt:0
sentinel_running_scripts:0
sentinel_scripts_queue_length:0
sentinel_simulate_failure_flags:0
master0:name=s20master,status=ok,address=127.0.0.1:6379,slaves=2,sentinels=3

[root@bogon sbredis]# redis-cli -p 26381 info sentinel
# Sentinel
sentinel_masters:1
sentinel_tilt:0
sentinel_running_scripts:0
sentinel_scripts_queue_length:0
sentinel_simulate_failure_flags:0
master0:name=s20master,status=ok,address=127.0.0.1:6379,slaves=2,sentinels=3


#�鿴�����²���,�ڱ�����ȷ��
master0:name=s20master,status=ok,address=127.0.0.1:6379,slaves=2,sentinels=3






6.ɱ������,�������״̬,�Ƿ���л�

[root@bogon sbredis]# ps -ef | grep redis
root      16538      1  0 22:27 ?        00:00:01 redis-server *:6379
root      16543      1  0 22:27 ?        00:00:01 redis-server *:6380
root      16549      1  0 22:27 ?        00:00:00 redis-server *:6381
root      16765      1  0 22:45 ?        00:00:00 redis-sentinel *:26379 [sentinel]
root      16770      1  0 22:46 ?        00:00:00 redis-sentinel *:26380 [sentinel]
root      16775      1  0 22:46 ?        00:00:00 redis-sentinel *:26381 [sentinel]
root      16832  15646  0 22:51 pts/0    00:00:00 grep --color=auto redis

[root@bogon sbredis]# kill -9 16538

[root@bogon sbredis]# ps -ef | grep redis
root      16543      1  0 22:27 ?        00:00:01 redis-server *:6380
root      16549      1  0 22:27 ?        00:00:01 redis-server *:6381
root      16765      1  0 22:45 ?        00:00:00 redis-sentinel *:26379 [sentinel]
root      16770      1  0 22:46 ?        00:00:00 redis-sentinel *:26380 [sentinel]
root      16775      1  0 22:46 ?        00:00:00 redis-sentinel *:26381 [sentinel]
root      16843  15646  0 22:52 pts/0    00:00:00 grep --color=auto redis




redis-cli -p 6380 info replication
redis-cli -p 6381 info replication



[root@bogon sbredis]# redis-cli -p 6381 info replication
# Replication
role:master               # ��Ϊ����,֤�������ɹ�
connected_slaves:1
slave0:ip=127.0.0.1,port=6380,state=online,offset=93350,lag=0
master_replid:a19874bf7196c339ccde64bc1b6825410b9c9450
master_replid2:c2d32464eed5e8e4219067530abe0b5fe69341fd
master_repl_offset:93350
second_repl_offset:78222
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:15
repl_backlog_histlen:93336

[root@bogon sbredis]# redis-cli -p 6380 info replication
# Replication
role:slave
master_host:127.0.0.1
master_port:6381
master_link_status:up
master_last_io_seconds_ago:0
master_sync_in_progress:0
slave_repl_offset:98082
slave_priority:100
slave_read_only:1
connected_slaves:0
master_replid:a19874bf7196c339ccde64bc1b6825410b9c9450
master_replid2:c2d32464eed5e8e4219067530abe0b5fe69341fd
master_repl_offset:98082
second_repl_offset:78222
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:98082







	
	


	
	
	
���߲��֣���Ⱥ	
	

1.redis-cluster��Ⱥ


redis-cluster��Ⱥ�
1.����׼��,6��redis���ݿ�ڵ�

Ҳ����׼��6�������ļ�,6ƥ��
redis-7000.conf
redis-7001.conf
redis-7002.conf
redis-7003.conf
redis-7004.conf
redis-7005.conf
#ÿ�������ļ�������,�����Ƕ˿ڵĲ�ͬ7000~7005
#��������
port 7000
daemonize yes
dir "/opt/redis/data/7000"
logfile "7000.log"
dbfilename "dump-7000.rdb"
cluster-enabled yes   #������Ⱥģʽ
cluster-config-file nodes-7000.conf����#��Ⱥ�ڲ��������ļ�
cluster-require-full-coverage no��
#redis cluster��Ҫ16384��slot��������ʱ����ܶ����ṩ���񣬻��仰˵��ֻҪ�κ�һ��slot�쳣��ô����cluster�������ṩ���� �����������һ��Ϊno




2.��������6���ڵ�������ļ�
# �ȴ���6�������ļ���
[root@bogon s20cluster-redis]# mkdir -p /opt/redis/data/{7000,7001,7002,7003,7004,7005}

# ��opt�½��ļ���20cluster-redis   �ڴ���6�������ļ� 
[root@bogon opt]# mkdir s20cluster-redis
[root@bogon opt]# cd s20cluster-redis/
[root@bogon s20cluster-redis]# touch redis-7000.conf

# ��д����������Ϣ
[root@bogon s20cluster-redis]# vim redis-7000.conf 
port 7000
daemonize yes
dir "/opt/redis/data/7000"
logfile "7000.log"
dbfilename "dump-7000.rdb"
cluster-enabled yes
cluster-config-file nodes-7000.conf
cluster-require-full-coverage no



# ���ٴ��������ļ�
[root@bogon s20cluster-redis]# sed "s/7000/7001/g" redis-7000.conf > redis-7001.conf 
[root@bogon s20cluster-redis]# sed "s/7000/7002/g" redis-7000.conf > redis-7002.conf
[root@bogon s20cluster-redis]# sed "s/7000/7003/g" redis-7000.conf > redis-7003.conf 
[root@bogon s20cluster-redis]# sed "s/7000/7004/g" redis-7000.conf > redis-7004.conf
[root@bogon s20cluster-redis]# sed "s/7000/7005/g" redis-7000.conf > redis-7005.conf
 
# �鿴�����ļ���û�����óɹ�
[root@bogon s20cluster-redis]# cat redis-7005.conf 

port 7005
daemonize yes
dir "/opt/redis/data/7005"
logfile "7005.log"
dbfilename "dump-7005.rdb"
cluster-enabled yes
cluster-config-file nodes-7005.conf
cluster-require-full-coverage no


 
 
 
 
3.����6��redis�ڵ�(׼������6ƥ��)
[root@bogon s20cluster-redis]# redis-server redis-7000.conf 
[root@bogon s20cluster-redis]# redis-server redis-7001.conf 
[root@bogon s20cluster-redis]# redis-server redis-7002.conf 
[root@bogon s20cluster-redis]# redis-server redis-7003.conf 
[root@bogon s20cluster-redis]# redis-server redis-7004.conf 
[root@bogon s20cluster-redis]# redis-server redis-7005.conf
[root@bogon s20cluster-redis]# !ps
ps -ef | grep redis
root      35082      1  0 15:31 ?        00:00:00 redis-server *:7000 [cluster]
root      35087      1  0 15:31 ?        00:00:00 redis-server *:7001 [cluster]
root      35092      1  0 15:31 ?        00:00:00 redis-server *:7002 [cluster]
root      35097      1  0 15:31 ?        00:00:00 redis-server *:7003 [cluster]
root      35102      1  0 15:32 ?        00:00:00 redis-server *:7004 [cluster]
root      35107      1  0 15:32 ?        00:00:00 redis-server *:7005 [cluster]
root      35112  17487  0 15:32 pts/5    00:00:00 grep --color=auto redis



 
4.���׼������,�����λ,��ʼ��������,�鿴��������
����redis-cluster�ļ�Ⱥ����,�Լ�����redis��slot��λ,����ruby���ԵĽű������Զ�����




1.����ruby�Ľ�����
	wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz

2.��ѹ��ruby��Դ���
tar -zxvf ruby-2.3.1.tar.gz
	
3.����ruby��Դ���Ŀ¼,����������
[root@bogon opt]# cd ruby-2.3.1/
[root@bogon ruby-2.3.1]# ./configure --prefix=/opt/ruby231/
[root@bogon ruby-2.3.1]# make && make install





4.����ruby�Ļ�������
vim /etc/profile 
д��PATH=""

[root@bogon opt]# cd ruby231/
[root@bogon ruby231]# ls
bin  include  lib  share

[root@bogon ruby231]# cd bin/
[root@bogon bin]# ls
erb  gem  irb  rake  rdoc  ri  ruby

[root@bogon bin]# pwd
/opt/ruby231/bin

[root@bogon bin]# vim /etc/profile
PATH="/opt/python36/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/opt/node-v8.6.0-linux-x64/bin:/opt/ruby231/bin"


# ��ȡ���/etc/profile
source /etc/profile

[root@bogon bin]# ruby -v
ruby 2.3.1p112 (2016-04-26 revision 54768) [x86_64-linux]



5.����ruby����redis��ģ��
wget http://rubygems.org/downloads/redis-3.3.0.gem

#��װruby����redis��ģ��
gem install -l redis-3.3.0.gem

# �������
[root@bogon bin]# cd /opt/s20cluster-redis/

[root@bogon s20cluster-redis]# ls
redis-7000.conf  redis-7001.conf  redis-7002.conf  redis-7003.conf  redis-7004.conf  redis-7005.conf

[root@bogon s20cluster-redis]# wget http://rubygems.org/downloads/redis-3.3.0.gem

[root@bogon s20cluster-redis]# ls
redis-3.3.0.gem  redis-7000.conf  redis-7001.conf  redis-7002.conf  redis-7003.conf  redis-7004.conf  redis-7005.conf

[root@bogon s20cluster-redis]# gem install -l redis-3.3.0.gem
Successfully installed redis-3.3.0
Parsing documentation for redis-3.3.0
Installing ri documentation for redis-3.3.0
Done installing documentation for redis after 0 seconds
1 gem installed



6.һ������redis��Ⱥ�Ĳ�λ


.rb  ruby���ԵĽű���׺
.py  python..
.php  php
.c  c
.java   java
.sh     linux��shell�������Ľű�


#����һ���������ľ���·��
[root@bogon s20cluster-redis]# find  / -name redis-trib.rb
/opt/redis-4.0.10/src/redis-trib.rb


#������� 1 ����,ÿ��redis����,ֻ��һ��redis�ӿ� 
/opt/redis-4.0.10/src/redis-trib.rb create --replicas 1 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005


[root@bogon s20cluster-redis]# /opt/redis-4.0.10/src/redis-trib.rb create --replicas 1 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005
>>> Creating cluster
>>> Performing hash slots allocation on 6 nodes...
Using 3 masters:
127.0.0.1:7000
127.0.0.1:7001
127.0.0.1:7002
Adding replica 127.0.0.1:7004 to 127.0.0.1:7000
Adding replica 127.0.0.1:7005 to 127.0.0.1:7001
Adding replica 127.0.0.1:7003 to 127.0.0.1:7002
>>> Trying to optimize slaves allocation for anti-affinity
[WARNING] Some slaves are in the same host as their master

# ����
M: 0d4e036c2ce7ec413fb238211f0b05b90536601c 127.0.0.1:7000
   slots:0-5460 (5461 slots) master
M: 847cff38f4e7bb07bc34025217aaa5a4fea9ef28 127.0.0.1:7001  
   slots:5461-10922 (5462 slots) master
M: a6852d9ffa6fde5feacb242724878f8b42ec4780 127.0.0.1:7002
   slots:10923-16383 (5461 slots) master
   
# �ӿ�   
S: c14968506221967663046f726e2b52cf56a4fcf2 127.0.0.1:7003
   replicates a6852d9ffa6fde5feacb242724878f8b42ec4780
S: f809153f38462476ce562923bdeca9e69d85185a 127.0.0.1:7004
   replicates 0d4e036c2ce7ec413fb238211f0b05b90536601c
S: 9e95d9a3ffc2aabefdc0b61ec6c18be09b73c702 127.0.0.1:7005
   replicates 847cff38f4e7bb07bc34025217aaa5a4fea9ef28


Can I set the above configuration? (type 'yes' to accept): yes
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join......
>>> Performing Cluster Check (using node 127.0.0.1:7000)
M: 0d4e036c2ce7ec413fb238211f0b05b90536601c 127.0.0.1:7000
   slots:0-5460 (5461 slots) master
   1 additional replica(s)
S: f809153f38462476ce562923bdeca9e69d85185a 127.0.0.1:7004
   slots: (0 slots) slave
   replicates 0d4e036c2ce7ec413fb238211f0b05b90536601c
S: c14968506221967663046f726e2b52cf56a4fcf2 127.0.0.1:7003
   slots: (0 slots) slave
   replicates a6852d9ffa6fde5feacb242724878f8b42ec4780
S: 9e95d9a3ffc2aabefdc0b61ec6c18be09b73c702 127.0.0.1:7005
   slots: (0 slots) slave
   replicates 847cff38f4e7bb07bc34025217aaa5a4fea9ef28
   
M: 847cff38f4e7bb07bc34025217aaa5a4fea9ef28 127.0.0.1:7001
   slots:5461-10922 (5462 slots) master
   1 additional replica(s)
M: a6852d9ffa6fde5feacb242724878f8b42ec4780 127.0.0.1:7002
   slots:10923-16383 (5461 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.




# Adding replica 127.0.0.1:7004 to 127.0.0.1:7000
# Adding replica 127.0.0.1:7005 to 127.0.0.1:7001
# Adding replica 127.0.0.1:7003 to 127.0.0.1:7002
# 7000 �� 7004 ������    ������ֵ�������
[root@bogon s20cluster-redis]# redis-cli -c  -p 7004
127.0.0.1:7004> info replication
# Replication
role:slave
master_host:127.0.0.1
master_port:7000
master_link_status:up
master_last_io_seconds_ago:3
master_sync_in_progress:0
slave_repl_offset:700
slave_priority:100
slave_read_only:1
connected_slaves:0
master_replid:674f7f850e8cf3e4c19700e3504de8698dba51e6
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:700
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:700




7.�����˼�Ⱥ״̬���ܺ�,��¼���ݿ�,�鿴����д������


[root@bogon s20cluster-redis]# /opt/redis-4.0.10/src/redis-trib.rb add-node --slave 127.0.0.1:7003  127.0.0.1:7000
>>> Adding node 127.0.0.1:7003 to cluster 127.0.0.1:7000
>>> Performing Cluster Check (using node 127.0.0.1:7000)
M: 0d4e036c2ce7ec413fb238211f0b05b90536601c 127.0.0.1:7000
   slots:0-5460 (5461 slots) master
   1 additional replica(s)
S: f809153f38462476ce562923bdeca9e69d85185a 127.0.0.1:7004
   slots: (0 slots) slave
   replicates 0d4e036c2ce7ec413fb238211f0b05b90536601c
S: c14968506221967663046f726e2b52cf56a4fcf2 127.0.0.1:7003
   slots: (0 slots) slave
   replicates a6852d9ffa6fde5feacb242724878f8b42ec4780
S: 9e95d9a3ffc2aabefdc0b61ec6c18be09b73c702 127.0.0.1:7005
   slots: (0 slots) slave
   replicates 847cff38f4e7bb07bc34025217aaa5a4fea9ef28
M: 847cff38f4e7bb07bc34025217aaa5a4fea9ef28 127.0.0.1:7001
   slots:5461-10922 (5462 slots) master
   1 additional replica(s)
M: a6852d9ffa6fde5feacb242724878f8b42ec4780 127.0.0.1:7002
   slots:10923-16383 (5461 slots) master
   1 additional replica(s)
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
Automatically selected master 127.0.0.1:7000
[ERR] Node 127.0.0.1:7003 is not empty. Either the node already knows other nodes (check with CLUSTER NODES) or contains some key in database 0.




����д�뼯Ⱥ���ݣ���¼��Ⱥ����ʹ��redis-cli -c -p 7000�������-c����

[root@bogon s20cluster-redis]# redis-cli -p 7000
127.0.0.1:7000>

# ��Ҫ�� -c ���� �������ݿ� 
[root@bogon s20cluster-redis]# redis-cli -c  -p 7000

# ��7000����һ��ֵ ��ֱ������7001
127.0.0.1:7000> set name ivan
-> Redirected to slot [5798] located at 127.0.0.1:7001
OK

# �� 7001 ����ȡ��ֵ
127.0.0.1:7001> get name
"ivan"

# ���� ��¼ 7000 getȡֵ ��ֱ������7001 ȡ��ֵ
[root@bogon s20cluster-redis]# redis-cli -c  -p 7000
127.0.0.1:7000> get name
-> Redirected to slot [5798] located at 127.0.0.1:7001
"ivan"
127.0.0.1:7001> keys *
1) "name"

# 7001 �� 7005 ������
# ��¼ 7005 �鿴����7001 ���õ�ֵ
[root@bogon s20cluster-redis]# redis-cli -c  -p 7005
127.0.0.1:7005> keys *
1) "name"

127.0.0.1:7005> set age 18
-> Redirected to slot [741] located at 127.0.0.1:7000
OK
# �� 7005 ����ֵ ������7000 
# ����ֵ�Ĳ�ͬ����䵽��ͬ��������
127.0.0.1:7000> keys *
1) "age"

# �������-c������¼ д�����ݻᱨ��
[root@bogon s20cluster-redis]# redis-cli  -p 7005
127.0.0.1:7005> set age1 20
(error) MOVED 9008 127.0.0.1:7001



# ����ҵ� �ӿ��������
# �Դ��ڱ�


# �Դ��ڱ� ���²��Գ�û�κ���˼
8.��ֹredis-cluster���ڵ����,���Դ��� redis-cluster +  redis-sentinel ,���ڱ�������ڵ�״̬,�����ڵ�崻�,�Զ��л��ӽڵ�Ϊ�µ�����

	1.redis-sentinel���÷�ʽ����,����������ڵ�7000  7001  7002
		port 27379
		dir "/var/redis/data"
		logfile "26379.log"
		sentinel monitor master1 127.0.0.1 7000 2  
		sentinel monitor master2 127.0.0.1 7001 2  
		sentinel monitor master3 127.0.0.1 7002 2  

		sentinel down-after-milliseconds master1 30000  
		sentinel down-after-milliseconds master2 30000  
		sentinel down-after-milliseconds master3 30000  

		sentinel parallel-syncs master1 1  
		sentinel parallel-syncs master2 1  
		sentinel parallel-syncs master3 1  

		sentinel failover-timeout master1 180000  
		sentinel failover-timeout master2 180000  
		sentinel failover-timeout master3 180000  

	2.�����ڱ�,���cluster�����ڵ�
	redis-sentinel redis-26379.conf
	
	3.ɱ��redis-cluster�����ڵ�,�鿴�ӽڵ�״̬(�Ƿ��Զ�����),�������ж���ӽڵ�,��֤���ݰ�ȫ



	




