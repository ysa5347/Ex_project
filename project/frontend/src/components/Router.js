import React from 'react';
import Signup from "../routes/signup";
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Login from 'routes/login';


const AppRouter = () =>{
    return(
        <Router>
            <Routes>
                <Route path="/signup" element={<Signup/>}></Route>
                <Route path="/login" element={<Login/>}></Route>
            </Routes>
        </Router>
    )
}

export default AppRouter;