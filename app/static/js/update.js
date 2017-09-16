chrome.permissions.request({
  permissions: ['clipboardRead'],
  origins: ['http://www.google.com/']
});

$(document).ready(function () {

  var textArea = $('#body');
  textArea.focus()
  document.execCommand("Paste");
  console.log(textArea);

})
