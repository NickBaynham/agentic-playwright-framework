"""Project logger.

Returns a module-scoped logger configured to stream to stderr at INFO. Test
code rarely needs to log; reserve for framework-level signals (settings
loaded, fixture lifecycle issues) rather than per-step narration.
"""

from __future__ import annotations

import logging
import sys

_CONFIGURED = False


def get_logger(name: str) -> logging.Logger:
    global _CONFIGURED
    if not _CONFIGURED:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
        )
        root = logging.getLogger()
        root.addHandler(handler)
        root.setLevel(logging.INFO)
        _CONFIGURED = True
    return logging.getLogger(name)
