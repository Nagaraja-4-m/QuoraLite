from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class BaseAuthenticatedView(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        # Customize the behavior when the user is not logged in
        return redirect('login')  # Redirect to your login URL
