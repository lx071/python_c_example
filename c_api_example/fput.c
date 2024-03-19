#define PY_SSIZE_T_CLEAN
#include <Python.h>

/*
    PyObject is an object structure that you use to define object types for Python.
    PyObject tells the Python interpreter to treat a pointer to an object as an object.
    self is the module object.
    args is a tuple containing the actual arguments to your function.
*/
static PyObject *method_fputs(PyObject *self, PyObject *args) {
    // char *str is the string you want to write to the file stream.
    // char *filename is the name of the file to write to.
    char *str, *filename = NULL;
    int bytes_copied = -1;

    /* Parse arguments */
    /*
        PyArg_ParseTuple() parses the arguments you’ll receive from your Python program into local variables.
        "ss" is the format specifier that specifies the data type of the arguments to parse.
        &str and &filename are pointers to local variables to which the parsed values will be assigned.
    */
    if(!PyArg_ParseTuple(args, "ss", &str, &filename)) {
        return NULL;
    }

    FILE *fp = fopen(filename, "w");
    bytes_copied = fputs(str, fp);
    fclose(fp);

    // PyLong_FromLong() returns a PyLongObject, which represents an integer object in Python.
    return PyLong_FromLong(bytes_copied);
}


/* Writing the Init Function */

// the methods defined in your module
/*
    "fputs" is the name the user would write to invoke this particular function.
    method_fputs is the name of the C function to invoke.
    METH_VARARGS is a flag that tells the interpreter that the function will accept two arguments of type PyObject*: (PyObject *self, PyObject *args)
    The final string is a value to represent the method docstring.
*/
static PyMethodDef FputsMethods[] = {
    {"fputs", method_fputs, METH_VARARGS, "Python interface for fputs C library function"},
    {NULL, NULL, 0, NULL}
};

// a single structure that’s used for module definition
static struct PyModuleDef fputsmodule = {
    PyModuleDef_HEAD_INIT,    // a member of type PyModuleDef_Base
    "fputs",        // the name of your Python C extension module
    "Python interface for the fputs C library function",    // your module docstring
    -1,            // the amount of memory needed to store your program state
    FputsMethods    // the reference to your method table
};


// When a Python program imports your module for the first time, it will call PyInit_*()
PyMODINIT_FUNC PyInit_func(void) {
    // pass the address of the method structure
    // return a new module object of type PyObject *
    return PyModule_Create(&fputsmodule);
}