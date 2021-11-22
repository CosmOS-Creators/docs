Report a bug
=============================

How to create an issue?
-------------------------
#. Choose the appropriate repository where the issue should be created.
#. Be specific with the title, use module or unit name and a short description.
#. Do not assign the issue to anyone.
#. Choose a proper label for the issue, in this case **bug**.
#. Choose *CosmOS reference project* in **Projects**.
#. Choose *Not planned* in **Milestone**, till we decide in which release we would like to include your issue.

List of items that should be included in the bug report
-----------------------------------------------------------
#. [Feature, Module, Unit Name] Title
#. Environment
#. Steps to reproduce
#. Expected result
#. Actual result
#. Visual proof (screenshots, videos, text)
#. Severity/Priority

Title
--------
Your title should serve as a concise summary of what the bug is. Our report titles start with the feature, module or unit name in brackets at the very beginning of the title.
    - [generator] - bug report for the generator feature.
    - [buffer] - bug report for the buffer module.
    - [memoryProtection] - bug report for the memory protection unit.

Environment
------------
The environment for every application can vary widely, but be as specific as you can. Testers should always follow the given bug report template unless otherwise specified — it helps to cut down on unnecessary information.

#. Device: What type of hardware are you using? Which specific model?
#. OS: Which version number of the OS has displayed the issue?
#. Software Version: Which version number are you testing? Simply writing "latest version" is not enough, since some bugs are version-specific, make sure you include this specific information.
#. Reproducibility Rate: How many times have you been able to reproduce the error, using the exact steps you have taken to activate the bug? It's also useful to report how many times the bug has been reproduced vs. the number of attempts it took to reproduce the issue, in case it's an intermittent occurrence.

Steps to Reproduce
--------------------
Create a list of steps that we can easily follow through by repeating the same process.

Expected Result
--------------------
What should happen when you trigger the call-to-action? This is where you put on your end-user cap and think about the desired outcome and offer deeper insights than "the app should not crash."

Actual Result
--------------------
Here is the result of the bug. Does the application crash? Does nothing happen at all? Is an error displayed?

Proof
--------------------
Any pertinent screenshots, videos, or log files should be attached.

Severity/Priority
--------------------
Sharing the severity offers a degree of impact the bug has on the functionality of the system and helps the dev team prioritize their work. We recommend using one of three categories of severity in your bug report:

#. High/Critical: anything that impacts the normal user flow or blocks software usage
#. Medium: anything that negatively affects the user experience
#. Minor: ALL else (e.g., typos, missing icons, layout issues, etc.)

Resources
--------------

- `How to write a bug report that will make your engineers love you <https://testlio.com/blog/the-ideal-bug-report/>`_
