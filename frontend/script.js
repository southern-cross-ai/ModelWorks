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
  } 
  catch (err) {
    answerBox.innerText = "❌ Error: " + err.message;
  }
  
}


// RAG functions
async function dragover(ev) {
  document.getElementById("dragbox").innerText = "insert drag function here"
}

async function drop(ev) {
  document.getElementById("dragbox").innerText = "insert drop function here"
}


// websearch functions
// TODO insert

// light/darkmode functions
async function light() { // lightmode
  console.log("lightmode")
  document.body.style.backgroundColor = "white"
  var all_text = document.getElementsByClassName("text")
  for (i = 0; i < all_text.length; i++) {
    all_text[i].style.color = 'black';
  }
}

async function dark() { // darkmode
  console.log("darkmode")
  document.body.style.backgroundColor = "black"
  var all_text = document.getElementsByClassName("text")
  for (i = 0; i < all_text.length; i++) {
    all_text[i].style.color = 'white';
  }
}
