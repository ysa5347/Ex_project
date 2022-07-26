import react from "react";
import logo from "./style/logo.png";
import { useNavigate } from "react-router-dom";
import { MDBBtn } from "mdb-react-ui-kit";
const Main =({isLogin,setIsLogin})=>{
    let navigate = useNavigate();
    const onLogin = () => {
        if(isLogin){
            console.log("hi")
        }
        else{
            navigate("Explist")
        }
    }

    return(
        <div>
            <div className="Main-middle">
                <div className="Main-left">
                    <div className="Main-title">
                        <div className="Main-left-title">실험을 신청하고 싶으면</div>
                        <div className="Main-left-button">
                            <button className="Main-left-button-style" onClick={onLogin}>클릭</button>
                        </div>
                        
                    </div>
                </div>
                <div className="Main-right">
                    <div className="Main-title">
                        <div className="Main-right-title">실험자를 모집하고 싶은면</div>
                        <div className="Main-right-button">
                            <button className="Main-right-button-style" onClick={onLogin}>클릭</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Main;