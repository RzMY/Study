/*
file       :App.jsx
Description: learn demo
Date       :2024/10/05 18:20:26
Author     :邱宗森
*/

import { 
  BrowserRouter,
  Routes,
  Route,
  Outlet
} from 'react-router-dom';
import SideMenu from './components/side_menu.jsx';
import {
  Row,
  Col,
} from 'antd';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/'
          element={
            <>
              <Row>
                <Col span={5}>
                  <SideMenu />
                </Col>
                <Col span={19}>
                  <Outlet />
                </Col>
              </Row>
            </>
          }
        >
          <Route path='/a' 
            element={<div>Page A</div>}
          ></Route>
        </Route>
        
      </Routes>
    </BrowserRouter>
  )
}

export default App;
