document.addEventListener('DOMContentLoaded', function () {
    var sectionMenuButton = document.getElementById('section')
    var navbarList = document.querySelector('.navbar ul');
  
    sectionMenuButton.addEventListener('click', function () {
      navbarList.classList.toggle('active');
    });
});