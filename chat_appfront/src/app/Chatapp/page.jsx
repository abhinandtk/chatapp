'use client'
import React, { useEffect, useState } from 'react'
import pusherJs from 'pusher-js';
import axios from 'axios';

function Chatapp() {
    const [username,setUsername]=useState('username')
    const [messages,setMessages]=useState([])
    const [message,setMessage]=useState('')
    let allmessages=[]
    console.log(allmessages);
    useEffect(()=>{
        Pusher.logToConsole = true;

    const pusher = new Pusher('107f169fb90c869fb329', {
      cluster: 'ap2'
    });

    const channel = pusher.subscribe('chat');
    channel.bind('message', function(data) {
        allmessages.push(data)
        setMessages(allmessages)
    });
    },[])
    const submit=()=>{
        axios.post('http://127.0.0.1:8000/chatmethod',{'message':message,'username':username}).then((res)=>{
            console.log(res);
        }).catch((error)=>{
            console.log(error);
        })
    }
    console.log(messages,'messsage');
  return (
    <div>
        <input type="text"  onChange={(e)=>setUsername(e.target.value)} />
        {messages.map((value,key)=>(
            <div>
                <h4>{value.username}</h4>
                <h4>{value.message}</h4>
            </div>
        ))}
        <input type="text" placeholder='write your message' />
        <button onClick={submit}>send</button>
    </div>
  )
}

export default Chatapp