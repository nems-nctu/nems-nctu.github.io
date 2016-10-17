$(document).ready(function() {

});

var scrollOffset = 60;

$('a[href=#]').click(function() {
  $('html, body').animate({ scrollTop: - scrollOffset }, 'show');
});

$('a[href=#members]').click(function() {
  $('html, body').animate({ scrollTop: $('#members').offset().top - scrollOffset }, 'show');
});

$('a[href=#projects]').click(function() {
  $('html, body').animate({ scrollTop: $('#projects').offset().top - scrollOffset }, 'show');
});

$('a[href=#photos]').click(function() {
  $('html, body').animate({ scrollTop: $('#photos').offset().top - scrollOffset }, 'show');
});