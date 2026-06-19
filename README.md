<div align="center">

# 🎙️ Synthetic Interview Dataset Generator

**A Python-based toolkit for generating structured, labeled synthetic interview datasets — built to test and benchmark AI interview evaluation systems.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Validation-PASSED-2ea44f?style=flat-square)
![License](https://img.shields.io/badge/License-Educational-lightgrey?style=flat-square)
![Samples](https://img.shields.io/badge/Total%20Samples-180-blue?style=flat-square)
![Domains](https://img.shields.io/badge/Domains-4-orange?style=flat-square)

</div>

---

## 📑 Table of Contents
- [Project Overview](#-project-overview)
- [Objective](#-objective)
- [Features](#-features)
- [Domains](#-domains)
- [Difficulty Levels](#-difficulty-levels)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Dataset Format](#-dataset-format)
- [Sample Output](#-sample-output)
- [How to Run](#️-how-to-run)
- [Output Files](#-output-files)
- [Validation](#-validation)
- [Results](#-results)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## 📌 Project Overview

The **Synthetic Interview Dataset Generator** is a Python-based application developed to generate synthetic interview datasets for testing AI-based interview evaluation systems. The project minimizes dependency on real interview data by generating structured interview questions and multiple answer variations with labels.

---

## 🎯 Objective

- Generate synthetic interview questions
- Generate **Correct**, **Partial**, and **Incorrect** answers
- Create a balanced interview dataset
- Export the dataset into **JSON** and **CSV** formats
- Validate the generated dataset automatically

---

## 🚀 Features

| Feature | Detail |
|---|---|
| 🧠 Technical Domains | 4 |
| 📊 Difficulty Levels | 3 |
| ❓ Interview Questions | 60 |
| 🗂️ Total Samples | 180 |
| 📤 JSON Export | ✅ |
| 📤 CSV Export | ✅ |
| 🔍 Dataset Validation | ✅ |
| 📝 Validation Report Generation | ✅ |

---

## 📚 Domains

1. 💻 Programming & Object-Oriented Concepts
2. 🗄️ SQL & Database Systems
3. 🤖 Machine Learning & AI
4. 🏗️ Software Engineering

---

## 📊 Difficulty Levels

| Level | Description |
|---|---|
| 🟢 Easy | Foundational, definition-level questions |
| 🟡 Medium | Applied, scenario-based questions |
| 🔴 Hard | In-depth, conceptual or design-level questions |

---

## 📂 Project Structure

```
Synthetic_Interview_Dataset_Generator/
│
├── question_bank.py
├── answer_bank.py
├── dataset_generator.py
├── validator.py
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── interview_dataset.json
│   ├── interview_dataset.csv
│   ├── validation_report.json
│   └── validation_sample.json
```

---

## 🛠 Technologies Used

- 🐍 Python 3.10+
- 📦 JSON
- 📄 CSV
- 📁 pathlib
- 🧮 collections
- 🏷️ typing

---

## 📄 Dataset Format

Each record in the dataset follows this structure:

```json
{
    "domain": "Programming & Object-Oriented Concepts",
    "difficulty": "Easy",
    "question": "What is a variable and why is it used in programming?",
    "answer": "A variable is a named storage location used to store data values during program execution.",
    "label": "correct"
}
```

---

## 🔎 Sample Output

A glimpse of the kind of labeled variations the generator produces for a single question:

```json
[
  {
    "domain": "SQL & Database Systems",
    "difficulty": "Medium",
    "question": "What is the purpose of a JOIN clause in SQL?",
    "answer": "A JOIN clause combines rows from two or more tables based on a related column between them.",
    "label": "correct"
  },
  {
    "domain": "SQL & Database Systems",
    "difficulty": "Medium",
    "question": "What is the purpose of a JOIN clause in SQL?",
    "answer": "A JOIN is used to combine tables, though it only works when both tables have the same number of rows.",
    "label": "partial"
  },
  {
    "domain": "SQL & Database Systems",
    "difficulty": "Medium",
    "question": "What is the purpose of a JOIN clause in SQL?",
    "answer": "A JOIN clause is used to delete duplicate rows from a single table.",
    "label": "incorrect"
  }
]
```

> Every question generates exactly 3 labeled answer variations — **correct**, **partial**, and **incorrect** — producing a perfectly balanced dataset.

---

## ▶️ How to Run

### Step 1 — Clone the repository
```bash
git clone <repository_link>
```

### Step 2 — Navigate to the project folder
```bash
cd Synthetic_Interview_Dataset_Generator
```

### Step 3 — Run the project
```bash
python main.py
```

---

## 📁 Output Files

Running `main.py` automatically generates the following files inside `data/`:

| File | Description |
|---|---|
| `interview_dataset.json` | Full dataset in JSON format |
| `interview_dataset.csv` | Full dataset in CSV format |
| `validation_report.json` | Summary report from the validator |
| `validation_sample.json` | Sample subset used for spot-checking |

---

## ✅ Validation

The validator automatically checks:

- ✔️ Total Samples
- ✔️ Missing Fields
- ✔️ Invalid Labels
- ✔️ Duplicate Records
- ✔️ Domain Distribution
- ✔️ Difficulty Distribution
- ✔️ Label Distribution

---

## 📈 Results

<div align="center">

| Metric | Value |
|---|---|
| **Total Questions** | 60 |
| **Total Samples** | 180 |
| **Domains** | 4 |
| **Difficulty Levels** | 3 |
| **Labels** | Correct, Partial, Incorrect |
| **Validation Status** | ✅ **PASSED** |

</div>

---

## 🔮 Future Enhancements

- 🤖 AI-powered Question Generation
- 🔗 Gemini / OpenAI Integration
- 🌐 REST API
- 📊 Streamlit Dashboard
- 📈 Dynamic Dataset Expansion

---

## 👩‍💻 Author

**Kumpati Saniya Darja**
*Prompt Engineering Intern*
**sushma Kumari**
*Python Developer Intern*

---


