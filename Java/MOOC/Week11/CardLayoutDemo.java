package Week11;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CardLayoutDemo {
    public static void main(String[] args) {
        Frame frame = new Frame("这是一个窗口容器Frame");

        //创建一个Panel，用来存储多张卡片
        Panel p1 = new Panel();
        //创建CardLayout对象，并且把该对象设置给p1
        CardLayout cLayout = new CardLayout();
        p1.setLayout(cLayout);
        //往p1中存储多个组件
        String[] names = {"第一张", "第二张", "第三张", "第四张", "第五张", "第六张"};
        for (int i = 0; i < names.length; i++) {
            //每次添加都是作为最后一个组件添加到末尾
            p1.add(names[i], new Button(names[i])); //添加时指定组件的名字
        }
        //把p1放到frame的中间区域
        frame.add(p1, BorderLayout.CENTER);

        //创建另外一个Panel，用来存放5个按钮组件
        Panel p2 = new Panel();
        Button btn1 = new Button("上一张");
        Button btn2 = new Button("下一张");
        Button btn3 = new Button("第一张");
        Button btn4 = new Button("最后一张");
        Button btn5 = new Button("第三张");
        //创建一个事件监听器，监听按钮的点击动作
        ActionListener listener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String actionCommand = e.getActionCommand(); //这个字符串其实就是按钮上的文字
                switch (actionCommand) {
                    case "上一张":
                        cLayout.previous(p1);
                        break;
                    case "下一张":
                        cLayout.next(p1);
                        break;
                    case "第一张":
                        cLayout.first(p1);
                        break;
                    case "最后一张":
                        cLayout.last(p1);
                        break;
                    case "第三张":
                        cLayout.show(p1, "第三张");
                        break;
                }
            }
        };
        //把当前事件监听器和多个按钮绑定到一起
        btn1.addActionListener(listener);
        btn2.addActionListener(listener);
        btn3.addActionListener(listener);
        btn4.addActionListener(listener);
        btn5.addActionListener(listener);
        //把按钮添加到容器p2中
        p2.add(btn1);
        p2.add(btn2);
        p2.add(btn3);
        p2.add(btn4);
        p2.add(btn5);
        //把p2放到frame的南边区域
        frame.add(p2, BorderLayout.SOUTH);

        //通过pack()方法设置最佳大小
        frame.pack();
        //设置Frame的位置和大小
        frame.setBounds(400, 200, 500, 300);
        //设置Frame可见
        frame.setVisible(true);
    }
}