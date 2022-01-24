import React from "react";
import { useNavigate } from "react-router-dom";

const Modal = (props) => {
    // 열기, 닫기, 모달 헤더 텍스트를 부모로부터 받아옴
    const { open } = props;
    let navigate = useNavigate();
    
    const redirect = () =>{
        navigate("/login");
    }
    return (
        <div className="signModal">
            {open? (
                <section>
                    <div>
                        회원가입을 축하드립니다.
                    </div>
                    <button onClick={redirect}>확인</button>
                </section>
            ):null}
        </div>
    )
};

export default Modal;