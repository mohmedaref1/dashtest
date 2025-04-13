// Simulate API calls until real API is ready
class APISimulator {
    static getOrders() {
        return {
            "orders": [
                {
                    "id": "ORD-001",
                    "customer_id": "CUST-001",
                    "department": "Electronics",
                    "status": "new",
                    "due_time": new Date().getTime() + 3600000 // 1 hour from now
                },
                // Add more simulated orders
            ]
        };
    }

    static getTeamMembers() {
        return {
            "members": [
                {
                    "id": 1,
                    "name": "John Doe",
                    "role": "team",
                    "department": "Shipping"
                }
            ]
        };
    }
}