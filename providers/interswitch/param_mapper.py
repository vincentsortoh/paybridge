from core.mapping_utils import ParamMapperBase

class InterswitchParamMapper(ParamMapperBase):
    request_mappings = {
        "lookup_invoice": {
            "invoiceId": "invoice_code",
        },
        "get_receipt": {
            "transactionId": "txn_reference"
        }
    }

    response_mappings = {
        "lookup_invoice": {
            "invoice_code": "invoiceId",
            "total_due": "amount",
            "payment_due": "dueDate"
        },
        "get_receipt": {
            "receipt_code": "receiptNo",
            "status_desc": "paymentStatus"
        }
    }