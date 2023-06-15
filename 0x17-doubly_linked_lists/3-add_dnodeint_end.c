#include "lists.h"

/**
 * add_dnodeint_end - Add new node at end of list
 * @head: list head pointer
 * @n: node assigned number
 *
 * Return: address of new node
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new;
	dlistint_t *curr;

	new = malloc(sizeof(dlistint_t));

	if (new == NULL)
	{
		return (NULL);
	}
	
	new -> next = NULL;
	new -> n = n;
	if ((*head) == NULL)
	{
		new -> prev = NULL;
		*head = new;
		return (*head);
	}
	
	curr = *head;
	while (curr -> next != NULL)
	{
		curr = curr -> next;
	}
	new -> prev = curr;
	curr -> next = new;
	
	return (new);

}
