'use client';
import { useState } from 'react';

export default function Home() {
  const [selectedChat, setSelectedChat] = useState(1);
  const [messages, setMessages] = useState([
    { from: 'ai', text: 'Hello! How can I help you today?' },
    { from: 'user', text: 'I need help with my project.' },
    { from: 'ai', text: 'Sure! What kind of project is it?' },
  ]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (input.trim() === '') return;

    setMessages((prev) => [...prev, { from: 'user', text: input }]);
    setInput('');

    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        { from: 'ai', text: 'Thanks for your message!' },
      ]);
    }, 800);
  };

  const handleCopy = (text) => {
    navigator.clipboard.writeText(text);
    alert('Copied!');
  };

  const handleSpeak = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-auto bg-zinc-50 py-6 space-y-6">
        <div className="px-6 text-sm text-zinc-500">
          You are chatting with <strong>Chat #{selectedChat}</strong>
        </div>

        {messages.map((msg, idx) => (
          <div key={idx} className="px-6">
            {msg.from === 'user' ? (
              <div className="flex justify-end">
                <div className="bg-blue-500 text-white px-4 py-2 rounded-lg max-w-[75%]">
                  {msg.text}
                </div>
              </div>
            ) : (
              <div className="flex flex-col items-start">
                <p className="text-gray-800 text-base max-w-[75%]">{msg.text}</p>
                <div className="mt-2 flex gap-3 text-sm text-gray-500">
                  <button onClick={() => handleCopy(msg.text)} className="hover:text-blue-500">📋</button>
                  <button className="hover:text-green-600">👍</button>
                  <button className="hover:text-red-600">👎</button>
                  <button onClick={() => handleSpeak(msg.text)} className="hover:text-purple-600">🔊</button>
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="p-4 border-t bg-white flex items-center gap-2">
        <input
            type="text"
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            className="w-full border border-gray-300 rounded-full px-4 py-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400 
                      text-gray-800 placeholder-gray-600"
          />

        <button
          onClick={handleSend}
          className="bg-blue-500 text-white px-4 py-2 rounded-full hover:bg-blue-600"
        >
          Send
        </button>
      </div>
    </div>
  );
}
