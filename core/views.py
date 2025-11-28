from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import MedicalRecord
from .serializers import MedicalRecordSerializer
from ai.predictor import predict, symptom_columns  # symptom_columns sesuai CSV

class MedicalRecordViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
    # def get_queryset(self):
    #     # hanya record milik user login
    #     return MedicalRecord.objects.filter(patient=self.request.user)

    
    def create(self, request, *args, **kwargs):
        input_data = {k: v for k, v in request.data.items() if k in symptom_columns}

        if not input_data:
            return Response(
                {"error": "Tidak ada gejala valid yang dikirim."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Convert semua input ke 0/1
        for k, v in input_data.items():
            if isinstance(v, str):
                input_data[k] = 1 if v.lower() == 'true' else 0
            else:
                input_data[k] = int(bool(v))

        # Jalankan AI predictor
        diagnosis_result = predict(input_data)

        # Simpan ke database
        record = MedicalRecord.objects.create(
            diagnosis=diagnosis_result,
            **input_data
        )

        serializer = MedicalRecordSerializer(record, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
