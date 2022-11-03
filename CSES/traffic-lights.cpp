#include <bits/stdc++.h>
using namespace std;

multiset<int> dist;
set<int> all;

int main(){
	int x, n;
	cin >> x >> n;
	all.insert(0);
	all.insert(x);
	dist.insert(x);
	for(int i = 0; i < n; i++) {
		int light, pval, nval;
		cin >> light;
		all.insert(light);
		auto loc = all.find(light);
        nval = *next(loc);
		pval = *prev(loc);
		dist.erase(dist.find(nval-pval));
        dist.insert(nval-light);
		dist.insert(light-pval);
		cout << *dist.rbegin() << " ";
	}
	cout << endl;
}