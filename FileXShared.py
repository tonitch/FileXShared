#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, send_from_directory, make_response, request
import os
app = Flask(__name__)

def sendFile(directory, filename):
	print('[+] Shared ', str(directory), '/', str(filename))
	return send_from_directory(directory=directory, filename=filename, as_attachment=True)

def index():
	page = '<!-- FileXSHared By Tiago Danin -->'
	page += '''
	<html>
		<head>
			<title>FileXShared</title>
			<style type="text/css">
				.btn {
					font-family: Arial;
					color: #000000;
					font-size: 21px;
					background: #ffffff;
					padding: 10px 5px 10px 5px;
					border: solid #ded5ce 4px;
					align-content: center;
					text-decoration: none;
					width: 100%;
				}

				.btn:hover {
					background: #ffffff;
					border: solid #e67925 4px;
					background-image: -webkit-linear-gradient(top, #ffffff, #ebebeb);
					background-image: -moz-linear-gradient(top, #ffffff, #ebebeb);
					background-image: -ms-linear-gradient(top, #ffffff, #ebebeb);
					background-image: -o-linear-gradient(top, #ffffff, #ebebeb);
					background-image: linear-gradient(to bottom, #ffffff, #ebebeb);
					text-decoration: none;
				}
			</style>
		</head>
		<body>
			<form class="form" id="form" name="form" method="post" action="/">

	'''
	get_file = request.form.get('file')
	get_dir = os.getcwd()

	page += '''
				<button type="submit" class="btn" name="dir" id="id" value="{home}">Root Folder</button></div></br>
	'''.format(home=get_dir)
	if request.form.get('dir'):
		get_dir = request.form.get('dir')

	for path_name, dir_names, file_names in os.walk(str(get_dir)):
		for s in dir_names:
			page += '''
				<button type="submit" class="btn" name="dir" id="id" value="{path_name}/{s}">Folder {s}</button></div></br>
	'''.format(s=s, path_name=path_name)
		for s in file_names:
			page += '''
				<button type="submit" class="btn" name="file" id="id" value="{s}">File {s}</button></div></br>
	'''.format(s=s)
		page += '''
			</form>
		</body>
	</html>
	'''
		if get_file:
			for s in file_names:
				print(s)
				if s == get_file:
					return sendFile(str(path_name), str(get_file))
		else:
			return make_response(page)

app.add_url_rule('/', 'Index', index, methods=['GET'])
app.add_url_rule('/', 'Index', index, methods=['POST'])
app.run(host='0.0.0.0', port='8002', debug=False, threaded=True)
__name__ == __info__