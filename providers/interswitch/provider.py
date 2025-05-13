
class InterswitchProvider:
    def lookup_invoice(self, invoice_code):
        return {"status": "found", "invoice_code": invoice_code}

    def make_payment(self, total_amount, txn_ref):
        return {"status": "success", "txn_id": txn_ref, "paid": total_amount}

    def get_receipt(self, transaction_id):
        return {"status": "retrieved", "receipt_id": f"R-{transaction_id}"}
