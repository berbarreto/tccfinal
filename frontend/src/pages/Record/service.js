export function getRecord(id, fn, fn2, fn3) {
  const opts = {
    mode: 'cors',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Authorization': 'oi'
    }
  }

  fetch(`http://192.168.100.114:5000/getResultById/${id}`, opts)
  .then(function (response) {
    if (response.status !== 200) {
      alert("Login Incorreto")
    } else {
      response.json().then(function (data) {
        console.log(data);
        fn(data.data)
        fn2(data.data.feedback)
        fn3(data.data.tag)
      });
    }
  })
}

export function updateRecord(body, callback) {
  const opts = {
    mode: 'cors',
    method: 'POST',
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Authorization': 'oi',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  }

  fetch(`http://192.168.100.114:5000/updateResult/`, opts)
  .then(function (response) {
    if (response.status !== 200) {
      alert("Login Incorreto")
    } else {
      response.json().then(function (data) {
        console.log(data);
        callback(data.data)
      });
    }
  })
}