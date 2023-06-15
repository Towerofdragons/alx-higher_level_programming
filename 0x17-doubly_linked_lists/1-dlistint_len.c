#include "lists.h"
/**
 * size_t dlistint_len - returns the number of elements in list
 * @h : list head pointer
 *
 * Return: number of elements
 */

size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *curr;
	size_t count;

	curr = h;
	count = 0;

	while (curr != NULL)
	{
		count++;
		curr = curr -> next;
	}
	return count;
}
