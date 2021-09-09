
#include"lists.h"
/**
 * insert_node - inserts number into sorted linked list
 * @head: head of the list
 * @number: number to insert
 * Return: adress of new node, Null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if(!newnode)
		return (NULL);
	newnode->n = number;

	if (!head)
	{
		newnode->next = NULL;
		*head = newnode;
		return (newnode);
	}

	while (current && current->next)
	{
		if (current->next->n < number)
			current = current->next;
		else
			break;
	}
	newnode->next = current->next;
	current->next = newnode;
	return (newnode);
}
