#include <Python.h>

// https://medium.com/@wansac/the-python-c-api-a-brief-introduction-7926ea0ef488

// C equivalent of calling platform.system() in Python 3.8

int main()
{
    // Py_Initialize must be called before any other 
    // Python C/API functions
    Py_Initialize();

    // Equivalent of "import platform" in Python
    PyObject * platform_module = PyImport_ImportModule("platform");
    if(!platform_module) {
        // The import failed.
        // Double check spelling in import call and confirm
        // you can import platform in Python on system.
        printf("\nCould not import platform module.\n");
        return 0;
    }

    PyObject* system_function = PyObject_GetAttrString(platform_module, "system");
    if(system_function && PyCallable_Check(system_function)) {

        // Call platform.system()
        PyObject * system_obj = PyObject_CallObject(system_function, NULL);

        // Convert PyObject * returned by above call into a human-readable string
        // we can print to stdin
        PyObject* str = PyUnicode_AsEncodedString(system_obj, "utf-8", "~E~");
        const char * system_str = PyBytes_AS_STRING(str);
        printf("\n\nPlatform name is %s \n\n", system_str);

        // Decrement reference counts for objects we are 
        // done using to allow garbage collection to dispose of them
        Py_XDECREF(system_function);
        Py_XDECREF(system_obj);
        Py_XDECREF(str);
    } else {
        // Something has gone wrong.
        // Double check spelling in PyObject_GetAttrString and try
        // calling platform.system() in Python.
        printf("\nCould not call platform.system() function.\n");
    }

    return 0;
}