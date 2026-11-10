import hashlib

# Variables you learnt
balance = 100
my_did = ""

# Function you learnt - Make DID from palm
def make_did(palm_data):
    palm_hash = hashlib.sha256(palm_data.encode()).hexdigest()
    did = "did:palm:" + palm_hash[:8]
    return did, palm_hash

# Function you learnt - Pay with if elif
def pay(balance, amount):
    if balance >= amount:
        balance = balance - amount
        print("Payment success! Paid", amount)
        print("New balance:", balance)
        return balance
    elif balance == 0:
        print("Balance is 0, cannot pay")
        return balance
    else:
        print("Not enough balance! You have only", balance)
        return balance

# Function you learnt - Verify palm with if else
def verify_palm(saved_hash, new_palm_data):
    new_hash = hashlib.sha256(new_palm_data.encode()).hexdigest()
    if new_hash == saved_hash:
        print("Palm matched! Real user")
        return True
    else:
        print("Palm NOT matched! Fake user")
        return False

# Test it
print("--- Step 1: Create DID ---")
my_did, my_hash = make_did("my_palm_photo")
print("Your DID:", my_did)

print("\n--- Step 2: Verify Palm ---")
is_real = verify_palm(my_hash, "my_palm_photo")

print("\n--- Step 3: Pay ---")
if is_real:
    balance = pay(balance, 10)
    balance = pay(balance, 200)  # This will fail, to test elif
else:
    print("Cannot pay, palm failed")