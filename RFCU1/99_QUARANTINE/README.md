# RFCU1 Quarantine

This directory stores historical, experimental, failed, contaminated, superseded, or otherwise noncanonical artifacts that must remain inspectable but cannot enter an active parent path.

Quarantined classes include:

- old failed numerical states and scores;
- contaminated packets or runs exposed to public targets before freeze;
- obsolete scalar or compressed proxies;
- repair outputs that changed the object being scored;
- exploratory fitted or retuned packets;
- failed runs and diagnostic branches;
- superseded schemas, symbols, and run plans;
- artifacts whose hashes, provenance, environment, or source authority cannot be verified.

## No-import rule

A quarantine artifact may inform diagnosis or design lessons, but it may not become an upstream numerical or physical input.

A prior successful artifact can leave quarantine only through a new clean replay that independently reproduces the result under the active architecture, passes all source and forbidden-input checks, and is promoted through a protected pull request. The old artifact itself remains historical.
