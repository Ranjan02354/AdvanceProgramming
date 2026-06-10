from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


class NotificationService(ABC):

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationService):

    def send(self, message):
        print(f"Email Sent: {message}")


class SMSNotification(NotificationService):

    def send(self, message):
        print(f"SMS Sent: {message}")


class PushNotification(NotificationService):

    def send(self, message):
        print(f"Push Notification Sent: {message}")


class Storage(ABC):

    @abstractmethod
    def save(self, order):
        pass


class DatabaseStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved to Database")


class FileStorage(Storage):

    def save(self, order):
        print(f"Order {order.order_id} saved to File")


class Order:

    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    def get_total(self):
        return self.amount


class RegularOrder(Order):

    def get_total(self):
        return self.amount


class DiscountedOrder(Order):

    def get_total(self):
        return self.amount * 0.9


class PriorityOrder(Order):

    def get_total(self):
        return self.amount + 100


class OrderService:

    # Dependency Injection (DIP)
    def __init__(self, payment_method, notification_service, storage):
        self.payment_method = payment_method
        self.notification_service = notification_service
        self.storage = storage

    def place_order(self, order):

        total = order.get_total()

        print("\nProcessing Order...")
        print(f"Customer: {order.customer_name}")
        print(f"Order ID: {order.order_id}")
        print(f"Final Amount: ₹{total}")

        self.payment_method.pay(total)

        self.notification_service.send(
            f"Order {order.order_id} placed successfully!"
        )

        self.storage.save(order)


if __name__ == "__main__":

    customer_name = input("Enter Customer Name: ")
    amount = float(input("Enter Order Amount: "))
    order_id = int(input("Enter Order ID: "))

    print("\nSelect Order Type:")
    print("1. Regular Order")
    print("2. Discounted Order")
    print("3. Priority Order")

    order_choice = int(input("Enter choice: "))

    if order_choice == 1:
        order = RegularOrder(order_id, customer_name, amount)
    elif order_choice == 2:
        order = DiscountedOrder(order_id, customer_name, amount)
    else:
        order = PriorityOrder(order_id, customer_name, amount)

    print("\nSelect Payment Method:")
    print("1. Credit Card")
    print("2. UPI")
    print("3. Wallet")

    payment_choice = int(input("Enter choice: "))

    if payment_choice == 1:
        payment = CreditCardPayment()
    elif payment_choice == 2:
        payment = UPIPayment()
    else:
        payment = WalletPayment()

    print("\nSelect Notification Type:")
    print("1. Email")
    print("2. SMS")
    print("3. Push Notification")

    notification_choice = int(input("Enter choice: "))

    if notification_choice == 1:
        notification = EmailNotification()
    elif notification_choice == 2:
        notification = SMSNotification()
    else:
        notification = PushNotification()

    print("\nSelect Storage Type:")
    print("1. Database")
    print("2. File")

    storage_choice = int(input("Enter choice: "))

    if storage_choice == 1:
        storage = DatabaseStorage()
    else:
        storage = FileStorage()

    service = OrderService(
        payment,
        notification,
        storage
    )

    service.place_order(order)