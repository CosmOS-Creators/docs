.. include:: ./../../../documentation/customBox/parser/replacement_links.rst

Generic json file structure
===========================

In the config file directory there can be an arbitrary number of json
files. Filenames should only have alphanumeric names and no special
symbols/spaces as the name of one config file will be used to define a
config class. All json files in the config directory will be parsed and
consolidated together.

If a property is not listed as mandatory the definition of that property
can be omitted if the conditions for it's requirement are not met.

Top level json keys
-------------------

Metadata
~~~~~~~~

Every json file has the following meta properties located at the root
level:

********
version
********

:Mandatory: Always
:Can be omitted: Never
:Value type: :data:`string`
:Description:
   Version of the file structure definition. Versions between files all
   have to match. This version attribute refers to the version of the
   config structure itself, so if there was some property added in the
   spec this version would have to be increased. That way the files can
   maybe even be automatically upgraded from one version to the next
   when opening them.

Attribute properties
~~~~~~~~~~~~~~~~~~~~

Every json file has the following property located at the root level:

*************
attributes
*************

:Mandatory: Always
:Can be omitted: Never
:Value type: :data:`dictionary`
:Description:
   Every entry in the dictionary holds the attributes for one element.
   Every element in that dict represents a UI element definition that
   can be reused (think of it as a class and it's usage as an instance)
   The dictionary key of the element will be used as a unique ID of this
   attribute property. Attribute property IDs have to be unique only
   inside of one file. If accessing an attribute from outside of a file
   it is required to state the config class before the ID. For example
   ``cores/:name`` will refer to the name attribute inside the core.json
   file while ``tasks/:name`` will will refer to the name attribute
   inside the tasks.json file.

Properties in an attribute element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every element in the attribute property should define the following
properties:

""""""""
inherit
""""""""

:Mandatory: If no `type`_ property was defined
:Has to be omitted: If `type`_ property was defined
:Value type: ``string``
:Example value: :data:`"cores/name"`
:Default value if omitted: :data:`""`
:Description:
   If defined all configuration of the target attribute will be taken
   over to this attribute. If a property was defined on this level it
   will overwrite the setting of the attribute which it inherits in case
   it already existed before.

""""""
label
""""""

:Mandatory: Always except if one of `placeholder`_ or `hidden`_ property is true
:Has to be omitted: Never
:Value type: ``string``
:Example value: :data:`"Core Name"`
:Default value if omitted: :data:`""`
:Description:
   A descriptive user friendly name of the attribute (might even be used
   to display the string in the UI)

""""""""
tooltip
""""""""

:Mandatory: Never
:Has to be omitted: Never
:Value type: ``string``
:Example value: :data:`"The core name is a user friendly human readable name used to easily identify a core"`
:Default value if omitted: :data:`""`
:Description:
   A description to describe to the user what this field in the UI is
   doing (maybe can be used as a comment field for hidden entries too)

""""""
type
""""""

:Mandatory: Always except if `inherit`_ property was defined.
   Changing the type when inheriting is not supported.
:Has to be omitted: If `inherit`_ property was defined.
:Value type: ``string``
:Example value: :data:`"string"`
:Default value if omitted: :data:`None`
:Description:
   This property will define the type of an attribute. Possible options are:

   ==================================   ============================   ====================================   ===============================================
   Type                                 Default value if placeholder   ``value`` property has to be of type   Note
   ==================================   ============================   ====================================   ===============================================
   |STRING_ATTRIB_SHORT|                :data:`""`                     string
   |BOOL_ATTRIB_SHORT|                  :data:`false`                  boolean
   |INT_ATTRIB_SHORT|                   :data:`0`                      number
   |FLOAT_ATTRIB_SHORT|                 :data:`0`                      number
   |REFERENCE_LIST_ATTRIB_SHORT|        :data:`[]`                     list
   |STRING_LIST_ATTRIB_SHORT|           :data:`[]`                     list
   |SELECTION_ATTRIB_SHORT|             :data:`None`                   string
   |HEX_ATTRIB_SHORT|                   :data:`0`                      string in the format of ``0xHHH``.     Will be parsed to an int by the config parsers
   |SLIDER_ATTRIB_SHORT|                :data:`0`                      number
   |PARENT_REFERENCE_ATTRIB_SHORT|      :data:`None`                   string
   ==================================   ============================   ====================================   ===============================================

""""
min
""""

:Mandatory: Never
:Has to be omitted: If `type`_ property is not one of: |INT_ATTRIB_SHORT|, |FLOAT_ATTRIB_SHORT|, |SLIDER_ATTRIB_SHORT|, |HEX_ATTRIB_SHORT|
:Value type: ``number``
:Example value: :data:`0`
:Default value if omitted: :data:`None`
:Description:
   Only relevant if type is int, float, hex or slider. Will be used for
   value validation instead of the ``validation`` property for these
   special types

""""
max
""""

:Mandatory: Never
:Has to be omitted: If `type`_ property is not one of: |INT_ATTRIB_SHORT|, |FLOAT_ATTRIB_SHORT|, |SLIDER_ATTRIB_SHORT|, |HEX_ATTRIB_SHORT|
:Value type: ``number``
:Example value: :data:`256`
:Default value if omitted: :data:`None`
:Description:
   Only relevant if type is int, float, hex or slider. Will be used for
   value validation instead of the `validation`_ property for these
   special types

""""
step
""""

:Mandatory: Never
:Has to be omitted: If `type`_ property is not |SLIDER_ATTRIB_SHORT|
:Value type: ``number``
:Example value: :data:`0.5`
:Default value if omitted: :data:`1`
:Description:
   Only relevant if type is slider. The type of the value could be
   inferred from this property. For example if step is a full number
   type would be int, if step would be a float the value would also be
   float. This property would define how much granularity a slider has.

""""""""""
elements
""""""""""

:Mandatory: If `type`_ property is |SELECTION_ATTRIB_SHORT|
:Has to be omitted: Always except when `type`_ property is |SELECTION_ATTRIB_SHORT| or |REFERENCE_LIST_ATTRIB_SHORT|
:Value type: ``list`` or ``string``
:Example value: :data:`["CM4", "CM7"]` or :data:`"core/:name"` or :data:`["core/:name"]` for |REFERENCE_LIST_ATTRIB_SHORT| types
:Default value if omitted: :data:`None`
:Description:
   For attributes of type |SELECTION_ATTRIB_SHORT|: The behavior of this property
   changes depending on the type of it's value:

   -  A list of strings that will be shown in a dropdown as the options
      to be able to choose from
   -  A string which refers to a config file for example ``cores/:name``
      would show all elements defined in the ``cores.json`` file in the
      elements list using the value of their ``name`` attribute instance
      as the displayed option label in the dropdown

   For attributes of type |REFERENCE_LIST_ATTRIB_SHORT|: If the elements key is not
   present attribute instances are hidden from the UI. If the elements
   key was defined:

   -  Always has to be of type list containing links in the form of
      ``core/:name``
   -  A UI list element will be shown to provide the user with the
      choice to add as many items of the matching types as desired. The
      provided attribute from the link will be used as labels for the
      elements
   -  When populating an attribute of this type a sanity check will be
      made to check that the new value does match with the defined
      elements.

""""""""""""
validation
""""""""""""

:Mandatory: Never
:Has to be omitted: If `type`_ property is not |STRING_ATTRIB_SHORT|
:Value type: ``string``
:Example value: :data:`"^[A-Za-z0-9]+$"`
:Default value if omitted: :data:`""`
:Description:
   A regex that determines if a string has a valid format or not.
   Validation can have the following states:

   -  If left empty validation is considered deactivated
   -  If the regex expression provided was invalid validation is
      considered erroneous
   -  If the regex expression provided was valid validation is
      considered active. In this case every pending change of the value
      property should be validated against this regex and only be
      written if the regex matches.

""""""""
hidden
""""""""

:Mandatory: Never
:Has to be omitted: If `type`_ is |PARENT_REFERENCE_ATTRIB_SHORT|
:Value type: ``boolean``
:Example value: :data:`True`
:Default value if omitted: :data:`False`
:Description:
   If true attribute instances of this attribute definition will not
   show up in the UI. This is useful for some helper "variables" that
   are only used by some logic and are not of interest for the user

""""""""""""""
placeholder
""""""""""""""

:Mandatory: Never
:Has to be omitted: If `type`_ is |PARENT_REFERENCE_ATTRIB_SHORT|
:Value type: ``boolean``
:Example value: :data:`True`
:Default value if omitted: :data:`False`
:Description:
   If true it signals that the value for an attribute instance of this
   would be populated by a script at a later point.

Element properties
~~~~~~~~~~~~~~~~~~

Every json file has the following property located at the root level:

*********
elements
*********

:Mandatory: Always
:Can be omitted: Never
:Value type: ``dictionary``
:Description:
   Each dictionary entry is considered a group whose id is the
   dictionary key. An element should always have a list as it's value.

Properties in an elements element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Every item in the elements list (attribute instance) should be a
dictionary with the following properties:

""""""""
target
""""""""

:Mandatory: Always
:Has to be omitted: Never
:Value type: ``string``
:Example value: :data:`"cores/:name"` or just :data:`"name"` if the attribute
   definition is within the same file
:Default value if omitted: :data:`None`
:Description:
   An ID of an attribute definition which is instantiated. If the
   attribute was defined within the same file simply list it's name. If
   it was defined in another file it has to be prefixed by the filename
   without the file extension.

""""""""""""""""""""
targetNameOverwrite
""""""""""""""""""""

:Mandatory: Never
:Has to be omitted: Never
:Value type: ``string``
:Example value: :data:`"coreName"`
:Default value if omitted: :data:`None`
:Description:
   If specified the attribute instance that the target property is
   pointing to will get this name instead of the targets name. For
   example if ``target`` is set to ``cores/:name`` but
   ``targetNameOverwrite`` was defined to ``coreName`` the name property
   can be accessed inside the object model by ``core_0.coreName`` but
   still instantiates the same ``cores/:name`` attribute definition and
   all it's validations etc.

""""""
value
""""""

:Mandatory: Always unless the targeted attribute definition has `placeholder`_ defined as True
:Has to be omitted: If targeted attribute definition has `placeholder`_ == True
:Value type: ``string``, ``number``, ``bool`` or ``list`` depending on the type of the targeted attribute definition
:Example value: :data:`"CM4"`
:Default value if omitted: Only comes to affect if `placeholder`_ == true. Will follow the defined defaults in the table of the attribute section for the `type`_ property
:Description:
   Stores the current value of the attribute instance. If `type`_ is a
   list, a list of links or list of strings is expected depending on the
   list type. For a `type`_ of |REFERENCE_LIST_ATTRIB_SHORT| the links should point
   to an element in the form of ``core/core_0``

""""""""
enabled
""""""""

:Mandatory: Never
:Has to be omitted: if the targeted attribute is `hidden`_ or is a `placeholder`_
:Value type: ``string`` or ``bool``
:Example value: :data:`True`
:Default value if omitted: :data:`True`
:Description:
   Defines if this element can be edited through the UI.
