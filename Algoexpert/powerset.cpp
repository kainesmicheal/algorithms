#include <vector>
using namespace std;

vector<vector<int>> powerset(vector<int> array) {
  if (array.size() < 0){
		return vector<vector<int>> {{}}; 
	}
	else{
		vector<vector<int>> subset = {{}};
		for (int x : array)
		{
			int len = subset.size();
			for (int i = 0; i<len; i++){
				vector<int> current = subset[i];
				current.push_back(x);
				subset.push_back(current);
			}
		}
			return subset;
	}

}


vector<vector<int>> helper(vector<int> array, int idx);


vector<vector<int>> powerset(vector<int> array) {
	return helper(array, array.size() - 1);
}


vector<vector<int>> helper(vector<int> array, int idx){
	if(idx < 0)
	{
		return vector<vector<int>> {{}};
	}
	else
	{
		int elm = array[idx];
		vector<vector<int>> subSet = helper(array, idx - 1);
		int len = subSet.size();
		for (int i = 0; i< len; i++)
		{
			vector<int> current = subSet[i];
			current.push_back(elm);
			subSet.push_back(current);
		}
		return subSet;	
	}
}

//time complexity is o(2^n * n)
//space complexity is o(2^n * n)
