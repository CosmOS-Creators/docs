Parser
=============================

It was built with the intention of being completely generic and reusable. Upon invocation the parser will load all of the configuration files,
validate all of the defined values and do some processing on some of the more complex datatypes (we called it linking). In the end it will
provide one huge object, which we call the (system) model, containing all of the information from the config files in an easy to use way.
This object provides a unified and generic API which will always stay the same no matter which datatype a certain value is or how the
model configuration was setup in the config files. This API is used every time any kind of information is requested/changed.
All changes done through these APIs will be validated against a basic set of rules defined in the config files before it is
actually saved to the model.

.. toctree::

    parser/config_files
    parser/links
    parser/constants
