#include<iostream>
#define maxChar 254

using namespace std;
void Search(string main, string pattern, int prime, int array[], int* index)
{
	int patLen = pattern.size();
	int strLen = main.size();
	int charIndex, patHash = 0, strHash = 0, h = 1;
	for (int i = 0; i < patLen - 1; i++)
	{
		h = (h * maxChar) % prime;
	}
	for (int i = 0; i < patLen; i++)
	{
		patHash = (maxChar * patHash + pattern[i]) % prime;
		strHash = (maxChar * strHash + main[i]) % prime;
	}
	for (int i = 0; i <= (strLen - patLen); i++)
	{
		if (patHash == strHash)
		{
			for (charIndex = 0; charIndex < patLen; charIndex++)
			{
				if (main[i + charIndex] != pattern[charIndex]) break;
			}
			if (charIndex == patLen)
			{
				(*index)++;
				array[(*index)] = i;
			}
		}
		if (i < (strLen - patLen))
			{
				strHash = (maxChar * (strHash - main[i] * h) + main[i + patLen]) % prime;

					if (strHash < 0) strHash += prime;
			}
		}
	}

