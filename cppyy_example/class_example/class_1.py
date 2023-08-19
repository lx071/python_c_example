import cppyy

cppyy.cppdef("""

#include <iostream>
using namespace std;

class MyClass 
{
public:
    MyClass() : m_data(0) {}
    virtual ~MyClass() {}
    virtual int add_int(int i) 
    { 
        cout << "i:" << i << endl;
        m_data = m_data + i;
        return m_data; 
    }
    void say_hello() {
        cout << "Hello, the number is: " << m_data << endl;
    }
    int m_data;
};

class Wrapper
{
public:
    std::string name;
    bool waveEnabled;
    MyClass top;

    Wrapper(const char * name)
    {
        waveEnabled = true;
        this->name = name;
    }

    virtual ~Wrapper()
    {
    }
};

void test()
{
    cout << "test()" << endl;
}

int main()
{
    test();
    return 0;
}

""")
# True

from cppyy.gbl import MyClass
from cppyy.gbl import test

m = MyClass()

m.say_hello()

print("add_int:", m.add_int(12))

m.say_hello()

test()
