
__all__ = ['MODEL_URL', 'MODEL_VIEW']


MODEL_URL = """from rest_framework.routers import SimpleRouter
from {{ app }}.api import views


router = SimpleRouter()
{% for model in models %}
router.register(r'{{ model | lower }}', views.{{ model }}ViewSet){% endfor %}

urlpatterns = router.urls
"""


MODEL_VIEW = """from rest_framework import viewsets, permissions
from {{ app }}.api.serializers import *
{% for model in models %}

class {{ model }}ViewSet(viewsets.ModelViewSet):
    \"\"\"

    ViewSet for {{ model }} model

    retrieve:
    Return the given {{ model }}.

    list:
    Return a list of all the existing {{ model }}.

    create:
    Create a new {{ model }} instance.

    update:
    Update a {{ model }} instance.

    partial_update:
    Partial update a {{ model }} instance by pk.

    destroy:
    Delete a {{ model }} instance.

    \"\"\"
    queryset = {{ model }}.objects.order_by('pk')
    serializer_class = {{ model }}Serializer
    permission_classes = (permissions.IsAuthenticated, )
{% endfor %}"""
