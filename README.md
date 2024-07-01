# AWSume nuitka binary

Compiled down to a single binary by Nuitka to make installation simpler, does not rely on a flaky python
installation.

See scripts: `build_bin.sh` and `create_symlinks_example.sh` and see PR for diff against unstream; changes are minimal.

## Installation

- Put `awsume` shell script on path.
- Put `awsumepy` binary on path.
- Also symlink the binary to `awsume-configure`, `autoawsume`, and `awsume-autocomplete`.

The binary will detect from argv which entrypoint it's meant execute.

---

# AWSume: AWS Assume Made Awesome

Check out the documentation at [awsu.me](https://awsu.me)!
