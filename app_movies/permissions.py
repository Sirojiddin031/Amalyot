
from rest_framework import permissions


class IsAdminOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or obj.user_id == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Faqat adminlar to‘liq CRUD huquqiga ega, boshqa foydalanuvchilar faqat o‘qiy oladi.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user.is_authenticated and request.user.is_admin


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Faqat o‘z kommentlarini tahrirlash va o‘chirish mumkin.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id == request.user or request.user.is_admin  
