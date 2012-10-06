# Process this file with cmake
# Table of Contents
# [Basic Configuration]
cmake_minimum_required(VERSION 2.8.7)                                           # We use a fairly recent cmake, and I do not wish to assume anything.
set(CMAKE_MODULE_PATH                                                           # We must add our local module directory to the search path for the following to work.
    ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/Modules/")
find_package(Python3Interp REQUIRED)
find_package(Git)
find_package(Pandoc)
project(ticket Python3)
