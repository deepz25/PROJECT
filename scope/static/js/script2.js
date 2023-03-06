function message(){
    var Name = document.getElementById('name');
    var email = document.getElementById('email');
    var message = document.getElementById('message');
    const success = document.getElementById('success');
    const danger = document.getElementById('danger');

    if(Name.value === '' || email.value === '' || message.value === ''){
        danger.style.display = 'block' ;
    }
    else{
        setTimeout(() => {
            Name.value = '';
            email.value = '';
            message.value = '';

        }, 2000);
        success.style.display = 'block';
    }
    setTimeout(() => {
        danger.style.display = 'none';
        success.style.display = 'none';
    }, 4000);
}