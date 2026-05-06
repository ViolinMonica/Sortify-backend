from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from .ai_service import classify_image
from apps.waste.recommendation import get_recommendation


class ClassifyView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        image_file = request.FILES.get("image")
        
        if not image_file:
            return Response(
                {"error": "'image' field has to be filled."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validasi tipe file
        allowed_types = ["image/jpeg", "image/png", "image/webp"]
        if image_file.content_type not in allowed_types:
            return Response(
                {"error": f"File format is not supported. Supported formats: jpg, png, webp."},
                status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            )

        try:
            # Klasifikasi AI
            result = classify_image(image_file)
            
            # Ambil rekomendasi berdasarkan kategori
            recommendation = get_recommendation(result["sortify_category"], raw_label=result["raw_label"])

            return Response({
                "success": True,
                "classification": {
                    "category": result["sortify_category"],
                    "raw_label": result["raw_label"],
                    "confidence": result["confidence"],
                },
                "recommendation": recommendation,
            }, status=status.HTTP_200_OK)

        except FileNotFoundError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        except Exception as e:
            return Response(
                {"error": f"Failed to process the photo: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
