import React, { useState,useRef } from "react";
import {users} from "./data/explist_data"


function Article({article}){
        console.log("hi")
        return (
            <div>안뇽하세요! {article.email}</div>
        );
    }

const Explist = ({isLogin,setIsLogin}) => {
    const [filter,setFilter] = useState({
        search:"False",
        day:"",
        
    })
    var data = users
    return(
        <div>
            {data.map((props)=>(<Article article={props} key={props.id}/>))}
            hi
        </div>
    )
}
export default Explist;