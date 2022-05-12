#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("race.in", "r", stdin);
	freopen("race.out", "w", stdout);
    int k, n, x, ans, res, i;
	cin >> k >> n;
	for (int idx = 0; idx < n; idx++) {
		cin >> x;
        res = 0, ans = 0;
        i = 1; 
        while (i < x && res < k) {
            res += i;
            ans ++;
            i ++;
        }
        i = x;
        while (res < k) {
            res += i;
            ans ++;
            if (res >= k) {
                break;
            }
            res += i;
            ans ++;
            i ++;
        }
		cout << ans << "\n";
	}
}