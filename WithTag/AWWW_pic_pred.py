import subprocess
import os

def pred(filename):
	bashCommand = "curl localhost/models/images/classification/classify_one.json -XPOST -F job_id=20170612-135113-88f4 -F image_file=@/home/akishinoshiame/AkishinoProject_flask_beta1/WithTag/test.jpg"
	delfilename = "test.jpg"
	path = "/home/akishinoshiame/AkishinoProject_flask_beta1/WithTag/uploads/"
	pathname = os.path.abspath(os.path.join(path, filename))
	output = subprocess.check_output(['bash','-c', bashCommand])
	os.remove(delfilename)
	if pathname.startswith(path):
		os.remove(pathname)
	return output
