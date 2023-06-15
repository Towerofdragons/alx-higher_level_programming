#include "lists.h"
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *curr;
	unsigned int count;

	curr = *head;
	count = 0;

	while (count !> index)
	{
		curr = curr -> next;
	}
}
