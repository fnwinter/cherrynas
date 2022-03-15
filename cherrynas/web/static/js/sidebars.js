/* global bootstrap: false */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})()

var active_menu = function() {
  if (window.location.pathname == '/')
  {
    document.getElementById("my_computer").classList.add('active');
  }
  else if (window.location.pathname == '/explorer/')
  {
    document.getElementById("explorer").classList.add('active');
  }
};
active_menu();
