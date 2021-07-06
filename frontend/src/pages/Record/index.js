import React, {useEffect, useState} from 'react';
import './styles.css';
import {getRecord, updateRecord} from "./service";

export default function Record(props) {

  const resultId = props.match.params.id

  const [product, setProduct] = useState({
    id: "",
    user: {name: ""},
    analysis: [],
    feedback: "",
    tag: "",
    created_at: ""
  });

  const [recordFeedback, setRecordFeedback] = useState("");
  const [tag, setTag] = useState("");

  const [saved, setSaved] = useState(false);

  const save = () => {
    updateRecord({...product, feedback: recordFeedback, tag: tag},
      (prd) => {
        setProduct(prd);
        setSaved(true);
        setTimeout(
          function () {
            setSaved(false)
          },
          3000
        );
      })
  }

  useEffect(() => {
    getRecord(resultId, setProduct, setRecordFeedback, setTag);
  }, []);


  const back = () => {
    window.location.href = "/"
  }

  return (
    <div className="outer-container">
      <header>
        <img src={process.env.PUBLIC_URL + '/logo.jpeg'} alt="Melskin"/>
        {/*<span>Welcome, username</span>*/}
        {/*<Link className="buttonS" to="/records/new">Análise</Link>*/}
        {/*<button type="button" placeholder="Log out">*/}
        {/*  <FiPower size={18} color="#fff"/>*/}
        {/*</button>*/}
      </header>

      <h1>Report</h1>

      <div className="details" key={product.id}>
        <div style={{display: 'flex'}}>
          <div style={{width: '45%'}}>
            <strong>Código :</strong>
            <p>{product.id}</p>
            <br/>
            <strong>Paciente:</strong>
            <p>{product.user.name}</p>
            <br/>
            <strong>Data de avaliação</strong>
            <p>{product.created_at}</p>
          </div>
          <div>
            <strong>Imagem</strong>
            <img width={{width: '40%'}} src={product.image}/>
          </div>
        </div>

        <br/><br/>
        <div>
          <hr/>
          <br/>
          <h2>Resultados</h2>
          <div style={{display: 'flex', marginTop: '25px', textAlign: 'center'}}>
            <div style={{width: '30%'}}>
              <strong>Diâmetro (cm):</strong>
              <p>{product.diameter} </p>
            </div>

            <div style={{width: '30%'}}>
              <strong>Simetria (%):</strong>
              <p>{product.symmetry}</p>
            </div>

            <div style={{width: '30%'}}>
              <strong>Detecção IA (%):</strong>
              <p>{product.ai_detection}</p>
            </div>
          </div>
        </div>
        <br/><br/>
        <div className="analyze-container">
          {
            product.analysis.map((analyze) => {
              return <div className="analysis-container">
                <p>{analyze.type}</p>
                <img src={analyze.image}/>
              </div>
            })
          }
        </div>
        <div>
          <strong>Análise</strong>
          <textarea style={{width: "100%", height: '100px'}} value={recordFeedback}
                    onChange={e => setRecordFeedback(e.target.value)} placeholder={"Análise"}/>

          <strong>Evolução</strong>
          <textarea style={{width: "100%",}} value={tag} onChange={e => setTag(e.target.value)} placeholder={"Tag"}/>
        </div>
        <br/><br/>
        <button className="btn-save" onClick={() => save()}>
          Salvar
        </button>
        <br/><br/><br/>
        {saved ? <p style={{color: "green"}}>Salvo com sucesso!</p> : <p/>}
        <br/><br/>
      </div>

      <br/>
      <button className="back-btn" onClick={() => back()}>
        Voltar
      </button>
    </div>
  );
}