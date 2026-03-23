import { useState } from "react";
import { uploadPDF } from "../api";

export default function Upload() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Select a PDF");

    setLoading(true);
    try {
      await uploadPDF(file);
      alert("PDF uploaded successfully!");
    } catch {
      alert("Upload failed");
    }
    setLoading(false);
  };

  return (
    <div>
      <h3>📄 Upload PDF</h3>

      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload}>
        {loading ? "Uploading..." : "Upload PDF"}
      </button>
    </div>
  );
}