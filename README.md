# Face Recognition-Based Attendance Management System

This project implements a **Face Recognition-Based Attendance Management System** using AWS services, providing a seamless and automated solution for tracking attendance.

---

## Project Overview

The system captures student images using a camera, processes them with AWS Rekognition for face recognition, and updates attendance records in DynamoDB. It also provides a web-based dashboard for easy visualization and management of attendance data.

---

## Key Features
- **Automated Attendance Tracking:** Uses face recognition to mark attendance.
- **Cloud Integration:** Leverages AWS Rekognition, S3, Lambda, API Gateway, and DynamoDB.
- **Frontend Interface:** Provides a user-friendly web dashboard for attendance management.
- **Real-Time Processing:** Captures and processes images at regular intervals.

---

## Implementation Details

### Data Collection and Training
1. **Capture Images Locally:**
   - Captured 50–60 facial images per student.
2. **Upload to AWS S3:**
   - Created an S3 bucket for storing images.
3. **Train Rekognition Model:**
   - Used AWS Rekognition Custom Labels to train a face recognition model with labeled images.

### Backend Setup
1. **DynamoDB Table:**
   - Created a table with attributes: `Name`, `Rollno`, and `Count`.
2. **AWS Lambda Functions:**
   - Functions to:
     - Update attendance in DynamoDB.
     - Fetch attendance data for the frontend.
3. **API Gateway:**
   - Configured REST APIs for Lambda triggers.

### Frontend
- Developed with HTML, CSS, and JavaScript.
- Fetches and displays attendance data using the API.

---

## Workflow
1. Capture images hourly using a camera.
2. Upload images to S3 and analyze them with Rekognition.
3. Identify faces and update attendance in DynamoDB via API Gateway and Lambda.
4. Display attendance records on the web dashboard.

---

## Code Highlights

### User Data Script for Camera Integration
```python
import cv2
vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    if cv2.waitKey(1) & 0xFF == ord(' '):
        cv2.imwrite('captured_image.jpg', frame)
        break
vid.release()
cv2.destroyAllWindows()
```
lambda
```lambda
Lambda Function to Update Attendance
python
import boto3
dynamo = boto3.resource("dynamodb")
table = dynamo.Table("AwsAttendTable")

def lambda_handler(event, context):
    res = table.get_item(Key={"Name": event['queryStringParameters']['Name']})
    Count = res['Item']['Count'] + 1
    table.put_item(Item={"Name": res['Item']['Name'], "Rollno": res['Item']['Rollno'], "Count": Count})
    return "Successful"
```

Cleanup
Deleted AWS resources after project completion to avoid unnecessary costs.
Notes
Ensure at least 50 images per person for accurate detection.
Adjust AWS region settings in scripts for compatibility.
