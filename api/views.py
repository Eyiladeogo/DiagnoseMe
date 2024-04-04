from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

import joblib
from user_app.constants import l1, disease
import numpy as np
def vectorize_symptoms(symptoms):
    vectorizer = CountVectorizer(vocabulary=l1, binary=True)
    X = vectorizer.transform(symptoms).toarray()
    return X

class DiagnosisView(APIView):
    def post(self, request):
        # ----------------- TOP THREE DISEASE INDEXES --------------
        data = request.data
        symptoms = data.get('symptoms', [])

        # Load the Naive Bayes model from the saved file
        model = joblib.load('./disease_predictor_v2.pkl')

        # Vectorize the symptoms using CountVectorizer
        # vectorizer = CountVectorizer()
        X = vectorize_symptoms(symptoms)

        # Use the model to predict the probabilities of all diseases
        probabilities = model.predict_proba(X)[0]
        indices = np.argsort(probabilities)[::-1]

        # Get the top three predicted disease indexes
        top_indexes = indices[:3].tolist()
        new_top_indices = [index+1 for index in top_indexes]
        predicted1 = disease[indices[0]]
        predicted2 = disease[indices[1]]
        predicted3 = disease[indices[2]]
        response_list = [predicted1, predicted2, predicted3]

        # Return the top three predicted disease indexes as a JSON response
        response = {'diagnosis': response_list, 'indexes': new_top_indices}
        return JsonResponse(response, status=status.HTTP_200_OK)
        
        # ----------------- TOP THREE DISEASE NAMES------------------
        # data = request.data
        # symptoms = data.get('symptoms', [])

        # # Load the Naive Bayes model from the saved file
        # model = joblib.load('./disease_predictor_v2.pkl')

        # # Vectorize the symptoms using CountVectorizer
        # # vectorizer = CountVectorizer()
        # X = vectorize_symptoms(symptoms)

        # # Use the model to predict the probabilities of all diseases
        # probabilities = model.predict_proba(X)[0]
        # indices = np.argsort(probabilities)[::-1]

        # # Get the top three predicted diseases
        # top_diseases = [disease[index] for index in indices[:3]]

        # # Return the top three predicted diseases as a JSON response
        # response = {'diagnosis': top_diseases}
        # return JsonResponse(response, status=status.HTTP_200_OK)
        
        # --------------SINGLE NUMBER --------------------
        # data = request.data
        # symptoms = data.get('symptoms', [])

        # # Load the Naive Bayes model from the saved file
        # model = joblib.load('./disease_predictor_v2.pkl')

        # # Vectorize the symptoms using CountVectorizer
        # # vectorizer = CountVectorizer()
        # X = vectorize_symptoms(symptoms)

        # # Use the model to predict the diagnosis
        # diagnosis = model.predict(X)[0]

        # # Return the diagnosis as a JSON response
        # response = {'diagnosis': diagnosis}
        # return Response(response, status=status.HTTP_200_OK)
        
    













# from django.shortcuts import render

# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from sklearn.naive_bayes import MultinomialNB
# from django.http import JsonResponse

# import joblib

# class DiagnosisView(APIView):
#     def get(self, request):
#         symptoms = request.query_params.getlist('symptoms')

#         # Load the Naive Bayes model from the saved file
#         model = joblib.load('disease_predictor.pkl')

#         # Use the model to predict the diagnosis
#         diagnosis = model.predict([symptoms])[0]

#         # Return the diagnosis as a JSON response
#         response = {'diagnosis': diagnosis}
#         return Response(response, status=status.HTTP_200_OK)
#     # def get(self, request):
#     #     symptoms = request.data.get('symptoms', [])
        
#     #     # Load the Naive Bayes model from the saved file
#     #     model = joblib.load('naive_bayes_model.joblib')

#     #     # Use the model to predict the diagnosis
#     #     diagnosis = model.predict([symptoms])[0]

#     #     # Return the diagnosis to the frontend
#     #     return Response({'diagnosis': diagnosis})

