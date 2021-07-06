import React, {useState} from 'react';
import {Link} from 'react-router-dom';
import {FiArrowLeft} from 'react-icons/fi';

import './styles.css';


import Phrase from '../../assets/impact-register.svg';
import toUrlParams from "../../helper";

export default function Register() {

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [cpf, setCpf] = useState('');
  const [birth_date, setBirthDate] = useState('');

  const login = () => {
    console.log(name);
    const params = toUrlParams({
      name: name,
      cpf: cpf,
      phone: phone,
      email: email,
      birth_date: birth_date,
    });

    fetch(`http://127.0.0.1:5000/createUser?${params}`)
    .then(function (response) {
      console.log(response)
      return response.json();
    })
    .then(function (myJson) {
      console.log(myJson);
    });
  }

  return (
    <div className="box-container">
      <div className="content">
        <section>
          <img src={process.env.PUBLIC_URL + '/logo.jpeg'} alt="Melskin"/>
          <h1>Sign up</h1>
          <img src={Phrase} alt="" id="phrase"/>
          <Link className="back-link" to="/login">
            <FiArrowLeft size={16} color="#158e0d"/>
            Back to login page
          </Link>
        </section>
        <form>
          <input id="phone" onChange={e => setPhone(e.target.value)} placeholder="Phone number" required/>
          <input id="email" onChange={e => setEmail(e.target.value)} placeholder="Email" required/>
          <input id="name" onChange={e => setName(e.target.value)} placeholder="Name" required/>
          <input id="cpf" onChange={e => setCpf(e.target.value)} placeholder="CPF" required/>
          <input id="birth_date" onChange={e => setBirthDate(e.target.value)} placeholder="Birth Date" required/>

          <button type="submit" className="button" onClick={() => login()}>Create account</button>
        </form>
      </div>
    </div>
  );
}