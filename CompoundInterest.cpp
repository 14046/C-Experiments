#include <iostream>
#include <cmath>

using namespace std;

int main() {

	double Amount, Principle, Interest;
	int Days;
	int x = 1, y = 2, z = 4;

	cout << "Enter initial investment: ";
	cin >> Principle;
	cout << "Enter interest (%): ";
	cin >> Interest;
	cout << "Enter amount of days: ";
	cin >> Days;

	for (int i = 1; i <= Days; i++) {
		Amount = Principle * pow((1 + (Interest / 100)), i);
		printf("Day %i: %.2f\n", i, Amount);
	}
}