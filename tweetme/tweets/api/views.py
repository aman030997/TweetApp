from rest_framework import generics,permissions
from django.db.models import Q
from .serializers import TweetModelSerializer
from tweets.models import Tweet
from .pagination import StandardResultsPagination
class TweetListAPIView(generics.ListAPIView):
	serializer_class = TweetModelSerializer
	pagination_class = StandardResultsPagination
	
	def get_queryset(self,*args,**kwargs):
		qs = Tweet.objects.all().order_by("-timestamp")
		query = self.request.GET.get('q', None)
		if query:
			qs = qs.filter(Q(content__icontains=query) | 
						   Q(user__username__icontains=query))
		return qs

class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class = TweetModelSerializer
	permission_classes = [permissions.IsAuthenticated]
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)