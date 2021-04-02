function changeText(){
    console.log('change text')
    var textToChange = document.getElementById('file-input-text')
    textToChange.innerHTML = 'Your file is uploaded. Press Upload to continue.'
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
