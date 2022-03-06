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



