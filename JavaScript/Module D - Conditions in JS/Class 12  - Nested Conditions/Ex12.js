//Else if

function DiscoveryDay() {
  
  var Result = document.getElementById('Result');

  var now = new Date();
  var hour = now.getHours();
  var minutes = now.getMinutes();


  if (hour <= 12) {
    Result.innerHTML = `<b>Good morning! it's ${hour}:${minutes} o'clock</b>`;
  } else if (hour > 12 && hour < 18) {
    Result.innerHTML = `<b>Good afternoon! it's ${hour}:${minutes} o'clock</b>`;
  } else if (hour >= 18) {
    Result.innerHTML = `<b>Good evening! it's ${hour}:${minutes} o'clock</b>`;
  }
}
