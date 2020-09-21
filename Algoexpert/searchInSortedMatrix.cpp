#include <vector>
using namespace std;

vector<int> searchInSortedMatrix(vector<vector<int>> matrix, int target) {
  int row = 0;
	int col = matrix[0].size() - 1;
	while(row < matrix.size() && col >= 0) {
		if (matrix[row][col] > target) {
			col -= 1;
		} else if(matrix[row][col] < target ) {
			row += 1;
		} else {
			return vector<int> {row,col};
		}
	}
	return vector<int> {-1,-1};
}

//time complexity is 0(n + m)
//space complexity is o(1)
