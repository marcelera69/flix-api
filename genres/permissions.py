from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        print(request.method)

        if request.method in ['GET','HEAD','OPTIONS']:
            print('Entrou GET')
            return request.user.has_perm('genres.view_genre')

        if request.method == 'POST':
            print('Entrou POST')
            return request.user.has_perm('genres.add_genre')

        if request.method =='PATCH' or 'PUT':
            print('Entrou PATCH')
            return request.user.has_perm('genres.change_genre')

        return False