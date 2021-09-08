#include "lists.h"
/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: linked list to check
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *prev = list;

	if (!list)
		return (0);
	current = list->next;

	while (current && prev && current->next)
	{
		if (current == prev)
			return (1);
		prev = prev->next;
		current = current->next->next;
	}
	return (0);
}
