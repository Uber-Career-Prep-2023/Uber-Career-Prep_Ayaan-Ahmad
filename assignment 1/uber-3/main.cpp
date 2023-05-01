#include <iostream>
 #include <vector>
using namespace std;

int main() {
   vector <int> arr = {8, -5, 0, -2, 3, -4};

int subs = 0;
int sum = 0; 
  int index;
for (int j = 0; j <arr.size(); j++) {
for (int i = j; i < arr.size() ; i++){
  sum = sum + arr[i];
  if (sum == 0) {
    subs++;
  }
  
  }
  sum = 0;
  
}
cout << subs;
  }
  
  
