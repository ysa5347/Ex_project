import react, { useState,useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {birthList,emailList} from "./data/signup_data";
import Modal from "./modal/signModal";
import logo from "./style/logo.png";
import { MDBBtn,
    MDBInputGroup,
    MDBInputGroupElement,
    MDBIcon,
    MDBInputGroupText,
    MDBRow,
    MDBCol,
    MDBCheckbox} from "mdb-react-ui-kit";
const Signup = ({isLogin,setIsLogin}) => {
    let navigate = useNavigate();
    const [check,setCheck] = useState(false) //id가 있는지 없는지 확인 state 확인
    const [on,setOn] = useState(false) //id 중복확인 눌렀는지 확인 state 확인
    const [final,setFinal] = useState("") //최종적으로 나오는 메일 state 확인
    const [passwordType,setPasswordType] = useState(true)
    
    const [inputs,setInputs] = useState({
        id:"", //userID
        password:"", //userPW
        name:'', 
        phone:'',
        email:'',
        birth:'',
        select_mail:'0'
    })

    const {id,password,name,phone,email,birth,select_mail} = inputs
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
    const onMain=()=>{
        navigate("/")
    }
    const checkID = (e)=>{
        e.preventDefault();
        setOn(true)
        const data ={
            userID : id
        }
        //setCheck(true)이거 해야됨
        //post 해서 그것만 받아오면 됨
        console.log(data)
    }

    const sign = () => {
        const data = {
            usersID : id,
            userPW : password,
            name : name,
            phone : phone,
            birth : birth,
            email : final,
        }
        //data 저장하는 post보내기
        console.log(data)
        
    }

    useEffect (() => {
        if (select_mail==0){
            setFinal(inputs.email)
        }
        else{
            setFinal(inputs.email+emailList[select_mail].name)
        }
    })
    
    return(
        <div>
            <div className="Header">
                <div className="Header-logo">
                    <img className="photo" onClick={onMain} src={logo}></img>
                </div>
                <div className="spacer"></div>
            </div>
            <div className="medium">
                <div className="signup">
                    <h2 className="title">회원가입</h2>
                        <div className="id">
                            ID
                            <MDBInputGroup className="mb-3">
                                <MDBInputGroupElement  
                                    placeholder="your ID"
                                    onChange={onChange}
                                    size="lg"
                                    name="id"
                                    type="text"/>
                                <MDBInputGroupText onClick={checkID}>중복확인</MDBInputGroupText>
                            </MDBInputGroup>
                            {on && (check ?(
                                <label>사용가능한 아이디입니다.</label>
                            ) : ( 
                            <label>중복입니다.</label>
                            ))}
                        
                        </div>
                    <div className="password">
                        비밀번호
                            <MDBInputGroup className="mb-3">
                            <MDBInputGroupElement  
                                placeholder="your password"
                                size="lg"
                                onChange={onChange}
                                name="password"
                                type={passwordType? "password":"text"}/>
                            <MDBInputGroupText>
                                <MDBIcon far icon="eye" onClick={() =>setPasswordType(!passwordType)}/>
                            </MDBInputGroupText>
                            </MDBInputGroup>
                    </div>
                    <div className="Name">
                        이름
                        <MDBInputGroup className="mb-3">
                        <MDBInputGroupElement  
                                placeholder="이름을 입력하세요"
                                size="lg"
                                onChange={onChange}
                                name="name"
                                type="text"/>
                        </MDBInputGroup>
                    </div>
                    <div className="phone">
                        전화번호
                        <MDBInputGroup className="mb-3">
                        <MDBInputGroupElement  
                                placeholder="전화번호를 입력하세요.(-를 빼주세요)"
                                size="lg"
                                onChange={onChange}
                                name="phone"
                                type="text"
                                value={phone}/>
                        </MDBInputGroup>
                    </div>
                    <div className="birth">
                        생년
                        <MDBInputGroup className="mb-3">
                        <select className="form-control" name="birth" onChange={onChange} defaultValue={0}>
                            {birthList.map((item)=>(
                                <option value={item.value} key={item.value}>
                                    {item.name}
                                </option>
                            ))}
                        </select>
                        </MDBInputGroup>
                    </div>
                    <div className="email">
                        E-mail
                        <MDBInputGroup className="mb-3">
                            <MDBInputGroupElement  
                                    placeholder="E-mail을 입력하세요"
                                    size="lg"
                                    onChange={onChange}
                                    name="email"
                                    type="text"
                                    />
                            <select className="form-control" name="cmail" onChange={onChange} >
                                {emailList.map((item)=>(
                                    <option value={item.value} key={item.value}>
                                        {item.name}
                                    </option>
                                ))}
                            </select>
                        </MDBInputGroup>
                    </div>
                </div>
                <div>
                    <react.Fragment>
                        <MDBBtn type="submit" outline onClick={sign}>회원가입</MDBBtn>
                        
                    </react.Fragment>
                </div>
            </div>
        </div>   
    )
}

export default Signup;