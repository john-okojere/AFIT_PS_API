import json 
from payment.models import Department, Level


data = [
    {
        "department": "Computer Science",
        "levels": [
            {"level": 100, "fee_amount": 150000},
            {"level": 200, "fee_amount": 140000},
            {"level": 300, "fee_amount": 130000},
            {"level": 400, "fee_amount": 120000},
            {"level": 500, "fee_amount": 110000}
        ]
    },
    {
        "department": "Electrical Engineering",
        "levels": [
            {"level": 100, "fee_amount": 160000},
            {"level": 200, "fee_amount": 150000},
            {"level": 300, "fee_amount": 140000},
            {"level": 400, "fee_amount": 130000},
            {"level": 500, "fee_amount": 120000}
        ]
    },
    {
        "department": "Mechanical Engineering",
        "levels": [
            {"level": 100, "fee_amount": 155000},
            {"level": 200, "fee_amount": 145000},
            {"level": 300, "fee_amount": 135000},
            {"level": 400, "fee_amount": 125000},
            {"level": 500, "fee_amount": 115000}
        ]
    },
    {
        "department": "Civil Engineering",
        "levels": [
            {"level": 100, "fee_amount": 165000},
            {"level": 200, "fee_amount": 155000},
            {"level": 300, "fee_amount": 145000},
            {"level": 400, "fee_amount": 135000},
            {"level": 500, "fee_amount": 125000}
        ]
    },
    {
        "department": "Business Administration",
        "levels": [
            {"level": 100, "fee_amount": 140000},
            {"level": 200, "fee_amount": 130000},
            {"level": 300, "fee_amount": 120000},
            {"level": 400, "fee_amount": 110000}
        ]
    },
    {
        "department": "Mathematics",
        "levels": [
            {"level": 100, "fee_amount": 145000},
            {"level": 200, "fee_amount": 135000},
            {"level": 300, "fee_amount": 125000},
            {"level": 400, "fee_amount": 115000}
        ]
    },
    {
        "department": "Physics",
        "levels": [
            {"level": 100, "fee_amount": 150000},
            {"level": 200, "fee_amount": 140000},
            {"level": 300, "fee_amount": 130000},
            {"level": 400, "fee_amount": 120000}
        ]
    },
    {
        "department": "Chemistry",
        "levels": [
            {"level": 100, "fee_amount": 150000},
            {"level": 200, "fee_amount": 140000},
            {"level": 300, "fee_amount": 130000},
            {"level": 400, "fee_amount": 120000}
        ]
    },
    {
        "department": "Biology",
        "levels": [
            {"level": 100, "fee_amount": 140000},
            {"level": 200, "fee_amount": 130000},
            {"level": 300, "fee_amount": 120000},
            {"level": 400, "fee_amount": 110000}
        ]
    },
    {
        "department": "Economics",
        "levels": [
            {"level": 100, "fee_amount": 135000},
            {"level": 200, "fee_amount": 125000},
            {"level": 300, "fee_amount": 115000},
            {"level": 400, "fee_amount": 105000}
        ]
    },
    {
        "department": "Accounting",
        "levels": [
            {"level": 100, "fee_amount": 150000},
            {"level": 200, "fee_amount": 140000},
            {"level": 300, "fee_amount": 130000},
            {"level": 400, "fee_amount": 120000}
        ]
    },
    {
        "department": "Architecture",
        "levels": [
            {"level": 100, "fee_amount": 170000},
            {"level": 200, "fee_amount": 160000},
            {"level": 300, "fee_amount": 150000},
            {"level": 400, "fee_amount": 140000},
            {"level": 500, "fee_amount": 130000}
        ]
    },
    {
        "department": "Environmental Science",
        "levels": [
            {"level": 100, "fee_amount": 165000},
            {"level": 200, "fee_amount": 155000},
            {"level": 300, "fee_amount": 145000},
            {"level": 400, "fee_amount": 135000},
            {"level": 500, "fee_amount": 125000}
        ]
    },
    {
        "department": "Chemical Engineering",
        "levels": [
            {"level": 100, "fee_amount": 175000},
            {"level": 200, "fee_amount": 165000},
            {"level": 300, "fee_amount": 155000},
            {"level": 400, "fee_amount": 145000},
            {"level": 500, "fee_amount": 135000}
        ]
    },
    {
        "department": "Petroleum Engineering",
        "levels": [
            {"level": 100, "fee_amount": 180000},
            {"level": 200, "fee_amount": 170000},
            {"level": 300, "fee_amount": 160000},
            {"level": 400, "fee_amount": 150000},
            {"level": 500, "fee_amount": 140000}
        ]
    },
    {
        "department": "Law",
        "levels": [
            {"level": 100, "fee_amount": 200000},
            {"level": 200, "fee_amount": 190000},
            {"level": 300, "fee_amount": 180000},
            {"level": 400, "fee_amount": 170000},
            {"level": 500, "fee_amount": 160000}
        ]
    }
]

