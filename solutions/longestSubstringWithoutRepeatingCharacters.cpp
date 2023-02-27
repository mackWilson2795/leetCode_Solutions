#include <queue>
#include <unorderded_set>

using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
       queue<char> win;
       unordered_set<char> seen;
       if (size(s) == 0){
           return 0;
       }
       int max_len = 1;
       for (char c : s){
           if (seen.count(c)){
               while (win.front() != c){
                   seen.erase(win.front());
                   win.pop();
               }
               win.pop();
               seen.erase(c);
           }
           seen.insert(c);
           win.push(c);
           if (win.size() > max_len){
                  max_len = win.size();
                  }
       }
       return max_len;
    }
};