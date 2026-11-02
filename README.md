# Captain of Industry — Web API guide

Unofficial, standalone documentation for the Web API exposed by Captain of Industry. It combines captured API metadata, observed read-only responses and explicitly labeled explanations of untested command behavior.

## Start here

- [Endpoint reference](docs/endpoints.md): all 12 routes, parameters, defaults, response semantics and error behavior.
- [Player-friendly command guide](docs/command-guide.md): plain-English descriptions of all 240 commands, grouped by gameplay area, with input explanations and uncertainty notes.
- [Technical command reference](docs/commands.md): all 244 constructor signatures, including exact parameter names, defaults, JSON hints and enum metadata.
- [Raw route catalog](discovery/routes.json) and [raw command catalog](discovery/commands.json).

## Quick start

Use a running game with its Web API enabled. The default local address is `http://localhost:3073`. Discover available routes at `/routes` and command metadata at `/commands`.

Use the endpoint reference to read product catalogs, current amounts, histories and production/consumption sources. Before using `POST /command`, read the [request format and cautions](docs/commands.md#request-format-and-cautions), back up your save and check the live command metadata. Do not expose write access to untrusted clients.

## Scope and stability

The captured discovery catalogs contain 12 routes and 240 command types (244 constructor signatures). All 11 GET route patterns were exercised during the original capture; no POST command was sent. Discovery metadata is specific to that game/session and its installed content. Game build/version was not exposed by the inspected metadata, so this is not an exhaustive reference for every release or mod setup.

`/api/v1/...` routes are versioned; `/command`, `/commands`, `/routes`, `/screenshot` and `/demo-dashboard` are outside that prefix. Treat the live `/routes` and `/commands` as authoritative after updating the game or changing mods.

Command identifiers and technical metadata are preserved from discovery. Most command effects are inferred from names and namespaces, not verified by execution. Descriptions, defaults and result types advertised by the game do not establish actual HTTP result envelopes or every side effect; the guides retain those limits explicitly.

## Validate the documentation

Python 3 standard library only:

```sh
python3 tools/validate.py
```

This checks discovery counts, route and command parameter coverage, constructor metadata, relative Markdown links, JSON catalog syntax and excluded assets. It does not contact the game or execute commands.

## Sources

Primary evidence is the game's captured `/routes`, `/commands`, read-only responses and inspected source of the built-in web client. Background announcement: [Captain's Diary #57](https://coigame.com/Blog/cd-57). This repository is unofficial and is not affiliated with the game developers. No license is asserted over game-provided descriptions or metadata.
