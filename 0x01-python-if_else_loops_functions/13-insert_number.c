#include "lists.h"

/**
 * insert_node - Inserts a number to a list
 * @head: A pointer the head 
 * @number: The number to enter.
 *
 * Return: NULL if the function fail or pointer in success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node1 = *h, *newn;

	newn = malloc(sizeof(listint_t));
	if (newn == NULL)
		return (NULL);
	newn->n = number;

	if (node1 == NULL || node1->n >= number)
	{
		new->next = node1;
		*h = newn;
		return (newn);
	}

	while (node1 && node1->next && node1->next->n < number)
		node1 = node1->next;

	newn->next = node1->next;
	n1ode->next = newn;

	return (newn);
}

