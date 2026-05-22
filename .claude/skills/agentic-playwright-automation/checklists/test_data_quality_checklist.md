# Test Data Quality Checklist

Apply per test data file or factory. Mark each item Pass, Fail, or Needs Review.

| Check | Status | Notes |
|---|---|---|
| Data is externalized to `automation/test_data/<environment>/` | | |
| Environment-specific data is stored in the matching environment folder | | |
| No private credentials, tokens, or PII are committed | | |
| Data shape aligns with a model in `framework/models/` | | |
| Stable IDs or names are used intentionally and documented | | |
| Generated-data strategy is documented next to the factory | | |
| Cleanup or reset requirements are identified next to the data | | |
