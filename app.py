from flask import Flask
import Tensorflow.emotions 
import cv2 

app = Flask(__name__)


@app.route('/')
def main():
	# emo = emotions.detect_emotion()
	# cap = cv2.VideoCapture(0)

	detect_emotion()

	# cap.release()
	# cv2.destroyAllWindows()
	return "hello"

if __name__ == '__main__':
	app.run()