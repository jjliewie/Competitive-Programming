#include <bits/stdc++.h>
using namespace std;
map<long long, long long> m;

int main(){
    int n; cin >> n;
    for (int i = 0; i < n; i++){
        int q; cin >> q;
        if (q != 0) {
            long long key;
            cin >> key;
            cout << m[key] << endl;
            continue;
        }
        long long key, val;
        cin >> key >> val;
        m[key] = val;
    }
    return 0;
}