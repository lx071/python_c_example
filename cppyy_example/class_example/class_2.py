import cppyy

cppyy.cppdef("""

#include <stdint.h>
#include <iostream>
#include <string>

using namespace std;

//8个字节
typedef uint64_t CData;

class Signal
{
    public:
        //指针指向信号值
        CData* raw;
        Signal(CData *raw) : raw(raw){}
        Signal(CData &raw) : raw(std::addressof(raw)){}
        uint64_t getValue() {return *raw;}
        void setValue(uint64_t value)  {*raw = value; }
};

//模拟dut
class VMyTopLevel
{
    public:
        uint64_t io_A;
        uint64_t io_B;
        uint64_t io_X;
        uint64_t clk;
        uint64_t reset;
        VMyTopLevel()
        {
            io_A=5;
            io_B=6;
            io_X=7;
            clk=0;
            reset=1;
        }
        void eval() 
        {
            std::cout<<"step()"<<endl;
        }
};

class Wrapper
{
    public:
        std::string name;
        // 指针数组, 指向各个Signal
        Signal *signal[5];
        // 是否产生波形
        bool waveEnabled;
        //dut
        VMyTopLevel top;

        Wrapper(const char * name)
        {
            waveEnabled = true;
            signal[0] = new Signal(top.io_A);
            signal[1] = new Signal(top.io_B);
            signal[2] = new Signal(top.io_X);
            signal[3] = new Signal(top.clk);
            signal[4] = new Signal(top.reset);
            this->name = name;
        }
        // 析构函数在对象消亡时即自动被调用
        virtual ~Wrapper()
        {
            for(int idx = 0;idx < 5;idx++){
                delete signal[idx];
            }
        }
};

Wrapper* getHandle(const char * name)
{
    Wrapper* handle = new Wrapper(name);
    return handle;
}

void setValue(Wrapper* handle, int id, uint64_t newValue)
{
    handle->signal[id]->setValue(newValue);
}

uint64_t getValue(Wrapper* handle, int id)
{
    return handle->signal[id]->getValue();
}

bool eval(Wrapper* handle)
{
    handle->top.eval();
    return true;
//    return Verilated::gotFinish();
}

""")

from cppyy.gbl import getHandle, getValue, setValue, eval

p = getHandle('value')
for i in range(5):
    value = getValue(p, i)
    print(value)
setValue(p, 0, 11)
value = getValue(p, 0)
print(value)
eval(p)
