import React, { useState,useRef, useEffect } from "react";

const Login = () => {
    const inputRef = useRef();
    const [inputs,setInputs] = useState({
        id:"",
        password:""
    })
    const {id,password} = inputs
    const onChange = (e) =>{
        const {name,value} = e.target
        const nextInputs = {
            ...inputs,
            [name]: value,
        }
        setInputs(nextInputs)
    }
    const onClick = () =>{
        const data ={
            id:id,
            password:password
        }
        console.log(data)
        //data post하면 됨
    }

    return(
        <div className="login">
            <div className="">
                ID
                <input
                    name="id" 
                    onChange={onChange} 
                    placeholder="아이디를 입력하세요"
                    ref={inputRef}
                    value={id}/>
            </div>
            <div className="">
                password
                <input
                    name="password" 
                    onChange={onChange}
                    type="password"
                    placeholder="아이디를 입력하세요"
                    ref={inputRef}
                    value={password}/>
            </div>
            <button onClick={onClick}>로그인</button>
        </div>
    )
}

export default Login;