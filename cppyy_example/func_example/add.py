import cppyy

cppyy.cppdef("""
int add(int i, int j)
{
    return i + j;
}""")

add = cppyy.gbl.add

for i in range(50000000):
    res = add(1, 2)

print('res =', res)
