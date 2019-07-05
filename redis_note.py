redis学习

第一部分内容：

一：
mysql 关系型数据库
非关系型数据库 redis    mongodb
nosql  不仅仅是sql

数据持久化,可以将数据存储到磁盘上,以文件形式存储

redis是内存性的数据库,读写是非常快的
缺点是:断电释放内存数据,redis数据丢失,redis进程挂掉,数据丢失,redis提供了持久化机制

which是在PATH里找
[root@bogon src]# echo $PATH
/opt/python36/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/opt/node-v8.6.0-linux-x64/bin:/root/bin


[root@bogon ~]# echo $PATH
/opt/python36/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/opt/node-v8.6.0-linux-x64/bin:/root/bin


redis的安装方式
1.yum  install  redis -y
rpm

源码编译(在选择编译的时候,注意删掉之前的yum安装的)
1.yum remove redis -y 

2.下载redis的源代码包
wget http://download.redis.io/releases/redis-4.0.10.tar.gz

3.解压缩源码包
编译三部曲:
#(此redis压缩包,已经提供好了makefile,只需要执行,编译的第二,第三曲)
# 因为该文件里有makefile文件  所以不用执行 ./confiure

2.执行gcc的make指令,执行makefile文件

make 
3.开始安装
make install

# 重新登陆一下会发现已经加载出来PATH
[root@bogon ~]# which redis-server
/usr/local/bin/redis-server

# which是在PATH里找
[root@bogon src]# echo $PATH
/opt/python36/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin:/opt/node-v8.6.0-linux-x64/bin:/root/bin

  

4.会安装在当前的源码包中的src目录,且帮你配置好了PATH变量
通过redis-加上tab补全查看所有命令

redis-benchmark  redis-check-rdb  redis-sentinel   
redis-check-aof  redis-cli        redis-server  


[root@bogon src]# pwd
/opt/redis-4.0.10/src
[root@bogon src]# redis-
redis-benchmark  redis-check-rdb  redis-sentinel   
redis-check-aof  redis-cli        redis-server 






5.制定一个安装可靠的redis数据库
如下功能通过配置文件定义
1.更改端口
2.设置密码
3.开启redis的安全启动模式

默认直接输入redis-server可以启动服务端,默认端口6379,且没有密码
redis-cli登录
[root@bogon ~]# redis-cli
127.0.0.1:6379> ping
PONG


[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING  Makefile   redis.conf       runtest-sentinel  tests
BUGS             deps     MANIFESTO  runtest          sentinel.conf     utils
CONTRIBUTING     INSTALL  README.md  runtest-cluster  src

[root@bogon redis-4.0.10]# vim redis.conf 
[root@bogon redis-4.0.10]# grep -v "^#" redis.conf  | grep  -v  "^$0"  >  ./s20redis.conf
# 把redis.conf有用的信息拷贝到新的s20redis.conf里

# 查看新的文件夹是否存在了
[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING  Makefile   redis.conf       runtest-sentinel  src
BUGS             deps     MANIFESTO  runtest          s20redis.conf     tests
CONTRIBUTING     INSTALL  README.md  runtest-cluster  sentinel.conf     utils
[root@bogon redis-4.0.10]# vim s20redis.conf 



[root@bogon ~]# cd /opt/redis-4.0.10/
[root@bogon redis-4.0.10]# vim s20redis.conf

#实际上直接touch一个 s20redis.conf  把配置信息直接复制粘贴过去
# vim s20redis.conf 内容如下
bind 192.168.190.11
protected-mode yes
port 6380
daemonize yes
pidfile /var/run/redis_6379.pid 
loglevel notice 
requirepass 123




redis.conf 内容如下,有多少参数,就有多少功能,

bind 192.168.16.142    	#绑定redis启动的地址
protected-mode yes		#开启redis的安全模式,必须输入密码才可以远程登录
port 6380			 	#指定redis的端口  
daemonize yes			#让redis以守护进程方式在后台运行,不占用窗口
pidfile /var/run/redis_6379.pid   #记录redis的进程id号的文件
loglevel notice    		#日志运行等级 .严重级别,警告级别,debug调试界别.....logging
requirepass haohaio     #设置redis的密码,是 haohaio


# 配置完成以后
指定配置文件的启动方式
redis-server  s20redis.conf  

[root@bogon redis-4.0.10]# redis-server  s20redis.conf  
11085:C 04 Jul 15:33:45.087 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
11085:C 04 Jul 15:33:45.087 # Redis version=4.0.10, bits=64, commit=00000000, modified=0, pid=11085, just started
11085:C 04 Jul 15:33:45.087 # Configuration loaded


# 显示配置的信息已经加载起来
# 如果没有显示加载 则需要重新退出会话 重新登录 配置一下s20redis.conf  保存退出
# 然后 redis-server  s20redis.conf  
[root@bogon ~]# netstat -tunlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
     
tcp        0      0 192.168.190.11:6380     0.0.0.0:*               LISTEN      11268/redis-server 




#此时登录redis必须加上参数了,并且登录了之后,必须输入密码才可以使用 
redis-cli -p 6380 -h 192.168.16.142

redis-cli -p 6380 -h 192.168.190.11

# 注意 启动时候在哪个目录都可以
[root@bogon ~]# redis-cli -p 6380 -h 192.168.190.11
192.168.190.11:6380> ping
(error) NOAUTH Authentication required.
# 并且登录了之后,必须输入密码才可以使用 
192.168.190.11:6380> auth 123
OK
192.168.190.11:6380> ping
PONG







二：

学习redis的数据类型使用

1.常用redis的公共命令
keys *         查看所有key
type key      查看key类型
expire key seconds    过期时间
ttl key     查看key过期剩余时间        -2表示key已经不存在了
persist     取消key的过期时间   -1表示key存在，没有过期时间

exists key     判断key存在    存在返回1    否则0
del keys     删除key    可以删除多个
dbsize         计算key的数量




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
192.168.190.11:6380> PERSIST name   # 阻止过期
(integer) 1
192.168.190.11:6380> ttl name
(integer) -1						# 回复为-1 是没有过期时间
192.168.190.11:6380> get name
"xiaobai"



192.168.190.11:6380> EXISTS age
(integer) 0
192.168.190.11:6380> set age 18
OK
192.168.190.11:6380> DBSIZE
(integer) 2						#name  age 两个key值
192.168.190.11:6380> EXISTS age
(integer) 1
192.168.190.11:6380> EXISTS name
(integer) 1


192.168.190.11:6380> del name age 
(integer) 2
192.168.190.11:6380> keys *
(empty list or set)







2.学习string类型的操作
set 　　设置key
get   获取key
append  追加string
mset   设置多个键值对
mget   获取多个键值对
del  删除key
incr  递增+1
decr  递减-1

list类型,双向队列

dic1={
	'k1':{"k2":"v2"}
}


dic1[k1][k2]


# string

# type name
192.168.190.11:6380> type name
none
# 不存在值为none


# set name
192.168.190.11:6380> set name ivan
OK
192.168.190.11:6380> type name
string
#通过set设置的就是string类型的key -value


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



# INCR  用作排行榜 
# 每次加1 转为字符串
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
# 列表的名字不能与上面的重复
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

#1   sadd/srem   添加/删除 元素
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


#2   sismember   判断是否为set的一个元素
# 判断在不在集合里
192.168.190.11:6380> SISMEMBER home xiaohai
(integer) 0
192.168.190.11:6380> SISMEMBER home2 xiaohai
(integer) 1



#3   sdiff             返回一个集合和其他集合的差异
# 查看两个集合的差异
# 显示写在前面的差异
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
# 因为home 比 home2 多一个ivan




#4    sinter           返回几个集合的交集

192.168.190.11:6380> SINTER home home2
1) "sail"

# sunion          返回几个集合的并集
192.168.190.11:6380> SUNION home home2
1) "xiaohai"
2) "ivan"
3) "xiaobai"
4) "sail"



# 哈希数据结构



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
















第二部分内容：：
#redis的发布订阅
#QQ群  
详细命令看博客


[root@bogon ~]# redis-cli -p 6380 -h 192.168.190.11
192.168.190.11:6380> auth 123
OK
192.168.190.11:6380> PUBLISH python2 hello
(integer) 2
192.168.190.11:6380> PUBLISH python22 hello
(integer) 1


截图


.












第三部分内容：


# 问题：
# 断掉进程 查看之前的数据为空
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
# 进程断线 数据丢失


解决问题的方式：

#redis的持久化机制
分为aof和rdb两种,具体看博客





一： rdb

环境准备

[root@bogon redis-4.0.10]# ps -ef | grep redis
root      12778      1  0 17:34 ?        00:00:00 redis-server 192.168.190.11:6380
root      12847  11284  0 17:41 pts/3    00:00:00 grep --color=auto redis
[root@bogon redis-4.0.10]# kill -9 12778
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      12858  11284  0 17:41 pts/3    00:00:00 grep --color=auto redis

[root@bogon redis-4.0.10]# touch s20rdb.conf


[root@bogon redis-4.0.10]# vim s20rdb.conf 
1.配置一个rdb的redis服务端
	s20rdb.conf内容如下
	
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
dbfilename  dbmp.rdb 
bind  127.0.0.1
save 900 1       
save 300 10
save 60  10000

# 参数详解
"""
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379              #定义持久化文件存储位置
dbfilename  dbmp.rdb        #rdb持久化文件
bind 10.0.0.10  127.0.0.1    #redis绑定地址
requirepass redhat            #redis登录密码
save 900 1                    #rdb机制 每900秒 有1个修改记录
save 300 10                    #每300秒        10个修改记录
save 60  10000                #每60秒内        10000修改记录

# save 30  1    #每30秒自动save一次
# 这个是可以是自己更改的
# 注意不能改为1秒一次save  太占用资源了 

"""




		 		
		
2.基于这个文件启动redis,支持rdb的数据库
redis-server s20rdb.conf 

# 1
[root@bogon redis-4.0.10]# redis-server s20rdb.conf

*** FATAL CONFIG FILE ERROR ***
Reading the configuration file, at line 4
>>> 'logfile /data/6379/redis.log'
Can't open the log file: No such file or directory


# 2
# 需要创建一个 /data/6379
[root@bogon redis-4.0.10]# mkdir -p /data/6379
[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING   INSTALL    README.md   runtest-cluster   s20redis.conf  tests
BUGS             deps      Makefile   redis.conf  runtest-sentinel  sentinel.conf  utils
CONTRIBUTING     dump.rdb  MANIFESTO  runtest     s20rdb.conf       src

[root@bogon redis-4.0.10]# redis-server s20rdb.conf 
# 启动成功 现在就不会报错了

# 3
[root@bogon redis-4.0.10]# redis-server s20rdb.conf 
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      12932      1  0 17:46 ?        00:00:00 redis-server 127.0.0.1:6379
root      12962  11284  0 17:49 pts/3    00:00:00 grep --color=auto redis

# 此时的进程就是修改文件里的 6379

[root@bogon redis-4.0.10]# cd /data/6379/
[root@bogon 6379]# ls
redis.log




3.登录redis设置key,然后手动触发save,生成rdb数据文件dbmp.rdb 


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
# 只有save了 才会生成dbmp.rdb 文件


# 断掉进程 查看数据

[root@bogon 6379]# pkill -9 redis
[root@bogon 6379]# ps -ef | grep redis
root      13149  11284  0 18:03 pts/3    00:00:00 grep --color=auto redis

[root@bogon 6379]# redis-server /opt/redis-4.0.10/s20rdb.conf 
[root@bogon 6379]# redis-cli 
127.0.0.1:6379> keys *
1) "name"
2) "age"
# 查看 断线了进程 数据也在

# 查看 dbmp.rdb文件里具体内容 
127.0.0.1:6379> 
[root@bogon 6379]# ls
dbmp.rdb  redis.log
[root@bogon 6379]# vim dbmp.rdb 

REDIS0008ú      redis-ver^F4.0.10ú
redis-bitsà@ú^Ectime???^]]ú^Hused-mem?^X^A^L^@ú^Laof-preambleà^@t^@?^B^@^@^Cageà^R^@^Dname^Divan??éE^D·¤X?
~     






二：aof



# 1 准备：
[root@bogon 6379]# cd /opt/redis-4.0.10/
[root@bogon redis-4.0.10]# touch s20aof.conf
[root@bogon redis-4.0.10]# ls
00-RELEASENOTES  COPYING   INSTALL    README.md   runtest-cluster   s20rdb.conf    src
BUGS             deps      Makefile   redis.conf  runtest-sentinel  s20redis.conf  tests
CONTRIBUTING     dump.rdb  MANIFESTO  runtest     s20aof.conf       sentinel.conf  utils
[root@bogon redis-4.0.10]# vim s20aof.conf 


# 2 配置s20aof.conf 
[root@bogon redis-4.0.10]# vim s20aof.conf 

#2 s20aof.conf 配置如下
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
# 为了不影响实践效果 断掉之前的进程和 6379里所有的文件

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


# 4 启动配置文件

[root@bogon 6379]# cd -      # 回到上一次的目录 启动配置文件
/opt/redis-4.0.10
[root@bogon redis-4.0.10]# redis-server s20aof.conf 
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      13437      1  0 18:29 ?        00:00:00 redis-server *:6379
root      13442  11284  0 18:29 pts/3    00:00:00 grep --color=auto redis

# 回到6379 查看启动配置文件 自动加载出来的文件
[root@bogon redis-4.0.10]# cd -
/data/6379
[root@bogon 6379]# ls
appendonly.aof  redis.log


# 5  实验开始
# 
# 窗口1
[root@bogon ~]# redis-cli
127.0.0.1:6379> auth 123
(error) ERR Client sent AUTH, but no password is set
127.0.0.1:6379> keys *
(empty list or set)

127.0.0.1:6379> set age 18
OK


# 窗口2
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



# 6  查看数据
# 查看到数据还在
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


# 测试优先级

aof 的级别比 rdb高













第四部分内容：


#在不重启redis的情况下,切换rdb中的数据,到aof中的操作
环境准备

1.配置一个rdb的redis服务端
	s20rdb.conf内容如下
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


# 删除6379下的文件
[root@bogon redis-4.0.10]# cd -
/data/6379
[root@bogon 6379]# ls
appendonly.aof  redis.log

[root@bogon 6379]# rm -rf *
[root@bogon 6379]# ls
#查看文件已经被删除

		
			
		
		
2.基于这个文件启动redis,支持rdb的数据库
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
# 手动保存
# 查看已经有文件
[root@bogon redis-4.0.10]# ls /data/6379/
dbmp.rdb  redis.log


3.登录redis设置key,然后手动触发save,生成rdb数据文件


4.通过登录redis,两条命令,切换为aof持久化方式

[root@bogon redis-4.0.10]# redis-cli
127.0.0.1:6379>  CONFIG set appendonly yes 
OK
127.0.0.1:6379> CONFIG SET save ""
OK


[root@bogon redis-4.0.10]# ls /data/6379/
appendonly.aof  dbmp.rdb  redis.log

# 出现了appendonly.aof
# 查看数据过来了
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




5.第4步的操作,仅仅是临时生效,还得修改配置文件,保证下次重启,也得用aof进行持久化



# 原来的配置文件信息

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

# 修改完的配置文件信息
daemonize yes
port 6379
logfile /data/6379/redis.log
dir /data/6379
bind  127.0.0.1
appendonly yes
appendfsync  always


[root@bogon redis-4.0.10]# vim s20rdb.conf 
# 配置完文件信息
# 查看数据信息
[root@bogon redis-4.0.10]# redis-cli
127.0.0.1:6379> keys *
1) "addr"
2) "age"
3) "name"
127.0.0.1:6379> 

# 开始 断掉进程 重新启动配置文件
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

# 查看appendonly.aof 里的信息
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


#在开个窗口 登录redis

[root@bogon ~]# redis-cli
127.0.0.1:6379> 
127.0.0.1:6379> set name123  ican
OK


# 动态的查看到 数据 变化了 记录到了appendonly.aof 
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






6. 扩展知识 redis事件机制

save 900 1：表示900 秒内如果至少有 1 个 key 的值变化，则保存
save 300 10：表示300 秒内如果至少有 10 个 key 的值变化，则保存
save 60 10000：表示60 秒内如果至少有 10000 个 key 的值变化，则保存

redis是单线程的,由c编写 








daemonize yes
port 6379
logfile "/data/6379/redis.log"
dir /data/6379
dbfilename dump.rdb
bind 127.0.0.1
save 30 1




第五部分内容：

       
#redis的主从复制



一： 详情了解
1.redis和mysql都是支持多实例功能,基于配置文件区分,就是一个数据库单独的实例



# 具体操作
# 原本的myredis.conf文件信息
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

# 对myredis.conf文件进行替换  替换的结果写入到 6380-redis.conf 中

# 查看6380-redis.conf的信息
[root@bogon redis-4.0.10]# cat 6380-redis.conf 
daemonize yes
port 6380
logfile "/data/6380/redis.log"
dir /data/6380
dbfilename dump.rdb
bind 127.0.0.1
save 30 1






2.分别启动2个redis实例
 1061  redis-server redis-6379.conf 
 1062  redis-server redis-6380.conf 

 
# 创建一个6380的文件夹
[root@bogon redis-4.0.10]# mkdir -p /data/6380

#查看进程信息 现在一个redis进程也没有
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      14796  11284  0 20:22 pts/3    00:00:00 grep --color=auto redis

# 运行 myredis.conf  127.0.0.1:6379
[root@bogon redis-4.0.10]# redis-server myredis.conf 
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      14800      1  0 20:22 ?        00:00:00 redis-server 127.0.0.1:6379
root      14805  11284  0 20:22 pts/3    00:00:00 grep --color=auto redis

# 运行 6380-redis.conf  127.0.0.1:6380
[root@bogon redis-4.0.10]# redis-server 6380-redis.conf 
[root@bogon redis-4.0.10]# ps -ef | grep redis
root      14800      1  0 20:22 ?        00:00:00 redis-server 127.0.0.1:6379
root      14817      1  0 20:22 ?        00:00:00 redis-server 127.0.0.1:6380
root      14822  11284  0 20:22 pts/3    00:00:00 grep --color=auto redis


# 现在是两个进程 进程之间是隔离的


# 6379的 数据库信息
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


# 6380的 数据库信息
[root@bogon ~]# redis-cli -p 6380
127.0.0.1:6380> keys *
(empty list or set)
# 此时 6380 是空的


# 基于配置文集在一台机子上运行多个数据库 
# 两个数据库不干扰  可以给不同的项目用






二：开始实践

1 环境准备,一个6379的redis(master),和一个6380的redis(slave)

分别准备2个配置文件,内容如下
redis-6379.conf

port 6379
daemonize yes
pidfile /data/6379/redis.pid
loglevel notice
logfile "/data/6379/redis.log"
dbfilename dump.rdb
dir /data/6379
protected-mode no


redis-6380.conf (从)

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



# 操作详情
# 为了避免干扰 在opt里创建smredis
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



# 6380 里有信息了 直接删除
[root@bogon smredis]# ls /data/6380/redis.log 
/data/6380/redis.log
[root@bogon smredis]# rm -rf /data/6380/*



# 在 smredis 生成 redis-6379.conf  
[root@bogon smredis]# sed 's/6380/6379/g'  redis-6380.conf  >  redis-6379.conf
[root@bogon smredis]# ls
redis-6379.conf  redis-6380.conf
# 现在 smredis 生成了 redis-6379.conf  redis-6380.conf 两个文件



# 杀死进程
[root@bogon smredis]# ps -ef | grep redis
root      14800      1  0 20:22 ?        00:00:01 redis-server 127.0.0.1:6379
root      14817      1  0 20:22 ?        00:00:01 redis-server 127.0.0.1:6380
root      14958  14901  0 20:31 pts/0    00:00:00 redis-cli -p 6380
root      15197  11284  0 20:55 pts/3    00:00:00 grep --color=auto redis
[root@bogon smredis]# pkill -9 redis
[root@bogon smredis]# ps -ef | grep redis
root      15200  11284  0 20:55 pts/3    00:00:00 grep --color=auto redis



# 查看刚才生成的 redis-6379.conf  信息
[root@bogon smredis]# cat redis-6379.conf 
port 6379
daemonize yes
pidfile /data/6379/redis.pid
loglevel notice
logfile "/data/6379/redis.log"
dbfilename dump.rdb
dir /data/6379
protected-mode no



# 清空 /data/6379/* 所有的内容
[root@bogon smredis]# rm -rf /data/6379/*



# 在 redis-6380.conf  文件中  加slaveof
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






2.分别启动2个redis实例
 1061  redis-server redis-6379.conf 
 1062  redis-server redis-6380.conf 

[root@bogon smredis]# redis-server redis-6379.conf 
[root@bogon smredis]# redis-server redis-6380.conf 
[root@bogon smredis]# ps -ef | grep redis
root      15361      1  0 21:01 ?        00:00:01 redis-server *:6379
root      15795      1  0 21:29 ?        00:00:00 redis-server *:6380
root      15801  15646  0 21:29 pts/0    00:00:00 grep --color=auto redis

 
 
 
 
3.登录数据库,查看两人之间的关系

登录6379数据库,输入如下命令
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





6380数据库查看如下关系
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




4.数据读写查看
在6379中是可以读写的

# 窗口1   6379
redis-cli -p 6379  set name5  haoxiangxiake

[root@bogon smredis]# redis-cli -p 6379  set name5  zuoyetaiduo
OK
[root@bogon smredis]# redis-cli
127.0.0.1:6379> keys *
1) "name5"



# 窗口2   6380
redis-cli -p 6380 get name5

[root@bogon ~]# redis-cli -p 6380 get name5
"zuoyetaiduo"
[root@bogon ~]# redis-cli -p 6380  
127.0.0.1:6380> keys *
1) "name5"

127.0.0.1:6380> set name6 buxiangxiezuoye
(error) READONLY You can't write against a read only slave.
# 只能读 不能写




5.主从复制故障恢复

# 在添加一个6381数据库  也是作为6379 的从数据库

# 在/data里创建一个 6381 文件
[root@bogon ~]# cd /data
[root@bogon data]# ls
6379  6380
[root@bogon data]# mkdir 6381
[root@bogon data]# ls
6379  6380  6381



# 创建一个 redis-6381.conf 文件
[root@bogon smredis]# sed 's/6380/6381/g'  redis-6380.conf  >  redis-6381.conf
[root@bogon smredis]# ls
！  redis-6379.conf  redis-6380.conf  redis-6381.conf
# 配置文件信息
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

# 启动 redis-6381.conf
[root@bogon smredis]# redis-server redis-6381.conf 
[root@bogon smredis]# redis-cli -p 6381

127.0.0.1:6381> keys *
1) "name1"
2) "name5"
3) "name2"


# 6379是主库  6380 6381 是从库


从库挂了无所谓
主库挂了得立即恢复主库,或者将从库切换为主库,继续工作

	-.实验步骤
	1.分别启动 6379  6380 6381 三个数据库实例,建立好主从关系
	
	2.杀死6379主库,此时6380 6381 群龙无首
	
	
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



	
	3.选择让6381为新的主库,就要去除6381的从的身份
	redis-cli -p 6381 slaveof  no one 
	#查看此时6381的身份
	redis-cli -p 6381 info replication
	
	[root@bogon smredis]# redis-cli -p 6381 slaveof  no one
	OK
	[root@bogon smredis]# redis-cli -p 6381 info replication
	# Replication
	role:master    		#    此时 6381为主的了
	connected_slaves:0
	master_replid:5b91f338a06af956a1050ca0deb5e3ba48925849
	master_replid2:bd80df540e6a5e4a235d52db0b36184eb8f93b6f
	master_repl_offset:2313
	second_repl_offset:2314
	repl_backlog_active:1
	repl_backlog_size:1048576
	repl_backlog_first_byte_offset:1460
	repl_backlog_histlen:854

	
	
	
	

	4.此时将6380的主人改为6381
	redis-cli -p 6380 slaveof 127.0.0.1 6381

	# 先创建一个数据 ，这样好看出数据的变化
	[root@bogon smredis]# redis-cli -p 6381
	127.0.0.1:6381> set name  zuoyexiebuwanle
	OK

	[root@bogon smredis]# redis-cli -p 6380 slaveof 127.0.0.1 6381
	OK


	[root@bogon smredis]# redis-cli -p 6380 info replication
	# Replication
	role:slave
	master_host:127.0.0.1
	master_port:6381                 # 主库为6381了
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

	
	# 查看到 刚才创建的那一条数据了
	[root@bogon smredis]# redis-cli -p 6380
	127.0.0.1:6380> keys *
	1) "name"
	2) "name5"
	3) "name2"
	4) "name1"





	
	
第六部分内容：	

	
redis的哨兵,自动的主从故障切换
配置步骤

1.环境准备,准备3个redis数据库实例,分别是 6379  6380  6381  
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

# 创建文件
[root@bogon sbredis]# mkdir -p /var/redis/data/{6379,6380,6381}

# 杀死进程
[root@bogon sbredis]# pkill -9 redis
[root@bogon sbredis]# ps -ef | grep redis
root      16528  15646  0 22:26 pts/0    00:00:00 grep --color=auto redis



	
2.分别启动三个redis数据库实例 
[root@bogon sbredis]# redis-server redis-6379.conf 
[root@bogon sbredis]# redis-server redis-6380.conf 
[root@bogon sbredis]# redis-server redis-6381.conf 
[root@bogon sbredis]# ps -ef | grep redis
root      16538      1  0 22:27 ?        00:00:00 redis-server *:6379
root      16543      1  0 22:27 ?        00:00:00 redis-server *:6380
root      16549      1  0 22:27 ?        00:00:00 redis-server *:6381
root      16555  15646  0 22:27 pts/0    00:00:00 grep --color=auto redis



# 查看三个文件的信息  看是否错误

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


# 主从信息 操作完毕




3.准备三个redis-sentinel哨兵的配置文件

redis-sentinel-26379.conf

port 26379  
dir /var/redis/data/26379
logfile "26379.log"

// 当前Sentinel节点监控 127.0.0.1:6379 这个主节点
// 2代表判断主节点失败至少需要2个Sentinel节点节点同意
// mymaster是主节点的别名
sentinel monitor s20master 127.0.0.1   6379  2
// 哨兵检测着 s20master  

//每个Sentinel节点都要定期PING命令来判断Redis数据节点和其余Sentinel节点是否可达，如果超过30000毫秒30s且没有回复，则判定不可达
sentinel down-after-milliseconds s20master 30000

//当Sentinel节点集合对主节点故障判定达成一致时，Sentinel领导者节点会做故障转移操作，选出新的主节点，
原来的从节点会向新的主节点发起复制操作，限制每次向新的主节点发起复制操作的从节点个数为1
sentinel parallel-syncs s20master 1

//故障转移超时时间为180000毫秒
sentinel failover-timeout s20master 180000

//让哨兵在后台运行
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

# daemonize yes 一定要加,让哨兵正在后端运行	
	

	
	
#如下26380和26381的配置文件,仅仅是端口的不同,可以快速生成	
redis-sentinel-26380.conf
redis-sentinel-26381.conf

#生成命令如下
 1119  sed "s/26379/26380/g"  redis-26379.conf > redis-26380.conf
 1121  sed "s/26379/26381/g"  redis-26379.conf > redis-26381.conf

 
[root@bogon sbredis]# sed "s/26379/26380/g"  redis-26379.conf > redis-26380.conf
[root@bogon sbredis]# sed "s/26379/26381/g"  redis-26379.conf > redis-26381.conf
[root@bogon sbredis]# ls
6379.log  redis-26379.conf  redis-26381.conf  redis-6380.conf
6380.log  redis-26380.conf  redis-6379.conf   redis-6381.conf


# 查看一下redis-26380.conf 信息
[root@bogon sbredis]# cat redis-26380.conf 
port 26380  
dir /var/redis/data/26380
logfile "26380.log"
sentinel monitor s20master 127.0.0.1   6379  2
sentinel down-after-milliseconds s20master 30000
sentinel parallel-syncs s20master 1
sentinel failover-timeout s20master 180000
daemonize yes	
 
# daemonize yes 一定要加,让哨兵正在后端运行	

 
# 查看一下redis-26381.conf 信息 
[root@bogon sbredis]# cat redis-26381.conf 
port 26381  
dir /var/redis/data/26381
logfile "26381.log"
sentinel monitor s20master 127.0.0.1   6379  2
sentinel down-after-milliseconds s20master 30000
sentinel parallel-syncs s20master 1
sentinel failover-timeout s20master 180000
daemonize yes	

# daemonize yes 一定要加,让哨兵正在后端运行	



4.分别运行三个哨兵进程
(保证sentinel的配置正确,否则,你在启动报错后,配置文件的内容发发生变化,这是个坑!!!!)

#创建哨兵的数据文件夹
[root@bogon sbredis]# mkdir -p /var/redis/data/26379
[root@bogon sbredis]# mkdir -p /var/redis/data/26380
[root@bogon sbredis]# mkdir -p /var/redis/data/26381
 
 
 
(保证sentinel的配置正确,否则,你在启动报错后,配置文件的内容发发生变化,这是个坑!!!!) 
(保证sentinel的配置正确,否则,你在启动报错后,配置文件的内容发发生变化,这是个坑!!!!) 
(保证sentinel的配置正确,否则,你在启动报错后,配置文件的内容发发生变化,这是个坑!!!!) 

# daemonize yes 一定要加,让哨兵正在后端运行	
# daemonize yes 一定要加,让哨兵正在后端运行	
# daemonize yes 一定要加,让哨兵正在后端运行	

 
 #分别启动三个哨兵
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


# 三个哨兵 和 三个数据库 已经启动




 
5.检查redis的哨兵状态
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


#查看到如下参数,哨兵就正确了
master0:name=s20master,status=ok,address=127.0.0.1:6379,slaves=2,sentinels=3






6.杀死主库,检查主从状态,是否会切换

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
role:master               # 变为主的,证明操作成功
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







	
	


	
	
	
第七部分：集群	
	

1.redis-cluster集群


redis-cluster集群搭建
1.环境准备,6个redis数据库节点

也就是准备6个配置文件,6匹马
redis-7000.conf
redis-7001.conf
redis-7002.conf
redis-7003.conf
redis-7004.conf
redis-7005.conf
#每个配置文件的内容,仅仅是端口的不同7000~7005
#内容如下
port 7000
daemonize yes
dir "/opt/redis/data/7000"
logfile "7000.log"
dbfilename "dump-7000.rdb"
cluster-enabled yes   #开启集群模式
cluster-config-file nodes-7000.conf　　#集群内部的配置文件
cluster-require-full-coverage no　
#redis cluster需要16384个slot都正常的时候才能对外提供服务，换句话说，只要任何一个slot异常那么整个cluster不对外提供服务。 因此生产环境一般为no




2.快速生成6个节点的配置文件
# 先创建6个数据文件夹
[root@bogon s20cluster-redis]# mkdir -p /opt/redis/data/{7000,7001,7002,7003,7004,7005}

# 在opt新建文件夹20cluster-redis   在创建6个配置文件 
[root@bogon opt]# mkdir s20cluster-redis
[root@bogon opt]# cd s20cluster-redis/
[root@bogon s20cluster-redis]# touch redis-7000.conf

# 填写如下配置信息
[root@bogon s20cluster-redis]# vim redis-7000.conf 
port 7000
daemonize yes
dir "/opt/redis/data/7000"
logfile "7000.log"
dbfilename "dump-7000.rdb"
cluster-enabled yes
cluster-config-file nodes-7000.conf
cluster-require-full-coverage no



# 快速创建配置文件
[root@bogon s20cluster-redis]# sed "s/7000/7001/g" redis-7000.conf > redis-7001.conf 
[root@bogon s20cluster-redis]# sed "s/7000/7002/g" redis-7000.conf > redis-7002.conf
[root@bogon s20cluster-redis]# sed "s/7000/7003/g" redis-7000.conf > redis-7003.conf 
[root@bogon s20cluster-redis]# sed "s/7000/7004/g" redis-7000.conf > redis-7004.conf
[root@bogon s20cluster-redis]# sed "s/7000/7005/g" redis-7000.conf > redis-7005.conf
 
# 查看其中文件有没有配置成功
[root@bogon s20cluster-redis]# cat redis-7005.conf 

port 7005
daemonize yes
dir "/opt/redis/data/7005"
logfile "7005.log"
dbfilename "dump-7005.rdb"
cluster-enabled yes
cluster-config-file nodes-7005.conf
cluster-require-full-coverage no


 
 
 
 
3.启动6个redis节点(准备好了6匹马)
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



 
4.马儿准备好了,分配槽位,开始放入数据,查看数据流向
开启redis-cluster的集群功能,以及分配redis的slot槽位,基于ruby语言的脚本工具自动分配




1.下载ruby的解释器
	wget https://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz

2.解压缩ruby的源码包
tar -zxvf ruby-2.3.1.tar.gz
	
3.进入ruby的源码包目录,编译三部曲
[root@bogon opt]# cd ruby-2.3.1/
[root@bogon ruby-2.3.1]# ./configure --prefix=/opt/ruby231/
[root@bogon ruby-2.3.1]# make && make install





4.配置ruby的环境变量
vim /etc/profile 
写入PATH=""

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


# 读取这个/etc/profile
source /etc/profile

[root@bogon bin]# ruby -v
ruby 2.3.1p112 (2016-04-26 revision 54768) [x86_64-linux]



5.下载ruby操作redis的模块
wget http://rubygems.org/downloads/redis-3.3.0.gem

#安装ruby操作redis的模块
gem install -l redis-3.3.0.gem

# 具体操作
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



6.一键分配redis集群的槽位


.rb  ruby语言的脚本后缀
.py  python..
.php  php
.c  c
.java   java
.sh     linux的shell解释器的脚本


#查找一下这个命令的绝对路径
[root@bogon s20cluster-redis]# find  / -name redis-trib.rb
/opt/redis-4.0.10/src/redis-trib.rb


#这个数字 1 代表,每个redis主库,只有一个redis从库 
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

# 主库
M: 0d4e036c2ce7ec413fb238211f0b05b90536601c 127.0.0.1:7000
   slots:0-5460 (5461 slots) master
M: 847cff38f4e7bb07bc34025217aaa5a4fea9ef28 127.0.0.1:7001  
   slots:5461-10922 (5462 slots) master
M: a6852d9ffa6fde5feacb242724878f8b42ec4780 127.0.0.1:7002
   slots:10923-16383 (5461 slots) master
   
# 从库   
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
# 7000 是 7004 的主库    是随机分的主副库
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




7.开启了集群状态功能后,登录数据库,查看数据写入流向


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




测试写入集群数据，登录集群必须使用redis-cli -c -p 7000必须加上-c参数

[root@bogon s20cluster-redis]# redis-cli -p 7000
127.0.0.1:7000>

# 需要加 -c 参数 进入数据库 
[root@bogon s20cluster-redis]# redis-cli -c  -p 7000

# 在7000设置一个值 会直接跳到7001
127.0.0.1:7000> set name ivan
-> Redirected to slot [5798] located at 127.0.0.1:7001
OK

# 在 7001 才能取到值
127.0.0.1:7001> get name
"ivan"

# 测试 登录 7000 get取值 会直接跳到7001 取到值
[root@bogon s20cluster-redis]# redis-cli -c  -p 7000
127.0.0.1:7000> get name
-> Redirected to slot [5798] located at 127.0.0.1:7001
"ivan"
127.0.0.1:7001> keys *
1) "name"

# 7001 是 7005 的主库
# 登录 7005 查看到有7001 设置的值
[root@bogon s20cluster-redis]# redis-cli -c  -p 7005
127.0.0.1:7005> keys *
1) "name"

127.0.0.1:7005> set age 18
-> Redirected to slot [741] located at 127.0.0.1:7000
OK
# 在 7005 设置值 会跳到7000 
# 根据值的不同会分配到不同的主库中
127.0.0.1:7000> keys *
1) "age"

# 如果不加-c参数登录 写入数据会报错
[root@bogon s20cluster-redis]# redis-cli  -p 7005
127.0.0.1:7005> set age1 20
(error) MOVED 9008 127.0.0.1:7001



# 主库挂掉 从库会变成主库
# 自带哨兵


# 自带哨兵 以下测试出没任何意思
8.防止redis-cluster主节点故障,可以搭配 redis-cluster +  redis-sentinel ,用哨兵检测主节点状态,当主节点宕机,自动切换从节点为新的主库

	1.redis-sentinel配置方式如下,检测三个主节点7000  7001  7002
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

	2.启动哨兵,检测cluster的主节点
	redis-sentinel redis-26379.conf
	
	3.杀死redis-cluster的主节点,查看从节点状态(是否自动重启),可以运行多个从节点,保证数据安全



	




