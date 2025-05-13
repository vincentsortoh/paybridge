
class MakePaymentCommand:
    def __init__(self, provider):
        self.provider = provider

    def execute(self, amt, ref):
        result = self.provider.make_payment(amt, ref)
        result["custom"] = True
        return result
