AI-Powered Data Cleaning Assistant is a smart and interactive tool built using Python, Streamlit, and Pandas that helps users clean and prepare datasets effortlessly. It identifies missing values, detects outliers, removes duplicate records, and even auto-generates SQL table schemas — all with a simple CSV upload.

This project is designed for students, data analysts, and developers who want to automate data preprocessing tasks with an easy-to-use interface.

🔥 Key Features

Missing Value Detection – Automatically scans your dataset for null entries.

Duplicate Handling – Identifies and removes duplicate rows.

Outlier Detection – Highlights unusual values using statistical methods.

SQL Schema Generator – Generates SQL CREATE TABLE scripts based on your dataset structure.

Cleaned CSV Export – Download the cleaned dataset instantly.

User-Friendly UI – Powered by Streamlit for an interactive and modern web experience.

🧰 Tech Stack

Python

Pandas

Streamlit

Scikit-learn (optional for advanced detection)

CSV / SQL

🎯 Purpose

This project simplifies the data-cleaning process, making it faster and more accurate. Perfect for:

Data science learners

Analysts preparing datasets

Students building ML or BI projects

Anyone working with messy CSV file

1. Perfect Project Folder Structure

Create your folder exactly like this:

AI-Data-Cleaning-Assistant/
│
├── app.py
├── sample_data.csv
├── requirements.txt
├── README.md
│
└── cleaner/
    ├── __init__.py
    └── cleaning.py


📌 This is the final structure you will upload to GitHub.

✅ 2. READY-TO-USE README.md (Copy–Paste This)

Create a file in VS Code → README.md
Paste the text below:

🤖 AI-Powered Data Cleaning Assistant

An AI-powered tool that automates:

✔ Missing Value Detection
✔ Duplicate Removal
✔ Outlier Identification
✔ SQL Schema Generation
✔ Cleaned CSV Export

This project uses Python, Streamlit, Pandas, and AI/LLM integration (optional) to create a complete data-cleaning pipeline.

🚀 Features
🔍 1. Missing Value Detection

Automatically detects missing values for every column.

🧹 2. Duplicate Handling

Identifies and removes duplicate rows.

⚠ 3. Outlier Detection

Uses IQR or Z-score rules to highlight outliers.

🧾 4. SQL Schema Generator

Auto-generates SQL CREATE TABLE script based on your dataset.

📥 5. Cleaned CSV Download

Download cleaned dataset with one click.

📁 Project Structure
AI-Data-Cleaning-Assistant/
│
├── app.py                 # Main Streamlit interface
├── sample_data.csv        # Example dataset
├── requirements.txt        # Libraries required
├── README.md               # Documentation
│
└── cleaner/
    ├── __init__.py
    └── cleaning.py        # Data cleaning functions

🛠️ Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/AI-Data-Cleaning-Assistant.git
cd AI-Data-Cleaning-Assistant

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
streamlit run app.py

📸 Usage

Upload a CSV file

View missing values

Detect outliers & duplicates

Generate SQL table schema

Download cleaned CSV

Easy, fast, automated! ⚡

📜 License

This project is open-source and free to use.



