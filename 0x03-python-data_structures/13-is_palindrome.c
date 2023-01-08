#include "lists.h"

/**
 * is_palindrome - checks if palindrome
 * @head: head of node
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	unsigned int cur = 1;
	listint_t *tem;

	if (head == NULL || *head == NULL)
		return (1);

	tem = *head;
	while (tem)
	{
		tem = tem->next;
		cur++;
	}
	return (0);
}
