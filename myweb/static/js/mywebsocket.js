var ws = new WebSocket("ws://localhost:3000");
ws.onopen = function(evt){
    console.log("connection open...");
}


ws.onmessage = function(ev){
    console.log("recv:" + ev.data);
    var val =  document.getElementById("msginfo").value;
    val = val + ev.data;
    val = val + "\n";
    console.log(val);
    document.getElementById("msginfo").innerText = val;
}

function ConnServer() {
    console.log("1234");
    MyUI("hello123");
}

function SendText(){
    var val = document.getElementById("chatvalue").value;
    console.log("send text:" + val);
    ws.send(val);
    document.getElementById("chatvalue").value="";
}