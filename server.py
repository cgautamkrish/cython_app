from bottle import route, run, template, get, post, request
from hello import say_hello, word_analyser
from bottle import HTTPResponse
import json
#from exceptions import incorrect_request

@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/test')
def test():
	return say_hello('gautam')

@post('/analyse')
def analyse():
	data = request.json
	print(data.keys())
	if 'data' in data.keys():
		return word_analyser(data['data'])
	else:
		return incorrect_request()

@post('/analyse_native')
def anaylse_native():
	data = request.json
	print(data.keys())
	if 'data' in data.keys():
		return word_analyser_native(data['data'])
	else:
		return incorrect_request()

# Exceptions
def incorrect_request():
	msg_body = json.dumps({'error_message': 'Invalid Request!'}) 
	return HTTPResponse(status=500, body=msg_body)

# Native function
def word_analyser_native(data):
	words_list = data.split()
	word_frequency = {}
	for word in words_list:
		if word in word_frequency:
			word_frequency[word] += 1
		else:
			word_frequency[word] = 1
	return word_frequency

run(host='localhost', port=8080)