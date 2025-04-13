class AjaxNavMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.htmx and not request.htmx.history_restore:
            response['HX-Push'] = request.path
        return response