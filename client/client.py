 
from gevent import monkey
monkey.patch_all()
import json
import time
import argparse
import requests
import gevent
 
  
# The URL of the server we gonna send data  
sendURL  ='http://127.0.0.1:8000/api/send/' 
   

def send_data():
        ##Detail of project and help ...
        parser = argparse.ArgumentParser(
            prog = 'send data - Client edition',
            description='send fast & easy in your server.',
            epilog = 'May enjoy my app',
            add_help = True)

        # Add argument to send data and get result
       
        parser.add_argument("-t","--type",type=str, help='command for process.')
        parser.add_argument("-n","--name" ,type=str ,help='name of process.')
        parser.add_argument("-e","--expresion",type=str,help='expression')
        parser.add_argument("-p","--collection",action='append',help='parameters',dest='collection')

        args =  parser.parse_args() 
        if args.type=='os':
    
            data={'type':args.type,
                'name':args.name ,
                'parameters':''.join(args.collection) if not (args.collection)==None else '',
                'expresion':'' 
                }
       
        elif args.type=='compute':
                data={'type':args.type,
                      'name':'',
                    'expresion':args.expresion,
                    'parameters':''
                    }
        else:
                data={
                    'type':'',
                    'name':'',
                    'expresion':'',
                    'parameters':''
                }
        jsondata=json.dumps(data)
    
        headers = {'content-type': 'application/json' }
        try:
            test_response=requests.post(sendURL,data=jsondata,headers=headers)
            test_response.raise_for_status
            print(test_response.text)
        except requests.exceptions.RequestException as error:
            print("Request Exception found",error)
            raise error
        return test_response
 
  
gevent.joinall([gevent.spawn(send_data)])   
 
 
 