Functional
=============================

This page will describe how to contribute to the CosmOS C code base. We strongly suggest using the VSCode development environment running in the docker container.

Example module folder structure creation
----------------------------------------------------
For better understanding of the module folder structure we will create it in the following example for the os module with an os unit inside.

#. In the os folder we create two folders :file:`src` for the unit source files and :file:`inc` for the included files as it is shown in the following example:
    ::

        os (module)
        ├── src
        └── inc


    - The :file:`utCfg.cpp` and :file:`utCfg.h` files use a specific file structure that can be found in the snippets (for :file:`utCfg.cpp` - keyword: test_source_configuration, for :file:`utCfg.h` - keyword: test_header_configuration) or copied from the already implemented :file:`utCfg.cpp` and :file:`utCfg.h` files - in that case doxygen comments must be fixed.

#. In the :file:`src` folder we create an :file:`os.c` file and in the :file:`inc` folder we create an :file:`os.h` file as it is shown in the following example:
    ::

        os (module)
        ├── src
        │   └── os.c
        └── inc
            └── os.h

    - The :file:`os.c` file uses a specific file structure that can be found in the snippets (keyword: source) or copied from the already implemented unit source file - in that case doxygen comments must be fixed.
    - The :file:`os.h` file uses a specific file structure for the module header that can be found in the snippets (keyword: module_header) or copied from the already implemented unit module header file - in that case doxygen comments must be fixed.
    - Module header is a special header that contains module and unit group definitions for doxygen. The module header file must be present in every module folder and must have exactly the same name as the module folder has.
    - If we would create another unit header file in the structure, for instance :file:`osInit.h`, this header file would use another file structure that can be found in the snippets (keyword: header) or copied from the already implemented unit header file - in that case doxygen comments must be fixed.

#. Final module folder structure should look exactly the same as it is shown in the following diagram:
    .. image:: ../../../../images/cUnitTests/moduleFolderStructure.png

Naming conventions
--------------------
#. Modules should use camelCase as it is shown in the following example:
    `cosmosTypes <https://github.com/CosmOS-Creators/core/blob/master/cosmosTypes>`_
#. Units should use camelCase as it is shown in the following example:
    `coreSync.c <https://github.com/CosmOS-Creators/core/blob/master/core/src/coreSync.c>`_
#. Macros
    #. Compiler dependent macros should use SNAKE_CASE and double underscore prefix as it is show in the following example:
        .. code-block:: c

            #define __COMPILER_DEPENDENT_MACRO
    #. Compiler independent macros should use SNAKE_CASE as it is show in the following example:
        .. code-block:: c

            #define COMPILER_INDEPENDENT_MACRO
#. Type definitions
    #. Configuration types should start with the CosmOS prefix followed by an underscore symbol, then PascalCase is used for the configuration struct as it is shown in the following example for the core configuration:
        .. code-block:: c

            typedef struct CosmOS_CoreConfigurationType CosmOS_CoreConfigurationType;
    #. Variable types should start with the CosmOS prefix followed by an underscore symbol, then PascalCase is used for the configuration struct as it is shown in the following example for the core variable:
        .. code-block:: c

            typedef struct CosmOS_CoreVariableType CosmOS_CoreVariableType;
    #. Enumerators should start with the CosmOS prefix followed by an underscore symbol, then PascalCase is used for the configuration struct as it is shown in the following example for the double buffer access state enumeration:
        - Internal enumeration names consist of two parts first is the enum type name but in the end is used enum instead of type in this case BUFFER_DOUBLE_ACCESS_ENUM (SNAKE_CASE) followed by two underscore symbols and the second is actual name of the current enumeration USER_FOO (SNAKE_CASE).
            .. code-block:: c

                typedef enum
                {

                    BUFFER_DOUBLE_ACCESS_ENUM__USER_FOO,
                    BUFFER_DOUBLE_ACCESS_ENUM__KERNEL_FOO,

                } CosmOS_BufferDoubleAccessType;

#. Functions
    #. The name of a function consists of two parts, the unit name (camelCase) and the function name (camelCase). Between those two is an underscore symbol as it shown in the following example for the function getFoo implemented in the fooInit unit:
        .. code-block:: c

            foo fooInit_getFoo( void );
    #. Arguments of the function should use camelCase as it is shown in the following example:
        .. code-block:: c

            foo fooInit_getFoo( CosmOS_BooleanType isTrue );
    #. Local variables of the function should use camelCase as it is shown in the following example:
        .. code-block:: c

            foo fooInit_getFoo( CosmOS_BooleanType isTrue )
            {
                BitWidthType fooId;
            }

#. Global variables should use PascalCase as it is shown in the following example:
    .. code-block:: c

        CosmOS_CoreVariableType CoresVar[CORE_NUM];

Implementation
----------------
#. First of all we would like to say that following rules can be easily observed in any C code implementation in the `repository <https://github.com/CosmOS-Creators/core>`_. You can use the already implemented code as an example for your implementation if you find it more efficient.
#. For C and C++ code we use `clang-format <https://clang.llvm.org/docs/ClangFormat.html>`_. If you use the docker development environment clang-format is preinstalled with the correct version and VSCode setup in a way to format your code on save.
#. Use proper mapping. For instance if you want to map a function you should use the following macros:
    #. For the function declaration:
        .. code-block:: c

            __OS_FUNC_SECTION void
            foo( void );
    #. For the function definition:
        .. code-block:: c

            /* @cond S */
            __SEC_START( __OS_FUNC_SECTION_START )
            /* @endcond*/
            __OS_FUNC_SECTION void
            foo( void )
            { }
            /* @cond S */
            __SEC_STOP( __OS_FUNC_SECTION_STOP )
            /* @endcond*/

#. Use proper doxygen comments:
    #. For the function declaration:
        .. code-block:: c

            /********************************************************************************
              * DOXYGEN DOCUMENTATION INFORMATION                                          **
              * ****************************************************************************/
            /**
              * @fn foo( CosmOS_CoreConfigurationType * core )
              *
              * @brief Brief description of your function.
              *
              * @param[in]  core configuration pointer
              *
              * @return CosmOS_BooleanType
            ********************************************************************************/
            __OS_FUNC_SECTION CosmOS_BooleanType
            foo( CosmOS_CoreConfigurationType * core );
    #. For the function definition:
        .. code-block:: c

            /********************************************************************************
              * DOXYGEN DOCUMENTATION INFORMATION                                          **
              * ****************************************************************************/
            /**
              * @fn foo( CosmOS_CoreConfigurationType * core )
              *
              * @details The implementation contains ... detailed decription of your function
              *
              * @see TEST_1_OF_YOUR_FUNCTION
              * @see TEST_2_OF_YOUR_FUNCTION
            ********************************************************************************/
            /* @cond S */
            __SEC_START( __OS_FUNC_SECTION_START )
            /* @endcond*/
            __OS_FUNC_SECTION CosmOS_BooleanType
            foo( CosmOS_CoreConfigurationType * core )
            { }
            /* @cond S */
            __SEC_STOP( __OS_FUNC_SECTION_STOP )
            /* @endcond*/
#. Put your code into the correct doxygen section. For instance if you want to create a getter function declaration for the core unit it will end up in the following section:
    .. code-block:: c

        /********************************************************************************
          * DOXYGEN START GROUP                                                        **
          * *************************************************************************//**
          * @addtogroup Getters_core_h Getters
          * @ingroup Apis_core_h
          * @{
        ********************************************************************************/
        /********************************************************************************
          * DOXYGEN DOCUMENTATION INFORMATION                                          **
          * ****************************************************************************/
        /**
          * @fn core_getFoo( CosmOS_CoreConfigurationType * core )
          *
          * @brief Brief description of your function.
          *
          * @param[in]  core configuration pointer
          *
          * @return CosmOS_BooleanType
        ********************************************************************************/
        __OS_FUNC_SECTION CosmOS_BooleanType
        core_getFoo( CosmOS_CoreConfigurationType * core );
        /********************************************************************************
          * DOXYGEN STOP GROUP                                                         **
          * *************************************************************************//**
          * @} */
        /*  Getters_core_h
        ********************************************************************************/

Tips and tricks
-----------------
#. If you develop in VSCode you can use code `snippets <https://github.com/CosmOS-Creators/reference_project_stmIDE/blob/master/.vscode/CosmOS%20snippets.code-snippets>`_. Just start typing the keyword of the code snippet and VSCode will automatically offer you the snippet (then press TAB).
#. Use the **IS_EQUAL_TO** macro to avoid assignments by mistake inside the if conditions etc.
    .. code-block:: c

        if ( var1 IS_EQUAL_TO 1000 )
        {
            foo();
        }
#. Use implemented getters and setters for structure members.
