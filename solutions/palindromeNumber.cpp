class Solution {
public:
    bool isPalindrome(int x) {
        bool palin = true;
        string s = to_string(x);
        int l = s.length();
        int j = l - 1;
        for (int i = 0; i < l / 2; i++){
            if (s[i] != s[j]){
               palin = false;
            }
            j--;
        }
        return palin;
    }
};