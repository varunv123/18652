var req;

// Sends a new request to update the message list
function sendRequest() {
    if (window.XMLHttpRequest) {
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.onreadystatechange = handleResponse;
    req.open("GET", "/intro/get-list", true);
    req.send(); 
}

// This function is called for each request readystatechange,
// and it will eventually parse the XML response for the request
function handleResponse() {
    if (req.readyState != 4 || req.status != 200) {
        return;
    }

    // Removes the old messages
    var list = document.getElementById("message-list");
    while (list.hasChildNodes()) {
        list.removeChild(list.firstChild);
    }

    // Parses the response to get a list of JavaScript objects for 
    // the messages.
    var items = JSON.parse(req.responseText);
    console.log(items)
    // Adds each new message to the list
    for (var i = 0; i < items.length; ++i) {
        // Extracts the item id and text from the response
        var messageText = items[i]["fields"]["text"];
        var messageTime = items[i]["fields"]["time"];
        var messageUser = items[i]["fields"]["username"];

  
        // Builds a new HTML list item for messages
        var newItem = document.createElement("li");
        console.log(messageTime)
        newItem.innerHTML = messageTime + ", " + messageUser + ": " +  messageText;
        // Adds the message to the HTML list
        list.appendChild(newItem);
    }
}

// causes the sendRequest function to run every 0.5 seconds
window.setInterval(sendRequest, 500);
