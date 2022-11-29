function tabover(evt, tabName, parId) {
  let i, tabcontent, tablinks;
  
  tabcontent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent.length; i++) {
    if (tabcontent[i].parentElement.getAttribute("for") === parId) {
      tabcontent[i].style.display = "none";
    }
  }

  tablinks = document.getElementsByClassName("tab");
  for (i = 0; i < tablinks.length; i++) {
    if (tablinks[i].parentElement.getAttribute("id") === parId) {
      tablinks[i].className = tablinks[i].className.replace(" tab-active", "");
    }
  }

  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " tab-active";
}