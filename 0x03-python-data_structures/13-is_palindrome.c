#include "lists.h"
/**
 * is_palindrome - checks if linked list is palindrome
 * @head: head of linked list
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int flag = 1;
	listint_t *slower, *slowest, *faster;
	listint_t *middle = NULL, *lasthalf = NULL;

	if (!head || !*head)
		return (1);
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

	while (current)
	{
		fast = current->next;
		current->next = slow;
		slow = current;
		current = fast;
	}
	*head = slow;
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
