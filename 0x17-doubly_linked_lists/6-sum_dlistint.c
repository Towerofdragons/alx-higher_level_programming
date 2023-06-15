#include "lists.h"

/**
 * sum_dlistint - sums all integers of a list
 * @head: list head pointer
 *
 * Return: sum of all elements
 */ 
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *curr;
	int sum;

	curr = head;
	sum = 0;
	while (curr != NULL)
	{
		sum += curr -> n;
		curr = curr -> next;
	}

	return (sum);
}
