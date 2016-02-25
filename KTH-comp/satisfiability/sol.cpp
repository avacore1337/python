#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>
#include <numeric>
#include <sstream>
#include <iterator>

int main (int argc, char const *argv[]){
  int rounds;
  using namespace std;

  std::cin >> rounds;
  for (size_t i = 0; i < rounds; i++) {
    int vars;
    int clauses;
    std::cin >> vars;
    std::cin >> clauses;
    vector<uint> positiveStates(clauses);
    vector<uint> negativeStates(clauses);
    string trash;
    getline(std::cin, trash);
    for (size_t j = 0; j < clauses; j++) {
      string in;
      getline(std::cin, in);
      // cerr << in << std::endl;
      stringstream lineStream(in);
      vector<string> strings;
      string word;
      while (lineStream >> word){
        if (word != "v") {
          strings.push_back(word);
        }
      }

      for(auto& s:strings){
        // cerr << s << " ";
        if (s[0] == '~'){
          s = s.substr(2);
          negativeStates[j] |= 1 << (stoi(s) - 1);
        }
        else{
          s = s.substr(1);
          positiveStates[j] |= 1 << (stoi(s) - 1);
        }
      }
      // cerr <<std::endl;
    }
    // for (size_t k = 0; k < clauses; k++) {
    //   cerr << positiveStates[k] << endl;
    //   cerr << negativeStates[k] << endl;
    // }
    bool success = false;
    for (size_t j = 0; j < int(pow(2, vars)); j++) {
      // vector<int> pStates(clauses);
      // vector<int> nStates(clauses);
      // copy(negativeStates.begin(), negativeStates.end(), nStates.begin());
      // copy(positiveStates.begin(), positiveStates.end(), pStates.begin());
      bool fail = false;
      for (size_t k = 0; k < clauses; k++) {
        // cerr << "j: " << j << "k: " << k << " result: " << (negativeStates[k] & ~j) << " " << (positiveStates[k] & j) << endl;
        if (((negativeStates[k] & ~j) + (positiveStates[k] & j)) == 0 ) {
          fail = true;
          break;
        }
      }
      if(!fail){
        success = true;
        // cerr << j << endl;
        break;
      }
    }
    if (success) {
      cout << "satisfiable" << endl;
    }
    else{
      cout << "unsatisfiable" << endl;
    }
    // for (size_t i = 0; i < clauses; i++) {
    //   cout << positiveStates[i] << std::endl;
    // }
  }
  return 0;
}
