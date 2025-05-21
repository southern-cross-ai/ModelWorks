// Theme toggle
const toggleBtn = document.getElementById('theme-toggle');
toggleBtn.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  if (toggleBtn.innerHTML == "🌔") {
    toggleBtn.innerHTML = "🌒"
  }
  else {
    toggleBtn.innerHTML = "🌔"
  }
});

let droppedFile = null;
// Drag and drop placeholders
const dragbox = document.getElementById('dragbox');
dragbox.addEventListener('dragover', (e) =>{ e.preventDefault(); 
const isDark = document.body.classList.contains('dark');
dragbox.style.border = isDark ? "2px dashed #88aacc" : "2px dashed #66cc88";
dragbox.style.backgroundColor = isDark ? "#333944" : "#f0fff0";
});
dragbox.addEventListener('dragleave', (e) => {
  e.preventDefault();
  dragbox.style.border = "2px dashed #ccc";
  dragbox.style.backgroundColor = "";
});
dragbox.addEventListener('drop', (e) => {
  e.preventDefault();
  dragbox.style.border = "2px dashed #ccc";
  dragbox.style.backgroundColor = "";
  // dragbox.textContent = 'File Dropped! (Implement handler)';
  const files = e.dataTransfer.files;
  if (files.length > 0 && files[0].type === "application/pdf") {
    droppedFile = files[0];
    dragbox.textContent = `Selected: ${droppedFile.name}`;
  }
});

// PDF upload
let uploadInProgress = false;
async function uploadPDF() {
  if (uploadInProgress) {
  dragbox.textContent = "⏳ Upload already in progress...";
  return;
  }

  if (!droppedFile) {
    dragbox.textContent = "⚠️ Please select a PDF first.";
    return;
  }
  uploadInProgress = true;
  const formData = new FormData();
  formData.append("file", droppedFile);

  dragbox.textContent = "📤 Uploading PDF...";

  try {
    const res = await fetch("http://localhost:7860/upload", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    uploadInProgress = false;
    dragbox.textContent = "✅ PDF uploaded: " + data.result;
  } catch (err) {
    dragbox.textContent = "❌ Upload failed: " + err.message;
  } finally {
    uploadInProgress = false;
  }
}


// Chat functionality
async function ask() {
  if (uploadInProgress) {
    alert("📄 PDF is still being processed. Please wait.");
    return;
  }
  const queryInput = document.getElementById('query');
  const query = queryInput.value.trim();
  if (!query) return;

  // Display user message
  const chatbox = document.getElementById('chatbox');
  const userMsg = document.createElement('div');
  userMsg.className = 'message user';
  userMsg.textContent = query;
  chatbox.appendChild(userMsg);

  queryInput.value = '';
  scrollToBottom(chatbox);

  // Placeholder for thinking state
  const botMsg = document.createElement('div');
  botMsg.className = 'message bot';
  botMsg.textContent = '⏳ Thinking...';
  chatbox.appendChild(botMsg);
  scrollToBottom(chatbox);

  try {
    const res = await fetch('http://localhost:7860/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });
    const data = await res.json();
    botMsg.textContent = data.result;
    document.getElementById('history').textContent += `You: ${query}\nAI: ${data.result}\n\n`; 
  } catch (err) {
    botMsg.textContent = '❌ Error: ' + err.message;
  }

  scrollToBottom(chatbox);
}

function scrollToBottom(chatbox) {
  chatbox.scrollTop = chatbox.scrollHeight;
}