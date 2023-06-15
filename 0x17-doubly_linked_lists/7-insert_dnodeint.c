#include "lists.h"

dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *curr;
	dlistint_t *new;
	unsigned int count;

	curr = *h;
	count = 0;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new -> n = n;

	while (count != idx)
	{
		curr = curr -> next;
		if (curr == NULL)
		{
			return (NULL);
		}
		count++;
	}

	new -> prev = curr;
	curr -> next -> prev = new; /* change address of next value after insertion of new to new's address*/
	new -> next = curr -> next;
	curr -> next = new;
	
	return (new);
}
