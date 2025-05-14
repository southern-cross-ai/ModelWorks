// GUI


// GENERAL
document.getElementById("alltogether").style.width = "100%"
document.getElementById("alltogether").style.display = "flex"
document.getElementById("alltogether").style.flexDirection = "row"
document.getElementById("alltogether").style.justifyContent = "center"

// text setup
var all_text = document.getElementsByClassName("text")
for (i = 0; i < all_text.length; i++) {
  all_text[i].style.color = 'black';
  all_text[i].style.textAlign = 'center';
}

// display setup
var all_display = document.getElementsByClassName("display")
for (i = 0; i < all_display.length; i++) {
    all_display[i].style.display = "flex"
    all_display[i].style.margin = "auto"
    all_display[i].style.alignItems = "center"
    all_display[i].style.justifyContent = "center"
 }


// LEFT DIV
document.getElementById("left").style.width = "30%"
document.getElementById("left").style.display = "inline-block"


// MIDDLE DIV
document.getElementById("middle").style.display = "inline-block"

// chatbox setup
document.getElementById("chatbox").style.width = "500px";
document.getElementById("chatbox").style.height = "550px";
document.getElementById("chatbox").style.display = "block";
document.getElementById("chatbox").style.margin = "auto";
document.getElementById("chatbox").style.backgroundColor = "purple"; // TODO: switch to diff colour for darkmode
document.getElementById("chatbox").style.padding = "10px"
document.getElementById("chatbox").style.overflow = "auto";
document.getElementById("chatbox").style.overflowY = "scroll";
//document.getElementById("chatbox").style.borderRadius = ".5em";

// LLM responses // TODO: CHANGE TO CLASS
document.getElementById("answer").style.textAlign = "left";
document.getElementById("answer").style.float = "left";
document.getElementById("answer").style.background = "purple"; // TODO: switch to bg colour for darkmode
document.getElementById("answer").style.borderRadius = ".5em";
document.getElementById("answer").style.width = "50%";
document.getElementById("answer").style.padding = "1%";
document.getElementById("answer").style.margin = "1%";

// user responses // TODO: CHANGE TO CLASS
document.getElementById("user").innerHTML = ""
document.getElementById("user").style.textAlign = "right";
document.getElementById("user").style.float = "right";
document.getElementById("user").style.background = "purple"; // TODO: switch to bg colour for darkmode
document.getElementById("user").style.borderRadius = ".5em";
document.getElementById("user").style.width = "50%";
document.getElementById("user").style.padding = "1%";
document.getElementById("user").style.margin = "1%";

// askbox setup
document.getElementById("askbox").style.width = "500px"
document.getElementById("askbox").style.height = "50px"
document.getElementById("askbox").style.display = "flex"
document.getElementById("askbox").style.margin = "auto"
document.getElementById("askbox").style.justifyContent = "center"
document.getElementById("query").style.width = "90%"


// RIGHT DIV
document.getElementById("right").style.width = "30%"
document.getElementById("right").style.display = "flex"
document.getElementById("right").style.alignItems = "center"
document.getElementById("right").style.justifyContent = "center"
document.getElementById("right").style.flexDirection = "column"
//document.getElementById("right").style.backgroundColor = "blue" // for visualisation only

// dragbox setup
document.getElementById("dragbox").style.width = "400px"
document.getElementById("dragbox").style.height = "150px";
document.getElementById("dragbox").style.display = "block"
document.getElementById("dragbox").style.margin = "auto"
document.getElementById("dragbox").style.backgroundColor = "grey"












// FUNCTIONS

// asking function
async function ask() {
  
  const query = document.getElementById("query").value;
  document.getElementById("query").value = "";

  
  const userBox = document.getElementById("user");
  userBox.innerText = query;
  userBox.style.background = "blue"; // TODO: switch to diff colour for darkmode

  
  const answerBox = document.getElementById("answer");
  answerBox.innerText = "⏳ Thinking...";
  answerBox.style.background = "white"; // TODO: switch to diff colour for darkmode

  try {
    const res = await fetch("http://localhost:7860/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query })
    });
    
    document.getElementById("history").innerHTML += "'" + query + "'" + '<br><br>'
    

    const data = await res.json();
    answerBox.innerText = data.result;
  } catch (err) {
    answerBox.innerText = "❌ Error: " + err.message;
  }
  
}


// drag and drop functions
async function dragover(ev) {
  document.getElementById("dragbox").innerText = "insert drag function here"
}

async function drop(ev) {
  document.getElementById("dragbox").innerText = "insert drop function here"
}


// display functions
// lightmode
async function light() { 

  document.body.style.backgroundColor = "white"
  for (i = 0; i < all_text.length; i++) {
    all_text[i].style.color = 'black';
  }

}

// darkmode
async function dark() { 

   document.body.style.backgroundColor = "black"
  for (i = 0; i < all_text.length; i++) {
    all_text[i].style.color = 'white';
 }

}
