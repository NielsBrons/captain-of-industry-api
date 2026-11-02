# Endpoint reference

[README](../README.md) · [Player-friendly command guide](command-guide.md) · [Technical command catalog](commands.md)

Generated route and parameter metadata is quoted from the live `/routes` capture. Explanatory notes distinguish observations from untested behavior.

## Common conventions

JSON resource responses observed here include `date` (game date string) and `tick` (simulation tick). Discovery arrays, images, HTML and early plain-text errors do not share that envelope. No pagination parameters were advertised. Product IDs and command proto IDs are case-sensitive identifiers; preserve their spelling. Select multiple IDs or series using comma-separated strings. Unknown query parameter names return 400 rather than being silently ignored.

Invalidate caches on session changes. A paused game can still change through commands without advancing tick, so tick alone is not a sufficient cache key while paused. Independent GETs are not proven to be an atomic cross-endpoint snapshot.

## Route inventory

| Method | Path | Advertised stage |
| --- | --- | --- |
| GET | `/api/v1/game-info` | Sim |
| GET | `/api/v1/icons/{id}` | Main |
| GET | `/api/v1/products` | Sim |
| GET | `/api/v1/products/history` | Sim |
| GET | `/api/v1/products/sources` | Sim |
| GET | `/api/v1/products/stats` | Sim |
| GET | `/api/v1/server-info` | Sim |
| POST | `/command` | Sync |
| GET | `/commands` | Sim |
| GET | `/demo-dashboard` | Background |
| GET | `/routes` | Background |
| GET | `/screenshot` | Main |

## GET /api/v1/game-info

Date, tick, pause state, speed, and the ids of the game and of the session. The ids are strings, gameId stays the same for a playthrough and sessionId changes with every start or load.

Advertised stage: `Sim`.

No path/query parameters advertised.

The IDs are opaque strings: do not coerce them to JavaScript numbers. `gameId` identifies the playthrough; `sessionId` changes on start/load. Clear cached catalogs/names/icons on session changes. `isPaused` and `speed` are separate fields. No game executable version is included.

## GET /api/v1/icons/{id}

PNG icon of a proto that has one, such as a product, machine, building or vehicle. 404 when the id is unknown or has no icon. Clients add 'v=<sessionId>' so the browser can cache icons until the next load, the server ignores it.

Advertised stage: `Main`.

| Parameter | Location | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `id` | path | `string` | Not advertised |  |

Returns PNG bytes, not JSON. Successful requests return `image/png`; unknown IDs return HTTP 404 with a JSON error. Append `?v=<sessionId>` to invalidate browser caches after loads; discovery says the server ignores v. URL-encode path IDs. Not every known proto necessarily has an icon. No icon assets are vendored here.

## GET /api/v1/products

Catalog of products with id, name, kind and isUnlocked. Without parameters all unlocked products sorted by name. 'ids' (comma-separated) gives these products in this order, 'pinned=true' the pinned ones, 'includeLocked=true' adds locked products. Unknown ids are listed in 'unknownIds'.

Advertised stage: `Sim`.

| Parameter | Location | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `ids` | query | `string` | `""` |  |
| `pinned` | query | `bool` | `false` |  |
| `includeLocked` | query | `bool` | `false` |  |

Without selection parameters, discovery says unlocked products sorted by name. Explicit `ids` preserves requested order; `pinned=true` selects the pinned catalog; `includeLocked=true` includes locked products. Catalog `products` is an array; stats/history/sources instead use an object keyed by ID. Observed kinds across the captured catalog: `countable`, `fluid`, `loose`, `molten`, `virtual`. Unknown IDs produce HTTP 200 with `unknownIds`, not a failure. Precedence for combined selection parameters was not tested.

## GET /api/v1/products/history

History of the unlocked products, or of 'ids' or 'pinned=true'. 'resolution' is day, month (default), year or quarterCentury. 'series' (comma-separated) defaults to produced,consumed, and to quantity,stored for resolution day, since only these two have days. 'count' is the number of finished periods, default 12. Each product has an array for every series with the finished periods from 'start', oldest first, then the period in progress.

Advertised stage: `Sim`.

| Parameter | Location | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `ids` | query | `string` | `""` |  |
| `pinned` | query | `bool` | `false` |  |
| `series` | query | `string` | `""` |  |
| `resolution` | query | `string` | `"month"` |  |
| `count` | query | `int` | `12` |  |

`count` counts finished periods; the server then appends the period in progress. Values are oldest first, aligned with `start`. Default month series are `produced,consumed`; default day series are `quantity,stored`. Discovery says only quantity/stored have daily history. Resolutions: `day`, `month`, `year`, `quarterCentury`. Use the returned `start` rather than assuming real-world quarter-century boundaries. The calendar used by the built-in web client has 30 days per month, 12 months per year and 25 years per quarter-century. Do not parse game dates as Gregorian dates. Bounds/clamping of count and every series/resolution combination were not tested.

## GET /api/v1/products/sources

Where products come from and go to, for the unlocked products, or for 'ids' or 'pinned=true'. Each side has a total and rows {type, quantity} sorted by quantity, recipe rows also have recipe and machine, entity rows have entity. 'period' is thisMonth, lastMonth (default), thisYear, lastYear or lifetime. 'names' has the names of the ids in the rows, a recipe without a name is named by its products.

Advertised stage: `Sim`.

| Parameter | Location | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `ids` | query | `string` | `""` |  |
| `pinned` | query | `bool` | `false` |  |
| `period` | query | `string` | `"lastMonth"` |  |

Periods: `thisMonth`, `lastMonth` (default), `thisYear`, `lastYear`, `lifetime`. Each product has `produced` and `consumed`, each containing `total` and `rows`. Recipe rows add `recipe` and `machine` IDs; entity rows add an `entity` proto/type ID, not an instance ID for a command. `names` maps IDs to display names. The built-in web client additionally recognizes import, fuel, export, construction and unknown row types; tolerate future types. Visible row quantities are not guaranteed to sum to `total`; the reason for observed differences was not established.

## GET /api/v1/products/stats

Current amounts and period totals of the unlocked products, or of 'ids' or 'pinned=true'. 'series' (comma-separated) picks the values, each product has a key for every series. A level is one number, a flow is [thisMonth, lastMonth, thisYear, lastYear, lifetime].

Advertised stage: `Sim`.

| Parameter | Location | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `ids` | query | `string` | `""` |  |
| `pinned` | query | `bool` | `false` |  |
| `series` | query | `string` | `"quantity,stored,storageCapacity,produced,consumed"` |  |

A level is a number. A flow is an array in the fixed order `[thisMonth, lastMonth, thisYear, lastYear, lifetime]`; it is not a time-series chart. `series` selects fields. The three level names are `quantity`, `stored`, `storageCapacity`. The built-in web client treats quantity as the current amount and stored/storageCapacity as storage data, and notes global buffers can exceed storage capacity. Exact inclusion of every buffer in quantity was not independently measured.

## GET /api/v1/server-info

Port of the server and which requests it accepts from web pages of other origins: none, get (every GET route) or getAndPost (also every POST route). Set by the console command web_api_start.

Advertised stage: `Sim`.

No path/query parameters advertised.

`port` is the game server port. `otherOrigins` is `none`, `get`, or `getAndPost` according to discovery. It describes cross-origin browser access, not listener binding or general client authentication.

## POST /command

Schedules an input command given as JSON { type, args } and returns its result. See /commands.

Advertised stage: `Sync`.

No path/query parameters advertised.

STATE-CHANGING. Not executed. Discovery advertises scheduling an input command and returning its result. The built-in web client sends a JSON object with `type` and an object of named `args`, with Content-Type application/json. Command-specific effects, result wrapping, failure codes, scheduling guarantees and behavior while paused remain unverified. See [command reference](commands.md).

## GET /commands

Lists the input commands that /command accepts in the current game.

Advertised stage: `Sim`.

| Parameter | Location | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `filter` | query | `string` | `""` | Only commands whose name contains this text are listed. |

The unfiltered capture contains 240 command types, with 244 constructor signatures. Each entry provides type, namespace, description, result and constructors. Many descriptions are empty: names alone are not a verified semantic specification. The catalog can depend on the current game/mods. Reading it does not execute commands.

## GET /demo-dashboard

Built-in interactive web client covering the /api/v1 routes.

Advertised stage: `Background`.

No path/query parameters advertised.

Returns text/html. Source was fetched and inspected, not executed in a browser. It demonstrates every /api/v1 route, polls game-info every 2000 ms and includes speed-changing POST buttons. The original HTML is not copied into this repository. The speed controls can change your game; do not treat this as a read-only page.

## GET /routes

Lists all routes and their parameters.

Advertised stage: `Background`.

No path/query parameters advertised.

Returns a JSON array of route objects. Fields: method, path, stage, description, params. Each parameter includes name/type/from, and may include default/description. The captured stages are Sim, Main, Sync and Background. These names are preserved verbatim; thread-safety or completion guarantees are not inferred from them. The default port is not advertised here, but is documented by the built-in web client and returned by server-info.

## GET /screenshot

Returns the current camera view as a JPG image.

Advertised stage: `Main`.

| Parameter | Location | Type | Default | Description |
| --- | --- | --- | --- | --- |
| `width` | query | `int` | `0` | Width in pixels, up to 4096. Zero means the width of the game window. |
| `height` | query | `int` | `0` | Height in pixels, up to 4096. Zero means the height of the game window. |

Returns the current camera view as JPEG bytes. Successful responses use `image/jpeg`. Zero dimensions request the game window dimensions; discovery advertises a maximum of 4096. Limit enforcement and aspect-ratio behavior were not tested.

## Series names

The server returned this allowed-values list in a 400 response for invalid stats/history series. This establishes recognized names, not successful support for every historical resolution:

- `quantity`
- `stored`
- `storageCapacity`
- `produced`
- `producedByBuildings`
- `producedByMining`
- `producedByRecycling`
- `producedByResearch`
- `producedBySettlements`
- `producedByImport`
- `producedByDeconstruction`
- `consumed`
- `consumedByConstruction`
- `consumedByMaintenance`
- `consumedBySettlements`
- `consumedByResearch`
- `consumedByFarms`
- `consumedByExport`
- `consumedAsFuel`
- `dumped`

Only quantity/stored/storageCapacity are levels in stats; the remaining advertised series use flow semantics according to the general route description. Component accounting identities were not tested.

## Error behavior

| Condition | HTTP | Response format |
| --- | --- | --- |
| Invalid parameter name, value or type | 400 | JSON with `error`, `parameter` and `message` |
| Unknown icon ID | 404 | JSON with `error` and `message` |
| Unknown route | 404 | Plain text |
| Rejected Host header | 403 | Plain text |

Always inspect Content-Type before JSON parsing. Host validation and unknown routes produced plain text; parameter and unknown-icon errors produced JSON. Common observed headers: Cache-Control: no-store, X-Content-Type-Options: nosniff, Connection: close. Do not assume status 200 implies browser CORS permission. Command errors were deliberately not tested.
