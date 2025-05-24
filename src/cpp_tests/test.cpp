#include <iostream>
#include <string>
#include <cstdlib>
//to compile the file: g++ test.cpp -o output $(python3.12-config --cflags --ldflags)

int access_to_files(std::string &filename, std::string &command){
  command += filename;
  return std::system(command.c_str());
}
