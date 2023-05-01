#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool test(string s1, string s2) {
    //creating two stacks for each string
    stack<char> stack1, stack2;

    // fill stack1 with characters from s1 using a loop
    for (char c : s1) {
        if (c == '#') {
          
                stack1.pop();
          
        } else {
            stack1.push(c);
        }
    }

    // fill stack2 with characters from s2
    for (char c : s2) {
        if (c == '#') {
            
                stack2.pop();
            
        } else {
            stack2.push(c);
        }
    }

    // compare stacks
    while (!stack1.empty() && !stack2.empty()) {
        if (stack1.top() != stack2.top()) {
            return false;
        }
        stack1.pop();
        stack2.pop();
    }

    return stack1.empty() && stack2.empty();
}

int main() {
    // example tests
   string s1 = "abcde";
   string s2 = "abcde";
   cout << test(s1, s2) <<endl;  // true

    s1 = "Uber Career Prep";
    s2 = "u#Uber Careee#r Prep";
   cout << test(s1, s2) <<endl;  // true

    s1 = "abcdef###xyz";
    s2 = "abcw#xyz";
   cout << test(s1, s2) <<endl;  // true

    s1 = "abcdef###xyz";
    s2 = "abcdefxyz###";
   cout << test(s1, s2) <<endl;  // false

    return 0;
}