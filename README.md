kirijo-group Cobblemon Modpack
==============================

[packwiz][1] metadata for the modpack used on the Cobblemon server.

### Development

This repo uses a [Nix][2] flake to package the development environment (which
currently consists of packwiz and Python 3.11). [`nix develop`][3] can be used
to start a shell with these tools. This repo also contains an .envrc file for
use with [direnv][4].

#### Adding mods

Use [`packwiz curseforge install` and `packwiz modrinth install`][5] to add mods
to the packwiz metadata. CurseForge is preferred as a source as Modrinth mods
will have their JARs downloaded and included in the generated modpack zip.

Note that datapacks and resourcepacks may need special handling. They should be
placed in config/paxi/datapacks and config/data/resourcepacks respectively.
packwiz may not do this automatically. Make sure to check index.toml and correct
the paths if needed. See [this commit][6] for an example.

Make sure to run [`packwiz refresh`][7] after making manual modifications to the
packwiz TOML files. 

#### Creating a new release

You should create a release whenever you make changes to the packwiz TOML files.

After checking in your changes, bump the version in [pack.toml][8]. We follow
[semver][9], so bump the patch version if you're just correcting something in
the packwiz metadata or updating the mod versions. If you're adding a new mod,
bump the minor version.

Once that's done, [draft a new release][10]. Use `v${VERSION}` for the tag and
release title, where `${VERSION}` is the version specified in pack.toml. You
don't have to put anything in the description - the build action will take care
of generating it.

[1]: https://packwiz.infra.link/
[2]: https://github.com/NixOS/nix
[3]: https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html
[4]: https://direnv.net/
[5]: https://packwiz.infra.link/tutorials/creating/adding-mods/
[6]: https://github.com/kirijo-group/cobblemon-modpack/commit/83ba3aa3f1245b13074058b1cdfa3acaad8a4cdb
[7]: https://packwiz.infra.link/reference/commands/packwiz/refresh/
[8]: pack.toml
[9]: https://semver.org/
[10]: https://github.com/kirijo-group/cobblemon-modpack/releases/new
