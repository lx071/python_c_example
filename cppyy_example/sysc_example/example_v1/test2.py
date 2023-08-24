# -*- coding: utf-8 -*-

import cppyy
from cppyy import gbl as cpp
import os

myDir = os.path.dirname( os.path.realpath(__file__))

cppyy.add_include_path('/usr/local/systemc-2.3.4/include')
cppyy.add_library_path('/usr/local/systemc-2.3.4/lib-linux64')
cppyy.load_library('systemc')

# Loading Components lib
cppyy.add_include_path(os.path.join(myDir, 'utils'))
cppyy.load_library(os.path.join(myDir, 'utils/lib_utils.so'))

# print('path:', os.path.join(myDir, 'utils'))

cppyy.cppdef("""

#include <systemc.h>
#include "clkgen.h"
#include "resetgen.h"


SC_MODULE(Counter) {
    sc_in<bool> clock;  // 输入时钟信号
    sc_in<bool> reset; // 输入复位信号
    sc_out<int> count; // 输出计数值

    int counter; // 计数器变量

    void count_process() {
        while (true) {
            if (reset.read()) { // 如果复位信号为高电平
                counter = 0;    // 计数器清零
            } else {
                counter++; // 计数器加1
            }

            count.write(counter); // 将计数器值写入输出端口

            cout << "Counter: " << counter << endl; // 打印计数器值

            wait(); // 等待下一个时钟周期
        }
    }

    SC_CTOR(Counter) {
        SC_THREAD(count_process); // 注册计数进程
        sensitive << clock.pos(); // 对上升沿敏感
    }
};

""")


###############################################################################
# instantiate
###############################################################################
clkgen = cpp.ClkGen(cpp.sc_core.sc_module_name("clk_gen"))
rstgen = cpp.ResetGen(cpp.sc_core.sc_module_name("rst_gen"))
counter = cpp.Counter(cpp.sc_core.sc_module_name("counter"))
###############################################################################
# signals
###############################################################################
sig_clk = cpp.sc_core.sc_signal[cpp.bool]("clk")
sig_rst = cpp.sc_core.sc_signal[cpp.bool]("rst")
sig_count = cpp.sc_core.sc_signal[cpp.int]("count")
###############################################################################
# connect it
###############################################################################
clkgen.clk_o(sig_clk)
rstgen.reset_o(sig_rst)

counter.clock(sig_clk)
counter.reset(sig_rst)
counter.count(sig_count)

if __name__ == "__main__":
    # cpp.sc_main()
    # cpp.sim_start(50)
    cpp.sc_core.sc_start()

    