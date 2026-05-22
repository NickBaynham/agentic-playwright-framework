# Fixture Quality Checklist

Apply per PyTest fixture. Mark each item Pass, Fail, or Needs Review.

| Check | Status | Notes |
|---|---|---|
| Fixture purpose is clear from name and signature | | |
| Fixture name describes the resource (not the action) | | |
| Fixture scope is appropriate (`function` by default; broaden only when safe) | | |
| Fixture avoids unnecessary magic (no autouse unless justified, no deep indirection) | | |
| No secrets are baked into the fixture body | | |
| Composed fixtures remain readable; a test should be understandable without reading three layers | | |
| Fixture is reused across tests rather than duplicated | | |
