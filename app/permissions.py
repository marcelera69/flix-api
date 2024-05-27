from rest_framework import permissions





class GlobalPermissions(permissions.BasePermission):
    
    def get_action_sufix(self, method):
        if method in ['GET','HEAD','OPTIONS']:
            return 'view'
        elif method == 'POST':
            return 'add'
        elif method in ['PATCH','PUT']:
            return 'change'
        else:
            return 'delete'


    def get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset._meta.model_name
            app_label = view.queryset._meta.model_label
            action = self.get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None


    def has_permission(self, request, view):
        model_permission_codename = self.get_model_permission_codename(
            method = request.method, 
            view=view
        )

        if not model_permission_codename:
            return None
        
        return request.user.has_perm(model_permission_codename)
    
    