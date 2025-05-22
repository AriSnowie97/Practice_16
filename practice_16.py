# 1. Abstract base class (interface) for payment
class PaymentProcessor:
    def process_payment(self, amount: float):
        raise NotImplementedError("Subclasses must implement this method")

# 2. Concrete implementations for different payment types (open for extension)
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount:.2f}.")
        # Add actual credit card processing logic here
        print("Credit card payment successful.")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}.")
        # Add actual PayPal processing logic here
        print("PayPal payment successful.")

class CryptocurrencyProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing cryptocurrency payment of ${amount:.2f}.")
        # Add actual cryptocurrency processing logic here (e.g., Bitcoin, Ethereum)
        print("Cryptocurrency payment successful.")

# 3. Class that uses processors (closed for modification)
class PaymentService:
    def process_order_payment(self, processor: PaymentProcessor, amount: float):
        print(f"\nPaymentService: Initiating payment for ${amount:.2f}...")
        processor.process_payment(amount)
        print("PaymentService: Payment processing complete.")

# Example Usage
if __name__ == "__main__":
    print("\n--- Task 2: Extensibility without Modification (OCP) ---")
    
    payment_service = PaymentService()

    # Process credit card payment
    credit_card_proc = CreditCardProcessor()
    payment_service.process_order_payment(credit_card_proc, 100.00)

    # Process PayPal payment
    paypal_proc = PayPalProcessor()
    payment_service.process_order_payment(paypal_proc, 50.75)

    # Process cryptocurrency payment
    crypto_proc = CryptocurrencyProcessor()
    payment_service.process_order_payment(crypto_proc, 25.00)

    # To add a new payment type (e.g., Apple Pay), you just need to:
    # 1. Create a new class that inherits from PaymentProcessor.
    # 2. Implement the process_payment method.
    # 3. Use it via PaymentService without modifying PaymentService.
    class ApplePayProcessor(PaymentProcessor):
        def process_payment(self, amount: float):
            print(f"Processing Apple Pay payment of ${amount:.2f}.")
            print("Apple Pay payment successful.")

    apple_pay_proc = ApplePayProcessor()
    payment_service.process_order_payment(apple_pay_proc, 75.00)