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
    scanf("%c", &node);
    BTNode *FoundNode = FindNode(b, node);
    if(FoundNode != NULL)
    {
        printf("查找到%c的节点,该节点的左右孩子分别为%c %c\n", node, FoundNode->lchild->data, FoundNode->rchild->data);
    }
    printf("4.该二叉树深度为%d\n", BTHeight(b));
    printf("5.操作结束，释放该二叉树");
    DestroyBTree(b);
    return 0;
}