#include "lists.h"
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *curr;
	size_t count;
	
	curr = head;
	count = 0;
	while (count != index)
	{
		curr = curr -> next;
		if (curr == NULL)
		{
			return (NULL);
		}
		count++;
	}
	return (curr);
}
