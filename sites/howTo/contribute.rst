Contribute
=============================

This page will describe how to contribute to the CosmOS open source project.

.. toctree::
    :maxdepth: 1

    contribute/c
    contribute/python

What does the Code of Conduct mean for me?
------------------------------------------------
Our Code of Conduct means that you are responsible for treating everyone on the project with respect and courtesy regardless of their identity. If you are the victim of any inappropriate behavior or comments as described in our Code of Conduct, we are here for you and will do the best to ensure that the abuser is reprimanded appropriately, per our code.

Few tips for the newcomers
---------------------------
#. The best that you can do before your first contribution is to try to go through the reference project, see what we use, how we implement features and get an overall overview how things work. During this process we strongly suggest asking any questions in the community `discord server <https://discord.gg/XTabzYYVxS>`_.
#. Next step would be to discuss the feature/idea you want to implement in our community `discord server <https://discord.gg/XTabzYYVxS>`_. We will try to answer all your questions and point you in the right direction.

What do I need to know to help?
------------------------------------------------
#. How to create an issue?
    #. Choose the appropriate repository where the issue should be created.
    #. Be specific with the title, use module or unit name and a short description.
    #. Do not assign the issue to anyone.
    #. Choose a proper label for the contribution issue, currently we use these:
        - **Feature** means new feature implementation.
        - **Improvement** means improvement for an already existing feature.
        - **Documentation** means improvements or additions to documentation.
    #. Choose *CosmOS reference project* in **Projects**.
    #. Choose *Not planned* in **Milestone**, till we decide in which release we would like to include your issue.
#. Which workflow do we use?
    In general, we follow the `Fork and Pull Request Workflow <https://github.com/susam/gitpr>`_.
#. Example workflow:
    #. Find an issue that you are interested in addressing or a feature that you would like to add.
    #. Fork the repository associated with the issue to your local GitHub organization. This means that you will have a copy of the repository under your-GitHub-username/repository-name.
    #. Clone the repository to your local machine using the following command:
        .. code-block::

            git clone https://github.com/github-username/repository-name.git
    #. Create a new branch for your issue using :code:`git checkout -b branch-name-issue-number`, for instance typos-fix-7.
    #. Make the appropriate changes for the issue you are trying to address or the feature that you want to add.
    #. Use :code:`git add insert-paths-of-changed-files-here` to add the file contents of the changed files to the "snapshot" git uses to manage the state of the project, also known as the index.
    #. Use :code:`git commit -m "Insert a short message of the changes made here"` to store the contents of the index with a descriptive message.
    #. Push the changes to the remote repository using :code:`git push origin branch-name-here`.
    #. Submit a pull request to the upstream repository.
    #. Title the pull request with a short description of the changes made and the issue or bug number associated with your change. For example, you can title an issue like so "Added more log outputting to resolve #4352".
    #. In the description of the pull request, explain the changes that you made, any issues you think exist with the pull request you made and any questions you have for the maintainer. It's OK if your pull request is not perfect (no pull request is), the reviewer will be able to help you fix any problems and improve it!
    #. Wait for the pull request to be reviewed by a maintainer.
    #. Make changes to the pull request if the reviewing maintainer recommends them.
    #. Celebrate your success after your pull request is merged!
