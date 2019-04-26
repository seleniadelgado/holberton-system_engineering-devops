Mysql
Learning Objectives

What is the main role of a databse?
To store important information, it is organized so that ican be easily accessed
 managed and updated.

What is a database replica?
This is when you have a database server, which is referred to as the
"master" server. This server is responsible for performing all writes and
updates. The data from this server is copied continuosly to a "slave server"

What is the purpose of a database replica?
a database replica can be used in case a server goes down.
Allows for the reads to be distributed to multiple machines, which can
dramatically improve the performance of machines.

Why database backups need to be stored in different physical locations?
In case one server goes down, the redundancy will help with this issue.

What operation should regularly perform to make sure that your databse backup
strategy actually works?
The operation of verifying backups periodically and should consider to do this
at least once a year and perform a full blown server recovery test.

RPO = Recovery point objective: How much data can you lose.
RTO = How long can you take to recover your lost data.

