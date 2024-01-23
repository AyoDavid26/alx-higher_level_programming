#include "lists.h"
#include <stdio.h>

void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);

/**
 * is_palindrome - code to check if a singly iinked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if palindrome, 0 if not palindrome
 */

int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t *tmp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	tmp = *head;
	middle = *head;

	for (len = 0; tmp != NULL; len++)
		tmp = tmp->next;

	len = len / 2;

	for (i = 1; i < len; i++)
		middle = middle->next;
	if(len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	reverse(&middle);
	i = compare_lists(*head, middle, len);

	return (i);
}

/**
 * Comparison - comparing two lists
 *
 * @head: head node
 * @middle: middle node
 * @len: list length
 * Return ifsame 1, if not; 0
 */

int compare_lists(listint_t *head, listint_t *middle, int len)
{
	int i;

	if (head == NULL || middle == NULL)
		return (1);
	for (i = 0; i < len; i++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}

/**
 * reverse - to reverse a list
 * @head: points to the head to reverse
 */
void reverse(listint_t **head)
{
	listint_t *curr;
	listint_t *next;
	listint_t *previous;

	if (head == NULL || *head == NULL)
		return;
	previous = NULL;
	curr = *head;
	while(curr != NULL)
	{
		next = curr->next;
		curr->next = previous;
		previous = curr;
		curr = next;
	}
	*head = previous;

}
