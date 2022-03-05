

const link_standard = document.getElementById("card-button-standard");
const link_express = document.getElementById("card-button-express");

function card_choice(clicked_id) {
    const standard_card = document.getElementById("card-standard");
    const express_card = document.getElementById("card-express");
    console.log(clicked_id);
    if(clicked_id=="card-button-standard") {
        standard_card.classList.remove("card-disabled");
        express_card.classList.add("card-disabled");

        
    } else if(clicked_id=="card-button-express"){
        standard_card.classList.add("card-disabled");
        express_card.classList.remove("card-disabled");
    }

}