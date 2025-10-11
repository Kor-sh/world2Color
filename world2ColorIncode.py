def incode_color(lat, lon):
    """위도/경도를 색상 2개로 인코딩"""
    lat = (lat + 180) % 360
    lon = (lon + 180) % 360

    lat_n = lat / 360
    lon_n = lon / 360

    lat_val = int(lat_n * (2**24 - 1))
    lon_val = int(lon_n * (2**24 - 1))

    total = (lon_val << 24) | lat_val

    color1 = total & 0xFFFFFF
    color2 = (total >> 24) & 0xFFFFFF

    def to_rgb(v):
        return ((v >> 16) & 255, (v >> 8) & 255, v & 255)

    return to_rgb(color1), to_rgb(color2)


def rgb_to_hex(rgb):
    """(R,G,B) → #RRGGBB"""
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

if __name__ == "__main__":
    print("🌍 world2Color — Encode (좌표 → 색상)")
    print("----------------------------------")

    lat = float(input("위도는?: "))
    lon = float(input("경도는?: "))

    color1, color2 = incode_color(lat, lon)
    hex1 = rgb_to_hex(color1)
    hex2 = rgb_to_hex(color2)

    print(f"\n🎨 Color 1: {hex1}")
    print(f"🎨 Color 2: {hex2}")