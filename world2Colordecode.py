# 🌍 world2Color — Decode: 색상(hex) → 좌표
# by 권승현 & ChatGPT

def hex_to_rgb(hexcode):
    """#RRGGBB → (R,G,B)"""
    hexcode = hexcode.lstrip("#")
    if len(hexcode) != 6:
        raise ValueError("❌ Hex 색상은 #RRGGBB 형식이어야 합니다.")
    r = int(hexcode[0:2], 16)
    g = int(hexcode[2:4], 16)
    b = int(hexcode[4:6], 16)
    return (r, g, b)


def decode_color(c1, c2):
    """두 색상(hex 또는 RGB) → 위도/경도 복원"""
    # hex 문자열이면 RGB로 변환
    if isinstance(c1, str):
        c1 = hex_to_rgb(c1)
    if isinstance(c2, str):
        c2 = hex_to_rgb(c2)

    def to_val(rgb):
        return (rgb[0] << 16) + (rgb[1] << 8) + rgb[2]

    total = (to_val(c2) << 24) | to_val(c1)

    lat_val = total & 0xFFFFFF
    lon_val = (total >> 24) & 0xFFFFFF

    lat_n = lat_val / (2**24 - 1)
    lon_n = lon_val / (2**24 - 1)

    lat = lat_n * 360 - 180
    lon = lon_n * 360 - 180

    return round(lat, 6), round(lon, 6)

if __name__ == "__main__":
    print("🌍 world2Color — Decode (색상 → 좌표)")
    print("----------------------------------")

    hex1 = input("Color 1 (#RRGGBB): ").strip()
    hex2 = input("Color 2 (#RRGGBB): ").strip()

    lat, lon = decode_color(hex1, hex2)
    print(f"\n🧭 복원된 좌표: 위도 {lat}°, 경도 {lon}°")