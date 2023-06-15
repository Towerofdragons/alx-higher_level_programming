#include "lists.h"

/**
 * free_dlistint - frees all elements of a list
 * @head: pointer to head
 *
 * Return: nothing
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *curr;
	dlistint_t *temp;
	curr = head;
	while (curr != NULL)
	{
		temp = curr -> next;
		free(curr);
		curr = temp;
	}
}
