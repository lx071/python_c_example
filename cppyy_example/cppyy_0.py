import cppyy

# 直接在ipython中写c++代码，cppyy会自动编译成python可以调用的模块，on-the-fly compilation
# 生成的模块接口和c++中定义的是一致的

cppyy.cppdef("""
std::vector<double> vec_dot(const std::vector<double> &vec1, const std::vector<double> &vec2){
    std::vector<double> ret;
    if (vec1.size() != vec2.size()) return ret;
    int size = vec1.size();
    for (int i=0;i<size;i++){
        ret.push_back(vec1[i] * vec2[i]);
    }
    return ret;
}
""")

# 使用上面定义的vec_dot

# cppyy.gbl 是global 命名空间，即时生成模块都在这里
vec_dot = cppyy.gbl.vec_dot
# vec_dot 使用了 std::vector 为入口和出口参数
Vector = cppyy.gbl.std.vector

# Vector[typename]()  Vector 是一个模板类，需要传入typename，但是python中使用[] 而不是<>
vec1 = Vector[float]([1.0, 2.0, 3.0, 4.0])
vec2 = Vector[float]([1.0, 3.0, 2.0, 4.0])

print(vec1, vec2)

# 可以转换成list，看到数据
print(list(vec1), list(vec2))

# 调用c++函数vec_dot
vec_ret = vec_dot(vec1, vec2)
print(list(vec_ret))
