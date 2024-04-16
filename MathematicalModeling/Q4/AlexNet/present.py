import os
import json
import torch
from PIL import Image
from torchvision import transforms
import matplotlib.pyplot as plt
from model import AlexNet
 
 
def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    #定义图片预处理函数
    data_transform = transforms.Compose(
        [transforms.Resize((224, 224)),#缩放到224*224
         transforms.ToTensor(),#转化成tensor
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])#标准化处理
 
    # load image
    img_path = "../tulip.jpg" #载入一张图像
    assert os.path.exists(img_path), "file: '{}' dose not exist.".format(img_path)
    img = Image.open(img_path)
 
    plt.imshow(img)
    # [N, C, H, W]
    img = data_transform(img)
    # expand batch dimension
    img = torch.unsqueeze(img, dim=0) #添加维度
 
    # read class_indict
    json_path = './class_indices.json' #读取文件
    assert os.path.exists(json_path), "file: '{}' dose not exist.".format(json_path)
 
    with open(json_path, "r") as f:
        class_indict = json.load(f) #进行解码
 
    # create model
    model = AlexNet(num_classes=5).to(device) #初始化网络
 
    # load model weights 载入模型
    weights_path = "./AlexNet.pth"
    assert os.path.exists(weights_path), "file: '{}' dose not exist.".format(weights_path)
    model.load_state_dict(torch.load(weights_path))
 
    model.eval()
    with torch.no_grad(): #不去跟踪变量的损失梯度
        # predict class
        output = torch.squeeze(model(img.to(device))).cpu() #压缩维度
        predict = torch.softmax(output, dim=0)
        predict_cla = torch.argmax(predict).numpy() #获取概率最大处的索引值
 
    print_res = "class: {}   prob: {:.3}".format(class_indict[str(predict_cla)],
                                                 predict[predict_cla].numpy())
    plt.title(print_res) #打印类别名称和预测概率
    for i in range(len(predict)):
        print("class: {:10}   prob: {:.3}".format(class_indict[str(i)],
                                                  predict[i].numpy()))
    plt.show()
 
 
if __name__ == '__main__':
    main()