# 🎓 Student Marks Analysis System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-orange.svg)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An end-to-end exploratory data analysis (EDA) and academic performance tracking pipeline built with **Python**, **Pandas**, and **Matplotlib**. It automatically processes raw exam datasets, performs descriptive statistical computations, assigns letter grades and rankings, and generates a multi-panel visual analytics dashboard.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Dataset Dictionary](#-dataset-dictionary)
- [Grading Criteria & Methodology](#-grading-criteria--methodology)
- [Analytical Insights & Highlights](#-analytical-insights--highlights)
- [Visual Dashboard](#-visual-dashboard)
- [Project Architecture](#-project-architecture)
- [Getting Started & Installation](#-getting-started--installation)
- [Code Structure & Functions](#-code-structure--functions)
- [Future Scope](#-future-scope)
- [Author & License](#-author--license)

---

## 📖 Project Overview

Educational institutions require quick, automated, and accurate evaluation of student examination records to identify top-performing students and at-risk candidates needing academic intervention.

This project delivers:
1. **Automated Evaluation**: Eliminates manual score aggregation, grade assignment, and rank evaluation.
2. **Comparative Section Analytics**: Compares class sections (e.g., Section 10-A vs 10-B) on performance and attendance.
3. **High-Resolution Graphical Dashboards**: Generates publication-ready visualizations in `.png` format.
4. **Enriched CSV Export**: Produces ready-to-use processed datasets for administrative records.

---

## ✨ Key Features

- **Automated Calculations**: Computes Total Aggregate Marks (out of 500), Percentage, and overall Pass/Fail status.
- **Dynamic Grading System**: Maps percentages to standard letter grades ($A^+$, $A$, $B$, $C$, $D$, $F$).
- **Statistical Profiling**: Calculates Mean, Median, Standard Deviation, Minimum, and Maximum scores for each academic subject.
- **Attendance-Performance Correlation**: Analyzes the linear relationship between student attendance percentages and total exam marks.
- **Top 5 Leaderboard**: Generates leaderboard rankings with student details.
- **Export Capabilities**: Automatically saves both tabular outputs (`.csv`) and graphical dashboards (`.png`) into the `output/` directory.

---

## 📊 Dataset Dictionary

The input dataset (`students_data.csv`) contains the following attributes:

| Field Name | Data Type | Description |
| :--- | :---: | :--- |
| `StudentID` | `String` | Unique alphanumeric identifier for each student (e.g., `STU001`) |
| `Name` | `String` | Full name of the student |
| `Gender` | `String` | Gender category (`Male` / `Female`) |
| `Class_Section`| `String` | Academic grade & section (`10-A`, `10-B`) |
| `Math` | `Integer` | Marks scored in Mathematics (0 – 100) |
| `Science` | `Integer` | Marks scored in Science (0 – 100) |
| `English` | `Integer` | Marks scored in English (0 – 100) |
| `History` | `Integer` | Marks scored in History (0 – 100) |
| `ComputerScience`| `Integer` | Marks scored in Computer Science (0 – 100) |
| `AttendancePercentage` | `Integer` | Student attendance rate over the academic term (0 – 100%) |

---

## 📐 Grading Criteria & Methodology

| Percentage Range | Grade | Description | Minimum Subject Mark |
| :---: | :---: | :--- | :---: |
| **90.0% – 100%** | **A+** | Outstanding / Distinction | $\ge 40$ |
| **80.0% – 89.9%** | **A** | Excellent | $\ge 40$ |
| **70.0% – 79.9%** | **B** | Good | $\ge 40$ |
| **60.0% – 69.9%** | **C** | Average | $\ge 40$ |
| **50.0% – 59.9%** | **D** | Below Average / Pass | $\ge 40$ |
| **< 50.0% or Subject < 40** | **F** | Fail / Needs Remediation | $< 40$ in any subject |

---

## 🏆 Analytical Insights & Highlights

Based on sample execution with $N = 25$ students:

```text
======================================================================
                    STUDENT PERFORMANCE REPORT
======================================================================
Total Students Analyzed: 25
Overall Class Average Percentage: 78.11%
Highest Score: 484 / 500 (96.80%)
Lowest Score:  233 / 500 (46.60%)
Pass Rate: 96.0% (24/25 Students)

----------------------------------------------------------------------
TOP 5 PERFORMERS (RANK LIST)
----------------------------------------------------------------------
 Rank StudentID           Name Class_Section  TotalMarks  Percentage Grade
    1    STU012 Tanvi Deshmukh          10-A         484        96.8    A+
    2    STU002    Ananya Iyer          10-A         473        94.6    A+
    3    STU024  Shruti Pillai          10-A         469        93.8    A+
    4    STU017  Siddharth Roy          10-A         461        92.2    A+
    5    STU006    Sneha Gupta          10-A         460        92.0    A+

----------------------------------------------------------------------
SECTION-WISE COMPARISON (Average Score)
----------------------------------------------------------------------
               TotalMarks  Percentage  AttendancePercentage
Class_Section
10-A               446.00       89.20                 94.08
10-B               339.38       67.88                 82.08
======================================================================
```

- **Top Performing Subject**: Computer Science ($\mu = 82.44$), followed by English ($\mu = 79.92$).
- **Attendance Impact**: Strong positive correlation ($r > 0.85$) between attendance $>90\%$ and achieving Grade A/A+.

---

## 📈 Visual Dashboard

The script creates a 4-panel dashboard saved as `output/student_performance_dashboard.png`:

1. **Average Score by Subject**: Bar chart highlighting performance across subjects.
2. **Grade Distribution**: Donut chart detailing proportions of $A^+$, $A$, $B$, $C$, and $F$ students.
3. **Attendance vs. Total Marks**: Scatter plot with fitted polynomial regression trendline.
4. **Top 5 Performers**: Horizontal bar chart comparing top aggregate scores.

---

## 📁 Project Architecture

```text
Student-Marks-Analysis/
│
├── Student Marks Analysis/
│   ├── students_data.csv                  # Raw input CSV dataset
│   ├── analysis.py                        # Python analysis script
│   ├── requirements.txt                   # Dependency manifest
│   ├── .gitignore                         # Git ignore file
│   ├── README.md                          # Sub-directory documentation
│   └── output/                            # Output directory (auto-created)
│       ├── students_results.csv           # Calculated output CSV
│       └── student_performance_dashboard.png # Visual charts
│
├── .gitignore                             # Root git ignore file
└── README.md                              # Root project documentation
```

---

## 🛠️ Getting Started & Installation

### 1. Clone the repository
```bash
git clone https://github.com/<YOUR_USERNAME>/Student-Marks-Analysis.git
cd Student-Marks-Analysis
```

### 2. Navigate to project folder
```powershell
cd "Student Marks Analysis"
```

### 3. Install required packages
```powershell
pip install -r requirements.txt
```

### 4. Execute the analysis pipeline
```powershell
python analysis.py
```

---

## 💻 Code Structure & Functions

In [`analysis.py`](file:///c:/Users/Admin/OneDrive/Desktop/MyFirst_project/Student%20Marks%20Analysis/analysis.py):

- `load_and_process_data(filepath)`: Reads raw CSV, calculates Total Marks, Percentage, assigns letter Grade, checks pass criteria, and determines rank.
- `print_summary_report(df, subjects)`: Generates tabular console summaries including class metrics, subject statistics, top rankers, and section comparisons.
- `create_visualizations(df, subjects)`: Plots the 4-panel analytical chart using Matplotlib and saves high-DPI image output.
- `main()`: Orchestrates pipeline execution from ingestion to reporting and exports.

---

## 🔮 Future Scope
- [ ] Interactive Web UI with **Streamlit** / **Dash**.
- [ ] Machine Learning predictive model (e.g. Scikit-learn Linear Regression) for future exam score forecasts.
- [ ] Automatic PDF Report Card generation per student using ReportLab.

---

## 📄 License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
