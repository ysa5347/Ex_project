import React, { useState,useRef } from "react";
import {users} from "./data/explist_data"
import logo from "./style/logo.png";
import { useNavigate } from "react-router-dom";
function Article({article}){
        console.log("hi")
        return (
            <div>안뇽하세요! {article.email}</div>
        );
    }

const Explist = ({isLogin,setIsLogin}) => {
    let navigate = useNavigate();   
    const [filter,setFilter] = useState({
        search:"False",
        day:"",   
    })
    const onMain=()=>{
        navigate("/")
    }

    var data = users
    return(
        <div>
            <div className="Header">
                <div className="Header-logo">
                    <img className="photo"onClick={onMain} src={logo}></img>
                </div>
            </div>
            <div>
                {data.map((props)=>(<Article article={props} key={props.id}/>))}
                his
            </div>
        </div>
        
    )
}
export default Explist;