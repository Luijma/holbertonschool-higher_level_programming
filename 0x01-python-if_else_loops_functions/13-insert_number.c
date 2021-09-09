#include"lists.h"
/**
 * insert_node - inserts number into sorted linked list
 * @head: head of the list
 * @number: number to insert
 * Return: adress of new node, Null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if(!newnode)
		return (NULL);

	current = *head;
	newnode->n = number;

	if (!current)
	{
		newnode->next = current;
		*head = newnode;
		return (newnode);
	}

	/* This while loop is probably the issue, I can't
	 * quite get it to work for the last 2 checkers
	 * if it doesnt work check in the morning
	 */
	while (curent && current->next && current->next->n < number)
	{
		current = current->next;
	}
	newnode->next = current->next;
	current->next = newnode;
	return (newnode);
}
