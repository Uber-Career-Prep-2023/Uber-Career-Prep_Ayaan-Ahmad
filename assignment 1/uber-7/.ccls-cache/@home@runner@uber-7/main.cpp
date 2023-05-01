#include<iostream>
#include<algorithm>

using namespace std;
int main() {
   string str1 = "debit curd";
  string str2 = "bad credit";


  //remove spaces 
str1.erase(remove(str1.begin(), str1.end(), ' '), str1.end());
str2.erase(remove(str2.begin(), str2.end(), ' '), str2.end());
  
  

  int count = 0;
   for (int i = 0;i < str1.length(); i++){
     for (int k = 0; k < str2.length(); k++) {
        if (str1[i] == str2[k]) {
          count++;
        }
     }
   }

  cout <<str1.length() << endl;
  cout << count << endl;

}