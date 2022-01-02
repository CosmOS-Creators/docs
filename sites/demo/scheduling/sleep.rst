Sleep
=============================
Thread sleep implemented in CosmOS is used for suspending thread execution
for the required periods of time. For this purpose, every thread has its alarm with
timer and state variable configured in the operating system. The internal alarm timer has the same period as the
scheduler preempt period. Still, we are not interrupting the task for the specified
worst-case critical execution time during the critical task execution. However, the
timer won't be updated for this period. Inaccuracy can also be caused by executing
a higher priority thread, which can delay the execution of the unblocked thread with
an expired alarm.
For more information please read the thread sleep section in the :ref:`about_whitepaper`.

Code examples
--------------

Thread sleep
``````````````
.. collapse:: Click to see function thread_sleepMs details

    .. doxygenfunction:: thread_sleepMs

.. code-block:: C

    #include <thread.h>
    #include <errorHandler.h>

    CosmOS_SleepStateType sleepState;

    sleepState = thread_sleepMs( 100 );
    if( errorHandler_isError( sleepState ) )
    {
        //error was returned, check its value
    }

Return values
"""""""""""""""
.. collapse:: Click to see return values

    .. doxygenenum:: CosmOS_SleepStateType
        :no-link:
