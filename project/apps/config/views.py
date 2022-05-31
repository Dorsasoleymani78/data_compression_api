 
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serialize import commandSerialize 
from rest_framework.response import Response
import subprocess
import platform
from sympy import sympify 
from gevent.subprocess import PIPE 
 
 
 
class Process_commands(APIView):
    def post(self,request):
        typeOfPlatform=platform.system()
        #system must be linux
        if  typeOfPlatform=='linux':
            # send data for serialize
            ser_data=commandSerialize(data=request.data)
            #check the data
            if ser_data.is_valid():
                if ser_data.validated_data['type']=='os':
                    
                    output=subprocess.Popen([ser_data.validated_data['name'],ser_data.validated_data['parameters']],shell=True, text=True,stdout=PIPE)
                 
                    context={
                        "given_os_command":f"{ser_data.validated_data['name']}{' '}{ser_data.validated_data['parameters']}" ,
                        "result": output.stdout
                        }
                    
                    return Response(data=context )
                
                elif ser_data.validated_data['type']=='compute':
                
                    object= ser_data.validated_data['expresion'] 
                    result=sympify(object, evaluate=True)
                    context={
                        "given_math_expression": ser_data.validated_data['expresion'] ,
                        "result":str(result)
                    }
                    
                    return Response(data=context)
            return Response(ser_data.errors)  
        content={'error':"the platform have to be Linux"} 
        return Response( content) 
 
        
        