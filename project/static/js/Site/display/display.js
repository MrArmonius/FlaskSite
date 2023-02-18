const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const uuid_file = urlParams.get('file');
console.log(uuid_file);

function card_choice(clicked_id) {
    const standard_card = document.getElementById("card-standard");
    const express_card = document.getElementById("card-express");

    if(clicked_id=="card-button-standard") {
        standard_card.classList.remove("card-disabled");
        express_card.classList.add("card-disabled");

        
    } else if(clicked_id=="card-button-express"){
        standard_card.classList.add("card-disabled");
        express_card.classList.remove("card-disabled");
    }

}

var triggerTabList = [].slice.call(document.querySelectorAll('#materialList a'));
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl);
  triggerEl.addEventListener('click', function (event) {
    event.preventDefault();
    tabTrigger.show();
  });
});


const collection_price =  document.getElementsByClassName("price");

function refresh_price() {
  for (const element_price of collection_price){
    element_price.innerHTML = '<div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>';
  }
  const req = new XMLHttpRequest();
  req.addEventListener("load", request_complete_price);
  req.addEventListener("error", request_failed_price);
  req.addEventListener("abort", request_failed_price);
  req.open("GET", "/api_engine/"+uuid_file);
  req.send();
}

function request_complete_price(evt) {
  console.log(evt);
}

function request_failed_price(evt) {
  console.log(evt);
}

//refresh_price();



