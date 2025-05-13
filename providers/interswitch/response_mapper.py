
def normalize_response(command: str, raw_response: dict) -> dict:
    if command == "make_payment":
        return {
            "status": raw_response.get("status"),
            "transaction_id": raw_response.get("txn_id"),
            "amount": raw_response.get("paid"),
            "provider": "interswitch"
        }
    elif command == "lookup_invoice":
        return {
            "status": raw_response.get("status"),
            "invoice_id": raw_response.get("invoice_code"),
            "provider": "interswitch"
        }
    elif command == "get_receipt":
        return {
            "status": raw_response.get("status"),
            "receipt_id": raw_response.get("receipt_id"),
            "provider": "interswitch"
        }
    return raw_response
