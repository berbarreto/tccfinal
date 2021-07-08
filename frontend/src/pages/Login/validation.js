import React, {useState} from "react";

import './styles.css';
import toUrlParams from "../../helper";

export default function Validation() {

  const [code, setCode] = useState('');

  const doLogin = () => {

    var d = new Date();
    var h = d.getHours();
    var m = d.getMinutes();

    console.log(h, m)

    if (code !== `${h}${m}`) {
      alert("Código invalido")
      return
    }

    var opts = {
      mode: 'cors',
      method: 'POST',
      body: JSON.stringify({}),
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Authorization': 'oi'
      }
    }
    fetch(`http://localhost:5000/loginDoctor`, opts)
    .then(function (response) {
      console.log(response)
      // if (response.status === 200)
        window.location = "/"
      // else
      //   alert("Login Incorreto")
    })
    .then(function (myJson) {
      console.log(myJson);
    });
  }

  return <>
    <div className="login-container">
      <section className="form">
        <img src={process.env.PUBLIC_URL + '/logo.jpeg'} alt="Melskin"/>
        <div id="login-container">
          <h1>Entrar</h1>
          <input onChange={e => setCode(e.target.value)} placeholder="Código" id="phone-input" className="input"
                 required/>
          <button id="signin-butt" className="button" onClick={() => doLogin()}>Sign in</button>
        </div>
      </section>

    </div>
  </>
}