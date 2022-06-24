from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # パスワード再設定メール送信画面
    path('admin_password_reset', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    # パスワード再設定メール送信完了画面
    path("admin_password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # パスワード再設定画面
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # パスワード再設定完了画面
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
