
class GetReceiptCommand:
    def __init__(self, provider):
        self.provider = provider

    def execute(self, txn_id):
        result = self.provider.get_receipt(txn_id)
        result["custom"] = True
        return result
