window.addEventListener("scroll", function () {

    let header = document.querySelector("header");

    header.classList.toggle("solid-header", window.scrollY > 15);
})