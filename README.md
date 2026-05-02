---
title: Fraud Detection Environment
emoji: 🛡️
colorFrom: blue
colorTo: purple
sdk: docker
sdk_version: "1.0"
app_file: app.py
pinned: false
---

# AI Fraud Decision Intelligence Platform

An AI-powered fraud detection environment that goes beyond simple classification — simulating how an intelligent system **reasons, evaluates risk, and makes financially aware decisions** in real time.

---

## 🧩 Problem

Most fraud detection systems behave like black boxes.  
They output *“fraud”* or *“safe”* — but provide no insight into:

- why the decision was made  
- how risky the situation is  
- what the financial consequences are  
- how the system improves over time  

This lack of transparency limits trust and real-world usability.

---

## 🚀 What We Built

This project introduces a **reinforcement learning–style fraud decision environment**.

Instead of a static classifier, we simulate an **agent interacting with a dynamic environment**, receiving feedback, and improving decisions over time.

The system combines:

- an interactive environment  
- a reward-driven decision process  
- a structured API  
- a premium frontend for visualization  

---

## 🔄 System Overview
User Input → Environment → Agent Decision → Reward Engine → Feedback → UI

### Agent Actions

- `0 → Safe`  
- `1 → Fraud`  
- `2 → Suspicious`  

---

## 🧠 Environment Design

The environment is built to resemble real-world fraud scenarios.

### Observations

The agent receives:
- message text  
- extracted signals (urgency, links, keywords, sender patterns)  

### Reward Logic

Decisions are evaluated using both correctness and financial impact:

- Correct fraud detection → high reward  
- Suspicious classification → partial reward  
- Missed fraud → strong penalty  
- Incorrect classification → negative reward  

### 💰 Financial Signals

Each decision includes:

- money saved  
- money lost  
- money at risk  

This introduces real-world stakes into the learning process.

---

## ⚙️ Backend Architecture

Built with FastAPI.

Core components:

- `env.py` → environment logic  
- `reward_engine.py` → reward + financial computation  
- `models.py` → structured outputs  
- `app.py` → API layer  

### API Endpoints

- `POST /reset` → initializes a new scenario  
- `POST /step` → applies agent action and returns result  
- `GET /state` → current environment state  

---

## 🎨 Frontend Experience

A multi-page SaaS-style interface designed to visualize decision intelligence.

Key capabilities:

- real-time fraud analysis  
- step-by-step reasoning simulation  
- risk and confidence visualization  
- financial impact display  
- training insights dashboard  

The frontend strictly consumes backend responses — no fabricated data.

---

## 📈 Training & Learning

<img width="829" height="429" alt="image" src="https://github.com/user-attachments/assets/88dcb213-ca0e-4064-a2ea-b62ce5648f16" />

The random baseline agent shows unstable performance with no learning pattern, while the RL agent demonstrates gradual improvement. The smoothed curve highlights a clear upward trend, indicating that the agent learns effective fraud detection strategies over time and consistently outperforms the baseline through reward-driven decision-making.


We evaluate the system using a simple training setup:

### Baseline Agent
- random decision-making  
- inconsistent rewards  

### Improved Agent
- rule-based decision strategy  
- learns to identify fraud patterns  
- achieves higher and more stable rewards  

---

## 📊 Results

Training demonstrates clear improvement:

- increasing reward trend across episodes  
- fewer missed fraud cases  
- more consistent classifications  

This validates that the environment provides **meaningful learning signals**.

---

## 🌍 Why This Matters

This system is relevant for domains where **decision quality and transparency are critical**:

- fintech and banking systems  
- phishing and scam detection  
- cybersecurity platforms  

### Key advantages:

- interpretable decision-making  
- visibility into financial risk  
- simulation of real-world fraud scenarios  
- foundation for reinforcement learning research  

---

## 🧪 Deployment

The platform is deployed using a unified architecture:

- FastAPI backend  
- React frontend  
- Docker-based deployment  
- hosted on Hugging Face Spaces  

---

## 🔗 Links

- Live Demo: <[https://huggingface.co/spaces/Vishwajeet8055/Fraud_Detection_ENV](https://huggingface.co/spaces/Vishwajeet8055/Fraud_Detection_ENV)>  
- Training Notebook: <[https://colab.research.google.com/drive/1iAXuWLal5Xu8nPjortVCWB3XjgM20iEC?usp=sharing](https://colab.research.google.com/drive/1iAXuWLal5Xu8nPjortVCWB3XjgM20iEC?usp=sharing)>  
- Demo Video (optional): <your-video-link>  

---

## 📝 Summary

This project reframes fraud detection as a **decision intelligence problem** rather than a classification task.

By combining environment simulation, reward-based learning, and explainable outputs, it creates a system that is both technically meaningful and practically relevant.
