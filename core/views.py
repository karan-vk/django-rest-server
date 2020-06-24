from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .sereializers import (
    customerSerial, ProfessionSerializer, DataSheetSerializer, DocumentSerializer)
from rest_framework import viewsets
from .models import Customer, Profession, DataSheet, Document
import json
from django_v.settings import db,auth
import pyrebase
config={
"apiKey": u"AIzaSyA7Qo112f6jIIImUptFtPracjhczTky_r4",
"authDomain": "react--burger.firebaseapp.com",
"databaseURL": u"https://react--burger.firebaseio.com",
"storageBucket": "react--burger.appspot.com",
"serviceAccount":'C:\\Users\\Karan\\Desktop\\Target\\FBdjango - Copy\\django_v\\static\\jj.json'
   
}
firebase1 = pyrebase.initialize_app(config)
y=firebase1.auth()
# import firebase_admin
# import firebase_admin.exceptions as excepttion
from firebase_admin import auth as admin_auth
import asyncio


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = customerSerial

    def get_queryset(self):
        print('hello')
        activeCustomers = Customer.objects.filter(active=True)
        return activeCustomers


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class CustomGet(APIView):
    """
    A custom endpoint for GET request.
    """

    def post(self, request, format=None):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        data = {
            "name": name,
            "email": email,
            "password": password
        }
        db.collection(u'test').document(email).set(data)

        return Response(data, status=205)

    def put(self, request, format=None):
        email = request.data.get('email')
        name = request.data.get('name')
        data = {

            "name": name
        }
        db.collection('test').document(email).update(data)
        return Response({'message': 'Successfully Updated the name for '+email}, status=201)

    def get(self, request, format=None):
        docs = db.collection(u'test').stream()
        a = []
        for doc in docs:
            # print(u'{} => {}'.format(doc.id, doc.to_dict()))
            print(doc)
            data = doc.to_dict()
            data['id'] = doc.id
            a.append(data)
        return Response({"res": a})

    def delete(self, request, format=None):
        docRef = db.collection('test')
        email = request.data.get('email')
        docRef.document(email).delete()
        return Response(status=204)
    def patch(self,request,format=json):
        docRef = db.collection('test')
        email = request.data.get('email')
        d=docRef.document(email).get().to_dict()
        print(type(d))
        logincount=d.get('logincount') + 1
        print(logincount)
        # print(d)
        # dat=[]
        # for doc in d:
        #     da=doc.to_dict()
        #     da["id"]=doc.id
        #     # print(da)
        #     dat.append(da)
        
        # print(dat)
        data={
            'logincount':logincount
        }
        docRef.document(email).update(data)
        return Response({"Done":data})
class AuthUser(APIView):
    def post(self,request,format=None):
        email=request.data.get('email')
        password=request.data.get('password')
        # aadhar=request.get('aadhar')  
        # async def createUser():
        res=""
        try:
            x=auth.create_user(email=email,password=password) 
            # excepttion(auth.EmailAlreadyExistsError("Email already exits"))
            res="Done"
            l=x.uid
            print(str(x.uid))
            
        except admin_auth.EmailAlreadyExistsError as e :
            res=str(e)
        
        finally:
            l=auth.generate_email_verification_link
            
        print(l)
        # email=str(email)
        # password=str(password)
        # print(email,password)
        # x=y.create_user_with_email_and_password(email, password)
        # print(x)
        # firebase1.auth().send_email_verification(x['idToken'])

        

        return Response({"res":res})
        
        




    # return Response({"success": True, "content": "Hello World!"})
