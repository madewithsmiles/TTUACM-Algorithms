#include <iostream>
#include <string>

int euler4(void);
bool palindrome(std::string s);

int main(void) {
  std::cout << euler4() << std::endl;
  return 0;
}

bool palindrome(std::string s) {
  return s == std::string(s.rbegin(), s.rend());
}

int euler4(void) {
  
  int largest = 0;
  
  for (int i = 100; i <= 999; i++) {
    for (int j = 100; j <= 999; j++) {
      
      int prod = i * j;
      if (palindrome(std::to_string(prod))) {
        if (prod > largest) {
          largest = prod;
        }
      }
    }
  }
  return largest;
}
