cmake_minimum_required(VERSION 3.10)
project(RandomImageGen)

set(CMAKE_CXX_STANDARD 17)

# Add SFML
find_package(SFML 2.5 COMPONENTS graphics REQUIRED)

add_executable(RandomImageGen main.cpp random_image.cpp)
target_link_libraries(RandomImageGen sfml-graphics)

enable_testing()
add_executable(Tests test_main.cpp random_image.cpp)
target_link_libraries(Tests sfml-graphics)