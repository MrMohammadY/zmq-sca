# What is ZeroSCA(ZeroMQ Server/Client Asynchronous)?

ZeroSCA is a zmq asynchronous server client which can receive data from many client and send response in the form of
asynchronous.

## What's server can receive and send?

User can input two type of commands:

- os
- compute

When user input os he should after this he should give commands like ls -r -l to application, and when user input
compute he should input your compute expression like 19 ** 2 - (5 / 2).

## Requirements:

- [x] Create this application with [ZMQ](https://zguide.zeromq.org/)
- [x] Server can receive request from many clients and operating as concurrency
- [ ] Implementation concurrency with [gevent](http://www.gevent.org/)


## ScreenShots:

<a href="https://ibb.co/V98JP7N"><img src="https://i.ibb.co/NCztH83/2022-01-17-22-24.png" border="0"></a>