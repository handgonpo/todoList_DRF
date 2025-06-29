from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status


# 전체보기
class TodoListAPI(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)  # 일반 json데이터 .data

# 생성하기
class TodoCreateAPI(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)

# 상세조회
class TodoRetrieveAPI(APIView): # 개발자가 커스터마이징 형식으로 짜놓은 API 상세조회
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo)
        return Response(serializer.data)


# 수정하기
class TodoUpdateAPI(APIView):
    pass

# 삭제하기
class TodoDeleteAPI(APIView):
    pass