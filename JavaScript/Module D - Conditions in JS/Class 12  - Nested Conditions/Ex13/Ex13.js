// Switch
function findDay() {


var Result = document.getElementById('Result')

  var now = new Date();
  var dayWeek = now.getDay();


  switch (dayWeek) {
    case 0:
      Result.innerHTML = `Today is Sunday`;
      break;
    case 1:
      Result.innerHTML = `Today is Moonday`;
      break;
    case 2:
      Result.innerHTML = `Today is Tuesday`;
      break;
    case 3:
      Result.innerHTML = `Today is Wednesday`;
      break;
    case 4:
      Result.innerHTML = `Today is Friday`;
      break;
    case 5:
      Result.innerHTML = `Today is Saturnday`;
      break;
    default:
      Result.innerHTML = `Wrong day`;
      break;
  }
}
