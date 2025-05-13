
class GenericCommand:
    def __init__(self, provider, method_name):
        self.provider = provider
        self.method_name = method_name

    def execute(self, **kwargs):
        method = getattr(self.provider, self.method_name, None)
        if not method:
            raise Exception(f"Method {self.method_name} not implemented by provider")
        return method(**kwargs)
