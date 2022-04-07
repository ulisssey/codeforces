#include "bits/stdc++.h"
using namespace std;

#define ll long long
#define speed ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define all(x) x.begin(), x.end()
#define pb push_back
#define fi first
#define se second
int a[100][100];
int main(){
    int n;
    cin>>n;
    int x = n;

    for (int i = 1; i<=n*2+1; i++) {
        for (int j = 1; j<=n*2+1; j++) {
            int b = n*2+1-j;
            int c = n*2+1-i;

            cout<<x-min(b,min(c,min(i-1,j-1)));
        }
        cout<<endl;
    }

}