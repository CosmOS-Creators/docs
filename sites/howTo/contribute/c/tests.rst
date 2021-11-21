Tests
=============================

This page will describe how to contribute with unit tests of the C code base. We strongly suggest using the VSCode development environment running in the docker container.

Example test folder structure creation in module folder
-----------------------------------------------------------
For better understanding of the test folder structure we will create it in the following example in the os module folder for the os unit. The following test folder structure will contain all necessary files for the os unit testing.

#. First of all we need to create :file:`CMakeLists.txt` in the module folder as it is shown in the following example:
    ::

        os (module)
        ├── src
        ├── inc
        └── CMakeLists.txt

    - The :file:`CMakeLists.txt` collects all unit tests from the module. It has the same content for every module and can be copied over. Here is its code which can be used during the setup of new test environments:
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

#. Then we create a :file:`test` folder in :file:`module` with two sub-folders - :file:`mock` and :file:`ut` as it is shown in the following example:
    ::

        os (module)
        ├── src
        ├── inc
        ├── CMakeLists.txt
        └── test
            ├── mock
            └── ut


#. In :file:`mock` we then create a :file:`os` folder for the os unit mock and two files, :file:`mock.cpp` and :file:`osMock.h` as it is shown in the following example:
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

#. In :file:`ut` we then create a :file:`os` folder for the os unit test cfg and two files, :file:`CMakeLists.txt` and :file:`ut.cpp` as it is shown in the following example:
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

    - The :file:`CMakeLists.txt` creates an executable for the current unit test folder. It has the same content for the every unit test folder and can be copied over. Here is its code which can be used during the setup of new test environments:
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
                EXTRA_ARGS --gtest_output=xml:${TEST_RESULTS_DIRECTORY}/googletest_${EXECUTABLE_NAME}.xml --gtest_filter=*
                )
    - The :file:`ut.cpp` file uses a specific file structure that can be found in the snippets (keyword: test_source) or copied from the already implemented :file:`ut.cpp` - in that case doxygen comments must be fixed.

#. In the :file:`cfg` folder we create two files, :file:`utCfg.cpp` and :file:`utCfg.h` as it is shown in the following example:
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

    - The :file:`utCfg.cpp` and :file:`utCfg.h` files use a specific file structure that can be found in the snippets (for :file:`utCfg.cpp` - keyword: test_source_configuration, for :file:`utCfg.h` - keyword: test_header_configuration) or copied from the already implemented :file:`utCfg.cpp` and :file:`utCfg.h` files - in that case doxygen comments must be fixed.

#. The final test folder structure should look exactly the same as it is shown in the following diagram:
    .. image:: ../../../../images/cUnitTests/testFolderStructure.png

Naming conventions
--------------------
#. Mocked folder names should be exactly the same as the unit name.
#. Unit test folder names should be exactly the same as the unit name.
#. Macros should use SNAKE_CASE as it is shown in the following example:
        .. code-block:: c

            #define FOO_BAR

#. Mock class names consist of two parts, the first one is the unit name (PascalCase) followed by an underscore symbol and MOCK as it is shown in the following example for the os unit mock:
    .. code-block:: c

        class Os_MOCK

#. Test fixture class names consist of two parts, the first one is the unit name (PascalCase) followed by an underscore symbol and TestFixture as it is shown in the following example for the os unit test fixture:
    .. code-block:: c

        class Os_TestFixture : public ::testing::Test

#. Test suite names should start with Test followed by an underscore symbol and then use camelCase as it is shown in the following example:
    .. code-block:: c

        Test_unitName

#. Test names should use SNAKE_CASE as it is shown in the following example for the os_start function where the test checks execution flow:
    .. code-block:: c

        #define TEST_OS_START_EXECUTIONFLOW()

#. Global variables should use PascalCase as it is shown in the following example:
    .. code-block:: c

        CosmOS_CoreVariableType CoresVar[CORE_NUM];

Implementation
----------------
#. First of all we would like to say is that the following rules can be easily observed in any unit test implementation in the `repository <https://github.com/CosmOS-Creators/core>`_. You can use the already implemented unit tests as an example for your implementation if you find it more efficient.
#. For C and C++ code we use `clang-format <https://clang.llvm.org/docs/ClangFormat.html>`_. If you use the docker development environment clang-format is preinstalled with the correct version and VSCode is setup in a way to format your code on save.
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

#. We have to define the test case with an unique macro name to be able to link them with the functions. The following example contains a test case definition for the os_start function where the test checks the execution flow:
    .. code-block:: cpp

        #define TEST_OS_START_EXECUTIONFLOW() TEST( Test_os, os_start_executionFlow )

#. To ease test description creation we define a macro mapped to the RecordProperty as it is shown in the following example:
    .. code-block:: cpp

        TEST_DESCRIPTION( desc ) RecordProperty( "description", desc )

#. Put the description inside the test case function definition:
    .. code-block:: c

        TEST_OS_START_EXECUTIONFLOW()
        {
            TEST_DESCRIPTION(
                "This test validates execution flow of the os_start function" );
        }

#. Use proper doxygen comments for the test case function definition. The following example contains a test case doxygen comment for the os_start function where the test checks the execution flow:
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
#. Put your code into the correct doxygen section, in this specific case inside the Testcases group as it is shown in the following example:
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
#. If you develop in the VSCode you can use code `snippets <https://github.com/CosmOS-Creators/reference_project_stmIDE/blob/master/.vscode/CosmOS%20snippets.code-snippets>`_. Just start typing the keyword of the code snippet and VSCode will automatically offer you the snippet (then press TAB).
