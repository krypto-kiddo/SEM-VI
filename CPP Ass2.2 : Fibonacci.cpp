#include<bits/stdc++.h>
using namespace std;
 
int fib(int n)
{
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-2);
}
 
int main ()
{

    int n;
    cin>>n;
    for(int x = 0; x<n; x++) {
        cout <<fib(x);
        cout <<" ";
    }
    getchar();
    return 0;
}
