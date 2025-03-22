from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .ml_model import predict_next_number


class PredictAPIView(APIView):
    def post(self, request):
        """
        API endpoint that takes a sequence of numbers and predicts the next number.
        """
        data = request.data  # Get JSON data from request
        sequence = data.get("sequence", [])

        if not isinstance(sequence, list) or not all(
            isinstance(i, (int, float)) for i in sequence
        ):
            return Response(
                {"error": "Invalid input. Provide a list of numbers."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if len(sequence) < 3:
            return Response(
                {"error": "Sequence must have at least 3 numbers."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            prediction = predict_next_number(sequence)
            return Response({"prediction": prediction}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)