#include <iostream>
#include <vector>

int sumDivs(int n);
bool contains(std::vector<int> v, int n);
int amicable(int n);
int euler21(void);

int main(void) {
	std::cout << euler21() << std::endl;
	return 0;
}

int sumDivs(int n) {
	int sum = 0;
	for (int i = 1; i < n; i++) {
		if (n % i == 0) {
			sum += i;
		}
	}
	return sum;
}

bool contains(std::vector<int> v, int n) {
	for (int i = 0; i < v.size(); i++) {
		if (v[i] == n) {
			return true;
		}
	}
	return false;
}

int amicable(int n) {
	int total = sumDivs(n);
	if (sumDivs(total) == n) {
		return total;
	}
	return -1;
}

int euler21(void) {

	std::vector<int> seen;
	int total = 0;

	for (int i = 0; i < 10000; i++) {

		int x = amicable(i);

		if (x != -1 && x != i) {
			
			if (!contains(seen, x)) {
				total += x + i;
				seen.push_back(x);
				seen.push_back(i);
			}

		}

	}
	return total;
}
