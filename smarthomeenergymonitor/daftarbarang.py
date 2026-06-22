daftar_barang = {
    "lampu led"     : 13,
    "tv"            : 70,
    "kulkas"        : 150,
    "kipas angin"   : 55,
    "mesin cuci"    : 400,
    "setrika"       : 650,
    "pompa air"     : 300,
    "dispenser"     : 250,
    "ac"            : 900,
    "rice cooker"   : 625,
    "blender"       : 300,
    "kompor listrik": 1500,
    "oven listrik"  : 1100,
    "microwave"     : 900,
    "laptop"        : 65,
    "komputer"      : 225,
    "charger hp"    : 10,
    "speaker"       : 120,
    "hair dryer"    : 650,
    "vacum cleaner" : 700
}

def tampilkan_daftar():
    print("\n=== DAFTAR BARANG ===")
    for i, (nama, watt) in enumerate(daftar_barang.items(), start=1):
        print(f"{i}. {nama} : {watt}W")
    print()