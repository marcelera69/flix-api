from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET' or 'HEAD' or 'OPTIONS':
            return request.user.has_perm('genres.view_genre')

        if request.method == 'POST':
            return False

        return False