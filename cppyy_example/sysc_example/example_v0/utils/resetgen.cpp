/*
 * resetgen.cpp
 *
 *  Created on: 02.01.2019
 *      Author: eyck
 */

#include <resetgen.h>
// #include <scc/utilities.h>

ResetGen::ResetGen(const sc_core::sc_module_name& nm)
: sc_core::sc_module(nm)
, reset_o("reset_o")
{
    SC_THREAD(thread);
}

ResetGen::~ResetGen() {
}

void ResetGen::thread() {
    reset_o=1;
    wait();
    std::cout<<"XXX"<<std::endl;
    reset_o=0;
}
