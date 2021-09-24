#include "lists.h"
/**
 * is_palindrome - checks if linked list is palindrome
 * @head: head of linked list
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int is_isnot = 0;
	int flag = 1;
	listint_t *slower;
	listint_t *slowest;
	listint_t *faster;
	listint_t *middle = NULL;
	listint_t *lasthalf = NULL;

	if (!head || !*head)
		return (0);
	slower = *head;
	slowest = *head;
	faster = *head;

	while (faster && faster->next)
	{
		faster = faster->next->next;
		slowest = slower;
		slower = slower->next;
	}
	if (faster != NULL)
	{
		middle = slower;
		slower = slower->next;
	}

	lasthalf = slower;
	slowest->next = NULL;
	/* SETTING FIRST HALF OF LIST */
	/* Reversing the list */
	turn_around(&lasthalf);
	flag = compare_lists(*head, lasthalf);

	turn_around(&lasthalf);

	if (middle)
	{
		slowest->next = middle;
		middle->next = lasthalf;
	}
	else
	{
		slowest->next = lasthalf;
	}
	return (flag);
}
/**
 * turn_around - reverses a linke dlist
 * @head: head of list to reverse
 */
void turn_around(listint_t **head)
{
	listint_t *slow = NULL;
	listint_t *current = *head;
	listint_t *fast;

	while (!current)
	{
		fast = fast->next;
		current->next = slow;
		slow = current;
		current = fast;
	}
	*head = slow;
}
