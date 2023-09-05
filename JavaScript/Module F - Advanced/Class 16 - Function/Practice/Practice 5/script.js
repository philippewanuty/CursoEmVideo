var Result = document.getElementById('hText');
var InputNumber = document.getElementById('iNumber');
var Stable = document.getElementById('sTable');

var numberList = [];

// function to validate the number between  1 and 100

function nMax(n) {
  if (Number(n) >= 1 && Number(n) <= 100) {
    return true;
  } else {
    return false;
  }
}

function inList(n, l) {
  if (l.indexOf(Number(n)) != -1) {
    return true;
  } else {
    return false;
  }
}

function inTable() {
  if (nMax(InputNumber.value) && !inList(InputNumber.value, numberList)) {
    numberList.push(Number(InputNumber.value));
    var item = document.createElement('option');
    item.text = `Value ${InputNumber.value} has added`;
    Stable.appendChild(item);
    Result.innerHTML = '';
  } else {
    window.alert(`Wrong number or number already in list`);
  }
  InputNumber.value = '';
  InputNumber.focus();
}

function Finalize() {
  if (numberList.length == 0) {
    window.alert(`Please enter values before finalize`);
  } else {
    const ArraySum = numberList.reduce((a, e) => a + e, 0);

    Result.innerHTML = `<br> ${numberList.length} Numbers registred <br>`;
    Result.innerHTML += `The number ${Math.max(...numberList)} is the biggest <br>`;
    Result.innerHTML += `The number ${Math.min(...numberList)} is the smallest <br>`;
    Result.innerHTML += `The Sum of all numbers is ${ArraySum}<br>`;
    Result.innerHTML += `the average of the values ​​is ${ArraySum / numberList.length}
  `;
  }
}
