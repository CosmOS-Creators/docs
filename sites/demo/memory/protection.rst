Protection
=============================

The memory protection software unit is dedicated to reconfiguring the memory
protection regions either during initialization or runtime of the operating system.
This is an optional feature and can be deactivated with the switch module. The memory
protection does not need any other special configuration and it is based on the memory mapping
sections. For more information please read the memory protection section in the CosmOS whitepaper.

Configuration
--------------
1. Open the CustomBox
```````````````````````
Then we have to open from the left panel Switch tab to see all configured switch elements in the system as it is shown in the picture below.

.. image:: ../../../images/demos/switch.png

2. Switch memory protection ON/OFF
`````````````````````````````````````
- State of the switch is set to on (checked checkbox), to turn off memory protection we just uncheck the checkbox.


Memory protection regions
------------------------------
Currently we are using eight different types of the memory regions in the
operating system listed below.

#. Flash memory region read-only protected for the privileged and user access.
    - shareable
    - cachable
    - not bufferable
    - contiguous and aligned start address and size of the memory region, done by the memory mapping python logic runner

#. Stack memory region read-write for the privileged and read-only protected for the user access.
    - shareable
    - cachable
    - not bufferable
    - contiguous and aligned start address and size of the memory region, done by the memory mapping python logic runner


#. OS constant memory region read-only protected for the privileged and user access.
    - shareable
    - cachable
    - not bufferable
    - contiguous and aligned start address and size of the memory region, done by the memory mapping python logic runner


#. OS variable memory region read-write for the privileged and read-only protected for the user access.
    - shareable
    - not cachable
    - not bufferable
    - contiguous and aligned start address and size of the memory region, done by the memory mapping python logic runner


#. Unprotected memory region full access.
    - shareable
    - cachable
    - not bufferable
    - contiguous and aligned start address and size of the memory region, done by the memory mapping python logic runner


#. Schedulable peripheral run-time window memory region full access.
    - shareable
    - not cachable
    - bufferable
    - contiguous and aligned start address and size of the memory region, done by the memory mapping python logic runner


#. Schedulable program memory run-time window memory region full access.
    - shareable
    - cachable
    - not bufferable
    - contiguous and aligned start address and size of the memory region, done by the memory mapping python logic runner


#. Schedulable stack memory run-time window memory region full access.
    - shareable
    - cachable
    - not bufferable
    - contiguous and aligned start address and size of the memory region, done by the memory mapping python logic runner
