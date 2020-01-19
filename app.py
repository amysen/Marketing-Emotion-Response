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


@app.route('/advert_01')
def ad_01():

	return "images/drac.jpg"

@app.route('/advert_02')
def ad_02():

	return "images/McD.jpg"


if __name__ == '__main__':
	app.run(debug=True)