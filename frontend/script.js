let uploadInProgress = false;

async function uploadPDF() {
  if (uploadInProgress) {
  answerBox.innerText = "⏳ Upload already in progress...";
  return;
  }
  const fileInput = document.getElementById("pdf");
  const answerBox = document.getElementById("answer");

  if (fileInput.files.length === 0) {
    answerBox.innerText = "⚠️ Please select a PDF first.";
    return;
  }
  uploadInProgress = true;
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  answerBox.innerText = "📤 Uploading PDF...";

  try {
    const res = await fetch("http://localhost:7860/upload", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    uploadInProgress = false;
    answerBox.innerText = "✅ PDF uploaded: " + data.result;
  } catch (err) {
    answerBox.innerText = "❌ Upload failed: " + err.message;
  }
}

async function ask() {
  if (uploadInProgress) {
    alert("📄 PDF is still being processed. Please wait.");
    return;
  }

  const query = document.getElementById("query").value;
  const answerBox = document.getElementById("answer");
  
  if (!query) {
    answerBox.innerText = "⚠️ Please enter a question.";
    return;
  }

  answerBox.innerText = "🤖 Thinking...";

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
