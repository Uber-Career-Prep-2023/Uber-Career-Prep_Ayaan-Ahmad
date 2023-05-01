#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<int> arr = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4};
  
int temp[arr.size()];
  
for (int i = 0; i < sizeof(temp)/sizeof(temp[0]); i++){
 temp[i] = -1;
  
}

int j = 0;
    for (int i = 0; i < arr.size() - 1; i++)
        if (arr[i] != arr[i + 1])
            temp[j++] = arr[i];
  
  
    temp[j++] = arr[arr.size() - 1];
  

for (int i = 0; i < sizeof(temp)/sizeof(temp[0]); i++){
  cout << temp[i]<< endl;
}
}
  
  