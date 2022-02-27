const bottles = document.querySelectorAll('.bottle')

bottles.forEach((bottle) => {
  bottle.addEventListener('click', (e) => {
      let letter = e.target.nextElementSibling
      if(letter.classList.contains('hidden')){
          letter.classList.remove('hidden')
          letter.classList.add('card')

      }else {
          letter.classList.add('hidden')
          letter.classList.remove('card')
      }
  });
});




setTimeout(function() { window.location=window.location;},90000);

// Message variables
const messages = document.getElementById('msg');
const alert = new bootstrap.Alert(messages);

if (messages)
  setTimeout(function () {
    alert.close();
  }, 2500);
