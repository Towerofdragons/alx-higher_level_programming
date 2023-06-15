#include "lists.h"

/**
 * add_dnodeint - Add node to list
 * @head: pointer to head ptr variable
 * @n: integer for created node
 *
 * Return: pointer to new list head
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL); /*upon malloc failure*/

	new -> n = n;
	new -> prev = NULL;

	if (*head == NULL)
	{
		new -> next = NULL;
		(*head) = new;
		return (*head);
	}
	new -> next = *head;
	(*head) -> prev = new;
	*head = new;
	return (*head);
}
