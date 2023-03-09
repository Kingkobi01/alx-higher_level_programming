#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a new node into a sorted singly linked list
 * @head: Pointer to a pointer to the head node of the list
 * @number: The number to be inserted
 *
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *curr_node = *head;
	listint_t *prev_node = NULL;

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (curr_node != NULL && curr_node->n < number)
	{
		prev_node = curr_node;
		curr_node = curr_node->next;
	}

	if (prev_node == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev_node->next = new_node;
		new_node->next = curr_node;
	}

	return (new_node);
}
