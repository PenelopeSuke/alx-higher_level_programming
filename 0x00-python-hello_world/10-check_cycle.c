#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: A singly-linked list.
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *two, *one;

	if (list == NULL || list->next == NULL)
		return (0);

	two = list->next;
	one = list->next->next;

	while (two && one && one->next)
	{
		if (two == one)
			return (1);
		two = two->next;
		one - one->next->next;
	}
	return (0);
}
