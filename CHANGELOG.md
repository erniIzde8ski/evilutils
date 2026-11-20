# Changelog

## v0.2.0

Breaking changes:

- Shuffled & remodularized `eviltyping`. Imports directly from `eviltyping`
  should still be preserved.

Major changes:

- Added `Setter`, `Destructor` types to `eviltypes`.
- Added CHANGELOG.md file.
- Added `evilstructs` module & `evilstructs.frozendict` class.
- Added `evildatetime` module.
- Added `evilrng` module.

## v0.3.0, 2026-09-28

Breaking changes:

- Renamed `evildatetime.TimeDelta` to `evildatetime.Duration`. The `TimeDelta`
  alias is deprecated & scheduled for future removal.

## v0.3.1-alpha1, 2026-09-28

Internal changes only. See `v0.3.0` for changes from `v0.2.0`.

## v0.3.1-alpha2, 2026-11-20

- `evildatetime`:
  - Add methods to class `Duration`: `from_seconds`, `from_milliseconds`
  - Add `Seconds` class.
- Add `evilaio` module

## master (unreleased)

- `evilaio`:
  - Add `to_thread`, `to_threaded` function & decorator
- Bump minimum Python to 3.13
