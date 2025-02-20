import boto3
import requests
import datetime
import time
import cv2

# AWS Credentials
client = boto3.client('rekognition',
                      aws_access_key_id="AKIAXNGUVPZPBFZAQYOG",
                      aws_secret_access_key="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",
                      region_name='ap-south-1')

# Capture Image
current_time = datetime.datetime.now().strftime("%d-%m-%y  %H-%M-%S ")
print(current_time)

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv2.imshow('frame', frame)

    # Capture image when space (' ') is pressed
    if cv2.waitKey(1) & 0xFF == ord(' '):
        image_path = 'img/' + current_time + '.jpg'
        cv2.imwrite(image_path, frame)
        print("Image captured!")
        break

    # Quit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera.release()
        cv2.destroyAllWindows()
        exit()

# Release camera and close window
camera.release()
cv2.destroyAllWindows()

# Upload captured image to S3
clients3 = boto3.client('s3', 
                        aws_access_key_id="AKIAXNGUVPZPBFZAQYOG",
                        aws_secret_access_key="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",
                        region_name='ap-south-1')

clients3.upload_file(image_path, 'attendence-system', current_time + '.jpg')

# Recognize students in captured image
with open(image_path, 'rb') as source_image:
    source_bytes = source_image.read()

print("Recognition Service")
response = client.detect_custom_labels(
    ProjectVersionArn='arn:aws:rekognition:ap-south-1:509399629406:project/facereckognition/version/facereckognition.2025-02-14T07.45.39/1739499340299',
    Image={'Bytes': source_bytes},
)

print(response)
if not response.get('CustomLabels'):
    print('Not identified')
else:
    student_name = response['CustomLabels'][0]['Name']
    print(student_name)

    # Update attendance in DynamoDB via API call
    url = f"https://sudlxfnm6e.execute-api.ap-south-1.amazonaws.com/default/AttendFunction?Name={student_name}"
    resp = requests.get(url)
    print("Attendance Mark Successful")

    if resp.status_code == 200:
        print("Successful")

# Wait for 6 minutes before closing (if needed)
time.sleep(10)

# Exit the script completely
print("Exiting script...")
exit()
