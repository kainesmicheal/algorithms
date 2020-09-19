#include <vector>
using namespace std;

void permutationsHelper(vector<int> &array,int i, vector<vector<int>>& permutations);
void swap(int i, int j, vector<int>& array);

vector<vector<int>> getPermutations(vector<int> array) {
  vector<vector<int>> permutations;
	permutationsHelper(array, 0, permutations);
	return permutations;
}

void permutationsHelper(vector<int>& array,int i, vector<vector<int>>& permutations)
{
	if(i == array.size() - 1){
		permutations.push_back(array);
	} else {
		for(int j = i; j < array.size(); j++) {
			swap(i,j,array);
			permutationsHelper(array, i + 1, permutations);
			swap(i,j,array);
		}
	}
}

void swap(int i,int j,vector<int>& array){
	int temp = array[i];
	array[i] = array[j];
	array[j] = temp;
}
//time complexity is o(n! * n)
//space compelxity is 0(n! * n)

#include <vector>
using namespace std;
void permutationsHelper(vector<int> array, vector<int> currentPermutation,vector<vector<int>>* permutations);

vector<vector<int>> getPermutations(vector<int> array) {
  vector<vector<int>> permutations;
	permutationsHelper(array,{},&permutations);
  return permutations;
}

void permutationsHelper(vector<int> array,vector<int> currentPermutation,
												vector<vector<int>>* permutations)
{
	if(array.size() == 0 && currentPermutation.size() > 0) {
		permutations->push_back(currentPermutation);
	}	else {
		for (int i = 0; i<array.size(); i++) {
			vector<int> newArray;
			newArray.insert(newArray.end(), array.begin(), array.begin() + i);
			newArray.insert(newArray.end(), array.begin()+i+1, array.end());
			vector<int> newPermutation = currentPermutation;
			newPermutation.push_back(array[i]);
			permutationsHelper(newArray, newPermutation, permutations);
		}
	}
}
//time complexity is o(n^2 * n!)
//space complexity is o(n! * n)
