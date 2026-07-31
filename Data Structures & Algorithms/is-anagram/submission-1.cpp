class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size()) return false;
        std::map<char,int>freq_s;
        std::map<char,int>freq_t;
        for(int i=0;i<s.size();i++){
            freq_s[s[i]]++;
            freq_t[t[i]]++;
        }
        return  freq_s==freq_t;
    }
};
