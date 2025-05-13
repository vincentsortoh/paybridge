
def normalize_response(command: str, raw_response: dict) -> dict:
    if command == "make_payment":
        return {
            "status": raw_response.get("status"),
            "transaction_id": raw_response.get("reference"),
            "amount": raw_response.get("amount"),
            "provider": "paystack"
        }
    elif command == "lookup_invoice":
        return {
            "status": raw_response.get("status"),
            "invoice_id": raw_response.get("invoice_id"),
            "provider": "paystack"
        }
    return raw_response
