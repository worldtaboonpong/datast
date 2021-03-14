import React , {useState,useEffect} from 'react'

const TestPage = () => {
    const [msg,setMsg] = useState([])

    useEffect(() => {
        fetch('/').then(res => {
            res.json()
        }).then((data) => {
            setMsg(data)
        })
    },[])

    return(
        <div>
            {msg}
        </div>
    )
}
export default TestPage