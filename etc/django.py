CONFIG = {                                                                      
        'mode':'wsgi',                                                          
        'working_dir':'/home/box/web/hello.py',                                 
        # 'python':'/usr/bin/python', 
	'pythonpath' : '/home/box/web/ask',	
	'args': (                                                               
        '--bind=0.0.0.0:8000',                                                  
        '--workers=16',                                                         
        '--timeout=60',
	'hello.app',
	),
}  
