from abc import ABC, abstractmethod

# Abstract Base Class
class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.original_amount = 0
        self.final_amount = 0

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self):
        print("\n--- Payment Receipt ---")
        print(f"User: {self.user_name}")
        print(f"Original Amount: ₹{self.original_amount}")
        print(f"Final Amount Paid: ₹{self.final_amount}")
        print("------------------------")


# Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        gateway_fee = 0.02 * amount
        gst = 0.18 * gateway_fee
        self.final_amount = amount + gateway_fee + gst

        print("\nProcessing Credit Card Payment...")
        self.generate_receipt()


# UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        cashback = 50 if amount > 1000 else 0
        self.final_amount = amount - cashback

        print("\nProcessing UPI Payment...")
        if cashback:
            print("Cashback Applied: ₹50")
        self.generate_receipt()


# PayPal Payment
class PayPalPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        transaction_fee = 0.03 * amount
        conversion_fee = 20
        self.final_amount = amount + transaction_fee + conversion_fee

        print("\nProcessing PayPal Payment...")
        self.generate_receipt()


# Wallet Payment
class WalletPayment(Payment):
    def __init__(self, user_name, balance):
        super().__init__(user_name)
        self.balance = balance

    def pay(self, amount):
        self.original_amount = amount
        print("\nProcessing Wallet Payment...")

        if amount > self.balance:
            print("Transaction Failed: Insufficient Balance")
            return
        else:
            self.balance -= amount
            self.final_amount = amount
            print(f"Remaining Wallet Balance: ₹{self.balance}")
            self.generate_receipt()


# Polymorphic Function
def process_payment(payment, amount):
    payment.pay(amount)


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    # Creating objects
    cc = CreditCardPayment("Krish")
    upi = UPIPayment("Krish")
    paypal = PayPalPayment("Krish")
    wallet = WalletPayment("Krish", balance=1500)

    # Processing payments
    process_payment(cc, 1000)
    process_payment(upi, 1200)
    process_payment(paypal, 800)
    process_payment(wallet, 500)
    process_payment(wallet, 1200)  # Should fail due to low balance