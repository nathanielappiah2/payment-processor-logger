import json
import uuid
from datetime import datetime

def lambda_handler(event, context):
    """
    Simulated fintech payment processor:
    - accepts a payment request
    - generates a transaction_id
    - logs the payment to CloudWatch
    - returns success response
    """

    try:
        # 1) Read input (test event JSON)
        amount = event.get("amount", 0)
        currency = event.get("currency", "GBP")
        customer_id = event.get("customer_id", "UNKNOWN")

        # 2) Generate transaction ID + timestamp
        transaction_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat()

        # 3) Log to CloudWatch (this is your "audit trail")
        log_data = {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "customer_id": customer_id,
            "timestamp": timestamp,
            "status": "PROCESSED"
        }

        print("✅ PAYMENT LOG:", json.dumps(log_data))

        # 4) Return response
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Payment processed successfully ✅",
                "transaction_id": transaction_id,
                "timestamp": timestamp
            })
        }

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
