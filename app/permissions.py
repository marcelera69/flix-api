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
        model_name = view.queryset.model._meta.model_name
        app_label = view.queryset.model._meta.app_label
        action = self.get_action_sufix(method)
        print (f'{app_label}.{action}_{model_name}')
        return f'{app_label}.{action}_{model_name}'
        


    def has_permission(self, request, view):
        model_permission_codename = self.get_model_permission_codename(
            method = request.method, 
            view=view
        )
        
        return request.user.has_perm(model_permission_codename)
    
    