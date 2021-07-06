import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom';
import {FiPower, FiTrash2} from 'react-icons/fi';
import './styles.css';
import getRecords from "./service";

export default function Sendings() {

  const [products, setProducts] = useState([]);

  const go_to = (id) => {
    window.location.href = "/" + id
  }

  const productsList = products.map((product) => {
    return <li key={product.id}>
      <strong>Código :</strong>
      <p>{product.id}</p>
      <strong>Paciente:</strong>
      <p>{product.user.name}</p>
      <strong>Análise</strong>
      <p>{product.feedback}</p>
      <strong>Data de avaliação</strong>
      <p>{product.created_at}</p>
      <br/>
      <button className={"btn-open-record"} onClick={() => go_to(product.id)}>
        Detalhes
      </button>
    </li>
  });

  useEffect(() => {
    getRecords(setProducts);
  }, []);

  return (
    <div className="outer-container">
      <header>
        <img src={process.env.PUBLIC_URL + '/logo.jpeg'} alt="Melskin"/>
        {/*<span>Welcome, username</span>*/}
        {/*<Link className="buttonS" to="/records/new">Avaliar análises</Link>*/}
        {/*<button type="button" placeholder="Log out" style={{float: 'right'}}>*/}
        {/*  <FiPower size={18} color="#fff"/>*/}
        {/*</button>*/}
      </header>

      <h1>Resultados</h1>

      <ul>
        {productsList}
      </ul>
    </div>
  );
}