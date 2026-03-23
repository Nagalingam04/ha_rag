import { useState } from "react";
import { askQuestion } from "../api";

export default function Chat() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question) return;

    setLoading(true);
    try {
      const res = await askQuestion(question);
      setResponse(res.data);
    } catch {
      alert("Error fetching answer");
    }
    setLoading(false);
  };

  return (
    <div>
      <h3>💬 Ask a Question</h3>

      <input
        type="text"
        placeholder="Type your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={handleAsk}>
        {loading ? "Thinking..." : "Ask"}
      </button>

      {response && (
        <div className="result">
          <p>
            <span className="label">Answer:</span> {response.answer}
          </p>

          <p>
            <span className="label">Pages:</span>{" "}
            {response.pages.join(", ")}
          </p>

          <p>
            <span className="label">Confidence:</span>{" "}
            {response.confidence}
          </p>
        </div>
      )}
    </div>
  );
}