Example Programs
=============================
Channel test CM4
-------------------------------------
Channel x core client CM4 Thread
``````````````````````````````````
This thread is a channels sender thread (client) for the xCore_channel. The xCore_channel_id channel
is inter-program and inter-core channel and this client thread tests if the implementation is
functional and client can send and receive a reply from the reply (server) thread.

Channel test CM7
-------------------------------------
Channel x core server CM7 Thread
``````````````````````````````````
This thread is a channels reply thread (server) for the xCore_channel. The xCore_channel_id channel
is inter-program and inter-core channel and this server thread tests if the implementation is
functional and server can initialize the channel, receive data and reply.

Channel same core server CM7 Thread
``````````````````````````````````````
This thread is a channels reply thread (server) for the sameCore_channel. The sameCore_channel_id channel
is inter-program but not inter-core channel and this server thread tests if the implementation is
functional and server can initialize the channel, receive data and reply.

Channel same core client CM4 Thread
```````````````````````````````````````
This thread is a channels sender thread (client) for the sameCore_channel. The sameCore_channel_id channel
is inter-program but not inter-core channel and this client thread tests if the implementation is
functional and client can send and receive a reply from the reply (server) thread.

Default CM4
---------------
sysJobsGroup 10ms CM4 handler function
``````````````````````````````````````````
This is the handler for the system jobs group which is scheduled every 10 miliseconds. We use this handler to do
timing measurements of the system job group scheduling with the digital logic analyzer.

Default CM7
---------------
sysJobsGroup 20ms CM7 handler function
``````````````````````````````````````````
This is the handler for the system jobs group which is scheduled every 20 miliseconds. We use this handler to do
timing measurements of the system job group scheduling with the digital logic analyzer.

Ethernet communication
-------------------------
TCPIP CM7 Thread
````````````````````
This thread contains demo LWIP code with the TCP/IP echo initialization and ethernet input function calls.

Logger
---------------
Logger Thread
````````````````````
This thread triggers DMA stream to USART3 when the USART3 TX was completed and logger buffer is not empty.

User log function
````````````````````
This function is a interface provided for the other programs to not explicitly call the buffer write array function there
with the logger buffer identifier.

HAL UART TxCpltCallback
````````````````````````
UART TX complete callback change the buffer tail position and the buffer full cells number after the data were sent successfully.

Timing measurement CM4
-------------------------
Timing measurement task CM4
````````````````````````````
This critical task can be used to do some timining measurements by toggling some of the GPIO pins. Also the buffer write and read
operations are tested within this task together with the spinlock obtaining. This task also tries to get mutex to see that the
operating system handles this request correctly and returns error.

Synchronization and dynamicAllocation test thread CM4
````````````````````````````````````````````````````````
This thread contains the dynamic allocation test of the new and delete operator. Also it tries to get resources mutex mapped to
the timing measurement CM4 program.

Synchronization test thread CM4
````````````````````````````````````````````````````````
This thread tries to get resources mutex mapped to the timing measurement CM4 program. This thread also uses user log function
to output some message through the USART3. To test semaphores this thread tries also to get the semaphore_test_0.

Timing measurement CM7
-------------------------
Timing measurement task CM7
````````````````````````````
This critical task can be used to do some timining measurements by toggling some of the GPIO pins. Also the buffer write and read
operations are tested within this task together with the spinlock obtaining. This task also tries to get mutex to see that the
operating system handles this request correctly and returns error.

Synchronization and dynamicAllocation test thread CM7
````````````````````````````````````````````````````````
This thread contains the dynamic allocation test of the new and delete operator. Also it tries to get gpio e mutex mapped to
the timing measurement CM7 program. This thread also uses user log function to output some message through the USART3.
To test semaphores this thread tries also to get the semaphore_test_0.
