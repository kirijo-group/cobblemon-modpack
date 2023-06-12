import tomllib

with open("index.toml", "rb") as f:
    index = tomllib.load(f)

with open("pack.toml", "rb") as f:
    pack = tomllib.load(f)

mods = {}
for mod_file in index["files"]:
    with open(mod_file["file"], "rb") as f:
        mod_file = tomllib.load(f)
    mods[mod_file["name"]] = mod_file["filename"]

print(f"Supported Minecraft version: {pack['versions']['minecraft']}\n");
print("Included mods:")
mods = dict(sorted(mods.items()))
for k, v in mods.items():
    print(f"- {k} (`{v}`)")
