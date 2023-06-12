kirijo-group Cobblemon Modpack
==============================

[packwiz][1] metadata for the modpack used on the Cobblemon server.

### Usage

Download the modpack ZIP from the [latest release][2]. The modpack can be
installed with launchers such as [Prism Launcher][3] or [CurseForge][4].

### Development

This repo uses a [Nix][5] flake to package the development environment (which
currently consists of packwiz and Python 3.11). [`nix develop`][6] can be used
to start a shell with these tools. This repo also contains an .envrc file for
use with [direnv][7].

#### Adding mods

Use [`packwiz curseforge install` and `packwiz modrinth install`][8] to add mods
to the packwiz metadata. CurseForge is preferred as a source as Modrinth mods
will have their JARs downloaded and included in the generated modpack zip.

Note that datapacks and resourcepacks may need special handling. They should be
placed in config/paxi/datapacks and config/data/resourcepacks respectively.
packwiz may not do this automatically. Make sure to check index.toml and correct
the paths if needed. See [this commit][9] for an example.

Make sure to run [`packwiz refresh`][10] after making manual modifications to the
packwiz TOML files. 

#### Creating a new release

You should create a release whenever you make changes to the packwiz TOML files.

After checking in your changes, bump the version in [pack.toml][11]. We follow
[semver][12], so bump the patch version if you're just correcting something in
the packwiz metadata or updating the mod versions. If you're adding a new mod,
bump the minor version.

Once that's done, [draft a new release][13]. Use `v${VERSION}` for the tag and
release title, where `${VERSION}` is the version specified in pack.toml. You
don't have to put anything in the description - the build action will take care
of generating it.

[1]: https://packwiz.infra.link/
[2]: https://github.com/kirijo-group/cobblemon-modpack/releases/latest
[3]: https://prismlauncher.org/wiki/getting-started/download-modpacks/
[4]: https://support.curseforge.com/en/support/solutions/articles/9000196984-installing-modpacks
[5]: https://github.com/NixOS/nix
[6]: https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-develop.html
[7]: https://direnv.net/
[8]: https://packwiz.infra.link/tutorials/creating/adding-mods/
[9]: https://github.com/kirijo-group/cobblemon-modpack/commit/83ba3aa3f1245b13074058b1cdfa3acaad8a4cdb
[10]: https://packwiz.infra.link/reference/commands/packwiz/refresh/
[11]: pack.toml
[12]: https://semver.org/
[13]: https://github.com/kirijo-group/cobblemon-modpack/releases/new
