class useraccount:
    
    def __init__(self, username="None", password="None", useremail="None", phone_num="None", payment_info=None, booking_info=None):
        self.username = username
        self.password = password
        self.useremail = useremail
        self.phone_num = phone_num
        self.payment_info = payment_info
        self.booking_info = booking_info
    # Setter methods

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_useremail(self, useremail):
        self.useremail = useremail

    def set_phone_num(self, phone_num):
        self.phone_num = phone_num

    def set_payment_info(self, payment_info):
        self.payment_info = payment_info

    def set_booking_info(self, booking_info):
        self.booking_info = booking_info

    # Getter methods
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_useremail(self):
        return self.useremail

    def get_phone_num(self):
        return self.phone_num

    def get_payment_info(self):
        return self.payment_info

    def get_booking_info(self):
        return self.booking_info

    def __str__(self):
        return f"User Account Information:\nUsername: {self.username}\nEmail: {self.useremail}\nPhone Number: {self.phone_num}\nPayment Information: {self.payment_info}\nBooking Information: {self.booking_info}"
