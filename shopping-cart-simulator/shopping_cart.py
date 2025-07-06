# 🛒 Shopping Cart Simulator
# A menu-driven application for managing a shopping cart

cart_items = []

# 🧾 Display the main menu options
def display_main_menu():
    print("\n======= 🛒 Welcome to the Orders_By_Online App 🛒 =======")
    print("Here is the 📃 Menu you can select from:\n")
    print("1️⃣  Add Item to Cart")
    print("2️⃣  Remove Item from Cart")
    print("3️⃣  View Cart Contents")
    print("4️⃣  Clear the Cart")
    print("5️⃣  Cart Summary")
    print("6️⃣  Exit\n")

# ➕ Add an item to the cart
def add_item():
    try:
        item = input("🛍️  Enter the item to add to the cart: ").strip()

        if not item:
            print("⚠️  Item name cannot be empty.")
        elif item.isdigit():
            print("⚠️  Item name should not be a number only. Please enter a valid item name (e.g., 'apple', 'milk').")
        else:
            cart_items.append(item)
            print(f"✅ '{item}' has been added to your cart.")
    except Exception as e:
        print("❌ Something went wrong while adding the item:", e)


# ➖ Remove an item from the cart
def remove_item():
    try:
        item = input("🗑️  Enter the item to remove from the cart: ").strip()
        cart_items.remove(item)
        print(f"✅ '{item}' has been removed from your cart.")
    except ValueError:
        print(f"❌ '{item}' was not found in your cart.")
    except Exception as e:
        print("❌ An unexpected error occurred:", e)

# 👀 View all items in the cart
def view_cart():
    if not cart_items:
        print("🧺 Your cart is currently empty.")
    else:
        print("🧾 Your cart contains the following items:")
        for idx, item in enumerate(cart_items, start=1):
            print(f"  {idx}. {item}")

# ❌ Clear all items in the cart
def clear_cart():
    cart_items.clear()
    print("🧹 Your cart has been cleared successfully.")

# 📊 Show a summary of the cart
def cart_summary():
    print(f"📦 Total items in your cart: {len(cart_items)}")
    if cart_items:
        print("📋 Items:")
        for idx, item in enumerate(cart_items, start=1):
            print(f"  {idx}. {item}")
    else:
        print("🛒 Your cart is empty.")

# 🎮 Handle option selection logic
def handle_option_selection(option):
    if option == 1:
        add_item()
    elif option == 2:
        remove_item()
    elif option == 3:
        view_cart()
    elif option == 4:
        clear_cart()
    elif option == 5:
        cart_summary()

# 🔢 Safely get the user's menu selection
def get_user_option():
    while True:
        try:
            choice = int(input("👉 Enter your option (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("⚠️  Please choose a number between 1 and 6.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

# 🚀 Main function to start the app
def main():
    while True:
        display_main_menu()
        option = get_user_option()
        if option == 6:
            print("👋 Thank you for shopping with us! Come again.\n")
            break
        handle_option_selection(option)

# Entry point
if __name__ == "__main__":
    main()