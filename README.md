# aws-kinesis-datastream-pipeline# AWS Kinesis DataStream Pipeline 🚀

## 📌 Project Overview
This project demonstrates a serverless real-time data streaming pipeline using AWS services.

When a file is uploaded to Amazon S3:
1. S3 triggers a Producer Lambda.
2. Producer Lambda sends file metadata to Amazon Kinesis Data Streams.
3. Consumer Lambda reads records from Kinesis.
4. Processed data is logged to CloudWatch.

---

## 🏗 Architecture

S3 → Producer Lambda → Kinesis Stream → Consumer Lambda → CloudWatch

---

## 🛠 AWS Services Used
- AWS Lambda (Python)
- Amazon S3
- Amazon Kinesis Data Streams
- CloudWatch
- IAM

---

## ⚙️ Setup Steps

1. Create an S3 bucket.
2. Create a Kinesis Data Stream.
3. Deploy Producer Lambda and set S3 trigger.
4. Deploy Consumer Lambda and set Kinesis trigger.
5. Upload a file to S3.
6. Check CloudWatch logs for output.

---

## 🎯 Key Features
- Real-time streaming architecture
- Event-driven serverless processing
- IAM-based secure access
- Error handling implemented

---

## 💡 Future Improvements
- Add DLQ (Dead Letter Queue)
- Add retry mechanism
- Add multi-shard scaling
- Add monitoring dashboard
