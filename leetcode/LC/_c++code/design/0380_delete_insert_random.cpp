// insert value in vector and map value's index in key

#include <vector>
#include <unordered_map>
using namespace std;


class RandomizedSet {
public:
    vector <int> v;
    unordered_map <int, int> m;
    RandomizedSet() {
    }
    
    bool insert(int val) {
        if(m.find(val) == m.end()){
            v.push_back(val);    
            m[val] = v.size() - 1;
            return true;
        }return false;    
    }
    
    bool remove(int val) {
        if(m.find(val) != m.end()){
            int idx = m[val];
            int last = v.back();
            v[idx] = last;
            m[last] = idx;
            v.pop_back();
            m.erase(val);
            return true;
        }return false;
    }
    
    int getRandom() {
        return v[rand() % v.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */