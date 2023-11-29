#include <stdio.h>
#include <mm_malloc.h>
#define MaxSize 100
typedef char ElemType;
typedef struct node
{
    ElemType data;
    struct node *lchild;
    struct node *rchild;
} BTNode;

void CreateBTree(BTNode *&b, char *str)
{
    BTNode *St[MaxSize], *p;
    int top = -1, j = 0, k;
    char ch;
    b = NULL;
    ch = str[j];
    while (ch != '\0')
    {
        switch (ch)
        {
        case '(':
            top++;
            St[top] = p;
            k = 1;
            break;
        case ')':
            top--;
            break;
        case ',':
            k = 2;
            break;
        default:
            p = (BTNode*)malloc(sizeof(BTNode));
            p->data = ch;
            p->lchild = p->rchild = NULL;
            if (b == NULL)
            {
                b = p;
            }else
            {
                switch (k)
                {
                case 1:
                    St[top]->lchild = p;
                    break;
                case 2:
                    St[top]->rchild = p;
                    break;
                }
            }
        }
        ch = str[++j];
    }
}

BTNode* FindNode(BTNode *b, ElemType x){
    BTNode *p;
    if (b == NULL)
    {
        return NULL;
    }else if (b->data == x)
    {
        return b;
    }else
    {
        p = FindNode(b->lchild, x);
        if(p != NULL)
            return p;
        else
            return FindNode(b->rchild, x);
    }
}

int BTHeight(BTNode *b){
    int lchildh, rchildh;
    if (b == NULL)
        return 0;
    else
    {
        lchildh = BTHeight(b->lchild);
        rchildh = BTHeight(b->rchild);
        return (lchildh > rchildh)?(lchildh+1):(rchildh+1);
    }
}

int BTNodeCount(BTNode *b){
    if (b == NULL){
        return 0;
    }else{
        return BTNodeCount(b->lchild) + BTNodeCount(b->rchild) + 1;
    }
}

void DispBTree(BTNode *b){
    if (b != NULL)
    {
        printf("%c", b->data);
        if(b->lchild != NULL || b->rchild != NULL)
        {
            printf("(");
            DispBTree(b->lchild);
            if(b->rchild != NULL)
                printf(",");
            DispBTree(b->rchild);
            printf(")");
        }
    }
}

void LevelOrder(BTNode *b){
    if(b == NULL) return;
    BTNode* queue[MaxSize];
    int front = 0, rear = 0;
    queue[rear++] = b;
    while(front != rear){
        BTNode *p = queue[front++];
        printf("%c ", p->data);
        if (p->lchild != NULL){
            queue[rear++] = p->lchild;
        }
        if (p->rchild != NULL){
            queue[rear++] = p->rchild;
        }
    }
}

void PreOrder(BTNode *b){
    if(b != NULL){
        printf("%c ", b->data);
        PreOrder(b->lchild);
        PreOrder(b->rchild);
    }
}

void PreOrderNonRecursive(BTNode *b){
    BTNode *St[MaxSize];
    int top = -1;
    St[++top] = b;
    while(top != -1){
        BTNode *p = St[top--];
        printf("%c ", p->data);
        if(p->rchild != NULL){
            St[++top] = p->rchild;
        }
        if(p->lchild != NULL){
            St[++top] = p->lchild;
        }
    }
}


void InOrder(BTNode *b){
    if(b != NULL){
        InOrder(b->lchild);
        printf("%c ", b->data);
        InOrder(b->rchild);
    }
}

void PostOrder(BTNode *b){
    if(b != NULL){
        PostOrder(b->lchild);
        PostOrder(b->rchild);
        printf("%c ", b->data);
    }
}

void DestroyBTree(BTNode *b){
    if (b != NULL){
        DestroyBTree(b->lchild);
        DestroyBTree(b->rchild);
        free(b);
    }
}

int main(){
    printf("1.请以括号表示法输入要建立的二叉树\n");
    BTNode *b;
    char str[MaxSize];
    scanf("%s", str);
    CreateBTree(b, str);
    printf("2.建立的二叉树如下：\n");
    DispBTree(b);
    printf("\n");
    printf("3.请输入要查找的节点：\n");
    char node;
    while ((getchar()) != '\n');
    scanf("%c", &node);
    BTNode *FoundNode = FindNode(b, node);
    if(FoundNode != NULL)
    {
        printf("查找到%c的节点,该节点的左右孩子分别为%c %c\n", node, FoundNode->lchild->data, FoundNode->rchild->data);
    }
    printf("4.该二叉树深度为%d\n", BTHeight(b));
    printf("5.操作结束，释放该二叉树\n");
    printf("6.该树有%d个节点\n", BTNodeCount(b));
    printf("7.层次遍历:\n");
    LevelOrder(b);
    DestroyBTree(b);
    return 0;
}