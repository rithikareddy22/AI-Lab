# Group Project

    Name            | github username   |
 ------------------ | ----------------- |
 ___Rithika Reddy__ |  rithikareddy22   |
   Sameeksha Reddy  |  sameeksha-reddy4 |
 ___Eshitha Reddy__ |  
 __Preethi Uyyuru__ | 

# Project Description
This repository contains the implementation of three Artificial Intelligence programming assignments:
1. **Architecture Design for Turing Test and CAPTCHA**
2. **AQI Prediction using a Simple Reflex Agent**
3. **Uninformed Search Algorithms (BFS and DFS)**

# 1
## Turing Test and CAPTCHA Architecture

### Objective

To design an architecture explaining how a system can implement:

* **Turing Test**
* **CAPTCHA**

### Description

The Turing Test evaluates whether a machine can exhibit intelligent behavior indistinguishable from a human.

CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is used to differentiate humans from bots by presenting challenges that are easy for humans but difficult for machines.

### Architecture Components

**Turing Test System**

* Human Interrogator
* Human Participant
* Machine Agent
* Communication Interface
* Evaluation Module

**CAPTCHA System**

* Challenge Generator
* Distortion Engine
* User Interface
* Verification System

---

# Assignment 2

## Simple Reflex Agent for AQI Detection

### Objective

To design a **Simple Reflex Agent** that reads environmental sensor data and determines the **Air Quality Index (AQI)**.

### Inputs (Sensor Data)

The system reads environmental parameters from a dataset file:

* PM2.5
* PM10
* CO
* NO2
* SO2
* O3

### Agent Working

1. Sensor data is read from a file.
2. The agent evaluates pollutant levels.
3. AQI is calculated based on predefined thresholds.
4. The system outputs the **AQI category**.

### AQI Categories

| AQI Range | Category     |
| --------- | ------------ |
| 0 – 50    | Good         |
| 51 – 100  | Satisfactory |
| 101 – 200 | Moderate     |
| 201 – 300 | Poor         |
| 301 – 400 | Very Poor    |
| 401 – 500 | Severe       |

---

# Assignment 3

## Uninformed Search Algorithms

### Objective

To implement and compare **Breadth First Search (BFS)** and **Depth First Search (DFS)** algorithms.

### Algorithms Implemented

* Breadth First Search (BFS)
* Depth First Search (DFS)

### Problems Solved

1. Tic Tac Toe
2. Eight Queens Problem
3. Milk and Water Jug Problem
4. Missionaries and Cannibals Problem

---

# Performance Comparison

| Algorithm | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| BFS       | O(b^d)          | O(b^d)           |
| DFS       | O(b^m)          | O(bm)            |

Where:

* **b** = branching factor
* **d** = depth of optimal solution
* **m** = maximum depth of tree

