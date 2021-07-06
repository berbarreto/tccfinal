export default function getRecords(fn) {
  const opts = {
    mode: 'cors',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Authorization': 'oi'
    }
  }

  fetch(`http://localhost:5000/getResultsByDoctor`, opts)
  .then(function (response) {
    if (response.status !== 200) {
      alert("Login Incorreto")
    } else {
      response.json().then(function (data) {
        console.log(data);
        fn(data.data)
      });
    }
  })
}