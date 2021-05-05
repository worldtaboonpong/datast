function changeText(){
    console.log('change text')
    var textToChange = document.getElementById('file-input-text')
    textToChange.innerHTML = 'Your file is uploaded. Press Upload to continue.'
    var submit_button = document.getElementById('upload-submitted-file')

    console.log(submit_button)
    submit_button.disabled = false
    submit_button.style.background = "#16a085"
    submit_button.style.borderBottom = "4px solid #117a60"
    // submit_button.appendChild(document.createTextNode(" background: #149174; color: #0c5645; "))
    // background: #16a085;
    // border-bottom: 4px solid #117a60;
}

// window.onload = function(){
//     document.addEventListener("scroll", function (e) {
//         var top = this.scrollY;
//         var navbar = document.getElementsByClassName("navbar-custom");
//         var navbar_brand = document.getElementById("header");
//         var navbar_nav = document.querySelectorAll("A")
//         if (top > 60) {
//           document.getElementsByClassName("navbar-custom")[0].style.cssText =
//             "background-color:black";
//           navbar_brand.style.color = "white";
//           // navbar_nav[0].style.color = "rgb(219, 217, 217)";
//           navbar_nav.forEach((item) => {
//             item.style.color = "white";
//           });
//         } else {
//           document.getElementsByClassName(
//             "navbar-custom"
//           )[0].style.backgroundColor = "white";
//           navbar_brand.style.color = "black";
//           navbar_nav.forEach((item) => {
//             item.style.color = "rgb(73, 72, 72)";
//           });
//         }
//       });
// }
