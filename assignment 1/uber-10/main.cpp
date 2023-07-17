#include <iostream>
using namespace std;

int main() {
  int arr[10] = {4, 3, 3, 5, 7, 0, 2, 3, 8, 6};
  int k = 6;
  int cnt = 0;

   for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
        for (int j = i + 1; j < sizeof(arr) / sizeof(arr[0]); j++)
            if (arr[i] + arr[j] == k)
                cnt++; 


  cout << cnt;

  
}