#include <bits/stdc++.h>
using namespace std;

string p[505], q[505];

int main() {

    freopen("cownomics.in", "r", stdin);
	freopen("cownomics.out", "w", stdout);

	int n, m, ans = 0;
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
        cin >> p[i];
    }

	for (int i = 0; i < n; i++){
        cin >> q[i];
    }

	for (int a = 0; a < m; a++){
        for (int b = a + 1; b < m; b++) {
            for (int c = b + 1; c < m; c++) {
                int tmp = 1;

                set<int> acgt;

                for (int i = 0; i < n; i++) {
                    acgt.insert(p[i][a] * 10000 + p[i][b] * 100 + p[i][c]);
                }

                for (int i = 0; i < n; i++) {
                    if (acgt.find(q[i][a] * 10000 + q[i][b] * 100 + q[i][c]) != acgt.end()) {
                        tmp = 0;
                    }
                } 

                ans += tmp;
            }
        } 
    } 

	cout << ans << endl;

	return 0;
}