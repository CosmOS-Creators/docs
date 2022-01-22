Measurements
=============================

Though the prototype implementation of the scheduling is done only as the software magic and
currently not supported directly by the system timer IP (we plan to include this HW design in the next release),
we tried to measure the scheduling of the critical tasks. You can find the results in the table below.


=================== ======================= ======================
 Task period [ms]    Measurement time [h]    Maximum jitter [us]
=================== ======================= ======================
 5                   24                      135
=================== ======================= ======================
