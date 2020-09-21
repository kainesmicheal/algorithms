#include<unordered_map>
#include<vector>
using namespace std;

class MinMaxStack {
public:
		vector<unordered_map<string, int>> minmax = {};
		vector<int> stack = {};
	
  int peek() {
    return stack[stack.size()-1];
  }

  int pop() {
    minmax.pop_back();
		int res = stack[stack.size() - 1];
		stack.pop_back();
		return res;
  }

  void push(int number) {
		unordered_map<string, int> newval = {{"max" , number},{"min" , number}};
		if (minmax.size()){
			unordered_map<string, int> lastval = minmax[minmax.size() - 1];
			newval["min"] = min(newval["min"],lastval["min"]);
			newval["max"] = max(newval["max"],lastval["max"]);
		}
		minmax.push_back(newval);
		stack.push_back(number);
  }

  int getMin() { 
    return minmax[minmax.size() - 1]["min"];
  }

  int getMax() {
    return minmax[minmax.size() - 1]["max"];
  }
};
//all methods run in o(1) time and o(1) space
