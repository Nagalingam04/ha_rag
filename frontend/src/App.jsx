import "./App.css";
import Upload from "./components/Upload";
import Chat from "./components/Chat";

function App() {
  return (
    <div className="container">
      <h1 className="title">HA-RAG Chatbot</h1>

      <div className="card">
        <Upload />
      </div>

      <div className="card">
        <Chat />
      </div>
    </div>
  );
}

export default App;