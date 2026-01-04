# 🌄 Weekend Getaway Ranker

A Python-based **travel recommendation system** that suggests the **best weekend getaway places** from a given Indian state using **distance, ratings, and popularity**.

The system ranks destinations using a **weighted scoring model** and the **Haversine distance formula** to calculate real-world travel distances between states.

---

## 🎯 Project Objective

To help users discover the **top nearby tourist destinations** for a weekend trip based on:
- Shorter travel distance
- Higher Google ratings
- Greater popularity (review volume)

---

## 🧠 How It Works

The recommendation engine:
1. Takes a **source state** as input
2. Calculates distance from the source state to all destinations
3. Normalizes:
   - Distance
   - Google review rating
   - Popularity (number of reviews)
4. Applies a **weighted scoring formula**
5. Returns the **Top N destinations**



---

## 🗂 Dataset Requirements

The CSV file (`data/data.csv`) must include at least the following columns:


> Column names are automatically cleaned and normalized in the script.

---

## 📍 Supported States

- Andhra Pradesh  
- Assam  
- Bihar  
- Delhi  
- Goa  
- Gujarat  
- Haryana  
- Himachal Pradesh  
- Karnataka  
- Kerala  
- Madhya Pradesh  
- Maharashtra  
- Punjab  
- Rajasthan  
- Tamil Nadu  
- Uttar Pradesh  
- Uttarakhand  
- West Bengal  

---

## ⚙️ Tech Stack

- **Language:** Python 3  
- **Libraries:** pandas, math  

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

Run the Script

```bash
python src/main.py



