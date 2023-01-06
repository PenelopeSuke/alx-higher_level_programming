#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node1 = *head, *new1;

	new1 = malloc(sizeof(listint_t));
	if (new1 == NULL)
		return (NULL);
	new1->n = number;

	if (node1 == NULL || node1->n >= number)
	{
		new1->next = node1;
		*head = new1;
		return (new1);
	}
	while (node1 && node1->next && node1->next->n < number)
		node1 = node1->next;
	new1->next = node1->next;
	node1->next = new1;
	return (new1);
}
