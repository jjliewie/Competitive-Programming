#include <iostream>
using namespace std;

int main() 
{

    freopen("billboard.in", "r", stdin);
	freopen("billboard.out", "w", stdout);

    int x1, y1, x2, y2;
    int x3, y3, x4, y4;

    cin >> x1 >> y1 >> x2 >> y2;
    cin >> x3 >> y3 >> x4 >> y4;

    if (x3 <= x1 && x2 <= x4) {   
        if (y1 < y4 && y3 < y1) {
            y1 = y4;
        }
        if (y3 < y2 && y2 < y4) {
            y2 = y3;
        }
    }
    if (y3 <= y1 && y2 <= y4) {
        if (x1 < x4 && x3 < x1) {
            x1 = x4;
        }
        if (x3 < x2 && x2 < x4) {
            x2 = x3;
        }
    }

    int ans = (x2 - x1) * (y2 - y1);

    cout << ans;

    return 0;
}