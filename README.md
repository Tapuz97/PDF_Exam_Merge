# [![Buy Me a Coffee](https://i.imgur.com/rlatSuk.png)](https://www.buymeacoffee.com/galmitrani1)
# PDF Exam Q&A Merger

## 📘 Introduction

**PDF Exam Q&A Merger** is a Python-based utility designed to help students and educators efficiently merge exam questions and solutions into single, organized PDFs. Whether your files are structured into Q/A folders or a single folder with solution variants, the script handles both cases intelligently.

---

## ⚙️ Features

### Mode 1: Strict Q/A Folder Matching
- Merges PDFs only if both **Q** and **A** folders contain files with **exact matching names**.
- Reports missing question/answer pairs.

### Mode 2: Single-Folder with Regex (Default)
- Automatically detects solution files by filename patterns like `-sol`, `solution`, etc.
- Merges base + solution files together.
- Logs and notifies unmatched files.

### 🪵 Logging
- All operations (merges, errors, skips) are recorded.
- User prompted whether to save the log in the output folder.

### 🧹 Deletion Prompt
- Optionally delete source files **to Recycle Bin** after successful merge using `send2trash`.

---

## 📁 Folder Structure

```
project_folder/
├── Q/                 # Question PDFs (Mode 1)
├── A/                 # Answer PDFs (Mode 1)
├── PDFs/              # Mixed PDFs (Mode 2)
├── Merged/            # Output folder
├── pdf_merger.py      # Main script
└── README.md
```

---

## 🚀 How to Use

### 🧰 Requirements
- Python 3.6+
- Install dependencies:
```bash
pip install PyPDF2 send2trash
```

### ▶️ Run Script

```bash
python Exam_Merge.py
```

- Choose mode (default = 2)
- Input folder paths (default = working directory or subfolders)
- Review merge results
- Decide whether to delete original files
- Choose whether to save log to `Merged/file_operations.log`

---

## 🧪 Example Console Output

```
✅ Merged: prob-23-A.pdf + prob-23-A-sol.pdf → Merged/prob-23-A.pdf
⚠️ No matching solution for: prob-24-A.pdf
⚠️ No base file for: prob-22-B-sol.pdf
🧹 Deleted: prob-23-A.pdf, prob-23-A-sol.pdf
✅ Log saved to: Merged/file_operations.log
```

---

## 🤝 Contribution

1. Fork the repository.
2. Create a branch:
```bash
git checkout -b feature/cool-feature
```
3. Commit your changes:
```bash
git commit -m "Add cool feature"
```
4. Push and open a Pull Request.

---

## 📄 License

MIT License © Gal Mitrani

---

Enjoy cleaner, smarter PDF merging! ☕ If this tool helps you, feel free to [buy me a coffee](https://www.buymeacoffee.com/galmitrani1).