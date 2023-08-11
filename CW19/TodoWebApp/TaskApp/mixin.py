from .models import Task
from django.core.exceptions import PermissionDenied as PD

class TodoOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(id = kwargs['task_id'])
        if not task.author == request.user:
            raise PD
        else:
            return super().dispatch(request, *args, **kwargs)