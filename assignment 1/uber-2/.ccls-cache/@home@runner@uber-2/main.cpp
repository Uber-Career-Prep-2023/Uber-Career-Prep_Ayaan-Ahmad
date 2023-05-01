#include <iostream>
#include <string.h>
#include <vector>
using namespace std;
int main() {

  string str = "flamingo";



  //cout << str;

   cout << str << endl;

  // creating a vector with postions for all vowels
  vector<int> vows;

  // create loop that iterates throuh string, adding vowel position
  for (int i = 0; i < str.length(); i++) {
    if (str[i] == 'A' || str[i] == 'E' || str[i] == 'I' || str[i] == 'O' ||
        str[i] == 'U' || str[i] == 'a' || str[i] == 'e' || str[i] == 'i' ||
        str[i] == 'o' || str[i] == 'u') {
      vows.push_back(i);
    }
  }

  
  

  
  // create loop that runs for half vectors length that replaces strings given
  // position somehow?
  for (int m = 0; m < (vows.size())/2 ; m++) {

    // cout << m << "     ";
    // cout << vows.size()-m << "         ";
    // cout << vows[m] << "     ";
    // cout << vows[vows.size()-m-1] << "     ";
    // cout <<  str[vows[m]];
    // cout << str[vows[vows.size()-m-1]] << endl;


    char temp = str[vows[m]];

    str[vows[m]]= str[vows[vows.size()-m-1]];
    str[vows[vows.size()-m-1]] = temp;
    
    
  }


  cout << str;


}