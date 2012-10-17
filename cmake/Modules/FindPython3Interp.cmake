# - Find python3 interpreter
# This module finds if Python3 interpreter is installed and determines where the
# executables are. This code sets the following variables:
#
#  PYTHON3INTERP_FOUND         - Was the Python3 executable found
#  PYTHON3_EXECUTABLE          - path to the Python3 interpreter
#
#  PYTHON3_VERSION_STRING      - Python3 version found e.g. 2.5.2
#  PYTHON3_VERSION_MAJOR       - Python3 major version found e.g. 2
#  PYTHON3_VERSION_MINOR       - Python3 minor version found e.g. 5
#  PYTHON3_VERSION_PATCH       - Python3 patch version found e.g. 2
#
#  Python3_ADDITIONAL_VERSIONS - list of additional Python3 versions to search for

#=============================================================================
# Copyright 2005-2010 Kitware, Inc.
# Copyright 2011 Bjoern Ricks <bjoern.ricks@gmail.com>
#
# Distributed under the OSI-approved BSD License (the "License");
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================
# (To distribute this file outside of CMake, substitute the full
#  License text for the above reference.)

# Search for the current active python3 version first
find_program(PYTHON3_EXECUTABLE NAMES python3)

# Set up the versions we know about, in the order we will search. Always add
# the user supplied additional versions to the front.
set(_Python3_VERSIONS
  ${Python3_ADDITIONAL_VERSIONS}
  3.3 3.2 3.1 3.0)

# Search for newest python3 version if python3 executable isn't found
if(NOT PYTHON3_EXECUTABLE)
    foreach(_CURRENT_VERSION ${_Python3_VERSIONS})
      set(_Python3_NAMES python3${_CURRENT_VERSION})
      if(WIN32)
        list(APPEND _Python3_NAMES python3)
      endif()
      find_program(PYTHON3_EXECUTABLE
        NAMES ${_Python3_NAMES}
        PATHS [HKEY_LOCAL_MACHINE\\SOFTWARE\\Python3\\Python3Core\\${_CURRENT_VERSION}\\InstallPath]
        )
    endforeach()
endif()

# determine python3 version string
if(PYTHON3_EXECUTABLE)
    execute_process(COMMAND "${PYTHON3_EXECUTABLE}" --version ERROR_VARIABLE _VERSION OUTPUT_QUIET ERROR_STRIP_TRAILING_WHITESPACE)
    string(REPLACE "Python3 " "" PYTHON3_VERSION_STRING "${_VERSION}")
    string(REGEX REPLACE "^([0-9]+)\\.[0-9]+\\.[0-9]+.*" "\\1" PYTHON3_VERSION_MAJOR "${PYTHON3_VERSION_STRING}")
    string(REGEX REPLACE "^[0-9]+\\.([0-9])+\\.[0-9]+.*" "\\1" PYTHON3_VERSION_MINOR "${PYTHON3_VERSION_STRING}")
    string(REGEX REPLACE "^[0-9]+\\.[0-9]+\\.([0-9]+).*" "\\1" PYTHON3_VERSION_PATCH "${PYTHON3_VERSION_STRING}")
endif()

# handle the QUIETLY and REQUIRED arguments and set PYTHON3INTERP_FOUND to TRUE if
# all listed variables are TRUE
include(${CMAKE_CURRENT_LIST_DIR}/FindPackageHandleStandardArgs.cmake)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(Python3Interp REQUIRED_VARS PYTHON3_EXECUTABLE VERSION_VAR PYTHON3_VERSION_STRING)

mark_as_advanced(PYTHON3_EXECUTABLE)
