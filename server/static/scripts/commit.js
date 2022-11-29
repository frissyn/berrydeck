function _htmlFromText(html) {
  // https://stackoverflow.com/a/35385518

  var template = document.createElement('template');
  template.innerHTML = html;
  return template.content.childNodes;
}


function _popFlash() {
  let stale = document.getElementById("flash");
  if (stale && typeof stale !== "undefined") {
    stale.remove();
  };
}


function _flashElement(success, type, msg) {
  let svg;

  if (success === true) {
    svg = (
      '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current ' +
      'flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path ' +
      'stroke-linecap="round" stroke-linejoin="round" stroke-width="2" ' +
      'd="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /> </svg>'
    );
  } else {
    svg = (
      '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current ' + 
      'flex-shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path ' + 
      'stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 ' +
      '0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"/> </svg>'
    );
  }

  return _htmlFromText(
    `<div id="flash" class="alert alert-${type} py-4 shadow">
      <div>${svg}<span>${msg}</span></div>
      <div class="object-right ml-auto mr-0">
        <button class="btn btn-sm btn-ghost" onclick="_popFlash()">OK</button>
      </div>
    </div>`
  )[0];
}


function commit(ev, el) {
  _popFlash();
  ev.preventDefault();
  ev.submitter.classList.add("loading");

  let form = {};
  let payload = new FormData(ev.target);
  let name = ev.target.getAttribute("name");
  let root = document.getElementById("mount");

  payload.forEach((value, key) => {
    form[key] = value;
  });

  fetch(`commit/${name}`, {method: "POST", body: JSON.stringify(form)})
  .then((res) => {
    if (res.ok) {
      res.text().then((t) => {
        let flash = _flashElement(true, "success", t);
        root.insertBefore(flash, root.children[0]);
      })
    } else {
      res.text().then((t) => {
        let flash = _flashElement(false, "error", t);
        root.insertBefore(flash, root.children[0]);
      })
    }
  });
  // .catch((res) => {
  //   res.body.text().then((t) => {
  //     let flash = _flashElement(false, "error", t);
  //     root.insertBefore(flash, root.children[1]);
  //   })
  // });

  ev.submitter.classList.remove("loading");
}