
class Customer():

    def __init__(self, lastname=None, firstname=None, street=None, zip=None, city=None, **kwargs):

        self.field = {}
        self.field['lastname'] = lastname
        self.field['firstname'] = firstname
        self.field['street'] = street
        self.field['zip'] = zip
        self.field['city'] = city

        if 'phone' in kwargs.keys():
            self.field['phone'] = kwargs['phone']

        if 'mobile' in kwargs.keys():
            self.field['mobile'] = kwargs['mobile']

        # Add more fields if you like

    def __str__(self):
        output = f"I am {self.field['firstname']} {self.field['lastname']} from {self.field['city']}"
        return output
