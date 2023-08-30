function getInformation() {
  var ShowAge = document.getElementById('showAge');
  var AgeImage = document.getElementById('Image');
  var PlaceAge = document.getElementById('placeAge');
  var inputRadio = document.getElementsByName('gender');

  var time = new Date();
  var year = time.getFullYear();
  var NumberpAge = Number(PlaceAge.value);
  var yearAge = year - NumberpAge;
  var getGender = '';

  if (inputRadio[0].checked) {
    getGender = `Male`;
    //Child
    if (NumberpAge >= 2008 && NumberpAge <= 2022) {
      ShowAge.innerHTML = `We detect: a child, gender ${getGender},  with ${yearAge} years old`;
      AgeImage.src = './img/MaleChild.jpeg';
      //Adult
    } else if (NumberpAge > 1963 && NumberpAge < 2008) {
      ShowAge.innerHTML = `We detect: an adult, gender ${getGender}, with ${yearAge} years old.`;
      AgeImage.src = './img/AdultMan.jpeg';
      //Elderly
    } else if (NumberpAge >= 1000 && NumberpAge < 1963) {
      ShowAge.innerHTML = `We detect: an elderly, gender ${getGender}, with ${yearAge} years old`;
      AgeImage.src = './img/OldMan.jpeg';
    } else {
      ShowAge.innerHTML = `ERROR, the value cannot be computed`;
      AgeImage.src = './img/Heaven.jpeg';
    }
  } else if (inputRadio[1].checked) {
    getGender = `Female`;
    //Child
    if (NumberpAge >= 2008 && NumberpAge <= 2022) {
      ShowAge.innerHTML = `We detect: a child, gender ${getGender}, with ${yearAge} years old`;
      AgeImage.src = './img/FamaleChild.jpeg';
      //Adult
    } else if (NumberpAge > 1963 && NumberpAge < 2008) {
      ShowAge.innerHTML = `We detect: an adult, gender ${getGender}, with ${yearAge} years old.`;
      AgeImage.src = './img/AdultWoman.jpeg';
      //Elderly
    } else if (NumberpAge >= 1000 && NumberpAge < 1963) {
      ShowAge.innerHTML = `We detect:  an elderly, gender ${getGender}, with ${yearAge} years old`;
      AgeImage.src = './img/OldWoman.jpeg';
    } else {
      ShowAge.innerHTML = `ERROR, the value cannot be computed`;
      AgeImage.src = './img/Heaven.jpeg';
    }
  }
}
