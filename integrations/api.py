import requests
from django.conf import settings

class APIClient:
    def __init__(self, integration):
        self.integration = integration
        
    def connect(self):
        """Test API connection"""
        try:
            response = requests.get(
                self.integration.base_url,
                headers=self._get_headers(),
                timeout=5
            )
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False
            
    def _get_headers(self):
        if self.integration.auth_type == 'api_key':
            return {'Authorization': f'Bearer {self.integration.api_key}'}
        # Add other auth types
        return {}