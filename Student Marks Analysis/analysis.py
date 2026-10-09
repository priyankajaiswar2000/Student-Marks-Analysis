"""
Student Marks Analysis System
Tools: Python, Pandas, Matplotlib
Author: Antigravity Assistant
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. Configuration & Directories
# -------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "students_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 2. Data Loading & Feature Engineering
# -------------------------------------------------------------
def load_and_process_data(filepath):
    """Loads CSV dataset and calculates calculated performance metrics."""
    df = pd.read_csv(filepath)
    
    subjects = ["Math", "Science", "English", "History", "ComputerScience"]
    
    # Calculate Total, Average, Percentage (assuming max 100 per subject)
    df["TotalMarks"] = df[subjects].sum(axis=1)
    df["Percentage"] = (df["TotalMarks"] / (len(subjects) * 100)) * 100
    
    # Assign Letter Grades based on Percentage
    def assign_grade(pct):
        if pct >= 90:
            return "A+"
        elif pct >= 80:
            return "A"
        elif pct >= 70:
            return "B"
        elif pct >= 60:
            return "C"
        elif pct >= 50:
            return "D"
        else:
            return "F (Fail)"
            
    df["Grade"] = df["Percentage"].apply(assign_grade)
    
    # Check Pass / Fail (passing criteria: >= 40 in every subject)
    df["Status"] = df[subjects].apply(lambda row: "Pass" if (row >= 40).all() else "Fail", axis=1)
    
    # Assign Rank based on Total Marks
    df["Rank"] = df["TotalMarks"].rank(ascending=False, method="min").astype(int)
    
    return df, subjects

# -------------------------------------------------------------
# 3. Statistical Analysis & Reporting
# -------------------------------------------------------------
def print_summary_report(df, subjects):
    """Displays analytical insights and statistical summaries."""
    print("=" * 70)
    print("                    STUDENT PERFORMANCE REPORT")
    print("=" * 70)
    print(f"Total Students Analyzed: {len(df)}")
    print(f"Overall Class Average Percentage: {df['Percentage'].mean():.2f}%")
    print(f"Highest Score: {df['TotalMarks'].max()} / 500 ({df['Percentage'].max():.2f}%)")
    print(f"Lowest Score:  {df['TotalMarks'].min()} / 500 ({df['Percentage'].min():.2f}%)")
    
    pass_count = (df['Status'] == 'Pass').sum()
    pass_rate = (pass_count / len(df)) * 100
    print(f"Pass Rate: {pass_rate:.1f}% ({pass_count}/{len(df)} Students)")
    
    print("\n" + "-" * 70)
    print("SUBJECT-WISE PERFORMANCE METRICS")
    print("-" * 70)
    subject_stats = df[subjects].agg(['mean', 'median', 'std', 'min', 'max']).T
    subject_stats.columns = ['Mean', 'Median', 'Std Dev', 'Min', 'Max']
    print(subject_stats.round(2))
    
    print("\n" + "-" * 70)
    print("TOP 5 PERFORMERS (RANK LIST)")
    print("-" * 70)
    top_5 = df.sort_values(by="Rank").head(5)[["Rank", "StudentID", "Name", "Class_Section", "TotalMarks", "Percentage", "Grade"]]
    print(top_5.to_string(index=False))
    
    print("\n" + "-" * 70)
    print("SECTION-WISE COMPARISON (Average Score)")
    print("-" * 70)
    section_summary = df.groupby("Class_Section")[["TotalMarks", "Percentage", "AttendancePercentage"]].mean()
    print(section_summary.round(2))
    print("=" * 70)

# -------------------------------------------------------------
# 4. Matplotlib Visualizations
# -------------------------------------------------------------
def create_visualizations(df, subjects):
    """Generates a professional 4-panel analysis dashboard using Matplotlib."""
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("Comprehensive Student Performance & Marks Analytics", fontsize=18, fontweight="bold", y=0.98)
    
    colors = ["#4C72B0", "#55A868", "#C44E52", "#8172B3", "#CCB974", "#64B5CD"]

    # 1. Subject-wise Average Marks (Bar Chart)
    ax1 = axes[0, 0]
    subject_means = df[subjects].mean()
    bars = ax1.bar(subject_means.index, subject_means.values, color="#3B82F6", edgecolor="#1E40AF", width=0.55)
    ax1.set_title("Average Score by Subject", fontsize=13, fontweight="bold", pad=10)
    ax1.set_ylabel("Average Marks (out of 100)", fontsize=11)
    ax1.set_ylim(0, 105)
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval:.1f}", ha="center", va="bottom", fontsize=10, fontweight="bold")
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    # 2. Grade Distribution (Donut Chart)
    ax2 = axes[0, 1]
    grade_counts = df["Grade"].value_counts().sort_index()
    palette = ["#10B981", "#3B82F6", "#F59E0B", "#EC4899", "#EF4444"]
    wedges, texts, autotexts = ax2.pie(
        grade_counts.values,
        labels=grade_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=palette[:len(grade_counts)],
        pctdistance=0.78,
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2)
    )
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight("bold")
    ax2.set_title("Grade Distribution", fontsize=13, fontweight="bold", pad=10)

    # 3. Attendance vs Total Marks Correlation (Scatter Plot)
    ax3 = axes[1, 0]
    scatter = ax3.scatter(df["AttendancePercentage"], df["TotalMarks"], c=df["Percentage"], cmap="viridis", s=80, edgecolors="black", linewidth=0.6, alpha=0.9)
    # Trendline
    z = np.polyfit(df["AttendancePercentage"], df["TotalMarks"], 1)
    p = np.poly1d(z)
    ax3.plot(df["AttendancePercentage"], p(df["AttendancePercentage"]), color="#DC2626", linestyle="--", linewidth=2, label="Trendline")
    ax3.set_title("Attendance % vs. Total Marks", fontsize=13, fontweight="bold", pad=10)
    ax3.set_xlabel("Attendance (%)", fontsize=11)
    ax3.set_ylabel("Total Marks (out of 500)", fontsize=11)
    ax3.legend(loc="upper left")
    cbar = plt.colorbar(scatter, ax=ax3)
    cbar.set_label("Overall %", rotation=270, labelpad=15)
    ax3.grid(True, linestyle='--', alpha=0.6)

    # 4. Top 5 Students (Horizontal Bar Chart)
    ax4 = axes[1, 1]
    top_students = df.sort_values(by="TotalMarks", ascending=True).tail(5)
    y_pos = np.arange(len(top_students))
    bars4 = ax4.barh(y_pos, top_students["TotalMarks"], color="#10B981", edgecolor="#047857", height=0.55)
    ax4.set_yticks(y_pos)
    ax4.set_yticklabels(top_students["Name"], fontsize=10)
    ax4.set_title("Top 5 Performers", fontsize=13, fontweight="bold", pad=10)
    ax4.set_xlabel("Total Marks (out of 500)", fontsize=11)
    ax4.set_xlim(0, 520)
    for bar in bars4:
        width = bar.get_width()
        ax4.text(width + 5, bar.get_y() + bar.get_height()/2.0, f"{int(width)}/500", ha="left", va="center", fontsize=10, fontweight="bold")
    ax4.grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    # Save chart
    dashboard_path = os.path.join(OUTPUT_DIR, "student_performance_dashboard.png")
    plt.savefig(dashboard_path, dpi=300)
    plt.close()
    print(f"\n[+] Visualization Dashboard saved to: {dashboard_path}")

# -------------------------------------------------------------
# 5. Main Execution Entry Point
# -------------------------------------------------------------
def main():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found!")
        return
        
    df, subjects = load_and_process_data(DATA_FILE)
    
    # Display Summary
    print_summary_report(df, subjects)
    
    # Export processed data
    output_csv = os.path.join(OUTPUT_DIR, "students_results.csv")
    df.to_csv(output_csv, index=False)
    print(f"\n[+] Enriched dataset saved to: {output_csv}")
    
    # Generate Visualizations
    create_visualizations(df, subjects)
    print("\nAnalysis completed successfully!")

if __name__ == "__main__":
    main()
