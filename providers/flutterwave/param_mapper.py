from core.mapping_utils import ParamMapperBase

class FlutterwaveParamMapper(ParamMapperBase):
    request_mappings = {
        "lookup_invoice": {
            "invoiceId": "inv_id",
            "customerRef": "cust_ref"
        },
        "get_receipt": {
            "transactionId": "txn_reference"
        }
    }

    response_mappings = {
        "lookup_invoice": {
            "inv_id": "invoiceId",
            "total_due": "amount",
            "payment_due": "dueDate"
        },
        "get_receipt": {
            "receipt_code": "receiptNo",
            "status_desc": "paymentStatus"
        }
    }