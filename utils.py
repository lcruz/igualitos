import uuid

def build_file_name(filename):
	return 'file_' + str(uuid.uuid1()) + '.' + filename.split('.')[-1]