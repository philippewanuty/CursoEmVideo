function calculating() {
  var Start = document.getElementById('start');
  var End = document.getElementById('end');
  var Step = document.getElementById('step');
  var Result = document.getElementById('showResult');

  var startValue = Number(Start.value);
  var endValue = Number(End.value);
  var stepValue = Number(Step.value);

  var resultString = ' ';

  if (Start.value === '' || End.value === '' || Step.value === '') {
    Result.innerHTML = ` Counting: <br> Empty field is Impossible to count!`;
  } else {
    if (stepValue == 0 || stepValue < 0) {
      window.alert(` Counting: Step 0 is Impossible to count, the value of 1 was adopted`);
      var stepValue = 1;
    }
    if (startValue > endValue) {
      for (var init = startValue; init >= endValue; init = init - stepValue) {
        resultString += init + '👉 ';
      }
      Result.innerHTML = ` Counting: (reverse) <br> ${resultString} 🚩`;
    } else {
      for (var init = startValue; init <= endValue; init += stepValue) {
        resultString += init + '👉 ';
      }
      Result.innerHTML = ` Counting: <br> ${resultString} 🚩`;
    }
  }
}
