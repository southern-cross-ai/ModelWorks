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

// Chat functionality
async function ask() {
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
  chatbox.scrollTop = chatbox.scrollHeight;

  // Placeholder for thinking state
  const botMsg = document.createElement('div');
  botMsg.className = 'message bot';
  botMsg.textContent = '⏳ Thinking...';
  chatbox.appendChild(botMsg);
  chatbox.scrollTop = chatbox.scrollHeight;

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

  chatbox.scrollTop = chatbox.scrollHeight;
}

// Drag and drop placeholders
const dragbox = document.getElementById('dragbox');
dragbox.addEventListener('dragover', (e) => e.preventDefault());
dragbox.addEventListener('drop', (e) => {
  e.preventDefault();
  dragbox.textContent = 'File Dropped! (Implement handler)';
});