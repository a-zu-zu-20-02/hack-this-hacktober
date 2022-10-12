#include <stdio.h>
#include <conio.h>
#include <stdlib.h>


struct node
{
    int data;
    struct node *next;
    struct node *prev;

};
struct node *head, *tail, *newnode, *temp, *nextnode;
int main()
{
    int ch;
    void create();
    void insert_beg();
    void insert_end();
    void insert_pos();
    void display();
    void delete_beg();
    void delete_end();
    void delete_pos();

    while(1)
    {
        printf("\n\n --------- Doubly Linked List --------");
        printf("\n 1.Create\n 2.Insert\n 3.Display \n 4.Delete \n 5.Exit\n\n");
        printf("Enter your choice(1-4):");
        scanf("%d", &ch);

        switch(ch){
            case 1:
                create();
                break;
            case 2:
                printf("\n----- Insert Menu------");
                printf("\n 1.Insert at beginning\n 2.Insert at end\n 3.Insert at specified position");
                printf("\n\n Enter your choice(1-3):");
                scanf("%d",&ch);

                switch(ch)
                {
                    case 1:
                        insert_beg();
                        break;
                    case 2:
                        insert_end();
                        break;
                    case 3:
                        insert_pos();
                        break;
                    default:
                        printf("Wrong choice");
                }
                break;
            case 3:
                display();
                break;
            case 4:
                printf("\n----- Delete Menu------");
                printf("\n 1.Delete from beginning\n 2.Delete from end\n 3.Delete from specified position");
                printf("\n\n Enter your choice(1-4):");
                scanf("%d",&ch);

                switch(ch)
                {
                case 1:
                    delete_beg();
                    break;
                case 2:
                    delete_end();
                    break;
                case 3:
                    delete_pos();
                    break;

                default:
                    printf("Wrong choice");
                }
                break;
             case 5:
                exit(0);
             default:
                printf("Wrong choice.");
        }
    }
    return 0;
}
void create()
{
    newnode = (struct node *)malloc(sizeof(struct node));
    printf("Enter the data:");
    scanf("%d", &newnode->data);
    newnode->prev = NULL;
    newnode->next = NULL;
    if(head == NULL)
    {
        head = tail = newnode;
    }
    else
    {
        tail->next = newnode;
        newnode->prev = tail;
        tail = newnode;
    }

}
void insert_beg()
{
    newnode = (struct node *)malloc(sizeof(struct node));
    printf("\nEnter data:");
    scanf("%d", &newnode->data);
    newnode->prev = NULL;
    head->prev = newnode;
    newnode->next = head;
    head = newnode;
}
void insert_end()
{
    newnode = (struct node *)malloc(sizeof(struct node));
    printf("\nEnter data:");
    scanf("%d", &newnode->data);
    newnode->prev = NULL;
    newnode->next = NULL;
    tail->next = newnode;
    newnode->prev = tail;
    tail = newnode;
}
void insert_pos()
{
    int pos, count=0, i=1;


    printf("\nEnter the position:");
    scanf("%d",&pos);
    temp = head;
    while(temp != NULL)
    {
        temp = temp->next;
        count++;
    }
    if(pos>count)
    {
        printf("Invalid position");
    }
    else if(pos==1)
    {
        insert_beg();
    }
    else
    {
        newnode = (struct node*)malloc(sizeof(struct node));
        printf("\nEnter data:");
        scanf("%d",&newnode->data);
        temp = head;
        while(i<pos-1)
        {
            temp = temp->next;
            i++;
        }
        newnode->prev = temp;
        newnode->next = temp->next;
        temp->next = newnode;
        newnode->next->prev = newnode;

    }
}
void display()
{
    temp = head;
    while(temp != NULL)
    {
        printf("%3d", temp->data);
        temp = temp->next;
    }
}

void delete_beg()
{
    if(head == NULL)
    {
        printf("List is empty");
    }
    else
    {
        temp = head;
        head = head->next;
        head->prev = NULL;
        free(temp);
    }
}
void delete_end()
{
    if(tail==NULL)
    {
        printf("List is empty.");
    }
    else
    {
        temp = tail;
        tail->prev->next = NULL;
        tail = tail->prev;
        free(temp);
    }
}
void delete_pos()
{
    int pos, i=1;
    printf("Enter the position:");
    scanf("%d",&pos);
    temp = head;
    while(i<pos)
    {
        temp = temp->next;
        i++;
    }
    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    free(temp);
}

