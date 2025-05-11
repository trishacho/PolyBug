#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include <fstream>
#include <sstream>
#include <iostream>
#include <filesystem>

int main(int argc, char* argv[]);

TEST_CASE("Help argument triggers help message", "[main]") {
    const char* argv[] = {"prog", "--help"};
    int argc = 2;

    std::stringstream log_stream;
    std::streambuf* old_buf = std::clog.rdbuf(log_stream.rdbuf());

    int result = main(argc, const_cast<char**>(argv));
    std::clog.rdbuf(old_buf);

    REQUIRE(result == 1);
    REQUIRE(log_stream.str().find("Usage") != std::string::npos);
}

TEST_CASE("Invalid argument count", "[main]") {
    const char* argv[] = {"prog"};
    int argc = 1;

    std::stringstream log_stream;
    std::streambuf* old_buf = std::clog.rdbuf(log_stream.rdbuf());

    int result = main(argc, const_cast<char**>(argv));
    std::clog.rdbuf(old_buf);

    REQUIRE(result == -1);
    REQUIRE(log_stream.str().find("Error") != std::string::npos);
}

TEST_CASE("Valid image generation", "[main]") {
    const char* filename = "test_output.png";
    const char* argv[] = {"prog", "64", "64", filename};
    int argc = 4;

    int result = main(argc, const_cast<char**>(argv));
    REQUIRE(result == 0);
    REQUIRE(std::filesystem::exists(filename));
    std::filesystem::remove(filename);
}