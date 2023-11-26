#include <stdio.h>
#include <mm_malloc.h>

#define MaxSize 100
typedef char ElemType;
typedef struct node
{
    ElemType data;              //数据元素
    struct node *lchild;        //指向左孩子
    struct node *rchild;        //指向右孩子
} BTNode;
void CreateBTNode(BTNode *&b,char *str);        //由str串创建二叉链
BTNode *FindNode(BTNode *b,ElemType x);     //返回data域为x的节点指针
BTNode *LchildNode(BTNode *p);  //返回*p节点的左孩子节点指针
BTNode *RchildNode(BTNode *p);  //返回*p节点的右孩子节点指针
int BTNodeDepth(BTNode *b); //求二叉树b的深度
void DispBTNode(BTNode *b); //以括号表示法输出二叉树
void DestroyBTNode(BTNode *&b);  //销毁二叉树

void CreateBTNode(BTNode *&b,char *str)     //由str串创建二叉链
{
    BTNode *St[MaxSize], *p;
    int top = -1, j = 0, k;
    b = NULL;
    char ch = str[j];
    while(ch != '\0'){
        switch(ch)
        {
            case '(':
                top++;
                St[top] = p;
                k = 1;
                break;
            case ',':
                k = 2;
                break;
            case ')':
                top--;
                break;
            default:
                p = (BTNode*)malloc(sizeof(BTNode));
                p->data = ch;
                p->lchild = p->rchild = NULL;
                if(b == NULL){
                    b = p;
                }else{
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
BTNode *FindNode(BTNode *b,ElemType x)  //返回data域为x的节点指针
{
    BTNode *p;
    if (b == NULL)
        return NULL;
    else if (b->data == x)
        return b;
    else
    {
        p = FindNode(b->lchild, x);
        if (p != NULL)
            return p;
        else
            return FindNode(b->rchild, x);
    }
}
BTNode *LchildNode(BTNode *p)   //返回*p节点的左孩子节点指针
{
    return p->lchild;
}
BTNode *RchildNode(BTNode *p)   //返回*p节点的右孩子节点指针
{
    return p->rchild;
}
int BTNodeDepth(BTNode *b)  //求二叉树b的深度
{
    int lchildh, rchildh;
    if (b==NULL)
        return 0;
    else
    {
        lchildh = BTNodeDepth(b->lchild);
        rchildh = BTNodeDepth(b->rchild);
        return (lchildh > rchildh)?(lchildh + 1):(rchildh + 1);
    }
}
void DispBTNode(BTNode *b)  //以括号表示法输出二叉树
{
    if(b != NULL)
    {
        printf("%c", b->data);
        if (b->lchild != NULL || b->rchild != NULL)
        {
            printf("(");
            DispBTNode(b->lchild);
            if(b->rchild != NULL)
                printf(",");
            DispBTNode(b->rchild);
            printf(")");
        }
    }
}
void DestroyBTNode(BTNode *&b)   //销毁二叉树
{
    if (b != NULL)
    {
        DestroyBTNode(b->lchild);
        DestroyBTNode(b->rchild);
        free(b);
    }
}

int main(){
    printf("1.请以括号表示法输入要建立的二叉树\n");
    BTNode *b;
    char str[MaxSize];
    scanf("%s", str);
    CreateBTNode(b, str);
    printf("2.建立的二叉树如下：\n");
    DispBTNode(b);
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
    printf("4.该二叉树深度为%d\n", BTNodeDepth(b));
    printf("5.操作结束，释放该二叉树");
    DestroyBTNode(b);
    return 0;
}

