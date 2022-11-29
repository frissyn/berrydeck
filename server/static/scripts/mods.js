function toggleUse(name) {
  let i, els, parent, sibling;

  els = document.getElementsByClassName(name);
  for (i = 0; i < els.length; i++) {
    if (els[i].tagName === "INPUT" || els[i].tagName === "SELECT") {
      parent = els[i].parentElement;
      sibling = els[i].previousElementSibling;
      
      if (els[i].disabled) {
        sibling.classList.remove("text-opacity-20");
        parent.classList.remove("cursor-not-allowed");
        parent.classList.add("cursor-pointer");
      } else {
        sibling.classList.add("text-opacity-20");
        parent.classList.remove("cursor-pointer");
        parent.classList.add("cursor-not-allowed");
      }

      els[i].disabled = !els[i].disabled || false;
    }
  }
}