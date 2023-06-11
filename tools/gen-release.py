import tomllib

with open("index.toml", "rb") as f:
    index = tomllib.load(f)

with open("pack.toml", "rb") as f:
    pack = tomllib.load(f)

print(f"Supported Minecraft version: {pack['versions']['minecraft']}\n");
print("Included mods:")

for mod_file in index["files"]:
    with open(mod_file["file"], "rb") as f:
        mod_file = tomllib.load(f)
    print(f"- {mod_file['name']} ({mod_file['filename']})")
