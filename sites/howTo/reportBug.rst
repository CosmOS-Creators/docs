Report a bug
=============================

How to create an issue?
-------------------------
#. Choose proper repository where the issue should be created.
#. Be specific with the title, use module or unit name and short description.
#. Do not assign the issue to anyone.
#. Choose proper label for the issue, in this case **bug**.
#. Choose *CosmOS reference project* in **Projects**.
#. Choose *Not planned* in **Milestone**, till we decide in which release we would like to include your issue.

List of items that should be included in the bug report
-----------------------------------------------------------
#. [Feature, Module, Unit Name] Title
#. Environment
#. Steps to reproduce
#. Expected Result
#. Actual Result
#. Visual Proof (screenshots, videos, text)
#. Severity/Priority

Title
--------
Your title should serve as a concise summary of what the bug is. Our report titles start with the core feature issue in brackets at the very beginning of the title.

Environment
------------
The environment for every application can vary widely, but be as specific as you can. Testers should always follow the given bug report template unless otherwise specified — it helps cut down on unnecessary information.

#. Device: What type of hardware are you using? Which specific model?
#. OS: Which version number of the OS has displayed the issue?
#. Software Version: Which version number are you testing? Simply writing “latest version” won’t cut it, since some bugs are version-specific, make sure you include this specific information.
#. Reproducibility Rate: How many times have you been able to reproduce the error, using the exact steps you’ve taken to activate the bug? It’s also useful to report how many times the bug has been reproduced vs. the number of attempts it’s taken to reproduce the issue, in case it’s an intermittent occurrence.

Steps to Reproduce
--------------------
Create list of steps that we can easily follow through by repeating the same process.

Expected Result
--------------------
What should happen when you trigger the call-to-action? This is where you put on your end-user cap and think about the desired outcome and offer deeper insights than “the app should not crash.“

Actual Result
--------------------
Here’s the result of the bug. Does the application crash? Does nothing happen at all? Is an error displayed?

In our experience, testers can be a little vague in this department, so encourage them to be as distinct as possible and provide some information on isolation to make the bug report more actionable – “Button does not work as expected” isn’t helpful, whereas “Button closes app across different platforms, different os versions, or different screen sizes” gives developers a much better feel for the problem. It also provides them with additional details to help start their investigation.

Proof
--------------------
Any pertinent screenshots, videos, or log files should be attached.

Severity/Priority
--------------------
Sharing the severity offers a degree of impact the bug has on the functionality of the system and helps the dev team prioritize their work. We recommend using one of three categories of severity in your bug report:

1. High/Critical: anything that impacts the normal user flow or blocks software usage
2. Medium: anything that negatively affects the user experience
3. Minor: ALL else (e.g., typos, missing icons, layout issues, etc.)

Resources
--------------

- `How to write a bug report that will make your engineers love you <https://testlio.com/blog/the-ideal-bug-report/>`_
