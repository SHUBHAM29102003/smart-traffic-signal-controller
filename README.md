# Smart Traffic Signal Controller 🚦

This project simulates a smart traffic signal system using AWS serverless architecture.

---

## 📌 Description
A Lambda function is triggered on a schedule using EventBridge. It randomly generates traffic data (LOW, MEDIUM, HIGH), stores it in DynamoDB, and sends an alert via SNS if the traffic level is HIGH.

---

## 🧰 AWS Services Used

- **AWS Lambda** – Main logic for traffic simulation and alerts
- **Amazon DynamoDB** – Stores timestamped traffic level data
- **Amazon SNS** – Sends high traffic alerts to subscribed email addresses
- **Amazon EventBridge (Scheduler)** – Runs Lambda on a defined schedule

---

## 🗃️ Folder Structure

