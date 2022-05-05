using namespace std;
#include<iostream>
#include<vector>

int main() {
    int even = 0;
    int odd = 0;

	int n; cin >> n;

	for(int i = 0; i < n; i++) {
		int cow; cin >> cow;
        if(cow % 2) odd++;
        else even++; 
	}

    while (even < odd) {
        even += 1;
        odd -= 2;
    }
	
    if (odd + 1 < even) even = odd + 1;

	cout << odd + even << '\n';

    return 0;
}