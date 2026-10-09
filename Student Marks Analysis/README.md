# 📊 Student Marks Analysis & Visualization System

A comprehensive Python data analysis pipeline built using **Python**, **Pandas**, and **Matplotlib** to analyze, evaluate, and visualize student academic performance.

---

## 🌟 Key Highlights & Insights

Based on the analyzed cohort of students:
- **Class Average**: **78.11%** with an overall pass rate of **96.0%**.
- **Top Subject**: **Computer Science** had the highest class average (**82.44%**), followed by English (**79.92%**).
- **Strong Attendance Correlation**: High attendance (>90%) strongly correlates with scoring 85%+ overall.
- **Section Comparison**:
  - **Section 10-A**: Average score of **89.20%** (Avg Attendance: 94.08%)
  - **Section 10-B**: Average score of **67.88%** (Avg Attendance: 82.08%)

---

## 🚀 Features

- **Automated Data Processing (Pandas)**:
  - Calculates Total Marks (out of 500), Overall Percentage, and Pass/Fail status.
  - Automatically assigns letter grades ($A^+$, $A$, $B$, $C$, $D$, $F$).
  - Computes ranking leaderboard based on total aggregate score.
  - Generates subject-level descriptive statistics (Mean, Median, Std Dev, Min, Max).
  - Exports enriched results to [`output/students_results.csv`](file:///c:/Users/Admin/OneDrive/Desktop/MyFirst_project/Student%20Marks%20Analysis/output/students_results.csv).

- **Visual Analytics Dashboard (Matplotlib)**:
  - **Subject Average Comparison**: Bar chart with individual score labels.
  - **Grade Distribution**: Donut chart showing grade percentage breakdown.
  - **Attendance vs. Marks Correlation**: Scatter plot with a linear regression trendline.
  - **Top 5 Performers**: Horizontal ranking chart.
  - Saves high-resolution chart to [`output/student_performance_dashboard.png`](file:///c:/Users/Admin/OneDrive/Desktop/MyFirst_project/Student%20Marks%20Analysis/output/student_performance_dashboard.png).

---

## 🏆 Top Performers (Rank List)

| Rank | Student ID | Name | Section | Total Marks | Percentage | Grade |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| 🥇 **1** | `STU012` | Tanvi Deshmukh | 10-A | **484 / 500** | **96.8%** | A+ |
| 🥈 **2** | `STU002` | Ananya Iyer | 10-A | **473 / 500** | **94.6%** | A+ |
| 🥉 **3** | `STU024` | Shruti Pillai | 10-A | **469 / 500** | **93.8%** | A+ |
| 🏅 **4** | `STU017` | Siddharth Roy | 10-A | **461 / 500** | **92.2%** | A+ |
| 🏅 **5** | `STU006` | Sneha Gupta | 10-A | **460 / 500** | **92.0%** | A+ |

---

## 📐 Grading Criteria

| Percentage Range | Grade | Result Status |
| :--- | :---: | :--- |
| **90% – 100%** | **A+** | Distinction |
| **80% – 89.9%** | **A** | First Class |
| **70% – 79.9%** | **B** | Second Class |
| **60% – 69.9%** | **C** | Average |
| **50% – 59.9%** | **D** | Pass |
| **Below 50% / <40 in any subject** | **F** | Needs Improvement / Fail |

---

## 📁 Project Structure

```text
Student Marks Analysis/
│── students_data.csv                  # Input raw dataset (scores & attendance)
│── analysis.py                        # Core analysis & Matplotlib visualization script
│── requirements.txt                   # Project dependencies (pandas, matplotlib, numpy)
│── README.md                          # Detailed documentation
└── output/                            # Output folder (auto-generated)
    ├── students_results.csv           # Enriched dataset with calculated Grades & Ranks
    └── student_performance_dashboard.png # High-resolution 4-panel visual dashboard
```

---

## 🛠️ Installation & Execution

### 1. Navigate to the project directory:
```powershell
cd "Student Marks Analysis"
```

### 2. Install dependencies:
```powershell
pip install -r requirements.txt
```

### 3. Run the script:
```powershell
python analysis.py
```

---

## 📈 Future Enhancements
- [ ] Add interactive web dashboard using **Streamlit** or **Plotly Dash**.
- [ ] Implement machine learning models (e.g., Linear Regression / Random Forest) to predict final exam scores from midterm marks.
- [ ] Add automated PDF student report card generation.
