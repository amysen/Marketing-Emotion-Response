from flask import Flask, render_template
import Tensorflow.emotions
# import cv2 

app = Flask(__name__)

imageNum = 1

@app.route('/')
def main():

	return render_template('index.html', title='Home')


@app.route('/advert')
def ad_01():
	global imageNum
	Tensorflow.emotions.detect_emotion(imageNum)
	imageNum += 1
	return render_template('index.html', title='Home')

# @app.route('/advert_02')
# def ad_02():

# 	return "images/McD.jpg"


if __name__ == '__main__':
	app.run(debug=True)