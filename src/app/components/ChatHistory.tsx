'use client';

const mockChats = [
  { id: 1, title: 'Chat with AI' },
];

export default function ChatHistory() {
  return (
    <ul className="space-y-2">
      {mockChats.map((chat) => (
        <li
          key={chat.id}
          className="cursor-pointer p-3 rounded-lg hover:bg-zinc-800 transition-colors"
        >
          {chat.title}
        </li>
      ))}
    </ul>
  );
}
