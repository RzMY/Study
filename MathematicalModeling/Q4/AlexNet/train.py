import os
import sys
import json
import torch
import torch.nn as nn
from torchvision import transforms, datasets, utils
import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim
from tqdm import tqdm
from model import AlexNet
 
 
def main():
    #指定使用的设备，若有GPU设备则使用GPU，若没有，则使用CPU
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("using {} device.".format(device))
 
    data_transform = {
        #对于训练集
        "train": transforms.Compose([transforms.RandomResizedCrop(224),#进行随机裁剪成224*224像素大小
                                     transforms.RandomHorizontalFlip(),#在水平方向进行随机翻转
                                     transforms.ToTensor(), #转化成tensor
                                     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]),#进行标准化处理
       #对于验证集
        "val": transforms.Compose([transforms.Resize((224, 224)),  # cannot 224, must (224, 224)
                                   transforms.ToTensor(),
                                   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])}
    #获取数据集所在的根目录，os.getcwd()获取当前文件所在的目录，通过os.path.join()函数将两个参数连接在一起
    data_root = os.path.abspath(os.path.join(os.getcwd(), "../.."))  # get data root path
    image_path = os.path.join(data_root, "data_set", "flower_data")  # flower data set path
    #表示进入data_set 文件下的flower_data文件夹
    assert os.path.exists(image_path), "{} path does not exist.".format(image_path)
    #通过datasets.ImageFolder()函数去加载数据集，root就是路径
    train_dataset = datasets.ImageFolder(root=os.path.join(image_path, "train"),
                                         transform=data_transform["train"])
    train_num = len(train_dataset) #通过len()函数打印训练数据集有多少个图片
 
    # {'daisy':0, 'dandelion':1, 'roses':2, 'sunflower':3, 'tulips':4}
    flower_list = train_dataset.class_to_idx #获取分类的名称所对应的索引
    #去遍历刚刚得到的字典，将key和val反过来，这样预测完可以之间看见类别
    cla_dict = dict((val, key) for key, val in flower_list.items())
    # write dict into json file
    #将cla_dict进行编码成json的格式
    json_str = json.dumps(cla_dict, indent=4)
    #将class_indices文件保存到json中
    with open('class_indices.json', 'w') as json_file:
        json_file.write(json_str)
 
    batch_size = 32
    nw = min([os.cpu_count(), batch_size if batch_size > 1 else 0, 8])  # number of workers
    print('Using {} dataloader workers every process'.format(nw))
    #获取一批批的数据
    train_loader = torch.utils.data.DataLoader(train_dataset,
                                               batch_size=batch_size, shuffle=True,
                                               num_workers=0)
    #num_workers表示加载数据需要的线程个数 0表示使用主线程加载数据
 
    validate_dataset = datasets.ImageFolder(root=os.path.join(image_path, "val"),
                                            transform=data_transform["val"])
    val_num = len(validate_dataset) #统计测试集的文件个数
    # 载入测试集
    validate_loader = torch.utils.data.DataLoader(validate_dataset,
                                                  batch_size=4, shuffle=True,
                                                  num_workers=0)
 
    print("using {} images for training, {} images for validation.".format(train_num,
                                                                           val_num))
    # test_data_iter = iter(validate_loader)
    # test_image, test_label = test_data_iter.next()
    #
    # def imshow(img):
    #     img = img / 2 + 0.5  # unnormalize
    #     npimg = img.numpy()
    #     plt.imshow(np.transpose(npimg, (1, 2, 0)))
    #     plt.show()
    #
    # print(' '.join('%5s' % cla_dict[test_label[j].item()] for j in range(4)))
    # imshow(utils.make_grid(test_image))
 
    net = AlexNet(num_classes=5, init_weights=True)
    #传入的参数num_classes=5，表示又5个类别
    net.to(device) #将网络确定到指定的设备上
    loss_function = nn.CrossEntropyLoss() #定义损失函数
    # pata = list(net.parameters()) #用来查看模型的参数
    optimizer = optim.Adam(net.parameters(), lr=0.0002) #定义优化器Adam，优化对象是网络中的所有的可训练的参数
 
    epochs = 10
    save_path = './AlexNet.pth' #保存权重的路径
    best_acc = 0.0 #定义最佳准确率
    train_steps = len(train_loader)
    for epoch in range(epochs): #迭代10次
        # train 进行训练
        net.train() #用来管理dropout方法，启用dropout
        running_loss = 0.0#用来统计训练过程中的平均损失
        train_bar = tqdm(train_loader, file=sys.stdout)
        for step, data in enumerate(train_bar): #遍历数据集
            images, labels = data #将数据分为图像和标签
            optimizer.zero_grad() #进行梯度清零 清空之前的梯度信息
            outputs = net(images.to(device)) #经过正向传播得到输出，并指定设备
            loss = loss_function(outputs, labels.to(device))#预测值和真实值的损失
            loss.backward() #反向传播到每个节点中
            optimizer.step() #更新每一个结点的参数
 
            # print statistics
            running_loss += loss.item() #得到的损失进行累加
 
            train_bar.desc = "train epoch[{}/{}] loss:{:.3f}".format(epoch + 1,
                                                                     epochs,
                                                                     loss)
 
        # validate 进行验证
        net.eval() #表示关闭dropout方法
        acc = 0.0  # accumulate accurate number / epoch
        with torch.no_grad():
            val_bar = tqdm(validate_loader, file=sys.stdout)
            for val_data in val_bar:
                val_images, val_labels = val_data
                outputs = net(val_images.to(device))
                predict_y = torch.max(outputs, dim=1)[1]
                acc += torch.eq(predict_y, val_labels.to(device)).sum().item()
 
        val_accurate = acc / val_num  #正确个数/总的训练样本
        print('[epoch %d] train_loss: %.3f  val_accuracy: %.3f' %
              (epoch + 1, running_loss / train_steps, val_accurate))
 
        if val_accurate > best_acc: #若当前的准确率大于历史最优的准确率
            best_acc = val_accurate  #就把当前的准确率赋给最优准确率
            torch.save(net.state_dict(), save_path) #保存当前的权重
 
    print('Finished Training')
 
 
if __name__ == '__main__':
    main()