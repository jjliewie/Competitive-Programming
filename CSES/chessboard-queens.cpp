#include<bits/stdc++.h>
using namespace std;

int ans = 0;
bool cols[8], first_diagonal[15], second_diagonal[15];
char board[8][8];

void res(int row){
    if (row == 8) {
        ans ++;
        return;
    }

    for (int c = 0; c < 8; c++) {
        if (cols[c] || first_diagonal[row + c] || second_diagonal[c - row + 7] || board[row][c] == '*') {
            continue;
        }
        cols[c] = first_diagonal[row + c] = second_diagonal[c - row + 7] = true;
        res(row + 1);
        cols[c] = first_diagonal[row + c] = second_diagonal[c - row + 7] = false;
    }
}

int main(){
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            cin >> board[i][j];
        }
    }

    res(0);
    cout << ans;

    return 0;
}