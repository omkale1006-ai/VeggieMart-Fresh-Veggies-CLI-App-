class Veg:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Category:
    def __init__(self, category):
        self.category = category


class VegCategory:
    def __init__(self):
        self.categories = [
            Category("Leafy Vegetables"),
            Category("Root Vegetables"),
            Category("Fruiting Vegetables"),
            Category("Pod Vegetables"),
            Category("Bulb Vegetables"),
            Category("Stem Vegetables")
        ]

    def show_categories(self):
        print("\n🌿 Available Vegetable Categories:")
        for index, category in enumerate(self.categories, start=1):
            print(f"{index}. {category.category}")


class VegShow:
    def __init__(self):
        self.leafy_vegetables = [
            Veg("Spinach (पालक)", 30),
            Veg("Fenugreek (मेथी)", 25),
            Veg("Mustard Leaves (सरसों)", 35),
            Veg("Coriander (धनिया)", 20)
        ]
        self.root_vegetables = [
            Veg("Carrot (गाजर)", 40),
            Veg("Beetroot (चुकंदर)", 35),
            Veg("Radish (मूली)", 25),
            Veg("Turnip (शलगम)", 30)
        ]
        self.fruiting_vegetables = [
            Veg("Tomato (टमाटर)", 25),
            Veg("Brinjal (बैंगन)", 30),
            Veg("Capsicum (शिमला मिर्च)", 50),
            Veg("Pumpkin (कद्दू)", 20)
        ]
        self.pod_vegetables = [
            Veg("Green Peas (मटर)", 60),
            Veg("Beans (फली)", 50),
            Veg("Okra (भिंडी)", 40)
        ]
        self.bulb_vegetables = [
            Veg("Onion (प्याज़)", 25),
            Veg("Garlic (लहसुन)", 180)
        ]
        self.stem_vegetables = [
            Veg("Celery (आजवाइन)", 80),
            Veg("Asparagus (शतावरी)", 200),
            Veg("Bamboo Shoots (बांस कोपल)", 100)
        ]
        self.order = []

        # 🧍 User info placeholders
        self.customer_name = ""
        self.customer_age = ""
        self.customer_gender = ""
        self.customer_phone = ""

    def userinfor(self):
        self.customer_name = input("Enter your name: ").title()
        self.customer_age = input("Enter your age: ")
        self.customer_gender = input("Enter your gender: ")
        self.customer_phone = input("Enter your phone number: ")

        print(f"\n✅ Welcome Mr./Ms. {self.customer_name}!")
        print(f"📋 Age: {self.customer_age} | Gender: {self.customer_gender} | Phone: {self.customer_phone}")
        print("\n➡️ Please choose your vegetable category below:")

    def wecome(self):
        print("\n🥕 Welcome to Om's VeggieMart!")

    def show_vegetables(self, veg_list, cat_name):
        print(f"\n🥗 Vegetables from {cat_name}:")
        for index, item in enumerate(veg_list, start=1):
            print(f"{index}. {item.name} - ₹{item.price}")

    def take_order(self, veg_list):
        while True:
            print("\n🛒 Choose the vegetable you want to order (enter 1006 to stop):")
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(veg_list):
                    selected_veg = veg_list[choice - 1]
                    quantity = int(input(f"Enter quantity for {selected_veg.name}: "))
                    self.order.append({
                        "name": selected_veg.name,
                        "price": selected_veg.price,
                        "quantity": quantity
                    })
                    print(f"✅ Added to order: {selected_veg.name} x {quantity}")
                elif choice == 1006:
                    print("✅ Order completed.\n")
                    break
                else:
                    print("❌ Invalid choice.")
            except ValueError:
                print("⚠️ Please enter a valid number.")

    def show_bill(self):
        if not self.order:
            print("\n🛑 No vegetables ordered.")
            return

        print("\n🧾 Order Summary:")
        print(f"👤 Customer Name: {self.customer_name}")
        print(f"📱 Phone Number: {self.customer_phone}")
        print(f"🧑 Age: {self.customer_age} | ⚧ Gender: {self.customer_gender}\n")

        total = 0
        for item in self.order:
            subtotal = item["quantity"] * item["price"]
            print(f"🥬 {item['name']} - ₹{item['price']} × {item['quantity']} = ₹{subtotal}")
            total += subtotal

        print(f"\n💰 Total Bill: ₹{total}")

    def category_choice(self):
        print("\n📦 Choose a vegetable category:")
        category = input("Enter your choice (1-6): ")
        if category == "1":
            self.show_vegetables(self.leafy_vegetables, "Leafy Vegetables")
            self.take_order(self.leafy_vegetables)
        elif category == "2":
            self.show_vegetables(self.root_vegetables, "Root Vegetables")
            self.take_order(self.root_vegetables)
        elif category == "3":
            self.show_vegetables(self.fruiting_vegetables, "Fruiting Vegetables")
            self.take_order(self.fruiting_vegetables)
        elif category == "4":
            self.show_vegetables(self.pod_vegetables, "Pod Vegetables")
            self.take_order(self.pod_vegetables)
        elif category == "5":
            self.show_vegetables(self.bulb_vegetables, "Bulb Vegetables")
            self.take_order(self.bulb_vegetables)
        elif category == "6":
            self.show_vegetables(self.stem_vegetables, "Stem Vegetables")
            self.take_order(self.stem_vegetables)
        else:
            print("❌ Invalid category choice.")


def main():
    print("\n🌽 Welcome to Om's VeggieMart — Your Fresh Veggie Destination! 🥦")
    category_menu = VegCategory()
    vegetable_shop = VegShow()

    vegetable_shop.userinfor()
    vegetable_shop.wecome()
    category_menu.show_categories()
    vegetable_shop.category_choice()
    vegetable_shop.show_bill()
    print("\n🙏 Thank you for shopping healthy with us! Stay fresh, stay fit! 🥗")


if __name__ == "__main__":
    main()
