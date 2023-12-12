import React, {useState} from 'react';
import {Link, useNavigate} from "react-router-dom";
import {toast, ToastContainer} from "react-toastify";
import axios from "axios";

import {setCookie} from "../utils/cookiesUtils";
import {FaRegEye, FaRegEyeSlash} from "react-icons/fa";
import {API_AUTH_TOKEN} from "../utils/apiUrls";

const Login = () => {
    const navigate = useNavigate()
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [isHidden, setIsHidden] = useState(true)


    const loginHandler = () => {
        const id = toast.loading('Please Wait...')
        axios.post(API_AUTH_TOKEN, {
            email,
            password
        }).then((response) => {
            if (response.status === 200) {
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 2000})
                setCookie('accessToken', response.data.access)
                setCookie('refreshToken', response.data.refresh)
                setTimeout(() => {
                    navigate('/account')
                }, 500)
            }
        }).catch((error) => {
            if (error.response) {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 5000})
            }else{
                toast.update(id, {render: 'Server error please contact administrator', type: "error", isLoading: false, autoClose: 5000})
            }
        })
    }

    const keyPressedHandler = (e) => {
        if (e.code === 'Enter') {
            loginHandler()
        }
    }
    return (
        <div>
            <ToastContainer/>
            Login
        </div>
    )
}

export default Login