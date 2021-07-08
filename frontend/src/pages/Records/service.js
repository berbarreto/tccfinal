export default function getRecords(fn) {
  const opts = {
    mode: 'cors',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Authorization': 'oi'
    }
  }

  fetch(`http://192.168.100.114:5000/getResultsByDoctor`, opts)
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