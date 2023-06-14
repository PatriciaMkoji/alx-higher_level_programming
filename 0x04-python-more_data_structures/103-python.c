#include "python_info.h"
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - willprint the basic info
 * @p: PyObject represents the python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t measurement, idx;
	PyObject *the_item;

	if (!PyList_Check(p)) {
		printf("Invalid Python list object\n");
		return;
	}

	measurement = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the list = %zd\n", measurement);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (idx = 0; idx < measurement; idx++) {
		the_item = PyList_GetItem(p, idx);
		printf("Element %zd: %s\n", idx, Py_TYPE(the_item)->tp_name);
	}
}
/**
 * print_python_bytes - it will prints basic info
 * @p: PyObject represents the python bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t measurement, idx;
	char *byt;
	int maximum = 10;

	if (!PyBytes_Check(p)) {
		printf("Invalid Python bytes object\n");
		return;
	}

	measurement = PyBytes_Size(p);
	byt = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %zd\n", measurement);
	printf("  trying string: %s\n", byt);

	printf("  first %d bytes: ", maximum);
	for (idx = 0; idx < measurement && idx < maximum; idx++) {
		printf("%02hhx", byt[idx]);
		if (idx + 1 < measurement && idx + 1 < maximum)
			printf(" ");
	}
	printf("\n");
}
