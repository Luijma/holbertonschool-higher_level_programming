#include"lists.h"
/**
 * insert_node - inserts number into sorted linked list
 * @head: head of the list
 * @number: number to insert
 * Return: adress of new node, Null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *newnode;

	if (!head && !*head)
		return (NULL);
	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;

	while (current)
	{
		/* if not at the end or the beginning */
		if (current->next && prev)
		{
			if (number > prev->n && number < current->n)
			{
				prev->next = newnode;
				newnode->next = current;
				break;
			} else if (number == current->n)
			{
				prev->next = newnode;
				newnode->next = current;
				*head = newnode;
				break;
			}
		} else if(!prev && number <= current->n)
		{
			newnode->next = current;
			*head = newnode;
			break;
		} else if (!current->next)
		{
			current->next = newnode;
			newnode->next = NULL;
			break;
		}
		prev = current;
		current = current->next;
	}
	return (newnode);
}
