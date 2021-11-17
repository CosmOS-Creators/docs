Tests
=============================

This page will describe how to contribute with unit tests of the C code base. We strongly suggest using VS Code development environment running in the docker container.


For better understanding of the test folder structure we will create it in following example in os module folder for the os unit. The following test folder structure will contain all necessary files for the os unit testing.

Example test folder structure creation in module folder
-----------------------------------------------------------
#. First of all we need to create CMakeLists.txt in the module folder as it is shown in the following example:
    ::

        os (module)
        ├── src
        ├── inc
        └── CMakeLists.txt

    - The CMakeLists.txt collects all unit tests from the module. It has the came content for the every module and can be copied over. Here is its code which can be used during the new test environment setup:
        .. code-block:: cmake

            cmake_minimum_required(VERSION 3.14)

            FILE(GLOB_RECURSE UNIT_TEST_DIRECTORIES LIST_DIRECTORIES true ${UNIT_TEST_DIRECTORY_WILDCARD})
            list(FILTER UNIT_TEST_DIRECTORIES INCLUDE REGEX "^.*/ut/*.")

            if(BUILD_TESTS)
                foreach(UNIT_TEST_DIRECTORY ${UNIT_TEST_DIRECTORIES})
                    if(EXISTS "${UNIT_TEST_DIRECTORY}/CMakeLists.txt")
                        add_subdirectory(${UNIT_TEST_DIRECTORY})
                    endif()
                endforeach(UNIT_TEST_DIRECTORY)
            endif()

#. Then we create in module folder test folder with two sub-folders - mock and ut as it is shown in the following example:
    ::

        os (module)
        ├── src
        ├── inc
        ├── CMakeLists.txt
        └── test
            ├── mock
            └── ut


#. In the mock folder we create then folder for os unit mock with name **os** and create there mock.cpp and osMock.h as it is shown in the following example:
    ::

        os (module)
        ├── src
        ├── inc
        ├── CMakeLists.txt
        └── test
            ├── ut
            └── mock
                └── os
                    ├── mock.cpp
                    └── osMock.h

#. In the ut folder we create then folder for os unit test cfg and two files, CMakeLists.txt and ut.cpp as it is shown in the following example:
    ::

        os (module)
        ├── src
        ├── inc
        ├── CMakeLists.txt
        └── test
            ├── mock
            │   └── os
            │       ├── mock.cpp
            │       └── osMock.h
            └── ut
                └── os
                    ├── ut.cpp
                    ├── CMakeLists.txt
                    └── cfg

    - The CMakeLists.txt create executable for the current unit test folder. It has the came content for the every unit test folder and can be copied over. Here is its code which can be used during the new test environment setup:
        .. code-block:: cmake

            cmake_minimum_required(VERSION 3.14)

            get_filename_component(UNIT_NAME ${CMAKE_CURRENT_SOURCE_DIR} NAME)

            set(CONFIGURATION_PATH "cfg")
            set(UNIT_SOURCE_PATH "../../../src")
            set(EXECUTABLE_NAME "${UNIT_NAME}_ut_executable")
            set(TEST_NAME "${UNIT_NAME}_test")

            list(APPEND LOCAL_MOCK_SOURCES ${MOCK_SOURCES})
            list(FILTER LOCAL_MOCK_SOURCES EXCLUDE REGEX ".*test/mock/${UNIT_NAME}")

            include_directories(${CONFIGURATION_PATH})
            FILE(GLOB_RECURSE CFG_SOURCES_C  "${CONFIGURATION_PATH}/*.c")

            include_directories(${CONFIGURATION_PATH})
            FILE(GLOB_RECURSE CFG_SOURCES_CPP  "${CONFIGURATION_PATH}/*.cpp")

            set(SOURCES
                "${UNIT_SOURCE_PATH}/${UNIT_NAME}.c"
                ${UNIT_TEST_SOURCE_WILDCARD}
                ${LOCAL_MOCK_SOURCES}
                ${CFG_SOURCES_C}
                ${CFG_SOURCES_CPP}
                )

            add_executable(${EXECUTABLE_NAME} ${SOURCES})
            target_link_libraries(${EXECUTABLE_NAME} gtest_main gmock_main)

            include(GoogleTest)
            gtest_add_tests(
                TARGET ${EXECUTABLE_NAME}
                EXTRA_ARGS --gtest_output=xml:${COSMOS}/generated/build/tests/results/googletest_${EXECUTABLE_NAME}.xml
                )
    - The ut.cpp file uses specific file structure that can be found in the snippets (test_source) or copied from the already implemented ut.cpp - in that case doxygen comments must be fixed.

#. In the cfg folder we create two files, utCfg.cpp and utCfg.h as it is shown in the following example:
    ::

        os (module)
        ├── src
        ├── inc
        ├── CMakeLists.txt
        └── test
            ├── mock
            │   └── os
            │       ├── mock.cpp
            │       └── osMock.h
            └── ut
                └── os
                    ├── ut.cpp
                    ├── CMakeLists.txt
                    └── cfg
                        ├── utCfg.cpp
                        └── utCfg.h

    - The utCfg.cpp and utCfg.h files use specific file structure that can be found in the snippets (utCfg.cpp test_source_configuration, utCfg.h test_header_configuration) or copied from the already implemented utCfg.cpp and utCfg.h files - in that case doxygen comments must be fixed.

#. Final test folder structure should look exactly the same as it is shown in the following diagram:
    .. image:: ../../../../images/cUnitTests/testFolderStructure.png

Naming conventions
--------------------
#. Mocked folder names should be exactly the same as the unit name.
#. Unit test folder names should be exactly the same as the unit name.
#. Macros should use SNAKE_CASE as it is shown in the following example:
        .. code-block:: c

            #define FOO_BAR

#. Mock class name consists of two parts, first one is the unit name (first letter uppercase) followed by underscore symbol and MOCK as it is shown in the following example for the os unit mock:
    .. code-block:: c

        class Os_MOCK

#. Test fixture class name consists of two parts, first one is the unit name (first letter uppercase) followed by underscore symbol and TestFixture as it is shown in the following example for the os unit test fixture:
    .. code-block:: c

        class Os_TestFixture : public ::testing::Test

#. Test suite name should use Snake_case as it is shown in the following example:
    .. code-block:: c

        Test_unitName

#. Test name should use SNAKE_CASE as it is shown in the following example for the os_start function where test checks execution flow:
    .. code-block:: c

        #define TEST_OS_START_EXECUTIONFLOW()

#. Global variables should use CamelCase as it is shown in the following example:
    .. code-block:: c

        CosmOS_CoreVariableType CoresVar[CORE_NUM];

Implementation
----------------
#. First of all we would like to say that following rules can be easily observed in any unit test implementation in the `repository <https://github.com/CosmOS-Creators/core>`_. You can use the already implemented unit tests as an example for your implementation if you find it more effective.
#. For the C and C++ code we use `clang-format <https://clang.llvm.org/docs/ClangFormat.html>`_. If you use the docker development environment the clang-format is preinstalled with correct version and VS Code setup in a way to format your code on save.
#. Example mock implementation for the os unit and os_getOsCfg function:
    #. For the mock class and test fixture class:
        .. code-block:: cpp

            class Os_MOCK
            {
            public:
                Os_MOCK()
                {}
                ~Os_MOCK()
                {}

                MOCK_METHOD( CosmOS_OsConfigurationType *, os_getOsCfg, () );
            };

            class Os_TestFixture : public ::testing::Test
            {
            public:
                Os_TestFixture()
                {
                    _OsMock.reset( new ::testing::NiceMock<Os_MOCK>() );
                }
                ~Os_TestFixture()
                {
                    _OsMock.reset();
                }

                static std::unique_ptr<Os_MOCK> _OsMock;

            protected:
                virtual void
                SetUp()
                {}
                virtual void
                TestBody()
                {}
                virtual void
                TearDown()
                {}
            };
    #. For the mocked function definition:
        .. code-block:: cpp

            std::unique_ptr<Os_MOCK> Os_TestFixture::_OsMock;

            CosmOS_OsConfigurationType *
            os_getOsCfg()
            {
                Os_TestFixture::_OsMock->os_getOsCfg();

                return ( NULL );
            }

#. We have to define test case with unique macro name to be able link them with the functions, the following example contains test case definition for the os_start function where test checks execution flow:
    .. code-block:: cpp

        #define TEST_OS_START_EXECUTIONFLOW() TEST( Test_os, os_start_executionFlow )

#. To ease test description creation we define macro mapped to the RecordProperty as it is shown in the following example:
    .. code-block:: cpp

        TEST_DESCRIPTION( desc ) RecordProperty( "description", desc )

#. Put description inside the test case function definition:
    .. code-block:: c

        TEST_OS_START_EXECUTIONFLOW()
        {
            TEST_DESCRIPTION(
                "This test validates execution flow of the os_start function" );
        }

#. Use proper doxygen comments. For the test case function definition, the following example contains test case doxygen comment for the os_start function where test checks execution flow:
    .. code-block:: c

        /********************************************************************************
          * DOXYGEN DOCUMENTATION INFORMATION                                          **
          * ****************************************************************************/
        /**
          * @brief This test validates execution flow of the os_start function.
          *
          * @see os_start
          * @authors https://github.com/author1 https://github.com/author2
        ********************************************************************************/
        TEST_OS_START_EXECUTIONFLOW()
        {

        }
#. Put your code to the correct doxygen section, in this specific case inside the Testcases group as it is shown in the following example:
    .. code-block:: c

        /********************************************************************************
          * DOXYGEN START GROUP                                                        **
          * *************************************************************************//**
          * @defgroup testcases_os_ut_c Testcases
          * @ingroup Test_os
          * @{
        ********************************************************************************/
        /********************************************************************************
          * DOXYGEN DOCUMENTATION INFORMATION                                          **
          * ****************************************************************************/
        /**
          * @brief This test validates execution flow of the os_start function.
          *
          * @see os_start
          * @authors https://github.com/author1 https://github.com/author2
        ********************************************************************************/
        TEST_OS_START_EXECUTIONFLOW()
        {

        }
        /********************************************************************************
          * DOXYGEN STOP GROUP                                                         **
          * *************************************************************************//**
          * @} */
        /*  testcases_os_ut_c
        ********************************************************************************/

Tips and tricks
-----------------
#. If you develop in the VS Code you can use code `snippets <https://github.com/CosmOS-Creators/reference_project_stmIDE/blob/master/.vscode/CosmOS%20snippets.code-snippets>`_. Just start typing the name of the code snippet and VS Code will automatically offer you the snippet (then press TAB).
