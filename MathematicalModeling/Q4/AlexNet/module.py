import torch.nn as nn
import torch
 
#首先创建一个AlexNet类，通过继承nn.Module这样一个父类
class AlexNet(nn.Module):
    #通过初始化函数，来定义网络在正向传播过程中使用到的层结构
    def __init__(self, num_classes=1000, init_weights=False):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            #nn.Sequential()模块可以将一系列的层结构进行打包成一个新的结构；features表示新的结构的图片特征
            #对于网络结构比较多的网路，可以使用nn.Sequential()模块
            #接下来，将卷积核的个数设置为原来论文中的卷积核的个数的一般
            nn.Conv2d(3, 48, kernel_size=11, stride=4, padding=2),  # input[3, 224, 224]  output[48, 55, 55]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[48, 27, 27]
            nn.Conv2d(48, 128, kernel_size=5, padding=2),           # output[128, 27, 27]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 13, 13]
            nn.Conv2d(128, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 192, kernel_size=3, padding=1),          # output[192, 13, 13]
            nn.ReLU(inplace=True),
            nn.Conv2d(192, 128, kernel_size=3, padding=1),          # output[128, 13, 13]
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),                  # output[128, 6, 6]
        )
        self.classifier = nn.Sequential(
            #classifier 表示包含了全连接的三层
            nn.Dropout(p=0.5), #加入了dropout，p是随机失活的比例
            nn.Linear(128 * 6 * 6, 2048), #节点个数2048
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(2048, 2048),
            nn.ReLU(inplace=True),
            nn.Linear(2048, num_classes),#num_classes是输出，数据集分类的类别
        )
 
        #初始化权重函数
        if init_weights:
            self._initialize_weights()
    #定义网络的正向传播过程
    def forward(self, x):#x是输入进来的变量
        x = self.features(x)
        x = torch.flatten(x, start_dim=1) #展平处理，从第一个维度开始，展成一维向量
        x = self.classifier(x) #得到的输出就是预测输出
        return x
 
    #初始化权重的方法
    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)