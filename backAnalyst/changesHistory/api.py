from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from manageBD.db_manage import last_changes
from changesHistory.serializers import ProductSerializer

import json

class ChangesHistoryViewSet(viewsets.ViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


    @action(detail=False, methods=['get'])
    def view_last_changes(self, request):
        last_10_changes = last_changes()
        answer = json.dumps(last_10_changes, default=str)
        return Response(answer)