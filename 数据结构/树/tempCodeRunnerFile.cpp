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