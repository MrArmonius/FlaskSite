// Get the template HTML and remove it from the doument template HTML and remove it from the document
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
  acceptedFiles: '.stl', //This the extensions of files accepted. We can have <image/*, audio/*> or <.stl, .pdf>
  autoQueue: true, // Make sure the files aren't queued until manually added
  previewsContainer: "#previews", // Define the container to display the previews
  maxFilesize: 95,  //10 MiB is here the max file upload size constraint
  maxFiles: 1, //Limit to one file
  timeout: 999999,
});

myDropzone.on("addedfile", function(file) {
  // Hookup the start button
  file.previewElement.querySelector("#previews .start").onclick = function() { myDropzone.enqueueFile(file); };
});

myDropzone.on("sending", function(file) {
  // And disable the start button
  file.previewElement.querySelector(".start").setAttribute("disabled", "disabled");

  //Change thumbnail default
  myDropzone.emit("thumbnail", file, "static/photo/stl.jpg")
});

myDropzone.on("removedfile", function(file) {
  var name = file.name;
  var xhr = new XMLHttpRequest();
  xhr.open("DELETE", "/upload", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({'id': name}));
  console.log("Succesful send request")
  if (myDropzone.files.length == 0) {
    var button_link = document.getElementById("button_to_display");
    button_link.disabled=true;
  }
  
});

myDropzone.on("complete", function(file) {
  file.previewElement.querySelector("#previews .start").style.display="none";
  file.previewElement.querySelector("#previews .cancel").style.display="none";
  file.previewElement.querySelector("#previews .delete").style.display="initial";
  if (myDropzone.files.length > 0) {
    var button_link = document.getElementById("button_to_display");
    button_link.disabled=false;
  }
  var name_file = file.name.substring(0, file.name.length - 4)
  get_thumbnail_link(name_file, file)
});

function get_thumbnail_link(file_name, file) {

  var path = "/thumbnail/" + file_name;
  send_XML_request(response_thumbnail,path, file);
}

function response_thumbnail(response, file) {
  myDropzone.emit("thumbnail", file, response)
}

function send_XML_request(function_response, path, extra_args, type="GET") {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       function_response(xhttp.responseText, extra_args);
    }
  };
  xhttp.open(type, path, true);
  xhttp.send();
}

function url_display() {
  var parameters = "?";
  var first =true;
  for (file of myDropzone.files) {
    if (!first) {
      parameters +="&";
    }
    parameters += "file=" + file.name;
    first = false;
  }
  console.log(parameters);
  var url = "/display" + parameters;

  location.href=url;
  
  
}
