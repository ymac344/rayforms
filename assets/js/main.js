(function () {
  'use strict';

  var en = document.documentElement.lang === 'en';
  var text = en
    ? { close: 'Close', name: 'Name', phone: 'Phone', email: 'Email', subject: 'Website inquiry' }
    : { close: 'סגירה', name: 'שם', phone: 'טלפון', email: 'אימייל', subject: 'פנייה מהאתר' };

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
  }

  // Dropdowns: open on click/tap as well as hover
  document.querySelectorAll('.nav-parent').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var li = btn.parentElement;
      var open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.nav li.open').forEach(function (li) { li.classList.remove('open'); });
    if (document.activeElement && document.activeElement.closest('.subnav')) document.activeElement.blur();
  });

  // Design picker: switch layout and colour scheme without reloading, and remember the choice
  var root = document.documentElement;
  var defaults = { design: 'classic', layout: 'standard' };
  var pickerLinks = document.querySelectorAll('a[data-set]');
  function currentValue(set) { return root.getAttribute('data-' + set) || defaults[set]; }
  function markPicker() {
    pickerLinks.forEach(function (a) {
      a.classList.toggle('is-current', a.getAttribute('data-value') === currentValue(a.getAttribute('data-set')));
    });
  }
  pickerLinks.forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var set = a.getAttribute('data-set');
      var value = a.getAttribute('data-value');
      if (value === defaults[set]) root.removeAttribute('data-' + set);
      else root.setAttribute('data-' + set, value);
      try {
        localStorage.setItem(set, value);
        history.replaceState(null, '', '?layout=' + currentValue('layout') + '&design=' + currentValue('design') + location.hash);
      } catch (err) {}
      markPicker();
    });
  });
  markPicker();

  // Hero video: skip it for visitors who prefer reduced motion or save data
  var video = document.querySelector('.hero-media[data-src]');
  if (video) {
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var saveData = navigator.connection && navigator.connection.saveData;
    if (!reduce && !saveData) {
      video.src = video.getAttribute('data-src');
      var p = video.play();
      if (p && p.catch) p.catch(function () {});
    }
  }

  // Image lightbox
  var links = document.querySelectorAll('[data-lightbox]');
  if (links.length && window.HTMLDialogElement) {
    var dialog = document.createElement('dialog');
    dialog.className = 'lightbox';
    dialog.innerHTML = '<button type="button" aria-label="' + text.close + '">&times;</button><img alt="">';
    document.body.appendChild(dialog);
    var img = dialog.querySelector('img');
    dialog.addEventListener('click', function (e) { if (e.target !== img) dialog.close(); });
    links.forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        img.src = a.href;
        img.alt = (a.querySelector('img') || {}).alt || '';
        dialog.showModal();
      });
    });
  }

  // Contact form: opens the visitor's email app with the details filled in
  document.querySelectorAll('form[data-mailto]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var lines = [
        text.name + ': ' + (d.get('name') || ''),
        text.phone + ': ' + (d.get('phone') || '')
      ];
      if (d.get('email')) lines.push(text.email + ': ' + d.get('email'));
      lines.push('', d.get('message') || '');
      var subject = text.subject + ' – ' + (d.get('name') || '');
      window.location.href = 'mailto:' + form.getAttribute('data-mailto') +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(lines.join('\n'));
    });
  });
})();
