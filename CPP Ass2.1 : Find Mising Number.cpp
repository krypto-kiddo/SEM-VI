#include <bits/stdc++.h>
using namespace std;

void printMissingElements(int arr[], int N)
{
	int b[arr[N - 1] + 1] = { 0 };
	for (int i = 0; i < N; i++) {
		b[arr[i]] = 1;
	}
	
	for (int i = arr[0]; i <= arr[N - 1]; i++) {
		if (b[i] == 0) {
			cout << i << " ";
		}
	}
}


int main()
{
	int arr[] = { 6, 7, 10, 13, 11};
	int n = sizeof(arr) / sizeof(arr[0]);
	sort(arr, arr + n);
	int N = sizeof(arr) / sizeof(int);
	printMissingElements(arr, N);
	return 0;
}

