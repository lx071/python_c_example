#include <memory>
#include "svdpi.h"
#include "verilated.h"
#include "VMyTopLevel.h"

using namespace std;

int main(int argc, char** argv)
{
    auto contextp {make_unique<VerilatedContext>()};
    contextp->commandArgs(argc, argv);
    //Verilated::traceEverOn(true);
    auto top {make_unique<VMyTopLevel>(contextp.get())};
    while(!contextp->gotFinish()){
        top->eval();
        contextp->timeInc(5000);
    }
    return 0;
}