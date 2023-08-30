var Time = document.getElementById('showTime');
var time = new Date();
var timeImage = document.getElementById('image');


var hour = time.getHours();
var minutes = time.getMinutes();

Time.innerHTML = `Now is ${hour}:${minutes} o'clock`;

function carregar() {
  // Good morning
  if (hour >= 0 && hour < 12) {
    timeImage.src = './img/Morning.jpg';
    document.body.style.backgroundColor = 'var(--color1)';
    // Good Afternoon
  } else if (hour >= 12 && hour < 18) {
    timeImage.src = './img/afternoon.jpg';
     document.body.style.backgroundColor = 'var(--color2)';
    // Good Evening
  } else if (hour >= 18 && hour <= 23) {
    timeImage.src = './img/evening.jpg';
     document.body.style.backgroundColor = 'var(--color3)';
  }
}
