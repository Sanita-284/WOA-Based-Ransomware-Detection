# 🐋 WOA-Based Ransomware Detection — Memory Signature Generation

> A memory-based ransomware detection framework using the Whale Optimization Algorithm (WOA) for behavior-derived feature selection across fileless and file-based ransomware families.

This repo accompanies the research paper:
**_Memory Detection: A Survey of Whale Optimization Algorithm-Based Signature Generation_**
**Course:** 23CSE615 Cyber-Law | Theme 19 | Jain (Deemed-to-be) University

**Authors:** Monica P · Sanita · Vaishnavi S — Dept. of CSE (Cyber Security)

> 🤖 AI Assistance: Developed with support from [Claude (Anthropic)](https://claude.ai) and [ChatGPT (OpenAI)](https://chatgpt.com) for research synthesis and writing. All academic contributions are original work of the authors.

---

## 🔗 Live Demo


---

## 🧩 How It Works

WOA optimizes behavior-derived memory indicators from real ransomware execution using 4 mechanisms:

```
Encircling Prey      →  Converge on optimal feature subsets
Bubble-Net Attacking →  Refine best behavioral indicators
Search for Prey      →  Discover diverse, non-redundant patterns
Position Updating    →  Balance exploration vs exploitation
```

**Fitness Function:**
```
F(X) = 0.99 * Error(K, X) + 0.01 * (|S_X| / |T|)
```
- `Error(K, X)` — classifier error on feature subset X  
- `|S_X|` — selected features · `|T|` — total features

---

## 🦠 Ransomware Families Analyzed (MalwareBazaar)

**Fileless (RAM-only):** Ryuk · Conti · REvil · Quantum · Hive

**File-Based (Disk + Memory):** WannaCry · LockBit · Maze · Clop · DarkSide

---

## 📊 Results

| Metric | Value |
|--------|-------|
| Detection Accuracy | 97.2% – 98.6% |
| Feature Reduction | 60% – 70% |
| Optimal Feature Subset | 20–30 (from 86) |
| Studies Reviewed (PRISMA 2020 SLR) | 45 (from 912 candidates) |

---

## 🗄️ Dataset Reference

Simulation inspired by the **MalwareBazaar Execution Dataset:**
- 58,596 memory snapshots · 86 Volatility-extracted features · 58 malware families

> **Note:** The demo simulates behavior inspired by this dataset — it does not use it directly in real-time.

---

## ✨ Demo Features

- Real-time WOA optimization simulation
- Feature selection: 86 → optimal subset visualization
- Baseline vs WOA accuracy comparison
- Whale swarm movement + convergence tracking

---

## 🚀 Run

```
1. Visit: https://sanita-284.github.io/WOA-Based-Ransomware-Detection-Demo/
2. Click RUN WOA
3. Watch feature selection and optimization unfold
```

---

## 📌 Note

This is a **conceptual simulation for academic purposes only** — not a production detection system.

---

## 📜 License

Academic and educational use only. All rights reserved by the authors.
