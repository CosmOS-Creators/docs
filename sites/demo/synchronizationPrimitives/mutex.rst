Mutex
=============================
Mutexes are one of the synchronization primitives that are implemented in CosmOS. A mutex is designed to grant exclusive access to shared resources to the specific
thread. The mutex locking mechanism can be used only for threads within one program. In CosmOS, we implemented two ways of obtaining a mutex. One way is a
non-blocking method and does not cause thread preemption in case of unsuccessful
locking of the mutex. In case of unsuccessful locking of the mutex, the other way
will trigger the thread preemption and unblock it after the mutex is unlocked again.
The mutex implementation also provides additional protection against a deadlock.
For more information please read the mutex section in the :ref:`about_whitepaper`.

Code examples
--------------

Mutex variable mapping
```````````````````````
If our compiler does not support the section pragmas we have to map the mutex variable with help of the
generated mapping macro as it is shown in the code example below.

.. code-block:: C

    /* @cond S */
    __SEC_START( __TIMING_MEASUREMENT_CM4_INIT_SECTION_START)
    /* @endcond*/
    // If your compiler does not support pragmas use __TIMING_MEASUREMENT_CM4_INIT_SECTION
    /********************************************************************************
    ** DO NOT MODIFY THIS COMMENT !                      USER SECTION | Start      **
    ** start_name =timing_measurement_CM4_init
    ********************************************************************************/

    CosmOS_MutexVariableType resourcesMutex __TIMING_MEASUREMENT_CM4_INIT_SECTION;

    /********************************************************************************
    ** stop_name =timing_measurement_CM4_init
    ** DO NOT MODIFY THIS COMMENT !                      USER SECTION | Stop       **
    ********************************************************************************/
    /* @cond S */
    __SEC_STOP( __TIMING_MEASUREMENT_CM4_INIT_SECTION_STOP)
    /* @endcond*/

Mutex get and release
```````````````````````
.. collapse:: Click to see function mutex_getMutex details

    .. doxygenfunction:: mutex_getMutex

.. collapse:: Click to see function mutex_releaseMutex details

    .. doxygenfunction:: mutex_releaseMutex

.. code-block:: C

    #include <mutex.h>
    #include <errorHandler.h>

    mutexState = mutex_getMutex( &resourcesMutex );
    if( errorHandler_isError( mutexState ) )
    {
        //error was returned, check its value
    }

    //Critical code section (safe in intra-program synchronization)

    mutexState = mutex_releaseMutex( &resourcesMutex );
    if( errorHandler_isError( mutexState ) )
    {
        //error was returned, check its value
    }

Return values
"""""""""""""""
.. collapse:: Click to see return values

    .. doxygenenum:: CosmOS_MutexStateType
        :no-link:
