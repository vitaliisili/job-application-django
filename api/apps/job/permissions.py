from rest_framework import permissions

class JobApplicationPermissions(permissions.BasePermissions):
    
    def has_permissions(self, request, view):
        if view.action in ['list', 'retrieve', 'destroy', 'update', 'partial_update', 'create']:
            return request.user.is_authenticated
        else:
            return False
            

    def has_object_permissions(self, request, view, obj):
        if not request.user.is_authenticated:
            return False 
        
        if view.action in ['list', 'retrieve', 'destroy', 'update', 'partial_update']:
            return obj == request.user or request.user.is_staff
        else:
            return False