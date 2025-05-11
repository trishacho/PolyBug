#include <SFML/Graphics.hpp>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include "random_image.h"

#define HELP_STR "--help"
#define MIN_CLA_COUNT 3
#define MAX_CLA_COUNT 3

int main(int argc, char *argv[]) {
  if(2 == argc && 0 == strcmp(HELP_STR, argv[1])){
    std::clog << "Usage: <width> <height> <filename>\n";
    return 1;
  }
  if(MIN_CLA_COUNT > argc-1 || argc-1 > MAX_CLA_COUNT){
    std::clog << "Error: Invalid number of arguments.\n";
    return -1;
  }
  int x = atoi(argv[1]), y = atoi(argv[2]);
  char *name = new char[strlen(argv[3]) + 1];
  strcpy(name, argv[3]);

  start_rand();
  sf::Image img = rand_imag(x, y);
  img.saveToFile(name);
  delete[] name;
  return 0;
}