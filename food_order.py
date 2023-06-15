import json

class FoodItem:
    food_id_counter = 1

    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = FoodItem.food_id_counter
        FoodItem.food_id_counter += 1
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def to_dict(self):
        return {
            'food_id': self.food_id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price,
            'discount': self.discount,
            'stock': self.stock
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            data['quantity'],
            data['price'],
            data['discount'],
            data['stock']
        )


class Admin:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Your Food item added successfully!")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Your Food item updated successfully!")
                return
        print("Food item not found.")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Your Food item removed successfully!")
                return
        print("Food item not found.")

    def view_food_items(self):
        if self.food_items:
            print("List of food items:")
            for food_item in self.food_items:
                print(f"Food ID: {food_item.food_id}")
                print(f"Name: {food_item.name}")
                print(f"Quantity: {food_item.quantity}")
                print(f"Price: ₹{food_item.price}")
                print(f"Discount: ₹{food_item.discount}")
                print(f"Stock: {food_item.stock}")
                print("---------------")
        else:
            print("No food items available.")

    def save_food_items(self, food_file):
        data = [food_item.to_dict() for food_item in self.food_items]
        with open(food_file, 'w') as file:
            json.dump(data, file)
        print("Your Food items saved successfully!")

    def load_food_items(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.food_items = [FoodItem.from_dict(item) for item in data]
            print("Your Food items loaded successfully!")
        except FileNotFoundError:
            print("Food items file not found.")

    def save_users(self, users, user_file):
        data = [user.to_dict() for user in users]
        with open(user_file, 'w') as file:
            json.dump(data, file)
        print("Your User data saved successfully!")

    def load_users(self, user_file):
        try:
            with open(user_file, 'r') as file:
                data = json.load(file)
                users = [User.from_dict(item) for item in data]
            print("Your User data loaded successfully!")
            return users
        except FileNotFoundError:
            print("User data file not found.")
            return []


class User:
    user_id_counter = 1

    def __init__(self, full_name, phone_number, email, address, password):
        self.user_id = User.user_id_counter
        User.user_id_counter += 1
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_new_order(self, food_items):
        order = []
        for item_number in food_items:
            if 1 <= item_number <= len(admin.food_items):
                order.append(admin.food_items[item_number - 1])
        if order:
            self.orders.append(order)
            print("Your Order placed successfully!\n Food will served in 10 min")
        else:
            print("Invalid food item number(s) selected.")

    def view_order_history(self):
        if self.orders:
            print("Order History:")
            for index, order in enumerate(self.orders):
                print(f"Order {index + 1}:")
                for food_item in order:
                    print(f"Food ID: {food_item.food_id}")
                    print(f"Name: {food_item.name}")
                    print(f"Quantity: {food_item.quantity}")
                    print(f"Price: ₹{food_item.price}")
                    print(f"Discount: ₹{food_item.discount}")
                    print(f"Stock: {food_item.stock}")
                    print("---------------")
        else:
            print("No order history available.")

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("Your Profile updated successfully!")

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'full_name': self.full_name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address,
            'password': self.password,
            'orders': [[food_item.to_dict() for food_item in order] for order in self.orders]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data['full_name'],
            data['phone_number'],
            data['email'],
            data['address'],
            data['password']
        )
        user.user_id = data['user_id']
        user.orders = [[FoodItem.from_dict(item) for item in order] for order in data['orders']]
        return user


# Creating an instance of Admin
admin = Admin()

# Loading food items from file (if available)
admin.load_food_items('food_items.json')

# Creating some food items
admin.add_food_item("Tandoori Chicken", "4 pieces", 140, 10, 10)
admin.add_food_item("Vegan Burger", "1 piece", 120, 10, 20)
admin.add_food_item("Truffle Cake", "500gm", 200, 10, 5)

# Saving food items to file
admin.save_food_items('food_items.json')

# Creating an instance of User
user = User("Tushar supare", "1234567890", "tusharsupare@gmail.com", "123,Street Nagpur", "password")

# Loading user data from file (if available)
users = admin.load_users('users.json')

# Registering the user
users.append(user)

# Saving user data to file
admin.save_users(users, 'users.json')

# User functionalities
user.place_new_order([2, 3])
user.view_order_history()
user.update_profile("Tushar", "9876543210", "tusharsupare@gmail.com", "456,Hingoli", "newpassword")

# Saving food items and user data after modifications
admin.save_food_items('food_items.json')
admin.save_users(users, 'users.json')
