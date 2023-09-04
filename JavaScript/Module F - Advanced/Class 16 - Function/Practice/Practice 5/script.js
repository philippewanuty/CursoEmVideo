var Result = document.getElementById('hText');

function Table() {
  var HtmlInput = document.getElementById('hNumber');

  var Stable = document.getElementById('sTable');
  var numberInput = Number(HtmlInput.value);

  var numberList = [];
  //numberInput = 7;

  if (HtmlInput.value == '') {
    window.alert('Please enter any number');
  }
  if (numberInput < 1 || numberInput > 100) {
    window.alert('Please, enter a number between 1 and 100');
  } else {
    Stable.innerHTML = '';
    //from here down
    numberList.push(numberInput);
    var item = document.createElement('option');
    item.text = `Value ${numberInput} has added`; //here should have the content;
    Stable.appendChild(item);
  }
}
function Finalize() {
  Result.innerHTML=`oi`;
}
//}
