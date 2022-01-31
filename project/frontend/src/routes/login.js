import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { MDBBtn,
    MDBInputGroup,
    MDBInputGroupElement,
    MDBIcon,
    MDBInputGroupText,
    MDBRow,
    MDBCol,
    MDBCheckbox} from "mdb-react-ui-kit";
import "./style/login.css"
import logo from "./style/logo.png";


const Login = ({isLogin,setIsLogin}) => {
    let navigate = useNavigate();
    const [passwordType,setPasswordType] = useState(true)
    const [inputs,setInputs] = useState({
        userID:"", //userID로 변경
        userPW:"" //userPW로 변경
    })
    const {userID,userPW} = inputs

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
            userID : userID,
            userPW : userPW
        }
        console.log(data)
        //if true => setIsLogin(True) 그다음 메인 페이지
        //data post하면 됨
    }
    const onSignup = () => {
        navigate("/signup")
    }
    return(
        <div>
            <div className="Header">
                <div className="Header-logo">
                    <img className="photo" src={logo}></img>
                </div>
                <div className="spacer"></div>
                <div className="signup-button">
                    <span className="signup-message">
                        아직 회원이 아니신가요?
                    </span>
                    <MDBBtn outline onClick={onSignup}size="sm">회원가입</MDBBtn>
                </div>
            </div>
            <div className="medium">
                <div className="login">
                    <h2 className="title">로그인</h2>
                    <div className="outline">
                        <div className="login_auto">
                            <div className="informtitle">아이디
                                <MDBInputGroup className="mb-3">
                                <MDBInputGroupElement type='text' 
                                    placeholder="your ID"
                                    onChange={onChange}
                                    name="userID"
                                    type="text"/>
                                </MDBInputGroup>
                            </div>
                            <div className="informtitle">
                                비밀번호
                                <MDBInputGroup className="mb-3">
                                <MDBInputGroupElement  
                                    placeholder="your password"
                                    size="lg"
                                    onChange={onChange}
                                    name="userPW"
                                    type={passwordType? "password":"text"}/>
                                <MDBInputGroupText>
                                    <MDBIcon far icon="eye" onClick={() =>setPasswordType(!passwordType)}/>
                                </MDBInputGroupText>
                                </MDBInputGroup>
                            </div>    
                        </div>
                    </div>
                    <div className="m_bottom">
                         <MDBBtn type="submit" outline onClick={onClick} className="mb-4" block>
                             로그인
                        </MDBBtn>
                    </div>
                    <div className="bottom">
                        <MDBRow className='mb-3'>
                            <MDBCol className='d-flex justify-content-start'>
                                <MDBCheckbox id='form2Example3' label='아이디 저장'/>
                            </MDBCol>
                            <MDBCol className="d-flex justify-content-end">
                                <a href="#">비밀번호 찾기</a>
                            </MDBCol>
                        </MDBRow>
                    </div>
                    
                </div>
            </div>
        </div>
        
    )
}

export default Login;