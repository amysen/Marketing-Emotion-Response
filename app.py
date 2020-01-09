from flask import Flask, render_template
# import Tensorflow.emotions 
# import cv2 

app = Flask(__name__)


@app.route('/')
def main():
	
	# cap = cv2.VideoCapture(0)

	# emo = detect_emotion(cap)

	# cap.release()
	# cv2.destroyAllWindows()

	return render_template('index.html', title='Home')

if __name__ == '__main__':
	app.run(debug=True)