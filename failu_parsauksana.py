import os
mape = "rekini(originali)"
jauna_mape = "rekini(parsaukti)"
os.makedirs(jauna_mape, exist_ok=True)

for count, filename in enumerate(os.listdir(mape)):
    src = os.path.join(mape, filename)
    dst = os.path.join(jauna_mape, f"rekins_{str(count)}.pdf")
    os.rename(src, dst)