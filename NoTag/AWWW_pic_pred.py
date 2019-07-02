import subprocess
import os

def pred(filename):
	bashCommand = "curl localhost/models/images/classification/classify_one/json -XPOST -F job_id=20190514-232706-548d -F image_file=@/AIkernel/SERVER/Chatbot-Server/NoTag/test.png"
	delfilename = "test.png"
	path = "/AIkernel/SERVER/Chatbot-Server/NoTag/uploads/"
	pathname = os.path.abspath(os.path.join(path, filename))
	output = subprocess.check_output(['bash','-c', bashCommand])
	os.remove(delfilename)
	if pathname.startswith(path):
		os.remove(pathname)
	return output
