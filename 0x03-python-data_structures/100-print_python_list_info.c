#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about a Python list
 * @p: Pointer to the PyObject representing the list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t sz, idx;
	PyObject *objitem;

	sz = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", sz);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (idx = 0; idx < sz; idx++)
	{
		objitem = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(objitem)->tp_name);
	}
}

