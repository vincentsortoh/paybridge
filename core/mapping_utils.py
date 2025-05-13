class ParamMapperBase:
    request_mappings: dict = {}
    response_mappings: dict = {}

    def map_parameters(self, command: str, params: dict) -> dict:
        mapping = self.request_mappings.get(command, {})
        return {provider_key: params.get(app_key) for app_key, provider_key in mapping.items()}

    def map_response(self, command: str, response: dict) -> dict:
        mapping = self.response_mappings.get(command, {})
        return {app_key: response.get(provider_key) for app_key, provider_key in mapping.items()}