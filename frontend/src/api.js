import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/rag/",
});

export const uploadPDF = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return API.post("upload/", formData);
};

export const askQuestion = (question) =>
  API.get(`ask/?q=${question}`);