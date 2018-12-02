
function MyUI(text) {
    console.log(text)
}

var id=1;

function AddTableRow(){
    var tr = document.createElement("tr");
    
    var td1 = document.createElement("td");
    var td2 = document.createElement("td");
    var td3 = document.createElement("td");

    td1.innerText = "产品" + id;
    id= id+1;

    td2.innerText = "002";

    td3.innerText = "ok";

    if(id % 3 == 1){
        tr.className = "success";
    }
    else if(id % 3 == 2){
        tr.className = "warning";
    }
    else{
        tr.className = "active";
    }
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);

    var elem = document.getElementById("table001body");
    elem.appendChild(tr);
}