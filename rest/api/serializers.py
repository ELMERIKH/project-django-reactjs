from rest_framework import serializers
from .models import Article, Task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields ='__all__'		