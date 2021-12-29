Architecture
===============================================================================================================================
- CosmOS architecture is microkernel based and implements near-minimum amount of the software for the operating system.
- The main parts of the CosmOS microkernel is scheduling, memory handling and data exchange interface. Data exchange interface is the operating system basic inter-program communication model. The microkernel can be easily expanded either with system jobs if it is necessary and make the microkernel modular, even though is highly suggested to implement all services in the user space and use data exchange interface for the inter-program communication as it is shown in the figure below.
- The programs are running in the user space and each of them is encapsulates its threads and tasks, providing them a safe memory space for the data and heap for the dynamic allocation (within the program). This design provides to user possibility to implement programs with multiple safety levels without any interference.
- To ensure memory safety the operating system configuration is completely static that includes also configured programs, tasks and threads and remain constant during the run-time.

.. image:: ../../images/architecture/system_architecture.png
