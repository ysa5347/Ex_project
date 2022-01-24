import react, { useState,useRef, useEffect } from "react";
import {birthList,emailList} from "./data";
import Modal from "./modal/signModal";

const Signup = () => {
    const inputRef = useRef();
    const [check,setCheck] = useState(false) //id가 있는지 없는지 확인 state
    const [popup,setPopup]= useState(false) //팝업
    const [on,setOn] = useState(false) //id 중복확인 눌렀는지 확인 state
    const [final,setFinal] = useState("") //최종적으로 나오는 메일 state확인
    const [passwordType,setPasswordType] = useState(true)
    const [click,setClick] = useState({
        birth:'',
        cmail:'0'
    })
    
    const handleSelect = (e) => {
        const {name,value} = e.target

        const nextClick = {
            ...click,
            [name]:value,
        }
        setClick(nextClick)
    }

    const [inputs,setInputs] = useState({
        id:"",
        password:"",
        name:'',
        phone:'',
        email:'',
    })

    const {id,password,name,phone,email} = inputs

    const onChange = (e) =>{
        const {name,value} = e.target
        const nextInputs = {
            ...inputs,
            [name]: value,
        }
        if (name==="phone"){
            const regex = /^[0-9]{0,11}$/;
            if(regex.test(value)){
                setInputs(nextInputs)
            }
        }else{
            setInputs(nextInputs)
        }
        
    }
    
    const checkID= (e)=>{
        e.preventDefault();
        setOn(true)
        const data ={
            id : id
        }
        //setCheck(true)이거 해야됨
        //post 해서 그것만 받아오면 됨
        console.log(data)
    }

    const sign = () => {
        setPopup(true)
        const data = {
            id : id,
            password : password,
            name : name,
            phone : phone,
            birth : click.birth,
            email : final,
        }
        //data 저장하는 post보내기
    }
    useEffect (() => {
        if (click.cmail==0){
            setFinal(inputs.email)
        }
        else{
            setFinal(inputs.email+emailList[click.cmail].name)
        }
        console.log(inputs)
    })
    
    return(
        <div className="회원가입">
            회원가입
            <div className="id">
                ID
                <input
                    name="id" 
                    onChange={onChange} 
                    placeholder="아이디를 입력하세요"
                    ref={inputRef}
                    value={id}/>
                <button onClick={checkID}>중복확인</button>
                {on && (check ?(
                    <label>사용가능한 아이디입니다.</label>
                ) : ( 
                <label>중복입니다.</label>
                ))}
                
            </div>
            <div className="password">
                password
                <input
                    name="password" 
                    type={passwordType? "password":"text"}
                    onChange={onChange} 
                    placeholder="비밀번호를 입력하세요"
                    ref={inputRef}
                    value={password}/>
                <button onClick={() =>setPasswordType(!passwordType) }>보기</button>
            </div>
            <div className="Name">
                이름
                <input
                    name="name" 
                    onChange={onChange} 
                    placeholder="이름을 입력하세요"
                    ref={inputRef}
                    value={name}/>
            </div>
            <div className="phone">
                전화번호
                <input
                    name="phone" 
                    onChange={onChange}
                    ref = {inputRef}
                    placeholder="전화번호를 입력하세요.(-를 빼주세요)"
                    value={phone}/>   
                - 숫자만 입력하세요
            </div>
            <div className="birth">
                생년
                <select name="birth" onChange={handleSelect} defaultValue={0}>
                    {birthList.map((item)=>(
                        <option value={item.value} key={item.value}>
                            {item.name}
                        </option>
                    ))}
                </select>          
            </div>
            <div className="email">
                E-mail
                <input
                    name="email" 
                    onChange={onChange}
                    ref = {inputRef}
                    placeholder="E-mail을 입력하세요"
                    value={email} />
                    <select name="cmail" onChange={handleSelect} >
                        {emailList.map((item)=>(
                            <option value={item.value} key={item.value}>
                                {item.name}
                            </option>
                        ))}
                    </select>
            </div>
            
            <react.Fragment>
                <button onClick={sign}>회원가입</button>
                <Modal open={popup}></Modal>
            </react.Fragment>
        </div>
    )
}

export default Signup;