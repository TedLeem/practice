#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX_SIZE 21

int n;
bool visitied[MAX_SIZE];
int s[MAX_SIZE][MAX_SIZE];
int ans = 987654321;
int total = 0;

void Dfs(int cur, int cnt)
{
	// n/2명을 뽑았으면 차이를 계산
	if (cnt == n / 2)
	{
		vector<int> start_team, link_team;
		total++;
		// 뽑은 선수들은 스타트팀과 링크팀으로
		for (int i = 1; i <= n; i++)
		{
			if (visitied[i]) start_team.push_back(i);
			else link_team.push_back(i);
		}

		for (auto x:start_team){
			cout << x << " ";
		}
		cout << endl << endl;
		for (auto x : link_team) {
			cout << x << " ";
		}
		cout << endl << endl;
		cout << endl << endl;
		int stat_start = 0, stat_link = 0;
		for (int i = 0; i < start_team.size(); i++)
		{
			for (int j = 0; j < start_team.size(); j++)
			{
				int start_x = start_team[i]-1, start_y = start_team[j]-1;
				int link_x = link_team[i]-1, link_y = link_team[j]-1;
				stat_start += s[start_x][start_y] + s[start_y][start_x];
				stat_link += s[link_x][link_y] + s[link_y][link_x];
			}
		}

		cout << stat_start << endl;
		cout << stat_link << endl << endl;

		ans = min(ans, abs(stat_start - stat_link));
		return;

	}

	// 완전탐색
	for (int i = cur + 1; i <= n; i++)
	{
		if (visitied[i] == false)
		{
			visitied[i] = true;
			Dfs(i, cnt + 1);
			visitied[i] = false;
		}
	}

}
int main()
{
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> s[i][j];
		}
	}

	visitied[1] = true;
	Dfs(1, 1);
	cout << ans;

	return 0;
}