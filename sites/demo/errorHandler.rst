Error handler
=============================
The error handler module detects, traces, and handles all errors which can occur
within the operating system.
The errors are traced for the every program configured in the operating system
that can be later used for the debug purpose. Error processing allows triggering the
required error reaction which can be configured in the CosmOS CustomBox.

Configuration
--------------
.. note::  This page is planned to be completed within a **Live release**. The error handler functionality will be expanded.

Code examples
--------------

Check if returned value is error
```````````````````````````````````

.. code-block:: C

    #include <interrupt.h>
    #include <errorHandler.h>

    CosmOS_InterruptStateType interruptState;

    interruptState = interrupt_handle( TIM2_interrupt_id );
    if( errorHandler_isError( interruptState ) )
    {
        //error was returned, check its value
    }
