from core.mapping_utils import ParamMapperBase

class PaystackParamMapper(ParamMapperBase):
    request_mappings = {
        "lookup_invoice": {
            "invoiceId": "invoice_id",
            "customerRef": "cust_ref"
        },
        "get_receipt": {
            "transactionId": "txn_reference"
        }
    }

    response_mappings = {
        "lookup_invoice": {
            "invoice_id": "invoiceId",
            "total_due": "amount",
            "payment_due": "dueDate"
        },
        "get_receipt": {
            "receipt_code": "receiptNo",
            "status_desc": "paymentStatus"
        }
    }