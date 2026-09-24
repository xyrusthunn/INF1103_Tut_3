def get_valid_input():
    user_entry = input("Input quantity (or type 'quit' to finish): ").strip()
    if user_entry.lower() == 'quit':
        return 'quit'
    elif not user_entry.isdigit():
        print("Invalid input. Please enter a valid integer number.")
        return None
    elif user_entry.startswith('-'):
        print("Invalid input. Please enter a valid integer number.")
        return None
    else:
        return user_entry

def process_delivery(running_total, delivery_cost):
    running_total += delivery_cost
    return running_total

def calculate_tax(base_amount):
    return base_amount * 0.1

def float_valid_input():
    user_entry = input("Input delivery amount: ").strip()
          
    try:
        parsed_amount = float(user_entry)
        
        if parsed_amount < 0:
            print("Invalid input. Please enter a valid amount.")
            return None
            
        return parsed_amount
        
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return None

def generate_report(sum_units, error_count, delivery_count, grand_total):
    print("\nInventory Audit Report")
    print("============================")
    print(f"Total Unit Quantity: {sum_units}")
    print(f"Total Deliveries Processed: {delivery_count}")   
    print(f"Total Amount including Tax: {grand_total}")
    print(f"Failed Attempts: {error_count}")
    return True


stock_qty = 0
invalid_attempts = 0
financial_total = 0
processed_count = 0


print("Inventory Audit System")
print("----------------------")

while True:
    input_status = get_valid_input()
    if input_status == 'quit':
        generate_report(stock_qty, invalid_attempts, processed_count, financial_total)
        break
    elif input_status is None:
        invalid_attempts += 1
    elif input_status is not None:
        projected_capacity = int(input_status) + stock_qty
        if projected_capacity > 500:
            print("Maximum inventory limit reached. Cannot add more units.")
            invalid_attempts += 1
            break
        processed_count += 1
        stock_qty += int(input_status)
        while True:
            validated_fee = float_valid_input()
            if validated_fee is None:
                invalid_attempts += 1
            elif validated_fee is not None:
                break
        
        financial_total = process_delivery(financial_total, validated_fee)
        financial_total += calculate_tax(validated_fee)