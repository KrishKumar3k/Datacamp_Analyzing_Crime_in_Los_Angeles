# 📊 Analyzing Crime in Los Angeles (DataCamp Project)

## 🚔 Project Overview

This project analyzes crime data from Los Angeles to identify patterns in criminal activity. The goal is to help the LAPD understand when and where crimes are most frequent so that resources can be allocated more effectively.

Los Angeles, known as the **City of Angels**, faces a high volume of crime due to its large population. This analysis focuses on uncovering insights from real-world crime data.

---

## 📁 Dataset

The dataset is a modified version of publicly available Los Angeles crime data.

Key columns include:

* `TIME OCC` → Time of occurrence (24-hour format)
* `AREA NAME` → Police patrol division area
* `Vict Age` → Age of the victim
* `Crm Cd Desc` → Crime description
* `Vict Sex` → Gender of victim
* `LOCATION` → Crime location

---

## 🎯 Objectives

The project answers the following key questions:

1. ⏰ What hour of the day has the highest frequency of crimes?
2. 🌙 Which area has the most night crimes (10 PM – 3:59 AM)?
3. 👥 How are crimes distributed across different victim age groups?

---

## 🛠️ Tools & Libraries Used

* Python 🐍
* Pandas 📊
* NumPy 🔢

---

## 📌 Key Steps

* Data cleaning and type conversion
* Feature engineering (extracting hours from time)
* Filtering night-time crime data
* Grouping and aggregation using `value_counts()`
* Binning ages using `pd.cut()`

---

## 📈 Key Insights

* Certain hours of the day show significantly higher crime activity.
* Specific areas experience more crime during night hours.
* Victim age distribution highlights the most affected age groups.

---

## 🚀 Conclusion

This project demonstrates how exploratory data analysis (EDA) can reveal meaningful patterns in crime data, helping support better decision-making in public safety.

---

## 👨‍💻 Author

Krish Kumar
Aspiring Data Scientist | AI & ML Enthusiast
