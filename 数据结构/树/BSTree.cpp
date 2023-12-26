//二叉排序树算法
#include <stdio.h>
#include <mm_malloc.h>
typedef int KeyType;
typedef char InfoType[10];

typedef struct node
{
	KeyType key;              		//关键字项
	InfoType data;             		//其他数据域
	struct node *lchild,*rchild;	//左右孩子指针
} BSTNode;           				//二叉排序树结点类型
bool InsertBST(BSTNode *&bt,KeyType k)
//在二叉排序树bt中插入一个关键字为k的结点。插入成功返回真，否则返回假
{	if (bt==NULL)						//原树为空，新插入的结点为根结点
	{	bt=(BSTNode *)malloc(sizeof(BSTNode));
		bt->key=k; bt->lchild=bt->rchild=NULL;
		return true;
	}
	else if (k==bt->key) 				//树中存在相同关键字的结点，返回假
		return false;
	else if (k<bt->key)
		return InsertBST(bt->lchild,k);	//插入到左子树中
	else
		return InsertBST(bt->rchild,k);	//插入到右子树中
}

BSTNode *CreateBST(KeyType A[],int n)		//创建二叉排序树
//返回BST树根结点指针
{	BSTNode *bt=NULL;				//初始时bt为空树
	int i=0;
	while (i<n)
	{	InsertBST(bt,A[i]);			//将关键字A[i]插入二叉排序树bt中
		i++;
	}
	return bt;						//返回建立的二叉排序树的根指针
}

void DispBST(BSTNode *bt)		//输出一棵排序二叉树
{
	if (bt!=NULL)
	{	printf("%d",bt->key);
		if (bt->lchild!=NULL || bt->rchild!=NULL)
		{	printf("(");						//有孩子结点时才输出(
			DispBST(bt->lchild);				//递归处理左子树
			if (bt->rchild!=NULL) printf(",");	//有右孩子结点时才输出,
			DispBST(bt->rchild);				//递归处理右子树
			printf(")");						//有孩子结点时才输出)
		}
	}
}
BSTNode *SearchBST(BSTNode *bt,KeyType k)
{
    if (bt==NULL || bt->key==k)      	//递归终结条件
		return bt;
	if (k<bt->key)
       	return SearchBST(bt->lchild,k);  //在左子树中递归查找
    else
     	return SearchBST(bt->rchild,k);  //在右子树中递归查找
}
BSTNode *SearchBST1(BSTNode *bt,KeyType k,BSTNode *f1,BSTNode *&f)
/*在bt中查找关键字为k的结点,若查找成功,该函数返回该结点的指针,
f返回其双亲结点;否则,该函数返回NULL。
其调用方法如下:
	         SearchBST(bt,x,NULL,f);
这里的第3个参数f1仅作中间参数,用于求f,初始设为NULL*/
{
	if (bt==NULL)
	{
		f=NULL;
		return(NULL);
	}
	else if (k==bt->key)
	{
		f=f1;
		return(bt);
	}
	else if (k<bt->key)
       	return SearchBST1(bt->lchild,k,bt,f);  //在左子树中递归查找
    else
     	return SearchBST1(bt->rchild,k,bt,f);  //在右子树中递归查找
}

void Delete1(BSTNode *p,BSTNode *&r)  //当被删p结点有左右子树时的删除过程
{
	BSTNode *q;
	if (r->rchild!=NULL)
		Delete1(p,r->rchild);	//递归找最右下结点r
	else						//找到了最右下结点r
	{	p->key=r->key;			//将*结点的值赋给结点p
		q=r;
		r=r->lchild;			//直接将其左子树的根结点放在被删结点的位置上
		free(q);				//释放原结点r的空间
	}
}
void Delete(BSTNode *&p)		//从二叉排序树中删除p结点
{
	BSTNode *q;
	if (p->rchild==NULL)		//p结点没有右子树的情况
	{
		q=p;
		p=p->lchild;			//直接将其右子树的根结点放在被删结点的位置上
		free(q);
	}
	else if (p->lchild==NULL)	//p结点没有左子树的情况
	{
		q=p;
		p=p->rchild;			//将p结点的右子树作为双亲结点的相应子树
		free(q);
	}
	else Delete1(p,p->lchild);	//p结点既没有左子树又没有右子树的情况
}
int DeleteBST(BSTNode *&bt,KeyType k)	//在bt中删除关键字为k的结点
{
	if (bt==NULL)
		return 0;				//空树删除失败
	else
	{
		if (k<bt->key)
			return DeleteBST(bt->lchild,k);	//递归在左子树中删除为k的结点
		else if (k>bt->key)
			return DeleteBST(bt->rchild,k);	//递归在右子树中删除为k的结点
		else
		{
			Delete(bt);		//调用Delete(bt)函数删除*bt结点
			return 1;
		}
	}
}
void DestroyBST(BSTNode *&bt)		//销毁二叉排序树bt
{
	if (bt!=NULL)
	{
		DestroyBST(bt->lchild);
		DestroyBST(bt->rchild);
		free(bt);
	}
}
KeyType maxnode(BSTNode *p) //返回一棵二叉排序树中的最大结点
{
    BSTNode *q = p;
    if (q == NULL){
        return -1;
    }
    while(q->rchild != NULL){
        q = q->rchild;
    }
    return q->key;
}
KeyType minnode(BSTNode *p)	  //返回一棵二叉排序树中的最小结点
{
    BSTNode *q = p;
    if (q == NULL){
        return -1;
    }
    while (q->lchild != NULL)
    {
        q = q->lchild;
    }
    return q->key;
}
void maxminnode(BSTNode *p)
{
	if (p!=NULL)
	{
		if (p->rchild!=NULL)
			printf("整棵树中最大结点为:%d\n",maxnode(p->rchild));
		if (p->lchild!=NULL)
			printf("整棵树中最小结点为:%d\n",minnode(p->lchild));
	}
}

int main()
{
	BSTNode *bt = NULL,*f = NULL;
	int i=0;
	KeyType a[]={25,18,46,2,53,39,32,4,74,67,60,11};
    while(i < 12){
        InsertBST(bt, a[i]);
        i++;
    }
	printf("1.根据数组创建的BST为:\n");
	DispBST(bt);
    printf("\n整棵树中最大结点为:%d\n", maxnode(bt));
    printf("\n整棵树中最小结点为:%d\n", minnode(bt));
	printf("2.删除%d结点\n",46);
	DeleteBST(bt, 46);
	printf("BST:");
	DispBST(bt);
    printf("\n");
	printf("3.准备查找值为%d的结点\n", 180);
    if(SearchBST1(bt,180,NULL,f) == NULL){
        printf("180是不存在的，需要插入到排序树中");
    }
    printf("插入后的排序树为：\n");
    InsertBST(bt, 180);
    DispBST(bt);
	return 1;
}
