#include <iostream>
#include <vector>

using namespace std;

const int MAX = 8 + 1;


int N, M;
int arr[MAX];
void f(int cnt) {

	if (cnt == M) {
		for (int i = 0; i < M; i++) {
			cout << arr[i] << " ";
		}
		cout << "\n";
		return;
	}

	for (int i = (cnt == 0) ? 1 : arr[cnt - 1]; i <= N; i++) {
		arr[cnt] = i;
		f(cnt + 1);
	}
}

int main() {


	cin >> N >> M;
	f(0);
	return 0;

}
