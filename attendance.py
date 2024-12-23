import boto3
import requests
import datetime
import time


import cv2

# Credentials----------------------------------------------------------------------------------
client = boto3.client('rekognition',
                      aws_access_key_id="************************",
                      aws_secret_access_key="*******************************************",
                      region_name='us-east-1')

# Capture images for every 1 hour and store the image with current date and time -----------------------------------------------------------------------------------
for j in range(0, 6):
    current_time = datetime.datetime.now().strftime("%d-%m-%y  %H-%M-%S ")
    print(current_time)
    camera = cv2.VideoCapture(0)

    while True:
        # Capture the video frame by frame
        ret, frame = camera.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)
        # Check if the image needs to be captured
        if cv2.waitKey(1) & 0xFF == ord(' '):
            # Save the captured frame as an image
            cv2.imwrite('img/' + current_time + '.jpg', frame)
            print("Image captured!")
            # Reset the flag
            break

        # Check if the 'q' button is pressed to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()

    del (camera)

    # Send the captured image to AWS S3 Bucket--------------------------------------------------------------------------------------
    clients3 = boto3.client('s3', aws_access_key_id="AKIAXQKH4EDNZYI5VFGW",
                            aws_secret_access_key="YA4TX/l9LLgR7fwuJnlgZq1ZHga+tWo+M/Fu6Dhl", region_name='us-east-1')
    # clients3.upload_file("Hourly Class Images/"+current_time+'.jpg', 'add your S3 bucket name', current_time+'.jpg')

    clients3.upload_file("img/" + current_time + '.jpg', 'dun-dun', current_time + '.jpg')

    # Recognize students in captured image ---------------------------------------------------------------------------------------
    image_path = 'img/' + current_time + '.jpg'
    with open(image_path, 'rb') as source_image:
        source_bytes = source_image.read()
    print(type(source_bytes))

    print("Recognition Service")
    response = client.detect_custom_labels(

        # Update the Recognition ARN with yours

        ProjectVersionArn='arn:aws:rekognition:us-east-1:516083687643:project/Face-Rek-Att-Sys/version/Face-Rek-Att-Sys.2023-10-29T21.42.26/1698595945940',

        Image={
            'Bytes': source_bytes
        },

    )

    print(response)
    if not len(response['Custom Labels']):
        print('Not identified')

    else:
        str = response['Custom Labels'][0]['Name']
        print(str)

        # Update the attendance of recognized student in DynamoDB by calling the API

        url = "https://kx62h8ef40.execute-api.ap-south-1.amazonaws.com/Name/AttendTable?Name=" + str

        resp = requests.get(url)
        print("Attendance Mark Successful")
        if resp.status_code == 200:
            print("Success")

    time.sleep(3600)
