import tomllib

with open("index.toml", "rb") as f:
    index = tomllib.load(f)

with open("pack.toml", "rb") as f:
    pack = tomllib.load(f)

mods = []
for mod_file in index["files"]:
    with open(mod_file["file"], "rb") as f:
        mod_file = tomllib.load(f)
    mods.append({
        "name": mod_file["name"],
        "filename": mod_file["filename"]
    })

print(f"Supported Minecraft version: {pack['versions']['minecraft']}\n");
print("Included mods:")
mods = sorted(mods, key=lambda mod: mod["name"])
for mod in mods:
    print(f"{mod['name']} (`{mod['filename']}`)")
