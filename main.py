from flask import Flask, render_template, Response
import  cv2 



app = Flask(__name__)
camera=cv2.VideoCapture(0)


def generate_frames():
    while True:
    ## read the camera frame
     sucess,frame=camera.read()
     if not sucess:
        break
     else:
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield(b'--frame\r\n'
              b'content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route("/")
def index():
    return render_template('index.html')



@app.route("/video")
def video():
    return Response (generate_frames(),mimetype="mutipart/x-mixed-replaace; boundary=frame")









if __name__== "__main__":
    app.run(debug=True)