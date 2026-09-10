with open("org.pbm", "rb") as f:
    data = f.read()

header_end = data.find(b"\n", data.find(b"\n") + 1) + 1

pixel_data = data[header_end:]

with open("org.x", "wb") as f:
    f.write(pixel_data)

print("Header size:", header_end)
print("Pixel data size:", len(pixel_data))