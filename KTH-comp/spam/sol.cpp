#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <numeric>


int main (int argc, char const *argv[]){
  int minLength;

  std::cin >> minLength;
  char value;
  std::vector<int> v;
  while ( std::cin >> value ) {
    v.push_back(value == '1');
  }

  float theSum = 0;
  int index = 0;
  int length = minLength;

  for (size_t i = minLength; i < minLength*2; i++) {
    if (i > v.size()) {
      break;
    }
    // std::cout << "length: " << i << std::endl;
    std::vector<int> sums(v.size()-i + 1);
    sums[0] = std::accumulate(v.begin(), v.begin() + i, 0);
    // std::cout << "sums[0]: " << sums[0] << std::endl;
    // std::cerr << "test" << std::endl;
    for (size_t j = 1; j < v.size() - i + 1; j++) {
      sums[j] = sums[j-1] - v[j-1] + v[j+i - 1];
      // std::cerr << "sumj, j-1, j+i " << sums[j]  << " " << j-1 << " " << j+i -1  << std::endl;
    }
    for (size_t j = 0; j < sums.size(); j++) {
      /* code */
      float tmp = sums[j];
      // std::cerr << "sums: " << sums[j] << std::endl;
      tmp = tmp/i;
      // std::cout << "tmp: " << tmp << std::endl;
      if (tmp > theSum) {
        theSum = tmp;
        index = j;
        length = i;
      }
    }
    // std::cerr << std::endl;
  }
  std::cout << index + 1 << " " << length << std::endl;
  return 0;
}
