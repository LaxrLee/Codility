Hadoop - Enables lateral scaling
Building systems that can withstand future of huge data influx

Legacy way of managing - limited to the exact data

Hadoop will divide data and distribute it.
Multiple machines - hadoop distributed file system(HDFS) - handles the storage issue

Master computer and slave computers

A company like yahoo has over 45000 machines in their hadoop cluster, trying to scan will cause overloads
At the time of storage, just as a project manager maintains a log, the master comp will maintain the log of metadata 
Metadata is data of your data information of your data. 
In scanning only the metadata will be scanned ands the logic will be sent to where the actual data exists.
Master computer consolidates the results and sends the report back to the client.
MapReduce - a programming modell, a technique usiing which you can address the processing related issues. 

Storage issues - Hdfs
Mapping issues - MapReduce - python or java need to be used to map reduce


Eco-systems
Pig - Scripting language - alternartive to map reduce if you don't know core java or puython for map reduce
Hive - same as SQ
Hbase - no SQL - in big data it is difficult to maintain row and column oriented data, hence noSql is used
Sqoop - import the data from RDBMS DBs to hadoop
Flume - Import the streaming data rom large log files into Hadoop
Oozie - Scheduler - to run your jobs in a particular pattern, as you will ru multiple jobs to maintain your data







(HDFS) - higlevel cluster

MASTER NODE - managers all the data. e.g you have temp.txt file, it will bediivided into chunks, who decides that? division is at file level. User can decide how they can divide the data. There is also a default division based on the hadoop version. You need to have a paramerter to divide, the parameter is called BlockSize.
Block size is a parameter, argument, using which we are going to divide the whole file into chunks of files.
default blocksiez is 64 mb in Hadoop 1.x, and 128mb in Hadoop 2.x
Block size is configurable, minimum BS is 1mb, max can be aything. As per recommendations you should not go beyond 256 mb.

For 5 machines, 
1TB and B.S - 64 mb
How many blocks ??
1 * 1024 * 1024 /64 = 16,384 blocks 

Namenode/master - is responsible for managing the metadata, managing all the extra clients in terms of writing the data into the hadoop cluster, in terms of reading the data out of the hadoop cluster.


SLAVE/WORKER/DATA NODE



A user want to request temp.txt, User does it through the master node, which contains the metadata
Metadata - information about the data which includes; Filename, filesizem blocksize #blocks blockslocation, user, usergroup, date, permission etc.
                                                      Temp.txt  100 mb    64 mb      2      b1=dn1,b2=dn500, xyz, supergroup, 0824, rwx-----
Master node will send request to datanode 1 and 500 instead of scanning each machine and causing an overload.

The nodes must always be active and responsive when requests are made. And at all other times
Daemon - process/program that will always be running in the background
There are 5 hadoop daemons. One i Name/master node
In eah machine you will run the daemon,

Evry one hour you are copying meta data, more like a backup - to recover. on the second master computer - this is configurable. (secondary /masternamenode machine)


