cmake_minimum_required(VERSION 3.25)


project(RTFluid)

add_executable(fluid main.cpp)

add_subdirectory("./gvdb_library")