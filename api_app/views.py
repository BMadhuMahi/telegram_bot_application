from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from .tasks import send_registration_email

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message': 'This is a public endpoint'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    serializer = UserSerializer(request.user)
    return Response({'message': 'This is a protected endpoint', 'user': serializer.data})


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        subject = "Welcome"
        message = "Thank you for registering."
        recipient_list = [user.email]

        send_registration_email.delay(subject, message, recipient_list)

        return Response({'message': 'User registered successfully'})
    return Response(serializer.errors, status=400)
@api_view(['POST'])
@permission_classes([AllowAny])
def telegram_webhook(request):
    from .telegram import process_update
    process_update(request.data)
    return Response({'ok': True})
