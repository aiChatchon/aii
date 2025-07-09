import hmac
import hashlib
import time
import os
from typing import List, Dict

# Mock fetch from Shopee API
def fetch_orders() -> List[Dict]:
    # Placeholder: return a list of order dicts
    now = int(time.time())
    return [
        {
            'order_id': f'shopee_{now}',
            'platform': 'shopee',
            'customer_name': 'John Doe',
            'status': 'NEW',
            'total_amount': 100.0,
            'items': [
                {'sku': 'SKU1', 'quantity': 2, 'price': 50.0}
            ]
        }
    ]

def generate_signature(path: str, partner_id: str, timestamp: str, partner_key: str) -> str:
    base_string = f"{partner_id}{path}{timestamp}"
    sign = hmac.new(partner_key.encode(), base_string.encode(), hashlib.sha256).hexdigest()
    return sign
