# Captain of Industry commands — a player-friendly guide

[README](../README.md) · [Technical command catalog](commands.md) · [HTTP endpoint reference](endpoints.md)

This guide explains all 240 command types in the captured catalog, grouped by gameplay area. Each entry gives a plain-English purpose, explains its inputs, and links to exact constructor signatures and JSON types. The catalog includes 244 constructor signatures; entries with overloads discuss the alternatives.

## What is confirmed and what is inferred

The command names, argument names, defaults, JSON hints and any game-provided descriptions come from the captured [live command metadata](../discovery/commands.json). Most commands have no game-provided description. Their explanations below are explicitly inferred from names, argument types and namespaces, not verified by running the commands. Group placement is editorial, not an API classification. Read an inferred explanation as an aid to understanding, not a guarantee of in-game behavior.

No commands were executed to write or validate this guide. Costs, eligibility, side effects, index bounds, priority ordering and null behavior are unknown unless specifically identified as game-provided metadata. Internal-looking commands may not be useful standalone. Back up your save before experimenting.

## How to read the inputs

- An entity ID identifies an existing instance in your save; a prototype ID identifies a kind of product, building, vehicle or recipe. They are not interchangeable.
- Train IDs, logistics-zone IDs, schedule indices and other identifiers refer to the relevant game objects. The inspected routes do not provide a complete lookup for every ID needed here.
- A toggle changes the current state. Retrying it can undo the previous change. Prefer a command with an explicit true/false state when one exists and is appropriate.
- A nullable argument and an argument with a declared default are different concepts. Neither establishes that omission is safe, nor what null means. Some game-specific `OrNone` IDs are encoded as integers, not JSON null.
- Use the linked technical reference for exact JSON encodings and enum values. Do not assume every slider accepts a percentage, every priority uses the same ordering, or every index starts at the same value.
- Inputs are named members of the `args` object in `POST /command`, not positional arguments. The `type` field selects the command. See [request format and cautions](commands.md#request-format-and-cautions) before sending requests.

## Browse by gameplay area

- [Ships, exploration, trade and loans](#ships-exploration-trade-and-loans) — 29 commands
- [Trains, stations and rail networks](#trains-stations-and-rail-networks) — 69 commands
- [Rockets, asteroids and the space station](#rockets-asteroids-and-the-space-station) — 15 commands
- [Terrain, decoration and bridges](#terrain-decoration-and-bridges) — 5 commands
- [Factories, power and transports](#factories-power-and-transports) — 31 commands
- [Vehicles and logistics zones](#vehicles-and-logistics-zones) — 31 commands
- [Farming, animals and forestry](#farming-animals-and-forestry) — 13 commands
- [Storage and product handling](#storage-and-product-handling) — 10 commands
- [Buildings, construction and priorities](#buildings-construction-and-priorities) — 25 commands
- [Game controls, research and notifications](#game-controls-research-and-notifications) — 12 commands

## Ships, exploration, trade and loans

### AcceptLoanCmd
Borrow a product for a chosen term

Inferred from the names, this accepts a loan for a specified quantity of a product over a chosen number of years. It is the borrowing action, rather than a way to inspect loan terms; interest and repayment rules are not documented here.

Inputs: `product` identifies what to borrow, `toBorrow` gives the quantity, and `yearsTotal` gives the loan duration in years. [Parameters and JSON types](commands.md#acceptloancmd).

### CargoDepotSetFuelSliderStepCmd
Adjust a cargo depot's fuel import and export settings

Inferred from the names, this changes a cargo depot's fuel settings using separate import and export slider steps. The parameter descriptions say a negative step means undefined, but do not explain the operational effect of undefined settings or nullable values.

Inputs: `cargoDepotId` identifies the depot; `importStep` supplies the import step and `exportStep` supplies the export step. Both steps accept null and declare null defaults, and both carry the game-provided note “Negative if undefined.” [Parameters and JSON types](commands.md#cargodepotsetfuelsliderstepcmd).

### CargoShipReplaceFuelCmd
Change a cargo ship's fuel selection

Inferred from the names, this requests replacement of a cargo ship's fuel with a specified product. Whether it changes a fuel configuration, handles existing onboard fuel, or both is not established by the catalog.

Inputs: `cargoShipId` identifies the ship and `fuelId` identifies the replacement fuel product. [Parameters and JSON types](commands.md#cargoshipreplacefuelcmd).

### FleetLoadCrewCmd
Request crew loading for the fleet

Inferred from the name, this requests loading crew for the fleet. No crew quantity, ship, or location is supplied, so the catalog does not establish how many crew are loaded or which fleet-state conditions are required.

Inputs: none. [Parameters and JSON types](commands.md#fleetloadcrewcmd).

### FleetModificationsCancelCmd
Cancel fleet modifications

Inferred from the name, this cancels fleet modifications. It appears to act on the current modification process rather than select a particular component; the affected work and any resource recovery are undocumented.

Inputs: none. [Parameters and JSON types](commands.md#fleetmodificationscancelcmd).

### FleetToggleAutoReturnCmd
Toggle the fleet's automatic-return setting

Inferred from the name, this switches automatic return for the fleet between its current alternatives. It does not specify a destination or an explicit enabled state, and the circumstances that trigger an automatic return are undocumented.

Inputs: none. [Parameters and JSON types](commands.md#fleettoggleautoreturncmd).

### FleetUnloadCrewCmd
Request crew unloading from the fleet

Inferred from the name, this requests unloading the fleet's crew. It does not take a quantity or destination, so the catalog does not establish how many crew leave or where unloading is permitted.

Inputs: none. [Parameters and JSON types](commands.md#fleetunloadcrewcmd).

### FleetUnloadFuelCmd
Request fuel unloading from the fleet

Inferred from the name, this requests unloading fuel from the fleet. It provides neither a product choice nor an amount, so the destination, quantity, and required fleet state remain undocumented.

Inputs: none. [Parameters and JSON types](commands.md#fleetunloadfuelcmd).

### GoToLocationCmd
Request a world-map visit for a chosen purpose

Inferred from the world namespace and visit-reason argument, this requests travel to a world-map location for a stated purpose. It should not be assumed to be camera navigation; route selection, travel requirements, and arrival behavior are not documented.

Inputs: `id` identifies the world-map location and `reason` selects `General`, `LoadCargo`, or `DeliverCargo`. [Parameters and JSON types](commands.md#gotolocationcmd).

### MakeLoanOverpaymentCmd
Request an extra payment on a loan

Inferred from the names, this makes an additional payment toward a selected product loan. It appears intended to pay beyond the ordinary repayment process, but effects on future payments, interest, and completion are not documented.

Inputs: `product` identifies the loan product, `loanId` selects the loan, and `toPay` gives the quantity to pay. [Parameters and JSON types](commands.md#makeloanoverpaymentcmd).

### NotifyOnBattleOpenedCmd
Undocumented battle-open notification

The name suggests an internal notification that a battle has been opened, but the catalog does not explain what receives it or what changes. Do not interpret it as a documented command to start combat or open a battle view.

Inputs: none. [Parameters and JSON types](commands.md#notifyonbattleopenedcmd).

### QuickTradeCmd
Request a predefined quick trade

Inferred from the name and namespace, this requests one of the game's quick trades. The command selects an existing trade definition rather than supplying custom quantities or exchange terms.

Inputs: `tradeId` identifies the trade prototype to request.

[Parameters and JSON types](commands.md#quicktradecmd)

### RecoverShipCmd
Request recovery of a ship

Inferred from the name, this requests recovery of a particular ship. It may be relevant when a ship needs recovery, but the catalog does not explain its destination, movement, or recovery conditions.

Inputs: `shipId` identifies the ship entity.

[Parameters and JSON types](commands.md#recovershipcmd)

### SetLoanBufferPriorityCmd
Set a loan buffer's priority

Inferred from the names, this changes the priority of a buffer associated with a loan. It appears relevant to loan-related product handling, but which handling operations use this priority is not explained.

Inputs: `loanId` identifies the loan; `priority` supplies its buffer priority value. The priority scale is undocumented.

[Parameters and JSON types](commands.md#setloanbufferprioritycmd)

### SetShiftsCountForMineCmd
Set a world mine's shift count

Inferred from the names and world-entity namespace, this changes the number of shifts assigned to a mine. It appears intended to adjust mine operation, but the catalog does not specify allowed counts or their effects on output and requirements.

Inputs: `entityId` identifies the mine entity; `shiftsCount` supplies the requested number of shifts.

[Parameters and JSON types](commands.md#setshiftscountforminecmd)

### ShipayardSetFuelSliderStepCmd
Adjust a shipyard's fuel import and export settings

Inferred from the names, this changes the step-based fuel import and export settings of a shipyard. The command's exact identifier contains `Shipayard`, which must be preserved even though the argument refers to a shipyard.

Inputs: `shipyardId` identifies the shipyard. `importStep` and `exportStep` are nullable integer steps, each defaulting to null; their descriptions say a negative value means undefined, but do not explain null separately.

[Parameters and JSON types](commands.md#shipayardsetfuelsliderstepcmd)

### ShipyardDiscardProductCmd
Discard a product at a shipyard

Inferred from the names, this requests discarding a selected product at a shipyard. Because there is no quantity input, the catalog does not establish how much is removed or whether any recovery is possible.

Inputs: `shipyardId` identifies the shipyard. `productId` identifies the product to discard.

[Parameters and JSON types](commands.md#shipyarddiscardproductcmd)

### ShipyardMakePrimaryCmd
Designate a primary shipyard

Inferred from the names, this makes the selected shipyard the primary one. The catalog does not describe which activities follow that designation or what happens to the previous primary shipyard.

Inputs: `shipyardId` identifies the shipyard to designate.

[Parameters and JSON types](commands.md#shipyardmakeprimarycmd)

### ShipyardSetRepairingCmd
Set a shipyard's repair activity

Inferred from the names, this explicitly enables or disables a shipyard's repairing state. It is not documented whether this applies to a particular ship or how repair work is scheduled.

Inputs: one overload takes only `isRepairing`, the requested repairing state; the target selection for that form is not documented. The other takes `shipyardId` to identify the shipyard and `isRepairing` to set its repairing state.

[Parameters and JSON types](commands.md#shipyardsetrepairingcmd)

### ShipyardToggleAutoRepairCmd
Switch automatic shipyard repairs on or off

Inferred from the names, this flips a shipyard's automatic-repair setting. It changes a policy rather than specifying a repair target or a fixed enabled state.

Inputs: `shipyardId` identifies the shipyard whose automatic-repair setting should be toggled.

[Parameters and JSON types](commands.md#shipyardtoggleautorepaircmd)

### ShipyardToggleUnloadPriorityCmd
Change a shipyard's unloading priority setting

Inferred from the names, this toggles unloading priority at a shipyard. The catalog does not specify what unloading takes priority over or how competing work is selected.

Inputs: `shipyardId` identifies the shipyard.

[Parameters and JSON types](commands.md#shipyardtoggleunloadprioritycmd)

### ShipyardToggleWorksPauseCmd
Pause or resume shipyard work

Inferred from the names, this toggles whether shipyard work is paused. The exact set of activities covered by “work” is not documented.

Inputs: one overload has no parameters, with no documented rule for selecting its shipyard. The other accepts `shipyardId` to target a particular shipyard.

[Parameters and JSON types](commands.md#shipyardtoggleworkspausecmd)

### ShipyardWorldEntityConstructionToggle
Toggle a shipyard's world-entity construction task

Inferred from the names, this toggles construction associated with a world entity at a shipyard. This is an ambiguous internal operation: the catalog does not establish whether toggling adds a task, pauses it, cancels it, or changes another construction state.

Inputs: `shipyardId` identifies the shipyard. `worldEntityIdToConstruct` identifies the world entity associated with the construction task.

[Parameters and JSON types](commands.md#shipyardworldentityconstructiontoggle)

### ToggleContractCmd
Switch a contract's active setting

Inferred from the names, this toggles a contract's state, plausibly its enabled status. The catalog does not describe whether this starts, pauses, or otherwise changes fulfillment, so those effects remain uncertain.

Inputs: `contractId` identifies the contract by prototype identifier.

[Parameters and JSON types](commands.md#togglecontractcmd)

### TradeDockToggleUnloadPriorityCmd
Change a trade dock's unloading priority

Inferred from the names, this toggles a trade dock's unloading-priority setting. The catalog does not specify what unloading takes precedence over or how that priority is enforced.

Inputs: `tradeDockId` identifies the trade dock.

[Parameters and JSON types](commands.md#tradedocktoggleunloadprioritycmd)

### WorldMapEntityCancelRepairCmd
Cancel a world-map entity's repair

Inferred from the names, this cancels repair associated with a world-map entity. The catalog does not describe material recovery, retained progress, or the conditions under which cancellation is accepted.

Inputs: `entityId` identifies the world-map entity.

[Parameters and JSON types](commands.md#worldmapentitycancelrepaircmd)

### WorldMapEntityStartRepairCmd
Start repairing a world-map entity

Inferred from the names, this requests repair of a world-map entity. The catalog does not specify prerequisites, required supplies, or repair duration.

Inputs: `entityId` identifies the world-map entity to repair.

[Parameters and JSON types](commands.md#worldmapentitystartrepaircmd)

### WorldMapEntityUpgradeCmd
Request a world-map entity upgrade

Inferred from the names, this requests an upgrade for a world-map entity. No target level is supplied, and the catalog does not establish the upgrade path, costs, or resulting capabilities.

Inputs: `entityId` identifies the world-map entity to upgrade.

[Parameters and JSON types](commands.md#worldmapentityupgradecmd)

### WorldMapSettlementAdoptPopsCmd
Request population adoption from a world-map settlement

Inferred from the names, this requests adopting a specified population count from a world-map settlement. The catalog does not state eligibility rules, destination, timing, or whether the requested count is always available.

Inputs: `entityId` identifies the settlement. `popsCount` supplies the integer population count to request.

[Parameters and JSON types](commands.md#worldmapsettlementadoptpopscmd)


## Trains, stations and rail networks

### AddEntityToScheduleItemCmd
Add a destination to an existing train schedule item

Inferred from the names, this adds an entity to an already existing item in a train line's schedule. It appears useful for adjusting the entities associated with that item without creating a new schedule entry; the meaning and ordering of priority values are undocumented.

Inputs: `scheduleItem` identifies the train line and schedule index, `entityId` identifies the entity to add, and `priority` supplies its priority. [Parameters and JSON types](commands.md#addentitytoscheduleitemcmd).

### AddNewScheduleItemToTrainLineCmd
Insert a train schedule entry

Inferred from the names, this creates a new schedule item on a train line with an associated entity and priority. The supplied parameter description explicitly says that a negative insertion index appends the item to the end of the schedule.

Inputs: `trainLineId` selects the line, `entityId` selects the associated entity, and `priority` supplies its priority. `index` chooses the insertion position and has a declared default of `-1`; negative values mean append. [Parameters and JSON types](commands.md#addnewscheduleitemtotrainlinecmd).

### AddTrainTrackPillarCmd
Add a support to a train track

Inferred from the names, this adds a pillar to a particular block of a track entity. It appears intended for track-support editing, but how block indices map to positions and when a pillar is permitted are undocumented.

Inputs: `entityId` identifies the track entity and `blockIdx` selects its block. [Parameters and JSON types](commands.md#addtraintrackpillarcmd).

### AssignTrainLineToTrainCmd
Give a train a line assignment

Inferred from the names, this assigns a train to a train line. The parameter description also explicitly allows unassignment using the game's None value, so it is not limited to adding an assignment.

Inputs: `trainId` selects the train and `trainLineId` selects its line or the game's None sentinel to unassign it. The advertised JSON type is integer; the description does not identify the sentinel's numeric encoding, so do not equate it with JSON null. [Parameters and JSON types](commands.md#assigntrainlinetotraincmd).

### AssignTrainLineToUnfinishedTrainCmd
Set a line assignment before a train is finished

Inferred from the names, this sets the line assignment of a train still represented by a depot queue entry. The parameter description explicitly allows the line to be unassigned using the game's None value; the role of the additional network ID is otherwise undocumented.

Inputs: `depotId` identifies the depot and `queueIndex` identifies the queued train. `trainLineId` selects a line or the game's None sentinel to unassign it, while `trainNetworkId` supplies the network ID and declares default `0`. Both line and network IDs are advertised as integers, not JSON null; the None encoding is not explained. [Parameters and JSON types](commands.md#assigntrainlinetounfinishedtraincmd).

### AssignTrainToNetworkCmd
Set a train's network assignment

Inferred from the names, this assigns a train to a train network. It controls network membership rather than specifying an individual travel destination; the consequences of changing networks are not documented.

Inputs: `trainId` identifies the train and `networkId` supplies its network assignment. The network type includes a None variant but is advertised as an integer; its sentinel encoding and effect are not specified. [Parameters and JSON types](commands.md#assigntraintonetworkcmd).

### CancelTrainBuildCmd
Cancel a queued train build

Inferred from the names, this cancels a train-build entry at a depot. It selects the queue entry rather than a completed train; material refunds and partially completed work are not documented.

Inputs: `depotId` identifies the depot and `queueIndex` selects its build-queue entry. [Parameters and JSON types](commands.md#canceltrainbuildcmd).

### CancelTrainJobCmd
Cancel a train's current job

Inferred from the names, this cancels a job associated with a train. It does not take a line or schedule ID, so it should not be read as a documented way to delete a line; subsequent routing and cargo handling are unknown.

Inputs: `trainId` identifies the train. [Parameters and JSON types](commands.md#canceltrainjobcmd).

### CancelTrainReplacementCmd
Cancel replacement of a train

Inferred from the names, this cancels a replacement operation for an existing train. It is distinct from canceling a depot build-queue entry, and the catalog does not describe how partially completed replacement is handled.

Inputs: `trainId` identifies the train whose replacement should be canceled. [Parameters and JSON types](commands.md#canceltrainreplacementcmd).

### CreateNewTrainLineCmd
Create a train line

Inferred from the name, this creates a new train line for subsequent configuration. No schedule or train assignment is supplied by this command, so the catalog does not establish any initial service pattern.

Inputs: none. [Parameters and JSON types](commands.md#createnewtrainlinecmd).

### CreateNewTrainNetworkCmd
Create a train network

Inferred from the name, this creates a new train network. It does not accept track boundaries, a name, or train members, so any initial configuration is unspecified.

Inputs: none. [Parameters and JSON types](commands.md#createnewtrainnetworkcmd).

### CreateTrainTrackEntityWithDirectionCmd
Create a track entity with a travel-direction setting

Inferred from the names, this creates a train-track entity with a specified placement and trajectory direction. It combines placement with direction configuration, but the catalog does not explain how each direction relates to the track's orientation or what `Unknown` does.

Inputs: `protoId` selects the entity definition, `transform` supplies position, rotation, and reflection, and `direction` is one of `Unknown`, `Forward`, `Backward`, or `Bidirectional`. [Parameters and JSON types](commands.md#createtraintrackentitywithdirectioncmd).

### NavigateTrainToCmd
Send a train toward an entity

Inferred from the names, this requests navigation of a train to a target entity. It specifies a destination rather than a new line assignment; whether it interrupts scheduled service and what happens on arrival are undocumented.

Inputs: `trainId` identifies the train and `targetEntityId` identifies its destination entity. [Parameters and JSON types](commands.md#navigatetraintocmd).

### QuickBuildCurrentTrainCmd
Request quick construction of the current train

Inferred from the name, this requests quick building of the train currently being handled by a depot. It targets the depot's current train rather than selecting a train design, and the catalog does not explain its resource requirements or completion rules.

Inputs: `depotId` identifies the train depot.

[Parameters and JSON types](commands.md#quickbuildcurrenttraincmd)

### QuickRepairTrainCmd
Request a quick train repair

Inferred from the names, this requests quick repair of a particular train using a selected product setting. The role of that product is not described, so the catalog does not establish whether it is a repair material or another repair-related choice.

Inputs: `trainId` identifies the train; `productId` identifies the product associated with the repair request.

[Parameters and JSON types](commands.md#quickrepairtraincmd)

### RecoverTrainCmd
Request recovery of a train

Inferred from the names, this requests train recovery with controls related to pausing and a destination depot. The catalog does not explain the recovery procedure or what happens when no target depot is supplied.

Inputs: `trainId` identifies the train; `forcePause` is the recovery's force-pause flag, advertised as defaulting to `false`; `targetDepot` is a depot entity ID or `null`, with an advertised default of `null`. The scope of the pause and the meaning of a null depot are unspecified.

[Parameters and JSON types](commands.md#recovertraincmd)

### RefuelTrainCmd
Request train refueling

Inferred from the name, this requests refueling for a selected train. It does not let you choose a fuel product or amount, and the catalog does not explain how refueling is carried out.

Inputs: `trainId` identifies the train to refuel.

[Parameters and JSON types](commands.md#refueltraincmd)

### RemoveDepartConditionCmd
Remove a train departure condition

Inferred from the names, this removes a condition from a train schedule entry's departure rules. Use it when revising the rules that govern departure; the exact condition grouping represented by the root ID is not documented.

Inputs: `scheduleItem` identifies the line and schedule position; `rootId` identifies the entity associated with the condition's root; `conditionIndex` selects the condition to remove.

[Parameters and JSON types](commands.md#removedepartconditioncmd)

### RemoveEntityFromScheduleItemCmd
Remove an entity from a train schedule entry

Inferred from the names, this removes an entity's association with one train schedule entry. It is a schedule edit, not a documented request to demolish the entity itself.

Inputs: `scheduleItem` identifies the train line and schedule position; `entityId` identifies the entity to remove from that entry.

[Parameters and JSON types](commands.md#removeentityfromscheduleitemcmd)

### RemovePathfindingRestrictionCmd
Remove a rail waypoint's routing restriction

Inferred from the names and train namespace, this removes one pathfinding restriction associated with a waypoint. Use it to revise rail routing constraints, without assuming how train routes will change afterward.

Inputs: `waypointId` identifies the waypoint entity; `restrictionIndex` selects the restriction to remove.

[Parameters and JSON types](commands.md#removepathfindingrestrictioncmd)

### RemoveTrainLineCmd
Remove a train line

Inferred from the name, this removes a train line definition. It is intended for reorganizing train services, but the catalog does not state what happens to trains assigned to the line.

Inputs: `trainLineId` identifies the line to remove.

[Parameters and JSON types](commands.md#removetrainlinecmd)

### RemoveTrainLineScheduleItemCmd
Remove an entry from a train line's schedule

Inferred from the names, this removes one scheduled entry from a train line. Use it to revise the line's itinerary rather than remove the whole line.

Inputs: `scheduleItem` identifies both the train line and the schedule entry's position.

[Parameters and JSON types](commands.md#removetrainlinescheduleitemcmd)

### RemoveTrainNetworkCmd
Remove a train network definition

Inferred from the name, this removes a train network definition. The catalog does not establish whether or how it changes assigned trains, stations, or physical track, so those consequences remain uncertain.

Inputs: `networkId` identifies the train network.

[Parameters and JSON types](commands.md#removetrainnetworkcmd)

### RemoveTrainTrackPillarCmd
Remove a rail support pillar

Inferred from the name, this requests removal of a train-track pillar. Use it when changing rail supports, but the catalog does not describe structural requirements or what happens to supported track.

Inputs: `pillarId` identifies the pillar entity.

[Parameters and JSON types](commands.md#removetraintrackpillarcmd)

### RenameTrainLineCmd
Rename a train line

Inferred from the names, this changes a train line's name. Use a descriptive name to distinguish services without requesting a schedule change.

Inputs: `trainLineId` identifies the line; `name` supplies its new name.

[Parameters and JSON types](commands.md#renametrainlinecmd)

### RenameTrainNetworkCmd
Rename a train network

Inferred from the names, this changes a train network's name. It is intended for identifying networks more clearly rather than editing their membership.

Inputs: `networkId` identifies the network; `name` supplies its new name.

[Parameters and JSON types](commands.md#renametrainnetworkcmd)

### ReorderDepartConditionCmd
Reorder a train departure condition

Inferred from the names, this moves a departure condition to a different position within a schedule entry's rules. It can help arrange those rules, but the catalog does not establish whether ordering changes their logical evaluation.

Inputs: `scheduleItemId` identifies the train line and schedule position; `rootId` identifies the entity associated with the condition root; `conditionIndex` selects the existing condition; `newConditionIndex` gives its destination position. The meaning of the root grouping is not explained.

[Parameters and JSON types](commands.md#reorderdepartconditioncmd)

### ReorderTrainLineScheduleItemCmd
Move an entry in a train line's schedule

Inferred from the names, this changes the position of an existing schedule entry. Use it to rearrange a train line's itinerary without requesting a new entry.

Inputs: `scheduleItem` identifies the line and the entry's current schedule position; `newIndex` supplies the requested destination position.

[Parameters and JSON types](commands.md#reordertrainlinescheduleitemcmd)

### ReplaceEntityInScheduleCmd
Substitute a station in train schedules

The argument description explicitly says this replaces a station in a selected schedule entry, or in every line when `scheduleItem` is `null`. This is useful when redirecting schedules to a replacement station; it does not describe physically replacing the station building.

Inputs: `scheduleItem` identifies a train line and schedule position, or is `null` to replace the station in every line; its advertised default is `null`. `oldEntityId` identifies the station being replaced, and `newEntityId` identifies its replacement.

[Parameters and JSON types](commands.md#replaceentityinschedulecmd)

### ScrapTrainCarCmd
Request scrapping of a train car type at a depot

Inferred from the names, this requests scrapping of a train car associated with a depot and a selected car type. It does not identify an individual car instance, so which matching car is affected and what scrapping returns are uncertain.

Inputs: `depotId` identifies the depot; `carProtoId` selects the train-car prototype.

[Parameters and JSON types](commands.md#scraptraincarcmd)

### SetArrivalRuleAlwaysAllowCmd
Set a station product's always-allow arrival flag

Inferred from the names, this changes an always-allow setting in a station's product-specific arrival rules. It appears intended to relax arrival gating for that product, but the catalog does not say which other rules it overrides.

Inputs: `stationId` identifies the station; `productId` selects the product; `alwaysAllow` enables or disables the always-allow flag.

[Parameters and JSON types](commands.md#setarrivalrulealwaysallowcmd)

### SetArrivalRuleNetworkPriorityCmd
Set network priority for a station's product arrival rule

Inferred from the names, this changes a product-specific arrival rule's network priority at a station. It is a way to express relative importance, but neither the priority scale nor which numeric direction is more important is documented.

Inputs: `stationId` identifies the station; `productId` selects the product; `priority` supplies the priority value.

[Parameters and JSON types](commands.md#setarrivalrulenetworkprioritycmd)

### SetArrivalRuleNetworkThresholdCmd
Set a station product's network arrival threshold

Inferred from the names, this changes the network threshold used by a station's arrival rule for a product. The catalog does not explain what quantity the percentage measures or how crossing it affects arrivals.

Inputs: `stationId` identifies the station; `productId` selects the product; `threshold` supplies the percentage as a fraction, with `0.5` representing 50%.

[Parameters and JSON types](commands.md#setarrivalrulenetworkthresholdcmd)

### SetDepartConditionCombineMethodCmd
Change how a train departure condition is combined

Inferred from the names, this changes the logical combination setting for a departure condition in a train schedule entry. The flag suggests a choice between OR and an alternative combination, but the catalog does not describe the surrounding expression structure or explicitly identify the false case.

Inputs: `scheduleItem` identifies the line and schedule position; `rootId` identifies the entity associated with the rule root; `conditionIndex` selects the condition; `combineAsOr` requests OR combination when true. The root's exact role and the false setting remain unspecified.

[Parameters and JSON types](commands.md#setdepartconditioncombinemethodcmd)

### SetDoNotSkipThisTrainStationCmd
Control a station's do-not-skip flag

Inferred from the names, this marks a train station as one that should not be skipped, or clears that setting. It is intended to control station skipping, but the catalog does not explain which skip rules it affects.

Inputs: `rootStationId` identifies the root station entity; `doNotSkip` enables or disables the do-not-skip flag.

[Parameters and JSON types](commands.md#setdonotskipthistrainstationcmd)

### SetNetworkCargoStationCmd
Add or remove a network cargo station

Inferred from the names, this changes whether a station belongs to a train network in a cargo-station role. It configures network membership rather than requesting construction of a station.

Inputs: `networkId` identifies the train network; `stationId` identifies the station; `add` selects adding when true or removing when false, inferred from the flag's name.

[Parameters and JSON types](commands.md#setnetworkcargostationcmd)

### SetNetworkFuelStationCmd
Add or remove a network fuel station

Inferred from the names, this changes whether a station serves as a fuel station for a train network. It is a network configuration request, not a direct request to refuel a specific train.

Inputs: `networkId` identifies the network; `stationId` identifies the station; `add` selects adding when true or removing when false, inferred from the flag's name.

[Parameters and JSON types](commands.md#setnetworkfuelstationcmd)

### SetNetworkRefuelThresholdCmd
Set a train network's refueling threshold

Inferred from the names, this changes the refueling threshold for a train network. It appears intended to control when network trains seek fuel, but the catalog does not specify the measured fuel quantity or exact trigger comparison.

Inputs: `networkId` identifies the train network; `threshold` supplies a percentage as a fraction, with `0.5` representing 50%.

[Parameters and JSON types](commands.md#setnetworkrefuelthresholdcmd)

### SetNetworkWaitingBayCmd
Add or remove a network waiting bay

Inferred from the names, this changes whether a station is associated with a train network as a waiting bay. Use it to configure waiting locations; the catalog does not explain when trains choose those locations.

Inputs: `networkId` identifies the network; `stationId` identifies the station; `add` selects adding when true or removing when false, inferred from the flag's name.

[Parameters and JSON types](commands.md#setnetworkwaitingbaycmd)

### SetStationRequireFullServiceOnArrivalCmd
Set a station product's full-transfer arrival requirement

Inferred from the names, this controls a station's requirement for full service on arrival for a selected product. The argument calls this “full transfer,” but the catalog does not explain what must be full or how the requirement affects admission and handling.

Inputs: `stationId` identifies the station; `productId` selects the product; `requireFullTransfer` enables or disables the full-transfer requirement.

[Parameters and JSON types](commands.md#setstationrequirefullserviceonarrivalcmd)

### SetTrainLineColorApplicationCmd
Control whether trains use their line's color

Inferred from the names, this sets whether a train line's color is applied to its trains. It controls color application rather than selecting a new color for the line.

Inputs: `trainLineId` identifies the line; `applyLineColorToTrains` enables or disables applying that line's color to trains.

[Parameters and JSON types](commands.md#settrainlinecolorapplicationcmd)

### SetTrainLineColorCmd
Choose a train line's colors

Inferred from the names, this changes the color scheme associated with a train line. Use it to distinguish services visually; the catalog does not establish which trains inherit the scheme.

Inputs: `trainLineId` identifies the line. `color` supplies a TrainLineColor structure containing primary and secondary colors and a train-color value.

[Parameters and JSON types](commands.md#settrainlinecolorcmd)

### SetTrainLineLocoColorModeCmd
Choose how a line colors its locomotives

Inferred from the names, this selects how locomotive colors relate to the line's colors. It lets you choose an inheritance or override policy rather than supplying a new color itself.

Inputs: `trainLineId` identifies the line. `mode` is `SameAsLine`, `NoOverride`, or `Custom`; the catalog lists these choices without detailing their precedence.

[Parameters and JSON types](commands.md#settrainlinelococolormodecmd)

### SetTrainLineLocoCustomColorCmd
Set custom locomotive colors for a line

Inferred from the names, this provides a custom locomotive color scheme for a train line. The separate color-mode command suggests that supplying custom colors and choosing whether to use them are distinct settings.

Inputs: `trainLineId` identifies the line. `color` supplies primary and secondary colors and the train-color value in a TrainLineColor structure.

[Parameters and JSON types](commands.md#settrainlinelococustomcolorcmd)

### SetTrainNetworkColorApplicationCmd
Choose whether a network applies line colors to trains

Inferred from the names, this controls whether trains in a network receive line colors. Use it to change color application without replacing the stored color scheme.

Inputs: `networkId` identifies the train network. `applyLineColorToTrains` states whether line colors should be applied to trains.

[Parameters and JSON types](commands.md#settrainnetworkcolorapplicationcmd)

### SetTrainNetworkColorCmd
Choose a train network's colors

Inferred from the names, this changes the color scheme associated with a train network. The catalog does not explain how network colors interact with colors assigned to individual lines.

Inputs: `networkId` identifies the network. `color` supplies a TrainLineColor structure with primary and secondary colors and a train-color value.

[Parameters and JSON types](commands.md#settrainnetworkcolorcmd)

### SetTrainNetworkLocoColorModeCmd
Choose a network's locomotive color policy

Inferred from the names, this selects a locomotive color policy for a train network. It changes the policy rather than specifying the custom colors themselves; precedence over line-specific settings is not documented.

Inputs: `networkId` identifies the network. `mode` selects `SameAsLine`, `NoOverride`, or `Custom`.

[Parameters and JSON types](commands.md#settrainnetworklococolormodecmd)

### SetTrainNetworkLocoCustomColorCmd
Set custom locomotive colors for a network

Inferred from the names, this stores custom locomotive colors for a train network. A separate color-mode setting exists, so the catalog does not establish that supplying colors alone activates their use.

Inputs: `networkId` identifies the network. `color` provides primary and secondary colors and a train-color value in the TrainLineColor structure.

[Parameters and JSON types](commands.md#settrainnetworklococustomcolorcmd)

### SetTrainSchedulePriority
Adjust priority at a train schedule stop

Inferred from the names, this changes a priority associated with a schedule entry and a root entity. It may help distinguish competing schedule operations, but the catalog does not explain what the priority ranks or how the root entity is used.

Inputs: `scheduleItemId` identifies a line and its schedule index. `priority` supplies an integer priority, and `rootId` identifies the associated root entity; neither priority ordering nor the root's precise role is documented.

[Parameters and JSON types](commands.md#settrainschedulepriority)

### SetTrainScheduleSkipIfCannotArriveCmd
Allow a train to skip an unreachable stop

Inferred from the names, this controls whether a schedule entry is skipped when the train cannot arrive there. The catalog does not define which conditions count as an inability to arrive.

Inputs: `scheduleItemId` identifies the entry by train line and schedule index. `skipIfCannotArrive` enables or disables the skip condition.

[Parameters and JSON types](commands.md#settrainscheduleskipifcannotarrivecmd)

### SetTrainScheduleSkipIfHighFuelCmd
Skip a stop when the train has enough fuel

Inferred from the names, this sets a fuel threshold above which a schedule entry can be skipped. It is useful for expressing a conditional visit rather than always visiting the stop, although the catalog does not document how fuel level is measured.

Inputs: `scheduleItemId` identifies the line and schedule index. `skipIfFuelHigherThan` supplies the fuel percentage threshold, expressed as a fraction such as `0.5` for 50%.

[Parameters and JSON types](commands.md#settrainscheduleskipifhighfuelcmd)

### SetTrainScheduleSkipIfNextCanArriveCmd
Skip a stop when the next stop is available

Inferred from the names, this controls skipping an entry when arrival at the next entry is possible. It appears intended for conditional routing, but the exact arrival test is not described.

Inputs: `scheduleItemId` identifies a line and schedule index. `skipIfNextCanArrive` enables or disables this condition.

[Parameters and JSON types](commands.md#settrainscheduleskipifnextcanarrivecmd)

### SetTrainStationTrainLimitCmd
Set a station's train limit

Inferred from the names, this changes a station's train-limit setting. The catalog does not say whether that limit counts incoming, waiting, or physically present trains, so do not assume it is simply a platform-capacity setting.

Inputs: `stationId` identifies the station. `trainLimit` supplies the integer limit; special values and valid bounds are not documented.

[Parameters and JSON types](commands.md#settrainstationtrainlimitcmd)

### SetTrainTrackBufferTurnaroundCmd
Allow or prevent turning around at a track buffer

The game-provided description says this sets a buffer's `AllowsTurnaround` property. Use it to choose whether that buffer permits turnaround, without assuming it issues an immediate movement order to a train.

Inputs: `bufferId` identifies the buffer. `allowsTurnaround` states whether turnaround is allowed.

[Parameters and JSON types](commands.md#settraintrackbufferturnaroundcmd)

### SetWagonProductFilterCmd
Choose a wagon compartment's product filter

Inferred from the names, this sets a product filter on part of a train wagon. It lets you target a particular wagon and sub-car rather than treating the entire train as one cargo filter.

Inputs: `trainId` identifies the train, `wagonIndex` selects its wagon, and `subCarIndex` selects the sub-car. `productId` supplies the product identifier or null, defaulting to null; the catalog does not define null's effect or index bounds.

[Parameters and JSON types](commands.md#setwagonproductfiltercmd)

### SkipScheduleItemCmd
Ask a train to skip its schedule item

Inferred from the names, this asks a train to skip a schedule item, likely its current one because no entry is supplied. The exact advancement behavior and conditions for accepting the request are not documented.

Inputs: `trainId` identifies the train whose schedule progression should change.

[Parameters and JSON types](commands.md#skipscheduleitemcmd)

### ToggleLoadUnloadTrainScheduleItemCmd
Control loading or unloading at a schedule entry

Inferred from the arguments, this sets whether loading or unloading is disabled for a train schedule entry. Although its name says “Toggle,” it takes an explicit disable value rather than only a target.

Inputs: `scheduleItemId` identifies the line and schedule index. `isUnload` selects unloading when true or, by inference, loading when false; `disable` supplies the requested disabled state.

[Parameters and JSON types](commands.md#toggleloadunloadtrainscheduleitemcmd)

### ToggleScrapTrainAtNearestDepotCmd
Change a train's nearest-depot scrapping order

Inferred from the names, this toggles an order to scrap a train at its nearest depot. The catalog does not establish when scrapping occurs, how the depot is chosen, or whether the order can still be reversed once work begins.

Inputs: `trainId` identifies the train whose scrapping order should change.

[Parameters and JSON types](commands.md#togglescraptrainatnearestdepotcmd)

### ToggleTrainPausedCmd
Pause or resume a train

Inferred from the names, this flips a train's paused state. The catalog does not describe whether a moving train stops immediately or how pausing interacts with station work.

Inputs: `trainId` identifies the train.

[Parameters and JSON types](commands.md#toggletrainpausedcmd)

### ToggleTrainStationAllowedFuelCmd
Allow or disallow a station fuel

Inferred from the names, this toggles a fuel product in a train station's allowed-fuel selection. It is a fuel-policy change rather than a request to deliver fuel or refuel a particular train.

Inputs: `rootStationId` identifies the root station. `fuelId` identifies the fuel product whose allowed state should change.

[Parameters and JSON types](commands.md#toggletrainstationallowedfuelcmd)

### ToggleTrainStationModuleLoadUnloadCmd
Change a station module's loading or unloading setting

Inferred from the names, this changes a train station module's load/unload setting. The nullable argument makes the exact operation ambiguous: the catalog does not define whether it chooses a mode, controls permission, or triggers a toggle when omitted.

Inputs: `entityId` identifies the module. `load` is a nullable boolean defaulting to null; neither the boolean mapping nor null's meaning is documented.

[Parameters and JSON types](commands.md#toggletrainstationmoduleloadunloadcmd)

### ToggleTrainStationStorageLinkCmd
Link or unlink a station and a storage

Inferred from the names, this toggles a link between a train station and a storage. The catalog does not specify transfer direction or other requirements for the link to function.

Inputs: `stationId` identifies the station. `storageId` identifies the storage on the other end of the link.

[Parameters and JSON types](commands.md#toggletrainstationstoragelinkcmd)

### TrainContainsDepartConditionEditCmd
Edit a train's cargo-based departure condition

Inferred from the names, this edits a schedule departure condition based on what a train contains. It supports product scope, comparison direction, and a percentage threshold, but the catalog does not fully define their evaluation or the simplified mode.

Inputs: `scheduleItemId` identifies the line and schedule index, `rootId` identifies an associated root entity whose precise role is undocumented, and `conditionIndex` selects the condition. Nullable `useInferiorToInsteadOfSuperiorTo` names a switch between less-than and greater-than comparison; nullable `mode` selects `AllProducts`, `AnyProduct`, or `SpecificProduct`; nullable `percent` supplies a fractional percentage; and nullable `productId` supplies a product identifier. `productIdSpecified` defaults to false and, according to its game-provided description, distinguishes interpreting a null product as clear versus unset; the boolean-to-case mapping is not spelled out. Nullable `isSimplified` controls an undocumented simplified form; all nullable inputs default to null, with no further null semantics supplied.

[Parameters and JSON types](commands.md#traincontainsdepartconditioneditcmd)

### TrainDurationDepartConditionEditCmd
Edit a train's time-based departure condition

Inferred from the names, this edits the delay associated with a train schedule departure condition. The catalog does not specify the duration unit, timing origin, or behavior when no delay is supplied.

Inputs: `scheduleItem` identifies the line and schedule index. `rootId` identifies an associated root entity, `conditionIndex` selects the condition, and `delay` supplies a nullable integer Duration value defaulting to null; the root's exact role and null's effect are undocumented.

[Parameters and JSON types](commands.md#traindurationdepartconditioneditcmd)

### TrainStationFuelSetFuelCmd
Choose or clear a station's primary fuel

Inferred from the names, this selects a train station's primary fuel product. The game-provided argument description explicitly says a null fuel identifier clears the selection.

Inputs: `stationId` identifies the station. `primaryFuelId` supplies a product identifier or null to clear it, defaulting to null.

[Parameters and JSON types](commands.md#trainstationfuelsetfuelcmd)

### TrainStationModuleClearProductCmd
Clear a station module's product

Inferred from the names, this clears a train station module's product-related state. It is uncertain whether this means clearing the configured product, stored contents, or another state; the catalog does not distinguish it from the separate quick-remove command.

Inputs: `moduleId` identifies the station module.

[Parameters and JSON types](commands.md#trainstationmoduleclearproductcmd)

### TrainStationModuleQuickRemoveProductCmd
Request quick product removal from a station module

Inferred from the names, this requests a quick-removal operation for a train station module's product. The catalog does not explain what is removed or how this differs from clearing the product, so do not assume instant disposal, refunds, or a particular cost.

Inputs: `moduleId` identifies the station module.

[Parameters and JSON types](commands.md#trainstationmodulequickremoveproductcmd)

### TrainStationModuleSetProductCmd
Choose a train station module's product

Inferred from the names, this sets the product assigned to a train station module. The catalog does not explain how existing contents are handled when the product changes.

Inputs: `moduleId` identifies the module. `productId` identifies the product to select.

[Parameters and JSON types](commands.md#trainstationmodulesetproductcmd)

### UpdateTrainStationArrivalRuleCmd
Adjust a station's product-based arrival threshold

Inferred from the names, this updates a train station's arrival rule for a selected product. The catalog does not say whether arrival is permitted above or below the threshold or what inventory the percentage measures.

Inputs: `stationId` identifies the station, `productId` identifies the product, and `threshold` supplies a fractional percentage such as `0.5` for 50%.

[Parameters and JSON types](commands.md#updatetrainstationarrivalrulecmd)


## Rockets, asteroids and the space station

### AddLaunchPadCargoBufferCmd
Add a product buffer to a launch pad

Inferred from the names, this adds a cargo buffer for a particular product at a launch pad. It appears to configure which cargo the pad can handle, not to supply that cargo directly; capacity and delivery behavior are not documented.

Inputs: `launchPadId` identifies the pad and `productId` selects the product for the buffer. [Parameters and JSON types](commands.md#addlaunchpadcargobuffercmd).

### BringAsteroidToOrbitCmd
Request an asteroid's move into orbit

Inferred from the names, this requests that a selected asteroid be brought into orbit. It identifies the asteroid rather than a ground destination; the required conditions and how the operation proceeds are not documented.

Inputs: `asteroidId` selects the asteroid. [Parameters and JSON types](commands.md#bringasteroidtoorbitcmd).

### BuildOrUpgradeSpaceStationCmd
Request space station construction or an upgrade

Inferred from the name, this requests construction or upgrading of the space station. Which action applies appears to depend on the current game state, because the command does not accept a station ID or a target level.

Inputs: none. [Parameters and JSON types](commands.md#buildorupgradespacestationcmd).

### CancelBuildOrUpgradeOfSpaceStationCmd
Cancel a space station construction or upgrade request

Inferred from the name, this cancels a space station build or upgrade operation. It is not named as removal of a completed station, and the catalog does not document refunds or the treatment of work already completed.

Inputs: none. [Parameters and JSON types](commands.md#cancelbuildorupgradeofspacestationcmd).

### DiscardAsteroidCmd
Discard a selected asteroid

Inferred from the name, this discards an asteroid from the space-program context. What discard removes, whether it can be reversed, and whether anything is recovered are undocumented, so do not assume it is merely hiding an entry.

Inputs: `asteroidId` identifies the asteroid. [Parameters and JSON types](commands.md#discardasteroidcmd).

### DowngradeSpaceStationCmd
Request a space station downgrade

Inferred from the name, this downgrades the space station. It does not specify a target level, and the size of the downgrade, eligibility conditions, and treatment of station contents are undocumented.

Inputs: none. [Parameters and JSON types](commands.md#downgradespacestationcmd).

### DropAsteroidAtCmd
Choose a ground location for an asteroid drop

Inferred from the names, this requests an asteroid drop at a specified terrain position. The catalog does not describe timing, impact effects, or prerequisites, so it should not be treated as a documented harmless relocation.

Inputs: `asteroidId` selects the asteroid and `position` gives the two-dimensional tile location. [Parameters and JSON types](commands.md#dropasteroidatcmd).

### LaunchRocketCmd
Request a rocket launch from a pad

Inferred from the names, this requests a rocket launch from a selected launch pad. It does not choose cargo or a destination in its arguments, and launch readiness requirements and mission results are undocumented.

Inputs: `launchPadId` identifies the launch pad. [Parameters and JSON types](commands.md#launchrocketcmd).

### RemoveLaunchPadCargoBufferCmd
Remove a launch pad's product buffer

Inferred from the names, this removes a cargo buffer associated with a particular product at a launch pad. It appears intended for changing the pad's cargo configuration, but the catalog does not explain what happens to any cargo already held there.

Inputs: `launchPadId` identifies the launch pad; `productId` selects the product whose buffer should be removed.

[Parameters and JSON types](commands.md#removelaunchpadcargobuffercmd)

### ReorderLaunchPadCargoBufferCmd
Reorder launch pad cargo buffers

Inferred from the names, this moves a cargo buffer within a launch pad's buffer list. It changes list order; whether that also changes cargo handling priority is not documented.

Inputs: `launchPadId` identifies the pad; `oldIndex` selects the buffer's current position; `newIndexAfterRemove` gives the destination position in the list after removing that entry, as indicated by the argument name.

[Parameters and JSON types](commands.md#reorderlaunchpadcargobuffercmd)

### ScanForNewAsteroidCmd
Request a scan for another asteroid

Inferred from the name and space-program namespace, this starts or requests a search for a new asteroid. The catalog does not specify scan duration, requirements, or whether a scan will find one.

Inputs: none; no asteroid or scanning entity is selected by this command.

[Parameters and JSON types](commands.md#scanfornewasteroidcmd)

### SetOrbitCargoLimitCmd
Set a product's orbital cargo limit

Inferred from the names, this changes a cargo limit for a product in the orbital part of the space program. It can express a desired cargo cap, but whether it limits storage, transfers, or another operation is not documented.

Inputs: `productId` identifies the product; `limit` supplies the quantity limit. No special meaning for zero or negative values is advertised.

[Parameters and JSON types](commands.md#setorbitcargolimitcmd)

### SetRocketAutoLaunchCmd
Control automatic launches at a launch pad

Inferred from the names, this enables or disables automatic rocket launches for a launch pad. It configures launch automation rather than documenting an immediate launch, and the conditions for an automatic launch are not given.

Inputs: `launchPadId` identifies the pad; `autoLaunch` sets whether automatic launching should be enabled.

[Parameters and JSON types](commands.md#setrocketautolaunchcmd)

### ToggleRocketCountdownMuteCmd
Mute or unmute a rocket countdown

Inferred from the names, this toggles countdown muting for a launch pad. It concerns the countdown's mute setting, not an instruction to pause or cancel a launch.

Inputs: `launchPadId` identifies the launch pad.

[Parameters and JSON types](commands.md#togglerocketcountdownmutecmd)

### ToggleSpaceStationCrewEnabledCmd
Enable or disable space-station crew

Inferred from the name, this toggles the enabled setting for space-station crew. The catalog does not explain whether that changes staffing, dispatch, or another crew-related system.

Inputs: none. No station or crew member is selected explicitly.

[Parameters and JSON types](commands.md#togglespacestationcrewenabledcmd)


## Terrain, decoration and bridges

### AddSurfaceDecalCmd
Place a surface marking

Inferred from the names, this adds a chosen decal across a rectangular terrain area. Rotation, reflection, and a color key let you specify its appearance, but the catalog does not explain the available decal designs or color-key meanings.

Inputs: `protoId` selects the decal definition and `area` gives the rectangle. `rotation` supplies its orientation, with declared default angle index `0`; `isReflected` controls mirroring, default `false`; `colorKey` selects a color key, default `0`. [Parameters and JSON types](commands.md#addsurfacedecalcmd).

### ChangeSurfaceDecalColorCmd
Recolor surface markings in an area

Inferred from the names, this changes surface-decal color within a rectangular terrain area. It supplies a color key rather than a new decal design; which markings are affected and what each key represents are undocumented.

Inputs: `area` selects the rectangle and `colorKey` supplies the color key, with declared default `0`. [Parameters and JSON types](commands.md#changesurfacedecalcolorcmd).

### QuickRemovePropsCmd
Clear terrain props in an area

Inferred from the names, this requests quick removal of terrain props within a selected rectangle. It appears intended for clearing an area, but the catalog does not identify which kinds of props qualify or what removal requires.

Inputs: `area` defines the terrain rectangle using an origin and size.

[Parameters and JSON types](commands.md#quickremovepropscmd)

### RemoveSurfaceDecalCmd
Remove surface decals from an area

Inferred from the names, this removes surface decals within a terrain rectangle. It targets surface markings rather than documenting any change to terrain height or material.

Inputs: `area` supplies the terrain rectangle's origin and size.

[Parameters and JSON types](commands.md#removesurfacedecalcmd)

### SetBridgeLaneLayoutCmd
Configure a bridge lane

Inferred from the names, this assigns a lane prototype to a particular lane on a bridge. It appears intended for bridge layout changes, but the catalog does not describe the available lane types or the meaning of a null lane prototype.

Inputs: `bridgeId` identifies the bridge; `laneIndex` selects the lane; `laneProtoId` supplies a prototype ID or `null`, with an advertised default of `null`. Do not assume null removes the lane.

[Parameters and JSON types](commands.md#setbridgelanelayoutcmd)


## Factories, power and transports

### AddTransportPillarCmd
Add a support to a transport route

Inferred from the names, this adds a pillar at a selected support tile of a transport. It is a support-editing action rather than a request to create a whole transport; the support-tile indexing scheme is not explained.

Inputs: `transportId` identifies the transport and `supportTileIndex` chooses the support location within it. [Parameters and JSON types](commands.md#addtransportpillarcmd).

### ClearTransportCmd
Request clearing of a transport

The name suggests a transport-clearing operation, but the catalog does not say whether this means clearing carried goods, removing a transport, or another internal cleanup. Treat its effect as uncertain rather than assuming it is safe maintenance or ordinary deconstruction.

Inputs: `transportId` identifies the transport. [Parameters and JSON types](commands.md#cleartransportcmd).

### ClearUnusedMachineBuffersCmd
Clear a machine's unused buffers

Inferred from the names, this clears buffers considered unused by a machine. It appears relevant when managing leftover machine buffers, but neither the definition of unused nor the destination of any contents is documented.

Inputs: `machineId` identifies the machine whose unused buffers should be cleared. [Parameters and JSON types](commands.md#clearunusedmachinebufferscmd).

### DataCenterToggleRackCmd
Add or remove data-center racks

Inferred from the names, this changes the rack allocation of a data center for a selected rack type. Despite “Toggle” in the command name, the parameter description defines a signed change: negative for removal and positive for addition, rather than a simple on/off value.

Inputs: `dataCenterId` identifies the data center, `serverRackId` identifies the rack definition, and `difference` supplies the signed change. The meaning of zero is not documented. [Parameters and JSON types](commands.md#datacentertogglerackcmd).

### DeconstructTransportSegmentCmd
Remove part of a transport

Inferred from the names, this requests deconstruction of the portion of a transport between two positions. A quick-removal option is available, but its timing, requirements, and resource consequences are not documented.

Inputs: `transportId` identifies the transport, while `startPosition` and `endPosition` identify the segment endpoints in three-dimensional tile coordinates. `quickRemove` selects the quick-removal option and declares default `false`. [Parameters and JSON types](commands.md#deconstructtransportsegmentcmd).

### MachineBoostToggleCmd
Toggle a machine's boost setting

Inferred from the name, this switches a machine's boost state. It is not an explicit enable or disable request, and the catalog does not describe boost costs, production changes, or eligibility.

Inputs: `machineId` identifies the machine whose boost setting should change. [Parameters and JSON types](commands.md#machineboosttogglecmd).

### MachineSetRecipeActiveCmd
Explicitly enable or disable a machine recipe

Inferred from the names, this sets whether a particular recipe is active on a machine. It is useful when the desired state is known, because it supplies an explicit boolean rather than toggling an unknown current state; activation does not document an immediate production result.

Inputs: `machineId` identifies the machine, `recipeId` identifies the recipe, and `enableRecipe` selects enabled when true or disabled when false. [Parameters and JSON types](commands.md#machinesetrecipeactivecmd).

### MachineToggleRecipeActiveCmd
Toggle a machine recipe's active state

Inferred from the names, this switches whether a selected machine recipe is active. Unlike the explicit-setting command, it does not take a desired enabled state, so its effect depends on the recipe's current setting.

Inputs: `machineId` identifies the machine and `recipeId` identifies the recipe to toggle. [Parameters and JSON types](commands.md#machinetogglerecipeactivecmd).

### NuclearReactorSetEnrichmentStepCmd
Set a reactor's enrichment step

Inferred from the names, this changes the enrichment-step setting of a nuclear reactor. The step-to-enrichment mapping and its operational effects are undocumented, so an integer step should not be treated as a literal enrichment percentage.

Inputs: `reactorId` identifies the reactor and `enrichmentStep` supplies the setting step. [Parameters and JSON types](commands.md#nuclearreactorsetenrichmentstepcmd).

### NuclearReactorSetPowerLevelCmd
Set a reactor's power-level setting

Inferred from the names, this changes a nuclear reactor's selected power level. The catalog does not define the level scale or units, and a requested setting is not a documented guarantee of delivered power.

Inputs: `reactorId` identifies the reactor and `powerLevel` supplies the integer level. [Parameters and JSON types](commands.md#nuclearreactorsetpowerlevelcmd).

### NuclearReactorToggleAllowedFuelCmd
Toggle whether a reactor allows a fuel product

Inferred from the names, this switches whether a selected fuel product is allowed in a nuclear reactor. It configures fuel acceptance rather than directly supplying fuel, and it does not take an explicit desired allowed state.

Inputs: `reactorId` identifies the reactor and `fuelProtoId` identifies the fuel product whose allowed status should be toggled. [Parameters and JSON types](commands.md#nuclearreactortoggleallowedfuelcmd).

### NuclearReactorToggleAutomaticRegulationCmd
Toggle a reactor's automatic regulation

Inferred from the name, this switches automatic regulation for a nuclear reactor. It appears to change how regulation is controlled, but the regulation algorithm, power response, and operating requirements are undocumented.

Inputs: `reactorId` identifies the reactor; there is no argument specifying the desired on/off state. [Parameters and JSON types](commands.md#nuclearreactortoggleautomaticregulationcmd).

### RemoveTransportPillarCmd
Remove a transport support pillar

Inferred from the name and transport namespace, this requests removal of a transport pillar. It targets a support rather than a whole transport route; the effect on anything it supports is undocumented.

Inputs: `pillarId` identifies the pillar entity.

[Parameters and JSON types](commands.md#removetransportpillarcmd)

### ReorderRecipeCmd
Reorder a machine's recipes

Inferred from the names, this moves a recipe within a machine's recipe list. Use it to revise recipe ordering, but the catalog does not confirm how that order affects recipe selection or production.

Inputs: `machineId` identifies the machine; `oldIndex` selects the existing recipe position; `newIndexAfterRemove` specifies the destination in the list after removing that entry, inferred from the argument name.

[Parameters and JSON types](commands.md#reorderrecipecmd)

### ReverseLiftCmd
Reverse a lift's direction

Inferred from the name and factory-lift namespace, this reverses a lift's transport direction. It is useful when reorienting a production route, but the catalog does not explain what happens to cargo already in the lift.

Inputs: `liftId` identifies the lift entity.

[Parameters and JSON types](commands.md#reverseliftcmd)

### ReverseTransportCmd
Reverse a transport's direction

Inferred from the name, this reverses the direction of a transport entity. Use it when revising product flow, without assuming it rebuilds or reroutes the transport itself.

Inputs: `transportId` identifies the transport entity.

[Parameters and JSON types](commands.md#reversetransportcmd)

### SetElectricityGenerationPriorityCmd
Set a generator's electricity priority

Inferred from the names, this changes an entity's electricity-generation priority. Use it to express a preference among generators, but the catalog does not explain the numeric scale or the scheduling rules that use it.

Inputs: `entityId` identifies the generating entity; `priority` supplies its priority value.

[Parameters and JSON types](commands.md#setelectricitygenerationprioritycmd)

### SetIsElectricitySurplusConsumerCmd
Set an entity's surplus-electricity consumer flag

Inferred from the names, this controls whether an entity is marked as a surplus-electricity consumer. It appears intended to distinguish surplus demand from other demand, but the catalog does not define when the entity receives electricity under this setting.

Inputs: `entityId` identifies the consumer; `isSurplusConsumer` enables or disables the surplus-consumer flag.

[Parameters and JSON types](commands.md#setiselectricitysurplusconsumercmd)

### SetIsElectricitySurplusGeneratorCmd
Set an entity's surplus-electricity generator flag

Inferred from the names, this controls whether an entity is marked as a surplus-electricity generator. The exact meaning of surplus generation and how it affects dispatch are undocumented, so it should not be assumed to mean export or continuous operation.

Inputs: `entityId` identifies the generator; `isSurplusGenerator` enables or disables the surplus-generator flag.

[Parameters and JSON types](commands.md#setiselectricitysurplusgeneratorcmd)

### SetOfficeComputingBoostStepCmd
Set an office's computing-boost level

Inferred from the names, this selects a computing-boost step for an office. It appears intended to adjust the office's boost setting, but the available steps, requirements, and resulting effects are not documented.

Inputs: `officeId` identifies the office; `step` supplies the requested step value.

[Parameters and JSON types](commands.md#setofficecomputingbooststepcmd)

### SetOfficeFocusStepCmd
Adjust an office focus setting

Inferred from the names, this changes a selected office focus by a step difference. Despite “Set” in the command name, the argument `diff` suggests a relative adjustment rather than an absolute level; that interpretation and the focus's gameplay effects remain unverified.

Inputs: `focusId` identifies the focus prototype; `diff` supplies the integer difference to apply, inferred from its name. No individual office ID is accepted.

[Parameters and JSON types](commands.md#setofficefocusstepcmd)

### SorterToggleProductCmd
Change whether a sorter selects a product

Inferred from the names, this toggles a product's selection in a sorter. The catalog does not specify which output receives selected products, so routing direction should not be inferred from this command alone.

Inputs: `sorterId` identifies the sorter. `productId` identifies the product whose selection is toggled.

[Parameters and JSON types](commands.md#sortertoggleproductcmd)

### SortingPlantSetBlockedProductAlertCmd
Control blocked-product alerts at a sorting plant

Inferred from the names, this sets whether a sorting plant alerts about a particular blocked product. It changes notification policy rather than directly clearing the blockage.

Inputs: `sortingPlantId` identifies the plant, `productId` identifies the product, and `isAlertEnabled` states whether its blocked-product alert should be enabled.

[Parameters and JSON types](commands.md#sortingplantsetblockedproductalertcmd)

### StackerTowerSetDumpRadiusCmd
Adjust a stacker tower's dumping reach

Inferred from the names, this sets left and right dumping-radius values for a stacker tower. The catalog does not explain the reference direction or how these radii translate into a dumping area.

Inputs: `entityId` identifies the tower. `radiusLeft` and `radiusRight` are nullable integer relative-tile distances, both defaulting to null; the effect of null is not documented.

[Parameters and JSON types](commands.md#stackertowersetdumpradiuscmd)

### StackerTowerSetFullAlertActiveCmd
Control a stacker tower's full alert

Inferred from the names, this enables or disables a stacker tower's full-alert setting. The catalog does not specify what must be full to trigger the alert.

Inputs: `entityId` identifies the tower. `active` supplies the requested alert state.

[Parameters and JSON types](commands.md#stackertowersetfullalertactivecmd)

### StackerTowerSetMaxSegmentsCmd
Set a stacker tower's segment limit

Inferred from the names, this changes the maximum segment count associated with a stacker tower. The catalog does not explain what a segment represents here, so its relationship to reach or construction is uncertain.

Inputs: `entityId` identifies the tower. `segmentsCount` provides the integer segment limit; valid bounds are not documented.

[Parameters and JSON types](commands.md#stackertowersetmaxsegmentscmd)

### ToggleMechGeneratorAutoBalanceCmd
Switch automatic balancing for a mechanical generator

Inferred from the names, this toggles a mechanical generator's automatic-balancing setting. The catalog does not explain what is balanced or how generator output changes under that policy.

Inputs: `entityId` identifies the generator.

[Parameters and JSON types](commands.md#togglemechgeneratorautobalancecmd)

### WellPumpAlertSetEnabledCmd
Enable or disable a well pump alert

Inferred from the names, this controls whether a well pump's alert is enabled. The catalog does not identify the triggering condition, so it should not be described as a specific low-water or depletion alert without further evidence.

Inputs: `wellPumpId` identifies the well pump. `isEnabled` supplies the requested alert state.

[Parameters and JSON types](commands.md#wellpumpalertsetenabledcmd)

### ZipperSetForceEvenInputsCmd
Require even inputs at a zipper

Inferred from the names, this sets whether a zipper forces even input handling. The catalog does not define whether “even” refers to alternating items, equal quantities over time, or another balancing rule.

Inputs: `zipperId` identifies the zipper. `forceEvenInputs` supplies the requested even-input setting.

[Parameters and JSON types](commands.md#zippersetforceeveninputscmd)

### ZipperSetForceEvenOutputsCmd
Require even outputs at a zipper

Inferred from the names, this sets whether a zipper forces even output handling. It concerns distribution policy, but the catalog does not explain the balancing algorithm or what happens when an output cannot accept items.

Inputs: `zipperId` identifies the zipper. `forceEvenOutputs` supplies the requested even-output setting.

[Parameters and JSON types](commands.md#zippersetforceevenoutputscmd)

### ZipperSetPriorityPortsCmd
Set or toggle priority for a zipper port

Inferred from the names, this changes priority for a named port on a zipper. The game-provided argument description confirms that a null priority value acts as a toggle, while the catalog does not explain how priority interacts with even-input or even-output settings.

Inputs: `zipperId` identifies the zipper. `portName` is the port's one-character name, and `isPrioritized` is a nullable boolean defaulting to null: supply a boolean to request a priority state, or null to toggle it.

[Parameters and JSON types](commands.md#zippersetpriorityportscmd)


## Vehicles and logistics zones

### AddVehicleReplacementTaskCmd
Set up replacement of a vehicle type

Inferred from the names, this adds a task to replace vehicles of one type with another, with zone and assignment filters. It appears intended for managing a replacement program rather than selecting one individual vehicle; the task's scheduling rules are not documented.

Inputs: `currentProtoId` selects the existing vehicle type, `replacementProtoId` selects its replacement, and `zoneId` selects the logistics zone. `vehicleDepotId` supplies a depot filter or selection, `unassignedOnly` indicates whether to restrict the task to unassigned vehicles, `assigneeId` supplies an assignee filter or selection, and `limit` supplies a numerical limit. Both ID fields `vehicleDepotId` and `assigneeId` accept null and declare null defaults, but the meaning of null and the exact limit behavior are unspecified. [Parameters and JSON types](commands.md#addvehiclereplacementtaskcmd).

### AddVehicleToBuildQueueCmd
Queue vehicle assembly at a depot

The game-provided description says this requests assembly of a vehicle from the given depot. Use it to request a quantity of a chosen vehicle type, rather than to assign an existing vehicle to a job.

Inputs: `protoId` identifies the vehicle type, `vehicleDepotId` identifies the assembling depot, and `count` gives the requested quantity, with declared default `1`. [Parameters and JSON types](commands.md#addvehicletobuildqueuecmd).

### AssignVehicleToEntityCmd
Assign one existing vehicle to an entity

The game-provided description says this assigns a concrete vehicle to an entity. Use this when you mean a particular vehicle instance, as distinct from requesting a number of vehicles of a given type.

Inputs: `vehicleId` identifies the existing vehicle and `entityId` identifies the entity receiving the assignment. [Parameters and JSON types](commands.md#assignvehicletoentitycmd).

### AssignVehicleTypeToEntityCmd
Assign vehicles by type rather than individual ID

The game-provided description says this assigns a vehicle type to an entity. The quantity and zone arguments appear to qualify that type-based assignment, but the catalog does not explain how individual vehicles are selected.

Inputs: despite its name, `vehicleId` is a vehicle-type prototype ID, not an individual vehicle ID. `entityId` selects the receiving entity, `count` gives the quantity with declared default `1`, and `zoneId` supplies a nullable logistics-zone ID with declared default null; null's meaning is undocumented. [Parameters and JSON types](commands.md#assignvehicletypetoentitycmd).

### BuildVehicleForeverCmd
Configure continuous vehicle production

The game-provided description says this builds a vehicle indefinitely and that a null type ID clears the setting. It is the continuous-production counterpart to requesting a finite quantity in a build queue.

Inputs: `vehicleDepotId` selects the depot and `protoId` selects the vehicle type to keep building. `protoId` accepts null to clear continuous production and declares a null default. [Parameters and JSON types](commands.md#buildvehicleforevercmd).

### CancelReplaceVehicleCmd
Cancel replacement of a particular vehicle

Inferred from the names, this cancels a replacement operation associated with one vehicle. It targets an individual vehicle, unlike the command for adding a replacement task by vehicle type; what happens to work already underway is unspecified.

Inputs: `vehicleId` identifies the vehicle whose replacement should be canceled. [Parameters and JSON types](commands.md#cancelreplacevehiclecmd).

### CreateNewLogisticsZoneCmd
Create a logistics zone

Inferred from the name, this creates a new logistics zone. It does not accept a name, area, or vehicle assignment, so it does not by itself describe a fully configured zone.

Inputs: none. [Parameters and JSON types](commands.md#createnewlogisticszonecmd).

### DiscardVehicleCargoCmd
Discard a vehicle's cargo

Inferred from the name, this requests discarding the cargo of an existing vehicle. It is not documented as a delivery or storage transfer, and the catalog does not establish the destination or recoverability of discarded goods.

Inputs: `vehicleId` identifies the vehicle carrying the cargo. [Parameters and JSON types](commands.md#discardvehiclecargocmd).

### ExcavatorTogglePreferredProductCmd
Change an excavator's preferred mining product

Inferred from the names, this toggles a preferred product setting for an excavator. It appears to influence mining preference rather than create material, but repeated-selection behavior and the effect of a null product are undocumented.

Inputs: `excavatorId` identifies the excavator and `productToMine` supplies the product preference. `productToMine` accepts null and declares a null default. [Parameters and JSON types](commands.md#excavatortogglepreferredproductcmd).

### NavigateVehicleToPositionCmd
Send a vehicle toward a tile position

Inferred from the names, this requests vehicle navigation to a map position. It identifies a coordinate rather than a work assignment or destination entity, and neither route availability nor arrival is guaranteed by the catalog.

Inputs: `vehicleId` identifies the vehicle and `position` gives the two-dimensional tile destination. [Parameters and JSON types](commands.md#navigatevehicletopositioncmd).

### NavigateVehicleToStaticEntityCmd
Send a vehicle toward a placed entity

Inferred from the names, this requests navigation of a vehicle to a static entity, such as a placed structure. It does not by itself document assignment, cargo transfer, or another interaction on arrival.

Inputs: `vehicleId` identifies the moving vehicle and `staticEntityId` identifies the destination entity. [Parameters and JSON types](commands.md#navigatevehicletostaticentitycmd).

### NavigateVehicleToVehicleCmd
Send one vehicle toward another

Inferred from the names, this requests navigation of one vehicle toward a second vehicle. Whether the target is followed as it moves, and whether any interaction happens on arrival, are undocumented.

Inputs: `vehicleId` identifies the moving vehicle and `goalVehicleId` identifies the target vehicle. [Parameters and JSON types](commands.md#navigatevehicletovehiclecmd).

### QuickBuildCurrentVehicleCmd
Quick-build the current vehicle using Unity

The game-provided description says this requests quick construction of the current vehicle and pays for it using Unity. Use it for the vehicle currently being built at a depot; the description gives no Unity amount or eligibility rules.

Inputs: `vehicleDepotId` identifies the vehicle depot handling that vehicle.

[Parameters and JSON types](commands.md#quickbuildcurrentvehiclecmd)

### RecoverVehicleCmd
Request recovery of a vehicle

Inferred from the name, this requests recovery of a vehicle that needs intervention. The catalog does not say where it is recovered to or what conditions permit recovery.

Inputs: `vehicleId` identifies the vehicle entity.

[Parameters and JSON types](commands.md#recovervehiclecmd)

### RemoveLogisticsZoneCmd
Remove a logistics zone

Inferred from the name, this removes a logistics zone definition. Use it when reorganizing logistics areas; the metadata does not describe how existing assignments respond to the removal.

Inputs: `zoneId` identifies the logistics zone.

[Parameters and JSON types](commands.md#removelogisticszonecmd)

### RemoveVehicleFromBuildQueueCmd
Vehicle build-queue operation with conflicting metadata

The name suggests removing a vehicle from a depot's build queue, but the game-provided description instead says, “Requests assembly of vehicle from the given depot depot.” These disagree, so queue cancellation should be treated as an inference rather than verified behavior.

Inputs: `index` selects a queue position; `vehicleDepotId` identifies the depot. The metadata does not resolve whether that entry is removed or assembled.

[Parameters and JSON types](commands.md#removevehiclefrombuildqueuecmd)

### RemoveVehicleReplacementTaskCmd
Remove a vehicle replacement task

Inferred from the name, this removes an existing vehicle replacement task. Use it to withdraw a replacement request, but the catalog does not explain consequences for any work already underway.

Inputs: `taskId` identifies the replacement task, not the vehicle itself.

[Parameters and JSON types](commands.md#removevehiclereplacementtaskcmd)

### RenameLogisticsZoneCmd
Rename a logistics zone

Inferred from the names, this gives a logistics zone a new name. It is useful for distinguishing zones by purpose; no change to the zone's area or assignments is described.

Inputs: `zoneId` identifies the zone; `name` supplies its new name.

[Parameters and JSON types](commands.md#renamelogisticszonecmd)

### ReplaceVehicleCmd
Request a different vehicle type

Inferred from the names, this requests replacement of a vehicle with a selected target type. It can express a fleet upgrade or other type change, but the catalog does not specify the replacement process, resource requirements, or timing.

Inputs: `vehicleId` identifies the existing vehicle; `targetProtoId` identifies the desired dynamic-entity prototype.

[Parameters and JSON types](commands.md#replacevehiclecmd)

### SetLogisticsZoneColorCmd
Choose a logistics zone's color

Inferred from the names, this assigns a color selection to a logistics zone. It is intended to help distinguish zones, without a documented change to logistics behavior.

Inputs: `zoneId` identifies the zone; `colorIndex` selects a color by index rather than supplying an RGB value. The palette and valid indices are not given.

[Parameters and JSON types](commands.md#setlogisticszonecolorcmd)

### SetVehicleDepotTargetZone
Choose a vehicle depot's target logistics zone

Inferred from the names, this sets a depot's target logistics zone. The catalog does not explain whether the setting affects newly produced vehicles, existing vehicles, or both.

Inputs: `vehicleDepotId` identifies the depot. `zoneId` supplies the logistics-zone identifier or null and defaults to null; the meaning of null is not documented.

[Parameters and JSON types](commands.md#setvehicledepottargetzone)

### SetVehicleLogisticsZoneCmd
Assign a truck's logistics zone

Inferred from the names, this changes the logistics zone associated with a truck. Use it to express which zone the truck belongs to, without assuming it changes any separate building assignment.

Inputs: `zoneId` supplies a zone identifier or null and has a declared default of null; null's effect is not specified. `truckId` identifies the individual truck.

[Parameters and JSON types](commands.md#setvehiclelogisticszonecmd)

### ToggleFuelStationTrucksAllowedToRefuelCmd
Change whether trucks may refuel at a station

Inferred from the names, this toggles permission for trucks to refuel at a fuel station. It changes station policy rather than selecting a particular truck for refueling.

Inputs: `fuelStationId` identifies the fuel station.

[Parameters and JSON types](commands.md#togglefuelstationtrucksallowedtorefuelcmd)

### ToggleLogisticsZoneConstructionCmd
Change a logistics zone's construction-zone relationship

Inferred from the names, this toggles a construction-related relationship between two logistics zones. This is an ambiguous internal setting: the catalog does not establish which zone supplies vehicles or what permissions the relationship grants.

Inputs: `zoneId` identifies the logistics zone being configured. `constructionZoneId` identifies the zone involved in its construction relationship.

[Parameters and JSON types](commands.md#togglelogisticszoneconstructioncmd)

### TogglePartialTrucksLoadCmd
Change the partial-truck-load setting

Inferred from the name, this toggles a setting related to allowing partial truck loads. With no target or description, its exact scope and the circumstances under which trucks depart partially loaded are uncertain.

Inputs: none. The command does not identify a truck, storage, or zone.

[Parameters and JSON types](commands.md#togglepartialtrucksloadcmd)

### ToggleVehicleScrapCmd
Change a vehicle's scrapping designation

Inferred from the names, this toggles a vehicle's scrapping setting or order. The catalog does not say when removal happens or whether materials are recovered.

Inputs: `vehicleId` identifies the individual vehicle.

[Parameters and JSON types](commands.md#togglevehiclescrapcmd)

### TruckConstructionRuleSetCmd
Set a truck type's construction rule in a zone

Inferred from the names, this sets construction-work policy for a truck type in a logistics zone. One named rule restricts use to situations where other trucks cannot reach, offering a way to express conditional construction participation rather than assigning individual vehicles.

Inputs: `truckId` is a prototype identifier, not an individual truck entity; `zoneId` identifies the logistics zone. `rule` selects `None`, `OnlyIfOthersCannotReach`, or `Forbid`; the catalog does not explain whether `None` means no extra restriction or another behavior.

[Parameters and JSON types](commands.md#truckconstructionrulesetcmd)

### TruckJobsAllowCmd
Allow a truck type's jobs in a logistics zone

Inferred from the names, this allows jobs for a truck type in a logistics zone. The catalog does not specify which job categories it covers or how this permission interacts with construction-specific rules.

Inputs: `truckId` identifies a truck prototype or type rather than an individual vehicle. `zoneId` identifies the logistics zone.

[Parameters and JSON types](commands.md#truckjobsallowcmd)

### TruckJobsForbidCmd
Forbid a truck type's jobs in a logistics zone

Inferred from the names, this forbids jobs for a truck type in a logistics zone. The catalog does not specify whether already-running jobs are interrupted or which job categories are covered.

Inputs: `truckId` identifies a truck prototype or type rather than an individual vehicle. `zoneId` identifies the logistics zone.

[Parameters and JSON types](commands.md#truckjobsforbidcmd)

### UnassignVehicleCmd
Remove an individual vehicle's assignment

Inferred from the names, this unassigns a vehicle from its current assignment. The catalog does not describe what assignment types are affected or where the vehicle goes afterward.

Inputs: `vehicleId` identifies the individual vehicle to unassign.

[Parameters and JSON types](commands.md#unassignvehiclecmd)

### UnassignVehicleFromEntityCmd
Remove vehicles of a type from an entity's assignments

Inferred from the inputs, this removes a requested number of vehicles of a specified type from an entity's assignments. Unlike the individual-vehicle command, it uses a prototype identifier and count; a further input suggests a zone to assign afterward, but the exact reassignment behavior is undocumented.

Inputs: `vehicleId` identifies the dynamic-entity prototype, despite its instance-like name. `entityId` identifies the entity to unassign vehicles from, `count` supplies the number and defaults to 1, and `zoneToAssign` supplies a nullable logistics-zone identifier defaulting to null; null's effect is not defined.

[Parameters and JSON types](commands.md#unassignvehiclefromentitycmd)


## Farming, animals and forestry

### AnimalFarmSetSlaughterLimitCmd
Adjust an animal farm's slaughter setting

Inferred from the names, this changes the slaughter-limit setting of an animal farm. The setting is expressed as a slider step rather than an explicitly documented animal count, so its conversion to a farming threshold is uncertain.

Inputs: `farmId` identifies the animal farm and `slaughterSliderStep` supplies the step. The step accepts null and declares a null default, but null's meaning is undocumented. [Parameters and JSON types](commands.md#animalfarmsetslaughterlimitcmd).

### AnimalFarmToggleGrowthPauseCmd
Pause or resume animal growth

Inferred from the names, this toggles the growth-pause state of an animal farm. It appears useful for changing whether growth is paused, but it does not accept an explicit desired state, so the effect depends on the farm's current setting.

Inputs: `farmId` identifies the farm whose growth-pause setting should be toggled. [Parameters and JSON types](commands.md#animalfarmtogglegrowthpausecmd).

### DesignateHarvestedTreesCmd
Mark or unmark trees for harvesting

The game-provided description says this adds or removes trees in a rectangular area from the set designated for harvesting. Despite “Harvested” in the name, it changes designation rather than documenting that trees have already been cut; an optional product filter narrows which trees are selected.

Inputs: `area` selects the rectangle and `addToHarvest` chooses whether to add trees to the harvesting set or remove them. `harvestedProductId`, nullable with declared default null, restricts selection to trees yielding that product when set. The description refers to two tile positions, while the advertised JSON represents the rectangle using origin and size; follow the linked technical shape. [Parameters and JSON types](commands.md#designateharvestedtreescmd).

### FarmAssignCropCmd
Choose a crop for a farm schedule slot

Inferred from the names, this assigns a crop to a selected slot in a farm's schedule. It appears intended to configure a planting sequence rather than trigger an immediate harvest; the effect on a crop already growing is undocumented.

Inputs: `farmId` identifies the farm, `scheduleSlot` selects the schedule slot, and `cropId` identifies the crop definition. `cropId` accepts null and declares a null default, whose meaning is not specified. [Parameters and JSON types](commands.md#farmassigncropcmd).

### FarmForceNextSlotCmd
Request advancement to the farm's next schedule slot

Inferred from the name, this forces a farm toward its next scheduled slot. It appears useful for intervening in the normal crop sequence, but the catalog does not say when the transition happens or what happens to the current crop.

Inputs: `farmId` identifies the farm. [Parameters and JSON types](commands.md#farmforcenextslotcmd).

### FarmHarvestNowCmd
Request a farm harvest now

Inferred from the name, this asks a farm to harvest rather than wait for its usual progression. Crop eligibility, timing, and yield consequences are not documented, so the name alone does not establish a guaranteed immediate harvest.

Inputs: `farmId` identifies the farm. [Parameters and JSON types](commands.md#farmharvestnowcmd).

### FarmSetFertilityTargetCmd
Set a farm's target fertility

Inferred from the names, this changes the fertility target for a farm. It sets a target rather than documenting an immediate change to soil fertility, and the mechanism for reaching the target is not described.

Inputs: `farmId` identifies the farm and `target` supplies the desired fertility as a fractional percentage, with `0.5` representing 50%. The catalog does not specify allowed bounds. [Parameters and JSON types](commands.md#farmsetfertilitytargetcmd).

### ForestryTowerSetCutPercentageCmd
Adjust a forestry tower's cutting percentage

Inferred from the names, this changes the cutting-percentage setting of a forestry tower. The catalog does not define what the percentage measures, so it should not be presented as a guaranteed share of trees, a growth threshold, or a yield multiplier.

Inputs: `towerId` identifies the forestry tower and `cutPercent` supplies the percentage as a fraction, with `0.5` representing 50%. Allowed bounds are not documented. [Parameters and JSON types](commands.md#forestrytowersetcutpercentagecmd).

### ForestryTowerSetTreeProtoCmd
Choose a tree definition for a forestry tower

Inferred from the names, this sets a forestry tower's tree-related definition. The argument refers to a group prototype, so whether this selects a species, a planting group, or another internal grouping is uncertain.

Inputs: `towerId` identifies the tower and `groupProtoId` identifies the selected group definition. [Parameters and JSON types](commands.md#forestrytowersettreeprotocmd).

### MoveAnimalsCmd
Request movement of animals associated with a farm

Inferred from the name, this moves a specified number of animals in connection with an animal farm. Because only one farm is identified, the direction of movement and the source or destination cannot be established from the catalog.

Inputs: `farmId` identifies the farm and `numberToMove` supplies the number of animals. The meaning of signs or special values is not documented. [Parameters and JSON types](commands.md#moveanimalscmd).

### PrepareManualPlantTreeCmd
Prepare a manually placed tree

Inferred from the names, this prepares a tree placement using a chosen tree type and location. The word “prepare” leaves uncertain whether it creates a planting task, reserves a location, or performs another internal preparation step; do not assume it produces a grown tree.

Inputs: `protoId` selects the prototype to place; `transform` supplies its tile position and orientation, with rotation and reflection forms described in the technical reference.

[Parameters and JSON types](commands.md#preparemanualplanttreecmd)

### RemoveManualPlantTreeCmd
Remove a manual tree-planting entry

Inferred from the names, this removes a tree entry associated with manual planting. It is unclear whether this cancels a pending planting or affects an existing tree, so it should not be assumed to be a general tree-felling command.

Inputs: `treeId` identifies the tree entry through its terrain position.

[Parameters and JSON types](commands.md#removemanualplanttreecmd)

### ToggleFullBufferNotificationCmd
Switch a farm's full-buffer notification

Inferred from the names, this toggles a farm's notification for a full buffer. It changes notification behavior rather than clearing the buffer or moving its contents.

Inputs: `farmId` identifies the farm.

[Parameters and JSON types](commands.md#togglefullbuffernotificationcmd)


## Storage and product handling

### AssignProductToSlotCmd
Choose a product for a storage slot

Inferred from the names and storage namespace, this assigns a product to one slot of a storage entity. It appears to configure the slot rather than put a quantity of goods into storage.

Inputs: `entityId` identifies the storage entity, `slot` selects the slot, and `productId` selects the product. `productId` accepts null and declares a null default; the catalog does not establish what null does. [Parameters and JSON types](commands.md#assignproducttoslotcmd).

### NuclearWasteStorageToggleOutputPortCmd
Toggle a nuclear-waste storage output port

Inferred from the names, this switches the output-port setting of a nuclear-waste storage. It appears to control output availability rather than directly move stored waste; the precise port behavior is not documented.

Inputs: `storageId` identifies the storage; there is no explicit enabled-state or individual port argument. [Parameters and JSON types](commands.md#nuclearwastestoragetoggleoutputportcmd).

### StorageAddAllowedTruckGroupCmd
Allow a truck group to serve a storage

Inferred from the names, this adds a truck group to a storage's allowed set. It is a permission change, not an assignment of an individual vehicle.

Inputs: `storageId` identifies the storage. `truckProtoId` identifies the truck prototype or group to allow, rather than a particular truck entity.

[Parameters and JSON types](commands.md#storageaddallowedtruckgroupcmd)

### StorageAlertSetEnabledCmd
Enable or disable a storage level alert

Inferred from the names, this controls one of a storage's above- or below-threshold alerts. It changes whether an alert is enabled without supplying a new threshold.

Inputs: `storageId` identifies the storage, and `isEnabled` supplies the requested enabled state. `isAbove` selects the above-threshold side when true and, by inference, the below-threshold side when false.

[Parameters and JSON types](commands.md#storagealertsetenabledcmd)

### StorageAlertSetThresholdCmd
Choose a storage alert's trigger level

Inferred from the names, this sets a storage level-alert threshold. It lets you tune the above- or below-threshold alert separately from enabling it.

Inputs: `storageId` identifies the storage. `value` supplies a percentage as a fraction such as `0.5` for 50%, and `isAbove` selects the above-threshold side when true or, by inference, the below-threshold side when false.

[Parameters and JSON types](commands.md#storagealertsetthresholdcmd)

### StorageDisableLogisticsToggleCmd
Enable or disable storage logistics in one direction

Inferred from the arguments, this explicitly sets whether input or output logistics are disabled for a storage. Despite “Toggle” in the name, an `isDisabled` input is supplied, so this should not be treated as a parameterless state flip.

Inputs: `storageId` identifies the storage. `isInput` selects input logistics when true or, by inference, output logistics when false; `isDisabled` states whether that direction is disabled.

[Parameters and JSON types](commands.md#storagedisablelogisticstogglecmd)

### StorageRemoveAllowedTruckGroupCmd
Remove a storage's permission for a truck group

Inferred from the names, this removes a truck group from a storage's allowed set. The catalog does not say how a storage with no explicitly allowed groups behaves.

Inputs: `storageId` identifies the storage. `truckProtoId` identifies the truck prototype or group whose permission should be removed.

[Parameters and JSON types](commands.md#storageremoveallowedtruckgroupcmd)

### StorageSetProductCmd
Choose a storage's product

Inferred from the names, this sets the product associated with a storage. The catalog does not explain what happens if the storage already contains a different product.

Inputs: `storageId` identifies the storage. `productId` identifies the product to select.

[Parameters and JSON types](commands.md#storagesetproductcmd)

### StorageSetSliderStepCmd
Adjust storage import, export, and transport thresholds

The game-provided description says this sets storage sliders and clamps steps above `MAX_STEPS` to that maximum when processed. Two overloads expose step-based and percentage-based inputs; the catalog does not provide the numeric maximum or the full relationship between slider settings and logistics behavior.

Inputs: both overloads take `storageId`. The integer-step overload accepts nullable `importStep`, `exportStep`, `transportFrom`, and `transportUntil`, all defaulting to null and described as negative when undefined. The percentage overload instead accepts nullable `importUntil`, `exportFrom`, `transportFrom`, and `transportUntil`, all defaulting to null, with fractional percentages such as `0.5` for 50%; its transport fields also carry the negative-means-undefined description. The names indicate import/export thresholds and a transport interval, but null handling is not documented.

[Parameters and JSON types](commands.md#storagesetsliderstepcmd)

### ToggleEnforceAssignedVehiclesForEntityCmd
Control enforcement of assigned vehicles

Inferred from the names, this sets whether a storage enforces its assigned-vehicle policy. Despite “Toggle” in the name, an explicit requested state is supplied; the exact effect on unassigned vehicles is not documented.

Inputs: `storageId` identifies the storage. `isEnforced` states whether the assigned-vehicle policy should be enforced.

[Parameters and JSON types](commands.md#toggleenforceassignedvehiclesforentitycmd)


## Buildings, construction and priorities

### CloneConfigBetweenEntitiesCmd
Copy settings from one entity to another

Inferred from the names, this copies configuration from a source entity to a target entity. It appears intended to reproduce settings rather than duplicate the physical entity; compatible entity types and the specific settings copied are not documented.

Inputs: `sourceEntityId` identifies the entity to copy from and `targetEntityId` identifies the entity to configure. [Parameters and JSON types](commands.md#cloneconfigbetweenentitiescmd).

### CreateStaticEntityCmd
Create a placed entity at a chosen transform

Inferred from the names, this creates a static entity from a prototype at a specified position and orientation. The validation flag only permits validation suppression when other conditions are met, according to its description; it is not a documented guarantee of unrestricted placement or instant construction.

Inputs: `protoId` selects the static entity definition and `transform` describes its position, rotation, and reflection. `allowValidationSuppression` says whether the entity may suppress validation if other conditions permit it, with declared default `false`. [Parameters and JSON types](commands.md#createstaticentitycmd).

### EntityDisableLogisticsToggleCmd
Set an entity's input or output logistics mode

Inferred from the arguments, this changes logistics handling for either the input or output side of an entity. Despite “Disable” and “Toggle” in the name, it accepts an explicit mode, including automatic and enabled modes, rather than only switching logistics off.

Inputs: `entityId` selects the entity, `isInput` selects the input side when true or the output side when false, and `mode` selects `Auto`, `On`, or `Off`. The precise behavior of automatic mode is undocumented. [Parameters and JSON types](commands.md#entitydisablelogisticstogglecmd).

### FinishBuildOfStaticEntityCmd
Use Unity for quick construction or removal

The game-provided description explicitly says this performs quick build or quick removal of an entity, paid with Unity. Despite its construction-only name, it therefore also covers removal; the catalog does not state the Unity amount or how the action is chosen.

Inputs: `id` identifies the entity whose construction or removal should be completed. [Parameters and JSON types](commands.md#finishbuildofstaticentitycmd).

### QuickRemoveEntityRefundCmd
Request quick removal with a refund

Inferred from the name, this requests a quick-removal operation involving a refund for an entity. The catalog does not establish what is refunded, how much is returned, or whether the operation is a separate internal step in removal.

Inputs: `entityId` identifies the entity concerned.

[Parameters and JSON types](commands.md#quickremoveentityrefundcmd)

### QuickRemoveFromEntityCmd
Request an entity-related quick-removal operation

This appears to be an internal quick-removal command for a static entity, inferred from its name and namespace. What is removed “from” the entity is not explained, so it should not be treated as a verified equivalent of demolishing the whole building.

Inputs: `entityId` identifies the entity used by the operation. Its advertised result is an entity ID, but the catalog does not explain which entity that represents.

[Parameters and JSON types](commands.md#quickremovefromentitycmd)

### QuickRepairEntityCmd
Request a quick repair

Inferred from the name and maintenance namespace, this requests quick repair of an entity. Use it to target a particular maintenance problem; the metadata does not specify repair amounts, costs, or conditions.

Inputs: `entityId` identifies the entity to repair.

[Parameters and JSON types](commands.md#quickrepairentitycmd)

### RecoverOceanAccessCmd
Attempt to restore an entity's ocean access

Inferred from the names, this attempts to recover ocean access around an entity with associated ocean areas. It includes a tile-count limit, but the catalog does not describe the terrain changes involved or guarantee that access can be restored.

Inputs: `entityWithOceanAreas` identifies the affected entity; `maxTilesToRecover` specifies the maximum number of tiles for the recovery operation. The command advertises a `RecoverOceanResult`, whose meaning is not explained here.

[Parameters and JSON types](commands.md#recoveroceanaccesscmd)

### RuinsScrapCmd
Control scrapping of ruins

Inferred from the names, this enables or disables scrapping of ruined buildings. One constructor identifies specific ruins and another does not; the scope of the version without an ID is undocumented, so it must not be assumed to affect all ruins.

Inputs: the first overload takes only `isScrapping`, the desired scrapping flag. The second takes `ruinsId` to identify the ruined entity and `isScrapping` to specify whether scrapping should be active.

[Parameters and JSON types](commands.md#ruinsscrapcmd)

### SetBillboardColorCmd
Set a billboard's two colors

Inferred from the names, this assigns primary and secondary colors to a billboard entity. Use it for visual differentiation; the metadata does not describe which parts use each color.

Inputs: `entityId` identifies the billboard entity; `primaryColor` and `secondaryColor` supply its two colors. Both accept the color representations listed in the technical reference, including packed and component-based forms.

[Parameters and JSON types](commands.md#setbillboardcolorcmd)

### SetConstructionPausedCmd
Control whether construction is paused

Inferred from the names, this changes the construction-pause state of an entity. It concerns construction rather than the whole game's pause state, and the nullable pause flag has no documented null behavior.

Inputs: `entityId` identifies the entity under construction; `isPaused` supplies true, false, or `null`, with an advertised default of `null`. The catalog does not establish that null means toggle.

[Parameters and JSON types](commands.md#setconstructionpausedcmd)

### SetConstructionPriorityCmd
Set an entity's construction priority

Inferred from the names, this changes the priority assigned to an entity's construction. Use it to express which construction work matters more, but the catalog does not define the priority scale or guarantee a build order.

Inputs: `entityId` identifies the construction target; `priority` supplies the priority value.

[Parameters and JSON types](commands.md#setconstructionprioritycmd)

### SetCustomPriorityCmd
Set a named priority on an entity

Inferred from the names, this changes one identified priority setting on an entity. The priority identifier makes this more specific than a general-priority request, but supported identifiers and their gameplay roles are not supplied.

Inputs: `entityId` identifies the entity; `priorityId` names the priority setting; `priority` supplies its value. Numeric ordering and allowed values are undocumented.

[Parameters and JSON types](commands.md#setcustomprioritycmd)

### SetDumpHeightOffsetCmd
Adjust an entity's dumping-height offset

Inferred from the names, this changes a dumping-height offset associated with an entity. It can express a different dumping level, but the reference height and the direction represented by positive values are not documented.

Inputs: `entityId` identifies the entity; `depth` supplies an integer tile-thickness value for the offset. The difference between the command's “height” wording and the argument's “depth” wording leaves the sign convention uncertain.

[Parameters and JSON types](commands.md#setdumpheightoffsetcmd)

### SetEntityEnabledCmd
Enable or disable an entity

Inferred from the names, this sets an entity's enabled state explicitly. It is a per-entity control rather than a game-wide pause, and the exact operational consequences depend on an entity's behavior, which is not described here.

Inputs: `entityId` identifies the entity; `isEnabled` sets whether it should be enabled.

[Parameters and JSON types](commands.md#setentityenabledcmd)

### SetEntityNameCmd
Give an entity a name

Inferred from the names, this changes an entity's title or name. Use it to label an entity by role or location rather than changing its prototype or function.

Inputs: `entityId` identifies the entity; `title` supplies the requested name text.

[Parameters and JSON types](commands.md#setentitynamecmd)

### SetGeneralPriorityCmd
Set an entity's general priority

Inferred from the names, this changes an entity's general priority setting. It can express relative importance, but the catalog does not identify every system affected or define whether larger numbers mean greater priority.

Inputs: `entityId` identifies the entity; `priority` supplies the priority value.

[Parameters and JSON types](commands.md#setgeneralprioritycmd)

### SetGlobalPriorityCmd
Set a named global priority

Inferred from the names and priorities namespace, this changes a global priority setting selected by an identifier. Unlike a per-entity priority command, it takes no entity ID; the exact scope of each priority identifier is not documented.

Inputs: `priorityId` names the global priority setting; `priority` supplies its value. Available identifiers and priority ordering are unspecified.

[Parameters and JSON types](commands.md#setglobalprioritycmd)

### SetPlanningModeEnabledCmd
Turn planning mode on or off

Inferred from the name, this sets whether planning mode is enabled. It controls the mode itself; the catalog does not explain its construction or placement rules.

Inputs: `isEnabled` sets whether planning mode should be active.

[Parameters and JSON types](commands.md#setplanningmodeenabledcmd)

### StartDeconstructionOfStaticEntityCmd
Begin removing a static entity

Inferred from the command name, this starts deconstruction of a static entity. The game-provided argument description explains that area removal also clears track beneath a waypoint, whereas an individual delete leaves plain replacement track.

Inputs: `entityId` identifies the entity, and `reason` is `Remove` or `Collapse`. `isAreaRemove` defaults to false and marks removal as part of bulldozing an area; its documented waypoint behavior makes this distinction significant.

[Parameters and JSON types](commands.md#startdeconstructionofstaticentitycmd)

### ToggleConstructionPriorityCmd
Change an entity's construction priority setting

Inferred from the names, this toggles an entity's construction-priority setting. It does not supply a numeric priority or document how priority affects the construction queue.

Inputs: `entityId` identifies the entity whose construction-priority setting should change.

[Parameters and JSON types](commands.md#toggleconstructionprioritycmd)

### ToggleDefaultLogisticsMode
Change the default logistics mode

Inferred from the name, this switches the default logistics mode. This is an ambiguous global-looking setting: the catalog does not name its modes or explain whether existing entities are affected.

Inputs: none. There is no target or requested-mode argument.

[Parameters and JSON types](commands.md#toggledefaultlogisticsmode)

### ToggleEnabledCmd
Enable or disable an entity

Inferred from the names, this flips an entity's enabled state. What disabling means depends on the entity; the catalog does not promise that every kind of activity stops.

Inputs: `entityId` identifies the entity to toggle.

[Parameters and JSON types](commands.md#toggleenabledcmd)

### ToggleStaticEntityConstructionCmd
Change a static entity's construction state

Inferred from the names, this toggles a construction-related state for a static entity. It plausibly controls whether construction proceeds, but the catalog does not confirm the states or distinguish pausing from other construction actions.

Inputs: `entityId` identifies the static entity.

[Parameters and JSON types](commands.md#togglestaticentityconstructioncmd)

### TryTransformEntityCmd
Rotate or flip an unbuilt ghost in place

The game-provided description says this tries to rotate or flip an entity in place and applies only to non-constructed ghosts. It is therefore not a general tool for rotating completed buildings, and the wording does not guarantee every requested transformation succeeds.

Inputs: `entityId` identifies the ghost. `rotate` requests rotation and `flip` requests flipping; the catalog does not document the rotation amount or flip axis.

[Parameters and JSON types](commands.md#trytransformentitycmd)


## Game controls, research and notifications

### GameConsoleCmd
Submit a game-console instruction

Inferred from its name and namespace, this submits text to the game's console-command system. It is a general-purpose internal entry point rather than a documented single gameplay action; accepted syntax, permissions, and effects are not provided here.

Inputs: `command` is the console instruction text. [Parameters and JSON types](commands.md#gameconsolecmd).

### GameSpeedChangeCmd
Change the simulation speed

Inferred from the name, this changes the game's simulation-speed multiplier. The parameter description explicitly says values are clamped to the range from `1` to `MAX_GAME_SPEED` when processed, but does not supply the numeric maximum.

Inputs: `newSpeedMultiplier` supplies the requested integer speed multiplier. Do not infer pause behavior from a value below `1`, because the documented processing clamps it into the stated range. [Parameters and JSON types](commands.md#gamespeedchangecmd).

### InputCommand
Undocumented internal input command

This generic name and the input namespace suggest an internal input-system command, but no game-provided description explains its effect. There is not enough information to recommend it as a player action or assign it a particular gameplay purpose.

Inputs: none. [Parameters and JSON types](commands.md#inputcommand).

### MarkGoalAsFinishedCmd
Record a goal as finished or skipped

Inferred from the names, this marks a goal as finished while recording whether it was skipped. It changes goal bookkeeping rather than documenting that the goal's gameplay requirements were met, and any rewards or progression effects remain unspecified.

Inputs: `protoId` identifies the goal definition and `goalWasSkipped` indicates whether it was skipped, with declared default `false`. [Parameters and JSON types](commands.md#markgoalasfinishedcmd).

### MarkMessageAsReadCmd
Record a message as read

Inferred from the name, this marks a message as read. It is a message-state action, not a documented dismissal or deletion operation; other consequences are unspecified.

Inputs: `protoId` identifies the message definition to mark as read. [Parameters and JSON types](commands.md#markmessageasreadcmd).

### MessageNotificationDismissCmd
Dismiss a message notification

Inferred from the name, this dismisses a particular message notification. The catalog does not establish that dismissing a notification also marks the underlying message as read or deletes it.

Inputs: `messageId` identifies the notification instance, using the notification-ID type rather than a message prototype ID. [Parameters and JSON types](commands.md#messagenotificationdismisscmd).

### PinnedProductReorderCmd
Reorder a pinned product

Inferred from the names, this moves an already pinned product to a different position in the pinned list. Use it to arrange the products you want to keep track of, rather than to change their production or stock.

Inputs: `productToMove` identifies the product by its prototype ID; `newIndex` is its requested position in the list. The catalog does not specify index bounds.

[Parameters and JSON types](commands.md#pinnedproductreordercmd)

### PinToggleCmd
Pin or unpin a product

Inferred from the name, this switches a product's pinned status. It is a toggle rather than an explicit request to keep the product pinned, so its intended effect depends on the current state.

Inputs: `productToToggle` identifies the product whose pinned status should change.

[Parameters and JSON types](commands.md#pintogglecmd)

### ResearchQueueDequeueCmd
Add or remove a research queue entry

Inferred from the names, this changes whether a research node is queued. Although the command name emphasizes dequeueing, its `isEnqueue` flag suggests it also handles enqueueing; this interpretation is not backed by a game-provided description.

Inputs: `nodeId` identifies the research node; `isEnqueue` selects enqueueing when true and dequeueing when false, inferred from the flag's name.

[Parameters and JSON types](commands.md#researchqueuedequeuecmd)

### ResearchStartCmd
Start researching a technology

The game-provided description says this starts research on the selected node in the research tree. It selects what to research, not a request to complete that research immediately.

Inputs: `nodeId` identifies the research node to start.

[Parameters and JSON types](commands.md#researchstartcmd)

### ResearchStopCmd
Stop the current research

The game-provided description says this stops the current research. It does not specify what happens to accumulated progress or queued research.

Inputs: none; the command acts on the current research rather than a supplied node.

[Parameters and JSON types](commands.md#researchstopcmd)

### SetSimPauseStateCmd
Pause or resume the game

The game-provided description says this pauses or resumes the game. Unlike a toggle, the boolean argument expresses the desired paused state directly.

Inputs: `isPaused` is true to pause or false to resume.

[Parameters and JSON types](commands.md#setsimpausestatecmd)

