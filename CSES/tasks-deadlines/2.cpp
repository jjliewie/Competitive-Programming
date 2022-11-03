#include <bits/stdc++.h>
using namespace std;
#define pv vector<pair<int, int>>
#define ll long long int

int main(){
    int n, t, d;
    ll ans, cnt;
    cin >> n;
    pv arr(n);
    for (int i = 0; i < n; i++){
        cin >> t >> d;
		arr[i] = make_pair(t, d);
    }
    sort(arr.begin(), arr.end());
	ans = 0, cnt = 0;
	for (auto e : arr) {
		cnt += e.first;
	    ans += e.second - cnt;
	}
	cout << ans;
}