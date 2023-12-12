import React, {useEffect, useState} from 'react';
import {Link, useNavigate} from "react-router-dom";
import axios from "axios";
import {toast, ToastContainer} from "react-toastify";
import {setCookie} from "../utils/cookiesUtils";
import {FaRegEye, FaRegEyeSlash} from "react-icons/fa";
import {API_USER_URL} from "../utils/apiUrls";


const Register = () => {
    const navigate = useNavigate()

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [checkPassword, setCheckPassword] = useState('')
    const [isHidden, setIsHidden] = useState(true)

    const registerHandler = () => {
        const id = toast.loading('Please Wait...')
        if (password !== checkPassword) {
            toast.update(id, {render: 'Password and check password not equals', type: "error", isLoading: false, autoClose: 7000})
            return
        }
        axios.post(API_USER_URL, {
            email,
            password,
        }).then((response) => {
            if (response.status === 201) {
                toast.update(id, {render: 'Success', type: "success", isLoading: false, autoClose: 1000})
                setCookie('accessToken', response.data.access)
                setCookie('refreshToken', response.data.refresh)
                setTimeout(()=> {
                    navigate('/account')
                }, 500)
            }
        }).catch((error) => {
            if (error.response) {
                toast.update(id, {render: error.response.data.errors[0].detail, type: "error", isLoading: false, autoClose: 7000})
            }else{
                toast.update(id, {render: 'Server error please contact administrator', type: "error", isLoading: false, autoClose: 7000})
            }
        })
    }

    const keyPressedHandler = (e) => {
        if (e.code === 'Enter') {
            registerHandler()
        }
    }

    return (
        <div>
            <ToastContainer closeOnClick/>
            Register
        </div>
    )
}

export default Register