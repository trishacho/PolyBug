cmake_minimum_required(VERSION 3.16)
project(NetworkStatParserTest)

find_package(Qt6 REQUIRED COMPONENTS Core Test)
add_executable(test_runner test_main.cpp)
target_link_libraries(test_runner Qt6::Core Qt6::Test)