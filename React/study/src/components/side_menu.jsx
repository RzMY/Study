import React from 'react';
import {
  PieChartOutlined,
  ClockCircleOutlined,
  UserAddOutlined,
  OrderedListOutlined,
  SettingOutlined,
  InfoCircleOutlined
} from '@ant-design/icons';
import { Menu } from 'antd';
import { Link } from 'react-router-dom';
const items = [
  {
    key: '1',
    icon: <PieChartOutlined />,
    // label: '首页',
    label: <Link to="/a">首页</Link>
  },
  {
    key: '2',
    icon: <ClockCircleOutlined />,
    label: '计费',
  },
  {
    key: '3',
    icon: <UserAddOutlined />,
    label: '会员',
  },
  {
    key: '4',
    icon: <OrderedListOutlined />,
    label: '订单',
  },
  {
    key: '5',
    icon: <SettingOutlined />,
    label: '设置',
  },
  {
    key: '6',
    icon: <InfoCircleOutlined />,
    label: '关于',
  }
];

const SideMenu = () => {
  return (
    <div
      // style={{
      //   width: 256,
      // }}
    >
      <Menu
        defaultSelectedKeys={['1']}
        mode="inline"
        theme="light"
        inlineCollapsed={false}
        items={items}
      />
    </div>
  );
};

export default SideMenu;