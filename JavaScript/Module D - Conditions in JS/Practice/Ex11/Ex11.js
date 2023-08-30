function voteAge() {
  //function actived by button
  var tagAge = document.getElementById('Age'); //call the tag input
  var age = Number(tagAge.value); //get the value of input
  var result = document.getElementById('result'); //call the tag for print the result

  // Nested condiction
  if (age >= 18 && age <= 69) {
    result.innerHTML = `Your age is ${age}, you have to vote this year. `;
  } else if (age >= 16 && age < 18) {
    result.innerHTML = `Your age is ${age},You reached the minimun age to vote, your vote is optional`;
  } else if (age > 69) {
    result.innerHTML = `Your age is ${age} ,You reached the maximum age to vote, your vote is optional`;
  } else {
    result.innerHTML = `Your age is ${age},You are too younger to vote `;
  }
}
