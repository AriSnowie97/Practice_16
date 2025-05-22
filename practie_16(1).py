
class EmailSender:
    def send_email(self, recipient: str, subject: str, message: str):
        raise NotImplementedError("Subclasses must implement send_email method")

class SMSSender:
    def send_sms(self, phone_number: str, message: str):
        raise NotImplementedError("Subclasses must implement send_sms method")

class PushNotificationSender:
    def send_push_notification(self, device_token: str, title: str, body: str):
        raise NotImplementedError("Subclasses must implement send_push_notification method")

# 2. Implementations of concrete senders (details)
class ConcreteEmailSender(EmailSender):
    def send_email(self, recipient: str, subject: str, message: str):
        print(f"Sending Email to {recipient}: Subject: '{subject}', Message: '{message}'")
        # Actual email sending logic
        pass

class ConcreteSMSSender(SMSSender):
    def send_sms(self, phone_number: str, message: str):
        print(f"Sending SMS to {phone_number}: Message: '{message}'")
        # Actual SMS sending logic
        pass

class ConcretePushNotificationSender(PushNotificationSender):
    def send_push_notification(self, device_token: str, title: str, body: str):
        print(f"Sending Push Notification to {device_token}: Title: '{title}', Body: '{body}'")
        # Actual Push Notification sending logic
        pass

# 3. Notification class (high-level module) that depends on abstractions (DIP)
class Notifier:
    def __init__(self, email_sender: EmailSender = None, sms_sender: SMSSender = None, push_sender: PushNotificationSender = None):
        # Dependencies are "inverted": Notifier receives implementations via its constructor (Dependency Injection)
        self.email_sender = email_sender
        self.sms_sender = sms_sender
        self.push_sender = push_sender

    def notify_event(self, event_type: str, details: dict):
        print(f"\nNotifier: Processing event type '{event_type}'")

        if self.email_sender and "email" in details:
            self.email_sender.send_email(
                details["email"]["recipient"],
                details["email"]["subject"],
                details["email"]["message"]
            )
        
        if self.sms_sender and "sms" in details:
            self.sms_sender.send_sms(
                details["sms"]["phone_number"],
                details["sms"]["message"]
            )
            
        if self.push_sender and "push" in details:
            self.push_sender.send_push_notification(
                details["push"]["device_token"],
                details["push"]["title"],
                details["push"]["body"]
            )
        
        print("Notifier: Event notification complete.")

# Example Usage
if __name__ == "__main__":
    print("\n--- Task 3: Interfaces and Dependencies (ISP, DIP) ---")
    email_sender = ConcreteEmailSender()
    sms_sender = ConcreteSMSSender()
    push_sender = ConcretePushNotificationSender()
    notifier_full = Notifier(email_sender, sms_sender, push_sender)
    notifier_email_only = Notifier(email_sender=email_sender)
    notifier_sms_push = Notifier(sms_sender=sms_sender, push_sender=push_sender)

    # Event data
    event_details_full = {
        "email": {
            "recipient": "user@example.com",
            "subject": "Order Confirmation",
            "message": "Your order has been confirmed!"
        },
        "sms": {
            "phone_number": "+380501234567",
            "message": "Your order #12345 is confirmed!"
        },
        "push": {
            "device_token": "abc123xyz",
            "title": "Order Confirmed!",
            "body": "Tap to view details."
        }
    }

    event_details_simple = {
        "email": {
            "recipient": "admin@example.com",
            "subject": "New User Registered",
            "message": "A new user just signed up."
        }
    }

    # Notify about an event using the full Notifier
    notifier_full.notify_event("Order Placed", event_details_full)

    # Notify about an event using an email-only Notifier
    notifier_email_only.notify_event("New Registration", event_details_simple)

    # Notify about an event with SMS and Push
    notifier_sms_push.notify_event("Promotional Offer", {
        "sms": {"phone_number": "+380971234567", "message": "Limited time offer! Check app."},
        "push": {"device_token": "def456uvw", "title": "Big Sale!", "body": "Don't miss out!"}
    })

    # To add a new message type (e.g., Telegram):
    # 1. Create a new interface (or check if an existing one fits).
    # 2. Create a new implementation of that interface.
    # 3. Modify Notifier to accept the new sender type in its constructor (a one-time change)
    #    and call it in notify_event (this might be a small modification).
    #    However, DIP still allows passing the new sender without changing existing working implementations.