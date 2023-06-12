kirijo-group Cobblemon Modpack
==============================

[packwiz][1] metadata for the modpack used on the Cobblemon server.

### Development

#### Creating a new release

You should create a release whenver you make changes to the packwiz TOML files.

After checking in your changes, bump the version in [pack.toml][2]. We follow
[semver][3], so bump the patch version if you're just correcting something in
the packwiz metadata or updating the mod versions. If you're adding a new mod,
bump the minor version.

Once that's done, [draft a new release][4]. Use `v${VERSION}` for the tag and
release title, where `${VERSION}` is the version specified in pack.toml. You
don't have to put anything in the description - the build action will take care
of generating it.

[1]: https://packwiz.infra.link/
[2]: pack.toml
[3]: https://semver.org/
[4]: https://github.com/kirijo-group/cobblemon-modpack/releases/new
