import React from 'react';
import Signup from "../routes/signup";
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Login from 'routes/login';
import Explist from 'routes/explist';


const AppRouter = ({isLogin,setIsLogin}) =>{
    return(
        <Router>
            <Routes>
                <Route path="/signup" element={<Signup isLogin={isLogin} setIsLogin={setIsLogin}/>}></Route>
                <Route path="/login" element={<Login isLogin={isLogin} setIsLogin={setIsLogin}/>}></Route>
                <Route path="/explist" element={<Explist isLogin={isLogin} setIsLogin={setIsLogin}/>}></Route>
            </Routes>
        </Router>   
    )
}

export default AppRouter;