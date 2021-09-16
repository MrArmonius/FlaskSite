// Get the template HTML and remove it from the doumenthe template HTML and remove it from the doument
var previewNode = document.querySelector("#template");
previewNode.id = "";
var previewTemplate = previewNode.parentNode.innerHTML;
previewNode.parentNode.removeChild(previewNode);

Dropzone.autoDiscover = false;

var myDropzone = new Dropzone('#demo-upload', {
  url:"/upload",
  thumbnailWidth: 1000,
  thumbnailHeight: 1000,
  parallelUploads: 1,
  previewTemplate: previewTemplate,
  autoQueue: true, // Make sure the files aren't queued until manually added
  previewsContainer: "#previews", // Define the container to display the previews
});

myDropzone.on("addedfile", function(file) {
  // Hookup the start button
  file.previewElement.querySelector("#previews .start").onclick = function() { myDropzone.enqueueFile(file); };
});

myDropzone.on("sending", function(file) {
  // And disable the start button
  file.previewElement.querySelector(".start").setAttribute("disabled", "disabled");
});

myDropzone.on("removedfile", function(file) {
  var name = file.name;
  $.ajax({
    type: 'DELETE',
    url: '/upload',
    data: {id: name},
    dataType: 'text'
  });
});

myDropzone.on("complete", function(file) {
  file.previewElement.querySelector("#previews .start").style.display="none";
  file.previewElement.querySelector("#previews .cancel").style.display="none";
  file.previewElement.querySelector("#previews .delete").style.display="initial";
  $.ajax({
    type: 'GET',
    url: '/profile'
  });
});
