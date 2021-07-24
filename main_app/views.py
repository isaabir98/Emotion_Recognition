from django.contrib.messages.api import success
from django.http import HttpResponse,StreamingHttpResponse 
from django.shortcuts import render,redirect
from flask.templating import render_template
from flask import Flask, render_template, Response
from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import cv2
from main_app.models import empInsert
from .forms import UserRegistrationForm
from django.template import Context, Template
from tensorflow.python.eager.context import context
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, redirects

face_classifier = cv2.CascadeClassifier(r'C:\Users\hp\Documents\SE\3rd year\Research Project\project\Emotion Recognition\emotion\models\haarcascade_frontalface_default.xml')
classifier =load_model(r'C:\Users\hp\Documents\SE\3rd year\Research Project\project\Emotion Recognition\emotion\models\Emotion_little_vgg.h5')

class_labels = ['Angry','Happy','Neutral','Sad','Surprise']



app = Flask(__name__)
camera = cv2.VideoCapture(0) 


def gen_frames(self):  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            labels = []
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray,1.3,5)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h,x:x+w]
                roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
                if np.sum([roi_gray])!=0:
                    roi = roi_gray.astype('float')/255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi,axis=0)  
                    preds = classifier.predict(roi)[0]
                    label=class_labels[preds.argmax()]
                    label_position = (x,y)
                    cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

        
            

@app.route('/video_feed')
def video_feed(self):
    #Video streaming route. Put this in the src attribute of an img tag
    return StreamingHttpResponse(gen_frames(camera), content_type='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index(request):
    """Video streaming home page."""
    return render(request,'index.html')


if __name__ == '__main__':
    app.run(debug=True)



def pagehome(request):
    context={'posts':posts}
    return render(request,'frontface.html',context)


def loginhome(request):
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            uname =form.cleaned_data.get('username')
            x=form.cleaned_data.get('password1')

            saverecord=empInsert()
            saverecord.username=uname
            saverecord.password=x
            saverecord.save()
            messages.success(request, f'YOUR RECORDS WAS PUBLISHED TO THE >>>DB')
            messages.success(request,f'Hi {uname},your password is  { x}, your account has been created sucessfully')
            return redirect('login')
    else:
            form=UserRegistrationForm()
    return render(request,'signup.html', {'form':form})