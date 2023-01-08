#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int size, all, k;
	PyObject *object;

	size = Py_SIZE(p);
	all = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", all);

	for (k = 0; k < size; k++)
	{
		printf("Element %d: ", k);

		object = PyList_GetItem(p, k);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
