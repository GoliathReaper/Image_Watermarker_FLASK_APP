var slider = document.getElementById("opacityRange");
var output = document.getElementById("price");
output.innerHTML = slider.value; // Display the default slider value
console.log(slider.value);
// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}