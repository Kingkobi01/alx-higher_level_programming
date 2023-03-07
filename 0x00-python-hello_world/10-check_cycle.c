#include "lists.h"

/**
 * check_cycle - Check if a linked list is a cycle
 * @list : list to be checked
 * Return: 1 if true and 0 if  false
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *new_tail, *temp_head;

	if (list == NULL || list->next == NULL)
		return (0);

	head = list;

	head = head->next;
	temp_head = list;

	while (head != NULL)
	{
		new_tail = head;

		while (list != new_tail)
		{
			if (head->next == list)
				return (1);

			list = list->next;
		}
		head = head->next;
		list = temp_head;
	}
	return (0);
}
