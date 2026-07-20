if True:
    # logika program, proses yang lain
    print("contoh penggunaan keyword if")

# 10 > 9 -> True / False?
# 10 == 9 -> True / False?
# 10 < 9 -> True / False?

# if else
model_name: str = "gemini-3.5-pro"
if model_name == "gemini-3.5-flash":
    print("model dikenali")
else:
    print("model tidak dikenali")

# if  elif elif else
price: int = 10_000
service_tier: str = ""

# price di antara 1000 dan 2000 -> service tier itu adalah basic
# price di antara 2000 dan 5000 -> service tier itu adalah premium
# price lebih dari 5000 -> service tier itu adalah platinum
# price di luar ini -> service tier itu adalah free

if price >= 1000 and price <= 2000:
    service_tier = "basic"
elif price >= 2000 and price <= 5000:
    service_tier = "premium"
elif price > 5000:
    service_tier = "platinum"
else:
    service_tier = "free"


print(service_tier)

service_label: str = ""
match service_tier:
    case "basic":
        service_label = "Basic"
    case "premium":
        service_label = "Premium"
    case "platinum":
        service_label = "Platinum"
    case "free":
        service_label = "Free"
    case _:
        service_label = "Unknown"

print(service_label)

# Cara debugging
# cd basic
# uv run 3_control_flow.py