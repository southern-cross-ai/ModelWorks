import '../app/globals.css';
import ChatHistory from './components/ChatHistory';

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="flex h-screen">
        <aside className="w-64 bg-zinc-900 text-white p-4 overflow-y-auto border-r border-zinc-800">
          <h2 className="text-2xl font-bold mb-6">💬 Chat History</h2>
          <ChatHistory />
        </aside>

        <main className="flex-1">{children}</main>
      </body>
    </html>
  );
}
