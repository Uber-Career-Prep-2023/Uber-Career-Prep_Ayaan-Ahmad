#include <iostream>

using namespace std;
int max_3(int position, int ind, int arr[]);
int main() {
  //sample array
  int arr[10] = {1, 1, 1, 1, -1, -1, 2, -1, -1, 6};
 //number of editions 
  int k = 5;

  //variable used to store largest su,
  int largest = 0;

  //loop that runs for arr length while skipping through every k numbers
  for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i = i + k) {

    //sees sum is larger then largest var
    if (max_3(i, k, arr) > largest) {
      largest = max_3(i, k, arr);
    }
  }

  cout << "largest pairing: " << largest/k;
  
    
  }


int max_3(int position,  int ind, int arr[]){
  int sum = 0;
  for (int m = position; m < (position+ind); m++){
    sum = sum + arr[m];
  }
  return sum;
}
