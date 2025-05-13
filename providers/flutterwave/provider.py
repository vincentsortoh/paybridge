
class FlutterwaveProvider:

    def lookup_invoice(self, invoice_id):
        print("invoice_id", invoice_id)
        return {"invoice_id": invoice_id, "status": "found"}

    def make_payment(self, amt, ref):
        return {"amt": amt, "ref": ref, "status": "paid"}
