#include <iostream>
#include <vector>
using namespace std;

int findmissing ( vector<int> nums, int n ) {
  for (int i = 0; i < n; i++) {
    // cout << "test: " << "vector value: " << nums[i] << "expecteed value" << i+1 << endl;
    if (!(nums[i] == i+1)) {
      
      return i+1;
    }
  }
}
int main() {

  vector<int> nums1 = {1, 2, 3, 4, 6, 7};
    int n1 = 7;
    cout << findmissing(nums1, n1) << endl; // 5

    vector<int> nums2 = {1};
    int n2 = 2;
    cout << findmissing(nums2, n2) << endl; // 2

    vector<int> nums3 = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12};
    int n3 = 12;
    cout << findmissing(nums3, n3) << endl; // 9

    return 0;

  
}