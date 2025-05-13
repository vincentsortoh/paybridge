
class PaystackProvider:
    def lookup_invoice(self, invoice_id, cust_ref):
        return {"invoice_id": invoice_id, "status": "found", "id": "paystack-001"}

    def make_payment(self, amount, reference):
        return {"amount": amount, "reference": reference, "status": "paid"}
