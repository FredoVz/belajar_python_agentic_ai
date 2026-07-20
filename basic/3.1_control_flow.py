# tier -> "premium", "basic", "free"
# service_price: int
# promo: str

# aturannya:
# apabila promo adalah LAUNCH50 -> mendapatkan potongan harga 50%
# apabila "tier" adalah "premium" -> mendapatkan potongan harga 30%
# apabila "tier" adalah "free" dan "service_price" di atas 0 -> tampilkan pesan "tidak bisa membeli layanan ini. Kamu harus upgrade"

# data sumber
tier: str = "premium"
promo: str = "LAUNCH50"
service_price: int = 299_999

final_price: int = service_price
message: str = "Tidak ada pesan"

if promo == "LAUNCH50":
    final_price = service_price * 0.5 # 50%
elif tier == "premium":
    final_price = service_price * 0.7 # mendaptkan potongan 30%
elif tier == "free" and service_price > 0:
    message = "tidak bisa membeli layanan ini. Kamu harus upgrade"
else:
    message = "kamu membeli dengan harga penuh"

tier_label: str = ""
match tier:
    case "basic":
        tier_label = "Basic"
    case "free":
        tier_label = "Free"
    case "premium":
        tier_label = "Premium"
    case _:
        tier_label = "Unknown"

print(message)
print(final_price)
print(tier_label)

# Cara debugging
# cd basic
# uv run 3.1_control_flow.py