#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}

	return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
/**
 * compare_lists - compares list for reversal
 * @head_1: first head
 * @head_2: second head
 * Return: 1 if the same, 0 if not
 */
int compare_lists(listint_t *head_1, listint_t *head_2)
{
	listint_t *temp_1 = head_1;
	listint_t *temp_2 = head_2;

	if (!temp_1 && !temp_2)
	{
		return (1);
	}

	while (temp_1 && temp_2)
	{
		if (temp_1->n == temp_2->n)
		{
			temp_1 = temp_1->next;
			temp_2 = temp_2->next;
		}
		else
		{
			return (0);
		}
	}
	if (!temp_1 && !temp_2)
	{
		return (1);
	}
	return (0);
}
