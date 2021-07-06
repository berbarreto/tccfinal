import React, {useState} from 'react';
import {FiLogIn} from 'react-icons/fi';
import {Link} from 'react-router-dom';
import './styles.css';

import toUrlParams from "../../helper";

export default function Login() {

  const [phone, setPhone] = useState('');

  const doLogin = () => {
    window.location.href = "/validation"
  }

  return (
    <div className="login-container">
      <section className="form">
        <img src={process.env.PUBLIC_URL + '/logo.jpeg'} alt="Melskin"/>
        <div id="login-container">
          <h1>Entrar</h1>
          <input onChange={e => setPhone(e.target.value)} placeholder="Phone number" id="phone-input" className="input"
                 required/>
          <button id="signin-butt" className="button" onClick={() => doLogin()}>Sign in</button>
        </div>
      </section>

    </div>
  );
}