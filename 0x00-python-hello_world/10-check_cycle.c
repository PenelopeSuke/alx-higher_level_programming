#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: A singly-linked list.
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *two = list;
	listint_t *one = list;

	if (!list)
		return (0);

	while (two && one && one->next)
	{
		two = two->next;
		one = one->next->next;
		if (two == one)
			return (1);
	}
	return (0);
}
