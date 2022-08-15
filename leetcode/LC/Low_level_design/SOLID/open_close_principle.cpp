#include <climits>
#include <iostream>
#include <vector>
using namespace std;

enum class COLOR {RED, BLACK, BLUE};
enum class SIZE {BIG, MEDIUM, SMALL};

// http://www.vishalchovatiya.com/open-closed-principle-in-cpp-solid-as-a-rock/

// classes should be open for extension, closed for modification


class Product {
    public:
    string name;
    COLOR color;
    SIZE size;

    Product(){};
    Product(string name, COLOR c, SIZE s){
        this->name = name;
        this->size = s;
        this->color = c;
    }
};

class filter {
    public:
    static vector<Product*> by_size(const vector<Product* > p, SIZE s){
        vector<Product *> result;
        for(auto &i : p){
            if(i->size == s)
                result.push_back(i);
        }
        return result;
    }

     static vector<Product*> by_color(const vector<Product* > p, COLOR c){
        vector<Product *> result;
        for(auto &i : p){
            if(i->color == c)
                result.push_back(i);
        }
        return result;
    }
};

class Specification{
        public:
        virtual bool is_satisfied(Product* item) const = 0;
    };

class ColorSpecification : public Specification{
    public:
    COLOR color;
    ColorSpecification(COLOR c){
        color = c;
    }
    bool is_satisfied(Product* item) const{
        return item->color == color; 
    }
};

class SizeSpecification : public Specification{
    public:
    SIZE size;
    SizeSpecification(SIZE c){
        size = c;
    }
    bool is_satisfied(Product* item) const{
        return item->size == size; 
    }
};


class filterSpecification{
    public:
    static vector <Product*> filterData(const vector<Product*> &p ,const Specification &s){
        vector <Product *> result;
        for(auto &i : p){
            if(s.is_satisfied(i))
                result.push_back(i);
        }
        return result;
    }
};

int main(){
    vector<Product*> v = {
        new Product("laptop", COLOR::BLACK, SIZE::SMALL),
        new Product("Apple", COLOR:: RED, SIZE:: SMALL),
        new Product("House", COLOR::BLACK, SIZE:: BIG),
    };

    // vector <Product *> ans = filter::by_size(v, SIZE::SMALL);
    // for(int i = 0; i< ans.size(); i++){
    //     cout<<ans[i]->name<<" "<<endl;
    // }

    vector <Product *> ans = filterSpecification::filterData(v, ColorSpecification(COLOR::RED));
    for(int i = 0; i< ans.size(); i++){
        cout<<ans[i]->name<<" "<<endl;
    }

}
