#include <bits/stdc++.h>
using namespace std;

int elevation[1001];
int ans = 1e9;

int main() {

    freopen("skidesign.in", "r", stdin);
	freopen("skidesign.out", "w", stdout);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> elevation[i];
	}
	
	for(int i = 0; i < 83; i++){

		int temp = 0;

		for (int j = 0; j < n; j++) {

			if(elevation[j] < i){
                temp += (i - elevation[j]) * (i - elevation[j]);
            }

			if(elevation[j] > i + 17){
                temp += (elevation[j] - i - 17) * (elevation[j] - i - 17);
            }
		}
		ans = min(ans, temp);
	}
	cout << ans;
}