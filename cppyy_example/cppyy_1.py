import cppyy

cppyy.cppdef("""
class MyClass {
public:
    MyClass(int i) : m_data(i) {}
    virtual ~MyClass() {}
    virtual int add_int(int i) { return m_data + i; }
    int m_data;
};""")
# True

from cppyy.gbl import MyClass
m = MyClass(42)

cppyy.cppdef("""
void say_hello(MyClass* m) {
    std::cout << "Hello, the number is: " << m->m_data << std::endl;
}""")
# True

MyClass.say_hello = cppyy.gbl.say_hello
m.say_hello()
# Hello, the number is: 42

m.m_data = 13
m.say_hello()
# Hello, the number is: 13

class PyMyClass(MyClass):
    def add_int(self, i):  # python side override (CPython only)
        return self.m_data + 2*i

cppyy.cppdef("int callback(MyClass* m, int i) { return m->add_int(i); }")
# True

print(cppyy.gbl.callback(m, 2))             # calls C++ add_int
# 15

print(cppyy.gbl.callback(PyMyClass(1), 2))  # calls Python-side override
# 5
