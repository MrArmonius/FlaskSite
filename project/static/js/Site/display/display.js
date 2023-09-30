const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const uuid_file = urlParams.get('file');
console.log(uuid_file);

const standard_card = document.getElementById("card-standard");
const express_card = document.getElementById("card-express");
const final_price = document.getElementById("final-price");

const final_color = document.getElementById("final-color");
const final_material = document.getElementById("final-material");

const collection_price =  document.getElementsByClassName("price");

function card_choice(clicked) {
    
    const clicked_id = clicked.id;
    if(clicked.parentElement.classList.contains("card-disabled")) {
      standard_card.classList.toggle("card-disabled");
      express_card.classList.toggle("card-disabled");
    }
    
    
    if(clicked_id == "card-button-standard") {
      console.log("Standard");
      final_price.innerHTML = document.getElementsByClassName("price-economy")[0].innerHTML;

    } else if (clicked_id == "card-button-express") {
      final_price.innerHTML = document.getElementsByClassName("price-express")[0].innerHTML;
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

function refresh_price(price) {
  for (const element_price of collection_price){
    if (price == null) {
      element_price.innerHTML = '<div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>';
    } else {
      if(element_price == final_price) {
        if(standard_card.classList.contains("card-disabled")) {
          final_price.innerHTML = document.getElementsByClassName("price-express")[0].innerHTML;
        } else {
          final_price.innerHTML = document.getElementsByClassName("price-economy")[0].innerHTML;
        }
      } else {
        if(element_price.classList.contains("price-express")) {
          element_price.innerHTML = (price*2).toString() + " €";
        } else {
          element_price.innerHTML = price.toString() + " €";
        }
        
      }
      
    }
    
  }

}



//Function to show the selected items
function selected_item(li_element) {
  
  //Get parents
  ul_element = li_element.parentElement;
  for (let li_sample of ul_element.children) {
    if (li_sample.classList.contains('choice-item-selected')) {
      li_sample.classList.remove('choice-item-selected');
    }

    if (li_sample == li_element) {
      li_element.classList.add("choice-item-selected");

    }
  }

  if(li_element.classList.contains("material-item")) {
    final_material.innerText = li_element.innerText;
  } else if (li_element.classList.contains("color-item")) {
    final_color.innerText = li_element.innerText;
  }
}

//Function calculate price
function calculate_price() {
  //Build data to send it with the request
  choices = document.getElementsByClassName("choice-item-selected");
  let json_data = {};
  for (let choice of choices) {
    console.log("Parent: ", choice.parentElement.parentElement.parentElement.parentElement);
    let key = choice.parentElement.parentElement.parentElement.parentElement.id;
    json_data[key] = choice.getAttribute("data-item");
  }

  console.log("Example JSON: ", json_data);
  console.log("Stringify json: ", JSON.stringify(json_data));

  //Send request
  const req = new XMLHttpRequest();
  req.addEventListener("load", request_complete_price);
  req.addEventListener("error", request_failed_price);
  req.addEventListener("abort", request_failed_price);
  req.open("POST", "/price/"+uuid_file);
  req.setRequestHeader("Content-Type", "application/json; charset=utf-8");
  req.send(JSON.stringify(json_data));
}

function request_complete_price(evt) {
  console.log("Succes");
  console.log(evt);
  console.log(this);
  if (this.status == 200){
    const response = JSON.parse(this.response);
    console.log(response);
    refresh_price(response.price)
  } else if (this.status == 206) {
    refresh_price(null)
    setTimeout(calculate_price, 3000);
  }

  
}

function request_failed_price(evt) {
  console.log("Failed");
  console.log(evt);
}



function setup_options() {
  const items_selected = document.getElementsByClassName("choice-item-selected");
  for(item_selected of items_selected) {
    if (item_selected.classList.contains("material-item")) {
      final_material.innerText = item_selected.innerText;
    } else if (item_selected.classList.contains("color-item")) {
      final_color.innerText = item_selected.innerText;
    }
  }
}

function add_cart() {
  
}


// Setup functions
calculate_price();
setup_options();