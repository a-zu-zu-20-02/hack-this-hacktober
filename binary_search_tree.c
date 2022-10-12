#include <stdio.h>
#include<conio.h>
#include <stdlib.h>

struct node{
    int key;
    struct node* left;
    struct node* right;
};

struct node* newnode(int data)
{
    struct node* pnewnode = (struct node*)malloc(sizeof(struct node));
    pnewnode->left = NULL;
    pnewnode->right = NULL;
    pnewnode->key = data;
    return pnewnode;
}
struct node* insert(struct node* bstnode,int key)
{
    if(bstnode == NULL) //if the tree is empty return newnode
        return newnode(key);
    //comparing with the root node key
    if(key < bstnode->key)
        bstnode->left = insert(bstnode->left,key);

    else if(key>bstnode->key)
        bstnode->right = insert(bstnode->right,key);

    return bstnode;
}

struct node* inorder(struct node* root)
{
    if(root == NULL)
        return NULL;
    inorder(root->left);
    printf("%d \t",root->key);
    inorder(root->right);


}
struct node* postorder(struct node* root)
{
    if(root == NULL)
        return NULL;
    postorder(root->left); //first recurring on the left child
    postorder(root->right);// and then recurring on the right child
    printf("%d \t",root->key);



}

int main()
{
    struct node* root = NULL;
    root = insert(root,50);
    insert(root,20);
    insert(root,30);
    insert(root,55);
    insert(root,60);
    insert(root,53);
    insert(root,15);

    inorder(root);
    printf("\n");
    postorder(root);

    return 0;
}
