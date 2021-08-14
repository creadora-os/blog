


function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf ,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200){
            window.location.href = '/account/'
        }
        else{
            alert(response.message)
        }
    })

}

function signup(){
    var username = document.getElementById('signUsername').value
    var email = document.getElementById('signEmail').value
    var password = document.getElementById('signPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && email == '' && password == ''){
        alert('You must enter all')
    }

    var data = {
        'username' : username,
        'email' : email ,
        'password' : password
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf ,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200){
            window.location.href = '/'
           
        }
        else{
            alert(response.message)
        }
    })


}
