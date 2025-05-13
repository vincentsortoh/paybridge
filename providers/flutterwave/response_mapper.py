
def normalize_response(command: str, raw_response: dict) -> dict:
    if command == "make_payment":
        return {
            "status": raw_response.get("status"),
            "transaction_id": raw_response.get("ref"),
            "amount": raw_response.get("amt"),
            "provider": "flutterwave"
        }
    elif command == "lookup_invoice":
        return {
            "status": raw_response.get("status"),
            "invoice_id": raw_response.get("inv_id"),
            "provider": "flutterwave"
        }
    return raw_response
