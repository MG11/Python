#include <climits>
#include <iostream>
#include <vector>
using namespace std;

// http://www.vishalchovatiya.com/single-responsibility-principle-in-cpp-solid-as-a-rock/
/* 
 class should have only one reason to change

In other words, SRP states that classes should be cohesive to
 the point that it has a single responsibility, where responsibility defines as “a reason for the change.”
*/

class Journal {
    string          m_title;
    vector<string>  m_entries;

public:
    Journal(){}
    Journal(const string &title) : m_title{title} {}
    void add_entries(const string &entry) {
        static int count = 1;
        m_entries.push_back(to_string(count++) + ": " + entry);
    }
    auto get_entries() const { return m_entries; }
    
    // save should be moved to some other class so, that if we want to save in other way, we can do that.
    // void save(const string &filename) {
    //     // save data in file but a file can have different ways of saving, if in future we want some
    //     // other way to save, that will violate the single responsibility principle.
    //     cout<<"saved in file";
    // }
};

class SaveManager : public Journal{

    public:
        void save(const Journal& j){
            cout<< "saved in book";
        }

};



int  main() {
    Journal journal{"Dear XYZ"};
    journal.add_entries("I ate a bug");
    journal.add_entries("I cried today");
    // journal.save("diary.txt");
    SaveManager s;
    s.save(journal);
    return 0;
}
