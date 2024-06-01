from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatSerializer
from drf_yasg.utils import swagger_auto_schema

from .utils.util_genai import user_input, read_file_transcripts_folder


class ChatView(APIView):
    def get(self, request):
        read_file_transcripts_folder()
        return Response({}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Chat Message",
        request_body=ChatSerializer,
        responses={200: ChatSerializer}
    )
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.data.get('message', '')
            response = serializer.data
            response['message'] = user_input(user_question=prompt).get('output_text', '')
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

