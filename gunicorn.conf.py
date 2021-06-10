import multiprocessing
bind="192.168.181.159:8001"
workers=multiprocessing.cpu_count()*2+1
accesslog='/var/tmp/technopark.gunicorn.log'