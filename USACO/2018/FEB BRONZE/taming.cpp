#include <bits/stdc++.h>
using namespace std;

int x[100], y[100], z[100];

int main(){

	freopen("taming.in", "r", stdin);
	freopen("taming.out", "w", stdout);

	cin.tie(0)->sync_with_stdio(0);

    int n; cin >> n;
    for (int i = 1; i <= n; i++) {
		cin >> x[i];
	}

    y[1] = 1;
    for (int i = 1; i <= n; i++) {
		if(x[i] >= 0) {
			for (int j = i; j > i - x[i]; j--) {
				z[j] = 1;
			}
			y[i - x[i]] = 1;
		}
	}

    for (int i = 1; i <= n; i++) {
		if (y[i] && z[i]) {
			return cout << -1, 0;
		}
	} 

    int first = 0, second = 0;

    for (int i = 1; i <= n; i++) {
		first += y[i];
		second += !z[i];
	} 

    cout << first << " " << second;
}