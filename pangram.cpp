#include <iostream>
#include <string>
using namespace std;

void pangram(string str)
{
    int arr[26] = {0};
    for (char i : str)
    {
        i = tolower(i);
        arr[i - 'a']++;
    }
    for (int i : arr)
    {
        if (i == 0)
        {
            cout << "not a pangram";
            return;
        }
    }
    cout << "pangram";
}

int main()
{
    string str = "";
    getline(cin, str);
    pangram(str);
    return 0;
}