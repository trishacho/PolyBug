#include "random_image.h"
#include <cstdlib>
#include <ctime>

void start_rand() {
    std::srand(static_cast<unsigned>(std::time(nullptr)));
}

sf::Image rand_imag(int width, int height) {
    sf::Image image;
    image.create(width, height, sf::Color::Black);
    for(int y = 0; y < height; ++y){
        for(int x = 0; x < width; ++x){
            sf::Color color(std::rand()%256, std::rand()%256, std::rand()%256);
            image.setPixel(x, y, color);
        }
    }
    return image;
}