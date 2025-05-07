async function ask() {
  const query = document.getElementById("query").value;
  const answerBox = document.getElementById("answer");
  answerBox.innerText = "⏳ Thinking...";

  try {
    const res = await fetch("http://localhost:7860/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ query })
    });

    const data = await res.json();
    answerBox.innerText = data.result;
  } catch (err) {
    answerBox.innerText = "❌ Error: " + err.message;
  }
}
