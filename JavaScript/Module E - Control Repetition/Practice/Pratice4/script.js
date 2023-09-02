function Table() {
  var HtmlInput = document.getElementById('hNumber');
  var Result = document.getElementById('hText');
  var Stable = document.getElementById('sTable');
  var numberInput = Number(HtmlInput.value);
  var ResulTable = '';
  //numberInput = 7;

  if (HtmlInput.value == '') {
    window.alert('Please enter any number');
  } else {
    Stable.innerHTML= ''
    for (var i = 1; i <= 10; i++) {
      var result = numberInput * i;
      var table = `${numberInput} x ${i} = ${result}`;
      var item = document.createElement('option');
      item.text = table;
      Stable.appendChild(item)
    }
  }

}
