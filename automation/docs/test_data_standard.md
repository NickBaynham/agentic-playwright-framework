# Test Data Standard

## Location

- All test data lives under `test_data/<environment>/` as YAML.
- Each environment's folder is independent; do not share files across `local`, `dev`, and `qa`.
- The active environment is selected by `APP_ENV` (default `local`). The data loader receives the resolved `test_data_path` from `config.settings`.

## Shape

- Use top-level dictionaries grouping data by domain: `users`, `products`, `checkout_customers`.
- Match keys to fixture names where possible (`users.standard_user` is read by the `standard_user` fixture).

## Models

- Loaders return dataclass instances from `framework/models/`.
- Add a new model only when a domain entity needs structured access in tests.

## Secrets

- Do not commit private credentials, tokens, or PII.
- Public demo credentials are acceptable when the application publishes them.
- Use environment variables for any value that must not be checked in.

## Generated data

- Use `framework/data/factories.py` when a test needs a unique instance (e.g., a one-off customer).
- Mark generated values so they are distinguishable from seed data (the existing `make_checkout_customer` appends a UUID fragment to the last name).
- Document cleanup or reset requirements next to the data file when applicable.

## Versioning

- Treat test data files as part of the spec. When the source BDD spec or exploration report changes, update test data in the same change set.
