const all_photos = document.getElementsByClassName("img-200");
for( photo of all_photos) {
    photo.ondragstart = function() { return false; };
}