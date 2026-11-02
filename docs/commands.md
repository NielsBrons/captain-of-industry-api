# Command catalog

[README](../README.md) · [Player-friendly command guide](command-guide.md) · [POST /command](endpoints.md)

This live catalog contains 240 distinct command types and 244 constructor signatures. No command was executed. Names and descriptions are game-provided metadata, not independently verified behavior.

## Request format and cautions

Send `POST /command` with Content-Type `application/json`. The body is an object with `type` (the command identifier) and `args` (an object of named constructor arguments, not a positional array). Result metadata below reports the game type; actual HTTP result envelopes are unverified.

JSON hints are reproduced verbatim, including object/array layouts, nullable shapes and enum choices when supplied. Where no json hint is advertised, do not invent encodings for unfamiliar game types. Defaults are metadata; omission semantics were not exercised. Some commands have overloaded constructors. Numeric instance IDs generally cannot be replaced with catalog proto IDs; obtaining every needed entity ID is outside the inspected routes. Back up a save before experimenting with write commands.

## Index

| Type | Namespace | Constructors |
| --- | --- | --- |
| [AcceptLoanCmd](#acceptloancmd) | `Mafi.Core.World.Loans` | 1 |
| [AddEntityToScheduleItemCmd](#addentitytoscheduleitemcmd) | `Mafi.Core.Trains` | 1 |
| [AddLaunchPadCargoBufferCmd](#addlaunchpadcargobuffercmd) | `Mafi.Core.SpaceProgram` | 1 |
| [AddNewScheduleItemToTrainLineCmd](#addnewscheduleitemtotrainlinecmd) | `Mafi.Core.Trains` | 1 |
| [AddSurfaceDecalCmd](#addsurfacedecalcmd) | `Mafi.Core.Terrain.Designation` | 1 |
| [AddTrainTrackPillarCmd](#addtraintrackpillarcmd) | `Mafi.Core.Trains` | 1 |
| [AddTransportPillarCmd](#addtransportpillarcmd) | `Mafi.Core.Factory.Transports` | 1 |
| [AddVehicleReplacementTaskCmd](#addvehiclereplacementtaskcmd) | `Mafi.Core.Vehicles` | 1 |
| [AddVehicleToBuildQueueCmd](#addvehicletobuildqueuecmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [AnimalFarmSetSlaughterLimitCmd](#animalfarmsetslaughterlimitcmd) | `Mafi.Core.Buildings.Farms` | 1 |
| [AnimalFarmToggleGrowthPauseCmd](#animalfarmtogglegrowthpausecmd) | `Mafi.Core.Buildings.Farms` | 1 |
| [AssignProductToSlotCmd](#assignproducttoslotcmd) | `Mafi.Core.Buildings.Storages` | 1 |
| [AssignTrainLineToTrainCmd](#assigntrainlinetotraincmd) | `Mafi.Core.Trains` | 1 |
| [AssignTrainLineToUnfinishedTrainCmd](#assigntrainlinetounfinishedtraincmd) | `Mafi.Core.Trains` | 1 |
| [AssignTrainToNetworkCmd](#assigntraintonetworkcmd) | `Mafi.Core.Trains` | 1 |
| [AssignVehicleToEntityCmd](#assignvehicletoentitycmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [AssignVehicleTypeToEntityCmd](#assignvehicletypetoentitycmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [BringAsteroidToOrbitCmd](#bringasteroidtoorbitcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [BuildOrUpgradeSpaceStationCmd](#buildorupgradespacestationcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [BuildVehicleForeverCmd](#buildvehicleforevercmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [CancelBuildOrUpgradeOfSpaceStationCmd](#cancelbuildorupgradeofspacestationcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [CancelReplaceVehicleCmd](#cancelreplacevehiclecmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [CancelTrainBuildCmd](#canceltrainbuildcmd) | `Mafi.Core.Trains` | 1 |
| [CancelTrainJobCmd](#canceltrainjobcmd) | `Mafi.Core.Trains` | 1 |
| [CancelTrainReplacementCmd](#canceltrainreplacementcmd) | `Mafi.Core.Trains` | 1 |
| [CargoDepotSetFuelSliderStepCmd](#cargodepotsetfuelsliderstepcmd) | `Mafi.Core.Buildings.Cargo` | 1 |
| [CargoShipReplaceFuelCmd](#cargoshipreplacefuelcmd) | `Mafi.Core.Buildings.Cargo.Modules` | 1 |
| [ChangeSurfaceDecalColorCmd](#changesurfacedecalcolorcmd) | `Mafi.Core.Terrain.Designation` | 1 |
| [ClearTransportCmd](#cleartransportcmd) | `Mafi.Core.Factory.Transports` | 1 |
| [ClearUnusedMachineBuffersCmd](#clearunusedmachinebufferscmd) | `Mafi.Core.Factory.Machines` | 1 |
| [CloneConfigBetweenEntitiesCmd](#cloneconfigbetweenentitiescmd) | `Mafi.Core.Entities.Static.Commands` | 1 |
| [CreateNewLogisticsZoneCmd](#createnewlogisticszonecmd) | `Mafi.Core.Vehicles` | 1 |
| [CreateNewTrainLineCmd](#createnewtrainlinecmd) | `Mafi.Core.Trains` | 1 |
| [CreateNewTrainNetworkCmd](#createnewtrainnetworkcmd) | `Mafi.Core.Trains` | 1 |
| [CreateStaticEntityCmd](#createstaticentitycmd) | `Mafi.Core.Entities.Static.Commands` | 1 |
| [CreateTrainTrackEntityWithDirectionCmd](#createtraintrackentitywithdirectioncmd) | `Mafi.Core.Trains` | 1 |
| [DataCenterToggleRackCmd](#datacentertogglerackcmd) | `Mafi.Core.Factory.Datacenters` | 1 |
| [DeconstructTransportSegmentCmd](#deconstructtransportsegmentcmd) | `Mafi.Core.Factory.Transports` | 1 |
| [DesignateHarvestedTreesCmd](#designateharvestedtreescmd) | `Mafi.Core.Terrain.Trees` | 1 |
| [DiscardAsteroidCmd](#discardasteroidcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [DiscardVehicleCargoCmd](#discardvehiclecargocmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [DowngradeSpaceStationCmd](#downgradespacestationcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [DropAsteroidAtCmd](#dropasteroidatcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [EntityDisableLogisticsToggleCmd](#entitydisablelogisticstogglecmd) | `Mafi.Core.Entities.Commands` | 1 |
| [ExcavatorTogglePreferredProductCmd](#excavatortogglepreferredproductcmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [FarmAssignCropCmd](#farmassigncropcmd) | `Mafi.Core.Buildings.Farms` | 1 |
| [FarmForceNextSlotCmd](#farmforcenextslotcmd) | `Mafi.Core.Buildings.Farms` | 1 |
| [FarmHarvestNowCmd](#farmharvestnowcmd) | `Mafi.Core.Buildings.Farms` | 1 |
| [FarmSetFertilityTargetCmd](#farmsetfertilitytargetcmd) | `Mafi.Core.Buildings.Farms` | 1 |
| [FinishBuildOfStaticEntityCmd](#finishbuildofstaticentitycmd) | `Mafi.Core.Entities.Static.Commands` | 1 |
| [FleetLoadCrewCmd](#fleetloadcrewcmd) | `Mafi.Core.World` | 1 |
| [FleetModificationsCancelCmd](#fleetmodificationscancelcmd) | `Mafi.Core.World` | 1 |
| [FleetToggleAutoReturnCmd](#fleettoggleautoreturncmd) | `Mafi.Core.World` | 1 |
| [FleetUnloadCrewCmd](#fleetunloadcrewcmd) | `Mafi.Core.World` | 1 |
| [FleetUnloadFuelCmd](#fleetunloadfuelcmd) | `Mafi.Core.World` | 1 |
| [ForestryTowerSetCutPercentageCmd](#forestrytowersetcutpercentagecmd) | `Mafi.Core.Buildings.Forestry` | 1 |
| [ForestryTowerSetTreeProtoCmd](#forestrytowersettreeprotocmd) | `Mafi.Core.Buildings.Forestry` | 1 |
| [GameConsoleCmd](#gameconsolecmd) | `Mafi.Core.Console` | 1 |
| [GameSpeedChangeCmd](#gamespeedchangecmd) | `Mafi.Core.Simulation` | 1 |
| [GoToLocationCmd](#gotolocationcmd) | `Mafi.Core.World` | 1 |
| [InputCommand](#inputcommand) | `Mafi.Core.Input` | 1 |
| [LaunchRocketCmd](#launchrocketcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [MachineBoostToggleCmd](#machineboosttogglecmd) | `Mafi.Core.Factory.Machines` | 1 |
| [MachineSetRecipeActiveCmd](#machinesetrecipeactivecmd) | `Mafi.Core.Factory.Machines` | 1 |
| [MachineToggleRecipeActiveCmd](#machinetogglerecipeactivecmd) | `Mafi.Core.Factory.Machines` | 1 |
| [MakeLoanOverpaymentCmd](#makeloanoverpaymentcmd) | `Mafi.Core.World.Loans` | 1 |
| [MarkGoalAsFinishedCmd](#markgoalasfinishedcmd) | `Mafi.Core.Messages.Goals` | 1 |
| [MarkMessageAsReadCmd](#markmessageasreadcmd) | `Mafi.Core.Messages` | 1 |
| [MessageNotificationDismissCmd](#messagenotificationdismisscmd) | `Mafi.Core.MessageNotifications` | 1 |
| [MoveAnimalsCmd](#moveanimalscmd) | `Mafi.Core.Buildings.Farms` | 1 |
| [NavigateTrainToCmd](#navigatetraintocmd) | `Mafi.Core.Trains` | 1 |
| [NavigateVehicleToPositionCmd](#navigatevehicletopositioncmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [NavigateVehicleToStaticEntityCmd](#navigatevehicletostaticentitycmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [NavigateVehicleToVehicleCmd](#navigatevehicletovehiclecmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [NotifyOnBattleOpenedCmd](#notifyonbattleopenedcmd) | `Mafi.Core.Fleet` | 1 |
| [NuclearReactorSetEnrichmentStepCmd](#nuclearreactorsetenrichmentstepcmd) | `Mafi.Core.Factory.NuclearReactors` | 1 |
| [NuclearReactorSetPowerLevelCmd](#nuclearreactorsetpowerlevelcmd) | `Mafi.Core.Factory.NuclearReactors` | 1 |
| [NuclearReactorToggleAllowedFuelCmd](#nuclearreactortoggleallowedfuelcmd) | `Mafi.Core.Factory.NuclearReactors` | 1 |
| [NuclearReactorToggleAutomaticRegulationCmd](#nuclearreactortoggleautomaticregulationcmd) | `Mafi.Core.Factory.NuclearReactors` | 1 |
| [NuclearWasteStorageToggleOutputPortCmd](#nuclearwastestoragetoggleoutputportcmd) | `Mafi.Core.Buildings.Storages.NuclearWaste` | 1 |
| [PinnedProductReorderCmd](#pinnedproductreordercmd) | `Mafi.Core.Products` | 1 |
| [PinToggleCmd](#pintogglecmd) | `Mafi.Core.Products` | 1 |
| [PrepareManualPlantTreeCmd](#preparemanualplanttreecmd) | `Mafi.Core.Terrain.Trees` | 1 |
| [QuickBuildCurrentTrainCmd](#quickbuildcurrenttraincmd) | `Mafi.Core.Trains` | 1 |
| [QuickBuildCurrentVehicleCmd](#quickbuildcurrentvehiclecmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [QuickRemoveEntityRefundCmd](#quickremoveentityrefundcmd) | `Mafi.Core.Entities` | 1 |
| [QuickRemoveFromEntityCmd](#quickremovefromentitycmd) | `Mafi.Core.Entities.Static` | 1 |
| [QuickRemovePropsCmd](#quickremovepropscmd) | `Mafi.Core.Terrain.Props` | 1 |
| [QuickRepairEntityCmd](#quickrepairentitycmd) | `Mafi.Core.Maintenance` | 1 |
| [QuickRepairTrainCmd](#quickrepairtraincmd) | `Mafi.Core.Trains` | 1 |
| [QuickTradeCmd](#quicktradecmd) | `Mafi.Core.World.QuickTrade` | 1 |
| [RecoverOceanAccessCmd](#recoveroceanaccesscmd) | `Mafi.Core.Entities.Static` | 1 |
| [RecoverShipCmd](#recovershipcmd) | `Mafi.Core.Entities.Ships` | 1 |
| [RecoverTrainCmd](#recovertraincmd) | `Mafi.Core.Trains` | 1 |
| [RecoverVehicleCmd](#recovervehiclecmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [RefuelTrainCmd](#refueltraincmd) | `Mafi.Core.Trains` | 1 |
| [RemoveDepartConditionCmd](#removedepartconditioncmd) | `Mafi.Core.Trains` | 1 |
| [RemoveEntityFromScheduleItemCmd](#removeentityfromscheduleitemcmd) | `Mafi.Core.Trains` | 1 |
| [RemoveLaunchPadCargoBufferCmd](#removelaunchpadcargobuffercmd) | `Mafi.Core.SpaceProgram` | 1 |
| [RemoveLogisticsZoneCmd](#removelogisticszonecmd) | `Mafi.Core.Vehicles` | 1 |
| [RemoveManualPlantTreeCmd](#removemanualplanttreecmd) | `Mafi.Core.Terrain.Trees` | 1 |
| [RemovePathfindingRestrictionCmd](#removepathfindingrestrictioncmd) | `Mafi.Core.Trains` | 1 |
| [RemoveSurfaceDecalCmd](#removesurfacedecalcmd) | `Mafi.Core.Terrain.Designation` | 1 |
| [RemoveTrainLineCmd](#removetrainlinecmd) | `Mafi.Core.Trains` | 1 |
| [RemoveTrainLineScheduleItemCmd](#removetrainlinescheduleitemcmd) | `Mafi.Core.Trains` | 1 |
| [RemoveTrainNetworkCmd](#removetrainnetworkcmd) | `Mafi.Core.Trains` | 1 |
| [RemoveTrainTrackPillarCmd](#removetraintrackpillarcmd) | `Mafi.Core.Trains` | 1 |
| [RemoveTransportPillarCmd](#removetransportpillarcmd) | `Mafi.Core.Factory.Transports` | 1 |
| [RemoveVehicleFromBuildQueueCmd](#removevehiclefrombuildqueuecmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [RemoveVehicleReplacementTaskCmd](#removevehiclereplacementtaskcmd) | `Mafi.Core.Vehicles` | 1 |
| [RenameLogisticsZoneCmd](#renamelogisticszonecmd) | `Mafi.Core.Vehicles` | 1 |
| [RenameTrainLineCmd](#renametrainlinecmd) | `Mafi.Core.Trains` | 1 |
| [RenameTrainNetworkCmd](#renametrainnetworkcmd) | `Mafi.Core.Trains` | 1 |
| [ReorderDepartConditionCmd](#reorderdepartconditioncmd) | `Mafi.Core.Trains` | 1 |
| [ReorderLaunchPadCargoBufferCmd](#reorderlaunchpadcargobuffercmd) | `Mafi.Core.SpaceProgram` | 1 |
| [ReorderRecipeCmd](#reorderrecipecmd) | `Mafi.Core.Factory.Machines` | 1 |
| [ReorderTrainLineScheduleItemCmd](#reordertrainlinescheduleitemcmd) | `Mafi.Core.Trains` | 1 |
| [ReplaceEntityInScheduleCmd](#replaceentityinschedulecmd) | `Mafi.Core.Trains` | 1 |
| [ReplaceVehicleCmd](#replacevehiclecmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [ResearchQueueDequeueCmd](#researchqueuedequeuecmd) | `Mafi.Core.Research` | 1 |
| [ResearchStartCmd](#researchstartcmd) | `Mafi.Core.Research` | 1 |
| [ResearchStopCmd](#researchstopcmd) | `Mafi.Core.Research` | 1 |
| [ReverseLiftCmd](#reverseliftcmd) | `Mafi.Core.Factory.Lifts` | 1 |
| [ReverseTransportCmd](#reversetransportcmd) | `Mafi.Core.Factory.Transports` | 1 |
| [RuinsScrapCmd](#ruinsscrapcmd) | `Mafi.Core.Buildings.RuinedBuildings` | 2 |
| [ScanForNewAsteroidCmd](#scanfornewasteroidcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [ScrapTrainCarCmd](#scraptraincarcmd) | `Mafi.Core.Trains` | 1 |
| [SetArrivalRuleAlwaysAllowCmd](#setarrivalrulealwaysallowcmd) | `Mafi.Core.Trains` | 1 |
| [SetArrivalRuleNetworkPriorityCmd](#setarrivalrulenetworkprioritycmd) | `Mafi.Core.Trains` | 1 |
| [SetArrivalRuleNetworkThresholdCmd](#setarrivalrulenetworkthresholdcmd) | `Mafi.Core.Trains` | 1 |
| [SetBillboardColorCmd](#setbillboardcolorcmd) | `Mafi.Base.Prototypes.Buildings` | 1 |
| [SetBridgeLaneLayoutCmd](#setbridgelanelayoutcmd) | `Mafi.Core.Bridges` | 1 |
| [SetConstructionPausedCmd](#setconstructionpausedcmd) | `Mafi.Core.Entities` | 1 |
| [SetConstructionPriorityCmd](#setconstructionprioritycmd) | `Mafi.Core.Entities.Commands` | 1 |
| [SetCustomPriorityCmd](#setcustomprioritycmd) | `Mafi.Core.Entities.Commands` | 1 |
| [SetDepartConditionCombineMethodCmd](#setdepartconditioncombinemethodcmd) | `Mafi.Core.Trains` | 1 |
| [SetDoNotSkipThisTrainStationCmd](#setdonotskipthistrainstationcmd) | `Mafi.Core.Trains` | 1 |
| [SetDumpHeightOffsetCmd](#setdumpheightoffsetcmd) | `Mafi.Core.Entities.Commands` | 1 |
| [SetElectricityGenerationPriorityCmd](#setelectricitygenerationprioritycmd) | `Mafi.Core.Factory.ElectricPower` | 1 |
| [SetEntityEnabledCmd](#setentityenabledcmd) | `Mafi.Core.Entities` | 1 |
| [SetEntityNameCmd](#setentitynamecmd) | `Mafi.Core.Entities` | 1 |
| [SetGeneralPriorityCmd](#setgeneralprioritycmd) | `Mafi.Core.Entities.Commands` | 1 |
| [SetGlobalPriorityCmd](#setglobalprioritycmd) | `Mafi.Core.Entities.Priorities` | 1 |
| [SetIsElectricitySurplusConsumerCmd](#setiselectricitysurplusconsumercmd) | `Mafi.Core.Factory.ElectricPower` | 1 |
| [SetIsElectricitySurplusGeneratorCmd](#setiselectricitysurplusgeneratorcmd) | `Mafi.Core.Factory.ElectricPower` | 1 |
| [SetLoanBufferPriorityCmd](#setloanbufferprioritycmd) | `Mafi.Core.World.Loans` | 1 |
| [SetLogisticsZoneColorCmd](#setlogisticszonecolorcmd) | `Mafi.Core.Vehicles` | 1 |
| [SetNetworkCargoStationCmd](#setnetworkcargostationcmd) | `Mafi.Core.Trains` | 1 |
| [SetNetworkFuelStationCmd](#setnetworkfuelstationcmd) | `Mafi.Core.Trains` | 1 |
| [SetNetworkRefuelThresholdCmd](#setnetworkrefuelthresholdcmd) | `Mafi.Core.Trains` | 1 |
| [SetNetworkWaitingBayCmd](#setnetworkwaitingbaycmd) | `Mafi.Core.Trains` | 1 |
| [SetOfficeComputingBoostStepCmd](#setofficecomputingbooststepcmd) | `Mafi.Core.Buildings.Offices` | 1 |
| [SetOfficeFocusStepCmd](#setofficefocusstepcmd) | `Mafi.Core.Buildings.Offices` | 1 |
| [SetOrbitCargoLimitCmd](#setorbitcargolimitcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [SetPlanningModeEnabledCmd](#setplanningmodeenabledcmd) | `Mafi.Core.Entities` | 1 |
| [SetRocketAutoLaunchCmd](#setrocketautolaunchcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [SetShiftsCountForMineCmd](#setshiftscountforminecmd) | `Mafi.Core.World.Entities` | 1 |
| [SetSimPauseStateCmd](#setsimpausestatecmd) | `Mafi.Core.Simulation` | 1 |
| [SetStationRequireFullServiceOnArrivalCmd](#setstationrequirefullserviceonarrivalcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainLineColorApplicationCmd](#settrainlinecolorapplicationcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainLineColorCmd](#settrainlinecolorcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainLineLocoColorModeCmd](#settrainlinelococolormodecmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainLineLocoCustomColorCmd](#settrainlinelococustomcolorcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainNetworkColorApplicationCmd](#settrainnetworkcolorapplicationcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainNetworkColorCmd](#settrainnetworkcolorcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainNetworkLocoColorModeCmd](#settrainnetworklococolormodecmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainNetworkLocoCustomColorCmd](#settrainnetworklococustomcolorcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainSchedulePriority](#settrainschedulepriority) | `Mafi.Core.Trains` | 1 |
| [SetTrainScheduleSkipIfCannotArriveCmd](#settrainscheduleskipifcannotarrivecmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainScheduleSkipIfHighFuelCmd](#settrainscheduleskipifhighfuelcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainScheduleSkipIfNextCanArriveCmd](#settrainscheduleskipifnextcanarrivecmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainStationTrainLimitCmd](#settrainstationtrainlimitcmd) | `Mafi.Core.Trains` | 1 |
| [SetTrainTrackBufferTurnaroundCmd](#settraintrackbufferturnaroundcmd) | `Mafi.Core.Trains` | 1 |
| [SetVehicleDepotTargetZone](#setvehicledepottargetzone) | `Mafi.Core.Vehicles.Commands` | 1 |
| [SetVehicleLogisticsZoneCmd](#setvehiclelogisticszonecmd) | `Mafi.Core.Vehicles` | 1 |
| [SetWagonProductFilterCmd](#setwagonproductfiltercmd) | `Mafi.Core.Trains` | 1 |
| [ShipayardSetFuelSliderStepCmd](#shipayardsetfuelsliderstepcmd) | `Mafi.Core.Buildings.Shipyard` | 1 |
| [ShipyardDiscardProductCmd](#shipyarddiscardproductcmd) | `Mafi.Core.Buildings.Shipyard` | 1 |
| [ShipyardMakePrimaryCmd](#shipyardmakeprimarycmd) | `Mafi.Core.Buildings.Shipyard` | 1 |
| [ShipyardSetRepairingCmd](#shipyardsetrepairingcmd) | `Mafi.Core.Buildings.Shipyard` | 2 |
| [ShipyardToggleAutoRepairCmd](#shipyardtoggleautorepaircmd) | `Mafi.Core.Buildings.Shipyard` | 1 |
| [ShipyardToggleUnloadPriorityCmd](#shipyardtoggleunloadprioritycmd) | `Mafi.Core.Buildings.Shipyard` | 1 |
| [ShipyardToggleWorksPauseCmd](#shipyardtoggleworkspausecmd) | `Mafi.Core.Buildings.Shipyard` | 2 |
| [ShipyardWorldEntityConstructionToggle](#shipyardworldentityconstructiontoggle) | `Mafi.Core.Buildings.Shipyard` | 1 |
| [SkipScheduleItemCmd](#skipscheduleitemcmd) | `Mafi.Core.Trains` | 1 |
| [SorterToggleProductCmd](#sortertoggleproductcmd) | `Mafi.Core.Factory.Sorters` | 1 |
| [SortingPlantSetBlockedProductAlertCmd](#sortingplantsetblockedproductalertcmd) | `Mafi.Core.Buildings.OreSorting` | 1 |
| [StackerTowerSetDumpRadiusCmd](#stackertowersetdumpradiuscmd) | `Mafi.Core.Factory.Transports` | 1 |
| [StackerTowerSetFullAlertActiveCmd](#stackertowersetfullalertactivecmd) | `Mafi.Core.Factory.Transports` | 1 |
| [StackerTowerSetMaxSegmentsCmd](#stackertowersetmaxsegmentscmd) | `Mafi.Core.Factory.Transports` | 1 |
| [StartDeconstructionOfStaticEntityCmd](#startdeconstructionofstaticentitycmd) | `Mafi.Core.Entities.Static.Commands` | 1 |
| [StorageAddAllowedTruckGroupCmd](#storageaddallowedtruckgroupcmd) | `Mafi.Core.Buildings.Storages` | 1 |
| [StorageAlertSetEnabledCmd](#storagealertsetenabledcmd) | `Mafi.Core.Buildings.Storages` | 1 |
| [StorageAlertSetThresholdCmd](#storagealertsetthresholdcmd) | `Mafi.Core.Buildings.Storages` | 1 |
| [StorageDisableLogisticsToggleCmd](#storagedisablelogisticstogglecmd) | `Mafi.Core.Buildings.Storages` | 1 |
| [StorageRemoveAllowedTruckGroupCmd](#storageremoveallowedtruckgroupcmd) | `Mafi.Core.Buildings.Storages` | 1 |
| [StorageSetProductCmd](#storagesetproductcmd) | `Mafi.Core.Buildings.Storages` | 1 |
| [StorageSetSliderStepCmd](#storagesetsliderstepcmd) | `Mafi.Core.Buildings.Storages` | 2 |
| [ToggleConstructionPriorityCmd](#toggleconstructionprioritycmd) | `Mafi.Core.Entities.Static.Commands` | 1 |
| [ToggleContractCmd](#togglecontractcmd) | `Mafi.Core.World.Contracts` | 1 |
| [ToggleDefaultLogisticsMode](#toggledefaultlogisticsmode) | `Mafi.Core.Entities` | 1 |
| [ToggleEnabledCmd](#toggleenabledcmd) | `Mafi.Core.Entities` | 1 |
| [ToggleEnforceAssignedVehiclesForEntityCmd](#toggleenforceassignedvehiclesforentitycmd) | `Mafi.Core.Buildings.Storages` | 1 |
| [ToggleFuelStationTrucksAllowedToRefuelCmd](#togglefuelstationtrucksallowedtorefuelcmd) | `Mafi.Core.Buildings.FuelStations` | 1 |
| [ToggleFullBufferNotificationCmd](#togglefullbuffernotificationcmd) | `Mafi.Core.Buildings.Farms` | 1 |
| [ToggleLoadUnloadTrainScheduleItemCmd](#toggleloadunloadtrainscheduleitemcmd) | `Mafi.Core.Trains` | 1 |
| [ToggleLogisticsZoneConstructionCmd](#togglelogisticszoneconstructioncmd) | `Mafi.Core.Vehicles` | 1 |
| [ToggleMechGeneratorAutoBalanceCmd](#togglemechgeneratorautobalancecmd) | `Mafi.Base.Prototypes.Machines.PowerGenerators` | 1 |
| [TogglePartialTrucksLoadCmd](#togglepartialtrucksloadcmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [ToggleRocketCountdownMuteCmd](#togglerocketcountdownmutecmd) | `Mafi.Core.SpaceProgram` | 1 |
| [ToggleScrapTrainAtNearestDepotCmd](#togglescraptrainatnearestdepotcmd) | `Mafi.Core.Trains` | 1 |
| [ToggleSpaceStationCrewEnabledCmd](#togglespacestationcrewenabledcmd) | `Mafi.Core.SpaceProgram` | 1 |
| [ToggleStaticEntityConstructionCmd](#togglestaticentityconstructioncmd) | `Mafi.Core.Entities.Static.Commands` | 1 |
| [ToggleTrainPausedCmd](#toggletrainpausedcmd) | `Mafi.Core.Trains` | 1 |
| [ToggleTrainStationAllowedFuelCmd](#toggletrainstationallowedfuelcmd) | `Mafi.Core.Trains` | 1 |
| [ToggleTrainStationModuleLoadUnloadCmd](#toggletrainstationmoduleloadunloadcmd) | `Mafi.Core.Trains` | 1 |
| [ToggleTrainStationStorageLinkCmd](#toggletrainstationstoragelinkcmd) | `Mafi.Core.Trains` | 1 |
| [ToggleVehicleScrapCmd](#togglevehiclescrapcmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [TradeDockToggleUnloadPriorityCmd](#tradedocktoggleunloadprioritycmd) | `Mafi.Core.Buildings.Cargo` | 1 |
| [TrainContainsDepartConditionEditCmd](#traincontainsdepartconditioneditcmd) | `Mafi.Core.Trains` | 1 |
| [TrainDurationDepartConditionEditCmd](#traindurationdepartconditioneditcmd) | `Mafi.Core.Trains` | 1 |
| [TrainStationFuelSetFuelCmd](#trainstationfuelsetfuelcmd) | `Mafi.Base.Prototypes.Trains` | 1 |
| [TrainStationModuleClearProductCmd](#trainstationmoduleclearproductcmd) | `Mafi.Core.Trains` | 1 |
| [TrainStationModuleQuickRemoveProductCmd](#trainstationmodulequickremoveproductcmd) | `Mafi.Core.Trains` | 1 |
| [TrainStationModuleSetProductCmd](#trainstationmodulesetproductcmd) | `Mafi.Core.Trains` | 1 |
| [TruckConstructionRuleSetCmd](#truckconstructionrulesetcmd) | `Mafi.Core.Vehicles` | 1 |
| [TruckJobsAllowCmd](#truckjobsallowcmd) | `Mafi.Core.Vehicles` | 1 |
| [TruckJobsForbidCmd](#truckjobsforbidcmd) | `Mafi.Core.Vehicles` | 1 |
| [TryTransformEntityCmd](#trytransformentitycmd) | `Mafi.Core.Entities.Static.Commands` | 1 |
| [UnassignVehicleCmd](#unassignvehiclecmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [UnassignVehicleFromEntityCmd](#unassignvehiclefromentitycmd) | `Mafi.Core.Vehicles.Commands` | 1 |
| [UpdateTrainStationArrivalRuleCmd](#updatetrainstationarrivalrulecmd) | `Mafi.Core.Trains` | 1 |
| [WellPumpAlertSetEnabledCmd](#wellpumpalertsetenabledcmd) | `Mafi.Core.Factory.Machines` | 1 |
| [WorldMapEntityCancelRepairCmd](#worldmapentitycancelrepaircmd) | `Mafi.Core.World` | 1 |
| [WorldMapEntityStartRepairCmd](#worldmapentitystartrepaircmd) | `Mafi.Core.World` | 1 |
| [WorldMapEntityUpgradeCmd](#worldmapentityupgradecmd) | `Mafi.Core.World` | 1 |
| [WorldMapSettlementAdoptPopsCmd](#worldmapsettlementadoptpopscmd) | `Mafi.Core.World` | 1 |
| [ZipperSetForceEvenInputsCmd](#zippersetforceeveninputscmd) | `Mafi.Core.Factory.Zippers` | 1 |
| [ZipperSetForceEvenOutputsCmd](#zippersetforceevenoutputscmd) | `Mafi.Core.Factory.Zippers` | 1 |
| [ZipperSetPriorityPortsCmd](#zippersetpriorityportscmd) | `Mafi.Core.Factory.Zippers` | 1 |

## AcceptLoanCmd

Namespace: `Mafi.Core.World.Loans`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `product`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `toBorrow`: game type `Quantity`.
  JSON hint: `int`.
- `yearsTotal`: game type `int`.

## AddEntityToScheduleItemCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItem`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `priority`: game type `int`.

## AddLaunchPadCargoBufferCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `launchPadId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## AddNewScheduleItemToTrainLineCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainLineId`: game type `TrainLineId`.
  JSON hint: `int`.
- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `priority`: game type `int`.
- `index`: game type `int`.
  Default: `-1`.
  New index, when negative, new item will be added to the end of the schedule.

## AddSurfaceDecalCmd

Namespace: `Mafi.Core.Terrain.Designation`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `protoId`: game type `Proto.ID`.
  JSON hint: `string`.
- `area`: game type `RectangleTerrainArea2i`.
  JSON hint: `{ origin: { x: int, y: int } | ..., size: { x: int, y: int } | ... }`.
- `rotation`: game type `Rotation90`.
  JSON hint: `{ angleIndex: int } | { dx: int, dy: int } | { direction: { x: int, y: int } }`.
  Default: `{"angleIndex": 0}`.
- `isReflected`: game type `bool`.
  Default: `false`.
- `colorKey`: game type `int`.
  Default: `0`.

## AddTrainTrackPillarCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `blockIdx`: game type `int`.

## AddTransportPillarCmd

Namespace: `Mafi.Core.Factory.Transports`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `transportId`: game type `EntityId`.
  JSON hint: `int`.
- `supportTileIndex`: game type `int`.

## AddVehicleReplacementTaskCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `currentProtoId`: game type `DynamicEntityProto.ID`.
  JSON hint: `string`.
- `replacementProtoId`: game type `DynamicEntityProto.ID`.
  JSON hint: `string`.
- `zoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.
- `vehicleDepotId`: game type `EntityId?`.
  JSON hint: `int or null`.
  Default: `null`.
- `unassignedOnly`: game type `bool`.
- `assigneeId`: game type `EntityId?`.
  JSON hint: `int or null`.
  Default: `null`.
- `limit`: game type `int`.

## AddVehicleToBuildQueueCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

Requests assembly of vehicle from the given depot depot.

### Constructor 1

- `protoId`: game type `DynamicEntityProto.ID`.
  JSON hint: `string`.
- `vehicleDepotId`: game type `EntityId`.
  JSON hint: `int`.
- `count`: game type `int`.
  Default: `1`.

## AnimalFarmSetSlaughterLimitCmd

Namespace: `Mafi.Core.Buildings.Farms`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `farmId`: game type `EntityId`.
  JSON hint: `int`.
- `slaughterSliderStep`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.

## AnimalFarmToggleGrowthPauseCmd

Namespace: `Mafi.Core.Buildings.Farms`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `farmId`: game type `EntityId`.
  JSON hint: `int`.

## AssignProductToSlotCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.
- `slot`: game type `int`.

## AssignTrainLineToTrainCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.
- `trainLineId`: game type `TrainLineIdOrNone`.
  JSON hint: `int`.
  Set None to unassign.

## AssignTrainLineToUnfinishedTrainCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `depotId`: game type `EntityId`.
  JSON hint: `int`.
- `queueIndex`: game type `int`.
- `trainLineId`: game type `TrainLineIdOrNone`.
  JSON hint: `int`.
  Set None to unassign.
- `trainNetworkId`: game type `TrainNetworkIdOrNone`.
  JSON hint: `int`.
  Default: `0`.

## AssignTrainToNetworkCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.
- `networkId`: game type `TrainNetworkIdOrNone`.
  JSON hint: `int`.

## AssignVehicleToEntityCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

Assigns a concrete vehicle to an entity.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.
- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## AssignVehicleTypeToEntityCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

Assigns a vehicle type to an entity.

### Constructor 1

- `vehicleId`: game type `DynamicEntityProto.ID`.
  JSON hint: `string`.
- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `count`: game type `int`.
  Default: `1`.
- `zoneId`: game type `LogisticsZoneId?`.
  JSON hint: `int or null`.
  Default: `null`.

## BringAsteroidToOrbitCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `asteroidId`: game type `AsteroidId`.
  JSON hint: `int`.

## BuildOrUpgradeSpaceStationCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## BuildVehicleForeverCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

Build vehicle forever, set null ID to clear.

### Constructor 1

- `protoId`: game type `DynamicEntityProto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.
- `vehicleDepotId`: game type `EntityId`.
  JSON hint: `int`.

## CancelBuildOrUpgradeOfSpaceStationCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## CancelReplaceVehicleCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.

## CancelTrainBuildCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `depotId`: game type `EntityId`.
  JSON hint: `int`.
- `queueIndex`: game type `int`.

## CancelTrainJobCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.

## CancelTrainReplacementCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.

## CargoDepotSetFuelSliderStepCmd

Namespace: `Mafi.Core.Buildings.Cargo`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `cargoDepotId`: game type `EntityId`.
  JSON hint: `int`.
- `importStep`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.
  Negative if undefined.
- `exportStep`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.
  Negative if undefined.

## CargoShipReplaceFuelCmd

Namespace: `Mafi.Core.Buildings.Cargo.Modules`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `cargoShipId`: game type `EntityId`.
  JSON hint: `int`.
- `fuelId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## ChangeSurfaceDecalColorCmd

Namespace: `Mafi.Core.Terrain.Designation`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `area`: game type `RectangleTerrainArea2i`.
  JSON hint: `{ origin: { x: int, y: int } | ..., size: { x: int, y: int } | ... }`.
- `colorKey`: game type `int`.
  Default: `0`.

## ClearTransportCmd

Namespace: `Mafi.Core.Factory.Transports`. Advertised result: `EntityId`.

No description advertised.

### Constructor 1

- `transportId`: game type `EntityId`.
  JSON hint: `int`.

## ClearUnusedMachineBuffersCmd

Namespace: `Mafi.Core.Factory.Machines`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `machineId`: game type `EntityId`.
  JSON hint: `int`.

## CloneConfigBetweenEntitiesCmd

Namespace: `Mafi.Core.Entities.Static.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `sourceEntityId`: game type `EntityId`.
  JSON hint: `int`.
- `targetEntityId`: game type `EntityId`.
  JSON hint: `int`.

## CreateNewLogisticsZoneCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## CreateNewTrainLineCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `TrainLineId`.

No description advertised.

### Constructor 1

No parameters advertised.

## CreateNewTrainNetworkCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `TrainNetworkId`.

No description advertised.

### Constructor 1

No parameters advertised.

## CreateStaticEntityCmd

Namespace: `Mafi.Core.Entities.Static.Commands`. Advertised result: `EntityId`.

No description advertised.

### Constructor 1

- `protoId`: game type `StaticEntityProto.ID`.
  JSON hint: `string`.
- `transform`: game type `TileTransform`.
  JSON hint: `{ position: { x: int, y: int, z: int } | ..., rotation?: { dx: int, dy: int } | ..., isReflected?: bool } | { position: { x: int, y: int, z: int } | ..., rotFlip: int | ... }`.
- `allowValidationSuppression`: game type `bool`.
  Default: `false`.
  Whether this entity can suppress validation, if other conditions are met.

## CreateTrainTrackEntityWithDirectionCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `EntityId`.

No description advertised.

### Constructor 1

- `protoId`: game type `StaticEntityProto.ID`.
  JSON hint: `string`.
- `transform`: game type `TileTransform`.
  JSON hint: `{ position: { x: int, y: int, z: int } | ..., rotation?: { dx: int, dy: int } | ..., isReflected?: bool } | { position: { x: int, y: int, z: int } | ..., rotFlip: int | ... }`.
- `direction`: game type `TrainTrackTrajectoryDirection`.
  JSON hint: `string`.
  Additional metadata: `{"values": ["Unknown", "Forward", "Backward", "Bidirectional"]}`.

## DataCenterToggleRackCmd

Namespace: `Mafi.Core.Factory.Datacenters`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `dataCenterId`: game type `EntityId`.
  JSON hint: `int`.
- `serverRackId`: game type `Proto.ID`.
  JSON hint: `string`.
- `difference`: game type `int`.
  Negative if removal, positive if addition.

## DeconstructTransportSegmentCmd

Namespace: `Mafi.Core.Factory.Transports`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `transportId`: game type `EntityId`.
  JSON hint: `int`.
- `startPosition`: game type `Tile3i`.
  JSON hint: `{ x: int, y: int, z: int } | { vector: { x: int, y: int } | ..., z: int } | { tileCoord: { x: int, y: int, z: int } | ... }`.
- `endPosition`: game type `Tile3i`.
  JSON hint: `{ x: int, y: int, z: int } | { vector: { x: int, y: int } | ..., z: int } | { tileCoord: { x: int, y: int, z: int } | ... }`.
- `quickRemove`: game type `bool`.
  Default: `false`.

## DesignateHarvestedTreesCmd

Namespace: `Mafi.Core.Terrain.Trees`. Advertised result: `bool`.

Adds or removes all trees in the specified area to/from the set of trees to be harvested. The area is represented by rectangle area specified by two tile positions.

### Constructor 1

- `area`: game type `RectangleTerrainArea2i`.
  JSON hint: `{ origin: { x: int, y: int } | ..., size: { x: int, y: int } | ... }`.
- `addToHarvest`: game type `bool`.
  Whether trees are to be added to the set of trees to harvest, or removed.
- `harvestedProductId`: game type `ProductProto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.
  If set, only trees with given harvested product will be selected.

## DiscardAsteroidCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `asteroidId`: game type `AsteroidId`.
  JSON hint: `int`.

## DiscardVehicleCargoCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.

## DowngradeSpaceStationCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## DropAsteroidAtCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `asteroidId`: game type `AsteroidId`.
  JSON hint: `int`.
- `position`: game type `Tile2i`.
  JSON hint: `{ x: int, y: int } | { coord: { x: int, y: int } } | { coord: { x: int, y: int } | ... }`.

## EntityDisableLogisticsToggleCmd

Namespace: `Mafi.Core.Entities.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `isInput`: game type `bool`.
- `mode`: game type `EntityLogisticsMode`.
  JSON hint: `string`.
  Additional metadata: `{"values": ["Auto", "On", "Off"]}`.

## ExcavatorTogglePreferredProductCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `excavatorId`: game type `EntityId`.
  JSON hint: `int`.
- `productToMine`: game type `ProductProto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.

## FarmAssignCropCmd

Namespace: `Mafi.Core.Buildings.Farms`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `farmId`: game type `EntityId`.
  JSON hint: `int`.
- `cropId`: game type `Proto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.
- `scheduleSlot`: game type `int`.

## FarmForceNextSlotCmd

Namespace: `Mafi.Core.Buildings.Farms`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `farmId`: game type `EntityId`.
  JSON hint: `int`.

## FarmHarvestNowCmd

Namespace: `Mafi.Core.Buildings.Farms`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `farmId`: game type `EntityId`.
  JSON hint: `int`.

## FarmSetFertilityTargetCmd

Namespace: `Mafi.Core.Buildings.Farms`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `farmId`: game type `EntityId`.
  JSON hint: `int`.
- `target`: game type `Percent`.
  JSON hint: `number (0.5 is 50%)`.

## FinishBuildOfStaticEntityCmd

Namespace: `Mafi.Core.Entities.Static.Commands`. Advertised result: `EntityId`.

Quick build or quick removal of an entity, paid with Unity.

### Constructor 1

- `id`: game type `EntityId`.
  JSON hint: `int`.

## FleetLoadCrewCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## FleetModificationsCancelCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## FleetToggleAutoReturnCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## FleetUnloadCrewCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## FleetUnloadFuelCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## ForestryTowerSetCutPercentageCmd

Namespace: `Mafi.Core.Buildings.Forestry`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `towerId`: game type `EntityId`.
  JSON hint: `int`.
- `cutPercent`: game type `Percent`.
  JSON hint: `number (0.5 is 50%)`.

## ForestryTowerSetTreeProtoCmd

Namespace: `Mafi.Core.Buildings.Forestry`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `towerId`: game type `EntityId`.
  JSON hint: `int`.
- `groupProtoId`: game type `Proto.ID`.
  JSON hint: `string`.

## GameConsoleCmd

Namespace: `Mafi.Core.Console`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `command`: game type `string`.

## GameSpeedChangeCmd

Namespace: `Mafi.Core.Simulation`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `newSpeedMultiplier`: game type `int`.
  From 1 to MAX_GAME_SPEED. Other values are clamped to this range when the command is processed.

## GoToLocationCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `id`: game type `WorldMapLocId`.
  JSON hint: `int`.
- `reason`: game type `LocationVisitReason`.
  JSON hint: `string`.
  Additional metadata: `{"values": ["General", "LoadCargo", "DeliverCargo"]}`.

## InputCommand

Namespace: `Mafi.Core.Input`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## LaunchRocketCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `launchPadId`: game type `EntityId`.
  JSON hint: `int`.

## MachineBoostToggleCmd

Namespace: `Mafi.Core.Factory.Machines`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `machineId`: game type `EntityId`.
  JSON hint: `int`.

## MachineSetRecipeActiveCmd

Namespace: `Mafi.Core.Factory.Machines`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `machineId`: game type `EntityId`.
  JSON hint: `int`.
- `recipeId`: game type `RecipeProto.ID`.
  JSON hint: `string`.
- `enableRecipe`: game type `bool`.

## MachineToggleRecipeActiveCmd

Namespace: `Mafi.Core.Factory.Machines`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `machineId`: game type `EntityId`.
  JSON hint: `int`.
- `recipeId`: game type `RecipeProto.ID`.
  JSON hint: `string`.

## MakeLoanOverpaymentCmd

Namespace: `Mafi.Core.World.Loans`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `product`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `loanId`: game type `uint`.
  JSON hint: `int`.
- `toPay`: game type `Quantity`.
  JSON hint: `int`.

## MarkGoalAsFinishedCmd

Namespace: `Mafi.Core.Messages.Goals`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `protoId`: game type `Proto.ID`.
  JSON hint: `string`.
- `goalWasSkipped`: game type `bool`.
  Default: `false`.

## MarkMessageAsReadCmd

Namespace: `Mafi.Core.Messages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `protoId`: game type `Proto.ID`.
  JSON hint: `string`.

## MessageNotificationDismissCmd

Namespace: `Mafi.Core.MessageNotifications`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `messageId`: game type `MessageNotificationId`.
  JSON hint: `int`.

## MoveAnimalsCmd

Namespace: `Mafi.Core.Buildings.Farms`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `farmId`: game type `EntityId`.
  JSON hint: `int`.
- `numberToMove`: game type `int`.

## NavigateTrainToCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.
- `targetEntityId`: game type `EntityId`.
  JSON hint: `int`.

## NavigateVehicleToPositionCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.
- `position`: game type `Tile2i`.
  JSON hint: `{ x: int, y: int } | { coord: { x: int, y: int } } | { coord: { x: int, y: int } | ... }`.

## NavigateVehicleToStaticEntityCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.
- `staticEntityId`: game type `EntityId`.
  JSON hint: `int`.

## NavigateVehicleToVehicleCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.
- `goalVehicleId`: game type `EntityId`.
  JSON hint: `int`.

## NotifyOnBattleOpenedCmd

Namespace: `Mafi.Core.Fleet`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## NuclearReactorSetEnrichmentStepCmd

Namespace: `Mafi.Core.Factory.NuclearReactors`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `reactorId`: game type `EntityId`.
  JSON hint: `int`.
- `enrichmentStep`: game type `int`.

## NuclearReactorSetPowerLevelCmd

Namespace: `Mafi.Core.Factory.NuclearReactors`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `reactorId`: game type `EntityId`.
  JSON hint: `int`.
- `powerLevel`: game type `int`.

## NuclearReactorToggleAllowedFuelCmd

Namespace: `Mafi.Core.Factory.NuclearReactors`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `reactorId`: game type `EntityId`.
  JSON hint: `int`.
- `fuelProtoId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## NuclearReactorToggleAutomaticRegulationCmd

Namespace: `Mafi.Core.Factory.NuclearReactors`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `reactorId`: game type `EntityId`.
  JSON hint: `int`.

## NuclearWasteStorageToggleOutputPortCmd

Namespace: `Mafi.Core.Buildings.Storages.NuclearWaste`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.

## PinnedProductReorderCmd

Namespace: `Mafi.Core.Products`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `productToMove`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `newIndex`: game type `int`.

## PinToggleCmd

Namespace: `Mafi.Core.Products`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `productToToggle`: game type `ProductProto.ID`.
  JSON hint: `string`.

## PrepareManualPlantTreeCmd

Namespace: `Mafi.Core.Terrain.Trees`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `protoId`: game type `Proto.ID`.
  JSON hint: `string`.
- `transform`: game type `TileTransform`.
  JSON hint: `{ position: { x: int, y: int, z: int } | ..., rotation?: { dx: int, dy: int } | ..., isReflected?: bool } | { position: { x: int, y: int, z: int } | ..., rotFlip: int | ... }`.

## QuickBuildCurrentTrainCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `depotId`: game type `EntityId`.
  JSON hint: `int`.

## QuickBuildCurrentVehicleCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

Requests to quick build current vehicle and pay for it via unity.

### Constructor 1

- `vehicleDepotId`: game type `EntityId`.
  JSON hint: `int`.

## QuickRemoveEntityRefundCmd

Namespace: `Mafi.Core.Entities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## QuickRemoveFromEntityCmd

Namespace: `Mafi.Core.Entities.Static`. Advertised result: `EntityId`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## QuickRemovePropsCmd

Namespace: `Mafi.Core.Terrain.Props`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `area`: game type `RectangleTerrainArea2i`.
  JSON hint: `{ origin: { x: int, y: int } | ..., size: { x: int, y: int } | ... }`.

## QuickRepairEntityCmd

Namespace: `Mafi.Core.Maintenance`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## QuickRepairTrainCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## QuickTradeCmd

Namespace: `Mafi.Core.World.QuickTrade`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `tradeId`: game type `Proto.ID`.
  JSON hint: `string`.

## RecoverOceanAccessCmd

Namespace: `Mafi.Core.Entities.Static`. Advertised result: `RecoverOceanResult`.

No description advertised.

### Constructor 1

- `entityWithOceanAreas`: game type `EntityId`.
  JSON hint: `int`.
- `maxTilesToRecover`: game type `int`.

## RecoverShipCmd

Namespace: `Mafi.Core.Entities.Ships`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `shipId`: game type `EntityId`.
  JSON hint: `int`.

## RecoverTrainCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.
- `forcePause`: game type `bool`.
  Default: `false`.
- `targetDepot`: game type `EntityId?`.
  JSON hint: `int or null`.
  Default: `null`.

## RecoverVehicleCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.

## RefuelTrainCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.

## RemoveDepartConditionCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItem`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `rootId`: game type `EntityId`.
  JSON hint: `int`.
- `conditionIndex`: game type `int`.

## RemoveEntityFromScheduleItemCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItem`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## RemoveLaunchPadCargoBufferCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `launchPadId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## RemoveLogisticsZoneCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `zoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.

## RemoveManualPlantTreeCmd

Namespace: `Mafi.Core.Terrain.Trees`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `treeId`: game type `TreeId`.
  JSON hint: `{ position: { x: int, y: int } }`.

## RemovePathfindingRestrictionCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `waypointId`: game type `EntityId`.
  JSON hint: `int`.
- `restrictionIndex`: game type `int`.

## RemoveSurfaceDecalCmd

Namespace: `Mafi.Core.Terrain.Designation`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `area`: game type `RectangleTerrainArea2i`.
  JSON hint: `{ origin: { x: int, y: int } | ..., size: { x: int, y: int } | ... }`.

## RemoveTrainLineCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainLineId`: game type `TrainLineId`.
  JSON hint: `int`.

## RemoveTrainLineScheduleItemCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItem`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.

## RemoveTrainNetworkCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.

## RemoveTrainTrackPillarCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `pillarId`: game type `EntityId`.
  JSON hint: `int`.

## RemoveTransportPillarCmd

Namespace: `Mafi.Core.Factory.Transports`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `pillarId`: game type `EntityId`.
  JSON hint: `int`.

## RemoveVehicleFromBuildQueueCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

Requests assembly of vehicle from the given depot depot.

### Constructor 1

- `index`: game type `int`.
- `vehicleDepotId`: game type `EntityId`.
  JSON hint: `int`.

## RemoveVehicleReplacementTaskCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `taskId`: game type `uint`.
  JSON hint: `int`.

## RenameLogisticsZoneCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `zoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.
- `name`: game type `string`.

## RenameTrainLineCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainLineId`: game type `TrainLineId`.
  JSON hint: `int`.
- `name`: game type `string`.

## RenameTrainNetworkCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `name`: game type `string`.

## ReorderDepartConditionCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItemId`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `rootId`: game type `EntityId`.
  JSON hint: `int`.
- `conditionIndex`: game type `int`.
- `newConditionIndex`: game type `int`.

## ReorderLaunchPadCargoBufferCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `launchPadId`: game type `EntityId`.
  JSON hint: `int`.
- `oldIndex`: game type `int`.
- `newIndexAfterRemove`: game type `int`.

## ReorderRecipeCmd

Namespace: `Mafi.Core.Factory.Machines`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `machineId`: game type `EntityId`.
  JSON hint: `int`.
- `oldIndex`: game type `int`.
- `newIndexAfterRemove`: game type `int`.

## ReorderTrainLineScheduleItemCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItem`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `newIndex`: game type `int`.

## ReplaceEntityInScheduleCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItem`: game type `TrainScheduleItemId?`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int } or null`.
  Default: `null`.
  Schedule item to replace the station in. If null, will replace that station in every line.
- `oldEntityId`: game type `EntityId`.
  JSON hint: `int`.
- `newEntityId`: game type `EntityId`.
  JSON hint: `int`.

## ReplaceVehicleCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.
- `targetProtoId`: game type `DynamicEntityProto.ID`.
  JSON hint: `string`.

## ResearchQueueDequeueCmd

Namespace: `Mafi.Core.Research`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `nodeId`: game type `ResearchNodeProto.ID`.
  JSON hint: `string`.
- `isEnqueue`: game type `bool`.

## ResearchStartCmd

Namespace: `Mafi.Core.Research`. Advertised result: `bool`.

Command to start a research of the given node from the research tree.

### Constructor 1

- `nodeId`: game type `ResearchNodeProto.ID`.
  JSON hint: `string`.

## ResearchStopCmd

Namespace: `Mafi.Core.Research`. Advertised result: `bool`.

Command to stop the current research.

### Constructor 1

No parameters advertised.

## ReverseLiftCmd

Namespace: `Mafi.Core.Factory.Lifts`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `liftId`: game type `EntityId`.
  JSON hint: `int`.

## ReverseTransportCmd

Namespace: `Mafi.Core.Factory.Transports`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `transportId`: game type `EntityId`.
  JSON hint: `int`.

## RuinsScrapCmd

Namespace: `Mafi.Core.Buildings.RuinedBuildings`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `isScrapping`: game type `bool`.

### Constructor 2

- `ruinsId`: game type `EntityId`.
  JSON hint: `int`.
- `isScrapping`: game type `bool`.

## ScanForNewAsteroidCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## ScrapTrainCarCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `depotId`: game type `EntityId`.
  JSON hint: `int`.
- `carProtoId`: game type `DynamicEntityProto.ID`.
  JSON hint: `string`.

## SetArrivalRuleAlwaysAllowCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `alwaysAllow`: game type `bool`.

## SetArrivalRuleNetworkPriorityCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `priority`: game type `int`.

## SetArrivalRuleNetworkThresholdCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `threshold`: game type `Percent`.
  JSON hint: `number (0.5 is 50%)`.

## SetBillboardColorCmd

Namespace: `Mafi.Base.Prototypes.Buildings`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `primaryColor`: game type `ColorRgba`.
  JSON hint: `int | { r: int, g: int, b: int, a?: int } | { rgb: int, a?: int } | { r: number, g: number, b: number, a?: number }`.
- `secondaryColor`: game type `ColorRgba`.
  JSON hint: `int | { r: int, g: int, b: int, a?: int } | { rgb: int, a?: int } | { r: number, g: number, b: number, a?: number }`.

## SetBridgeLaneLayoutCmd

Namespace: `Mafi.Core.Bridges`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `bridgeId`: game type `EntityId`.
  JSON hint: `int`.
- `laneIndex`: game type `int`.
- `laneProtoId`: game type `Proto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.

## SetConstructionPausedCmd

Namespace: `Mafi.Core.Entities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `isPaused`: game type `bool?`.
  JSON hint: `bool or null`.
  Default: `null`.

## SetConstructionPriorityCmd

Namespace: `Mafi.Core.Entities.Commands`. Advertised result: `EntityId`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `priority`: game type `int`.

## SetCustomPriorityCmd

Namespace: `Mafi.Core.Entities.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `priorityId`: game type `string`.
- `priority`: game type `int`.

## SetDepartConditionCombineMethodCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItem`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `rootId`: game type `EntityId`.
  JSON hint: `int`.
- `conditionIndex`: game type `int`.
- `combineAsOr`: game type `bool`.

## SetDoNotSkipThisTrainStationCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `rootStationId`: game type `EntityId`.
  JSON hint: `int`.
- `doNotSkip`: game type `bool`.

## SetDumpHeightOffsetCmd

Namespace: `Mafi.Core.Entities.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `depth`: game type `ThicknessTilesI`.
  JSON hint: `int`.

## SetElectricityGenerationPriorityCmd

Namespace: `Mafi.Core.Factory.ElectricPower`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `priority`: game type `int`.

## SetEntityEnabledCmd

Namespace: `Mafi.Core.Entities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `isEnabled`: game type `bool`.

## SetEntityNameCmd

Namespace: `Mafi.Core.Entities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `title`: game type `string`.

## SetGeneralPriorityCmd

Namespace: `Mafi.Core.Entities.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `priority`: game type `int`.

## SetGlobalPriorityCmd

Namespace: `Mafi.Core.Entities.Priorities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `priorityId`: game type `string`.
- `priority`: game type `int`.

## SetIsElectricitySurplusConsumerCmd

Namespace: `Mafi.Core.Factory.ElectricPower`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `isSurplusConsumer`: game type `bool`.

## SetIsElectricitySurplusGeneratorCmd

Namespace: `Mafi.Core.Factory.ElectricPower`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `isSurplusGenerator`: game type `bool`.

## SetLoanBufferPriorityCmd

Namespace: `Mafi.Core.World.Loans`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `loanId`: game type `uint`.
  JSON hint: `int`.
- `priority`: game type `int`.

## SetLogisticsZoneColorCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `zoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.
- `colorIndex`: game type `int`.

## SetNetworkCargoStationCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `add`: game type `bool`.

## SetNetworkFuelStationCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `add`: game type `bool`.

## SetNetworkRefuelThresholdCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `threshold`: game type `Percent`.
  JSON hint: `number (0.5 is 50%)`.

## SetNetworkWaitingBayCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `add`: game type `bool`.

## SetOfficeComputingBoostStepCmd

Namespace: `Mafi.Core.Buildings.Offices`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `officeId`: game type `EntityId`.
  JSON hint: `int`.
- `step`: game type `int`.

## SetOfficeFocusStepCmd

Namespace: `Mafi.Core.Buildings.Offices`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `focusId`: game type `Proto.ID`.
  JSON hint: `string`.
- `diff`: game type `int`.

## SetOrbitCargoLimitCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `limit`: game type `Quantity`.
  JSON hint: `int`.

## SetPlanningModeEnabledCmd

Namespace: `Mafi.Core.Entities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `isEnabled`: game type `bool`.

## SetRocketAutoLaunchCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `launchPadId`: game type `EntityId`.
  JSON hint: `int`.
- `autoLaunch`: game type `bool`.

## SetShiftsCountForMineCmd

Namespace: `Mafi.Core.World.Entities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `shiftsCount`: game type `int`.

## SetSimPauseStateCmd

Namespace: `Mafi.Core.Simulation`. Advertised result: `bool`.

Pauses or resumes the game.

### Constructor 1

- `isPaused`: game type `bool`.

## SetStationRequireFullServiceOnArrivalCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `requireFullTransfer`: game type `bool`.

## SetTrainLineColorApplicationCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainLineId`: game type `TrainLineId`.
  JSON hint: `int`.
- `applyLineColorToTrains`: game type `bool`.

## SetTrainLineColorCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainLineId`: game type `TrainLineId`.
  JSON hint: `int`.
- `color`: game type `TrainLineColor`.
  JSON hint: `{ primary: { r: int, g: int, b: int, a?: int } | ..., secondary: { r: int, g: int, b: int, a?: int } | ..., trainColor: int | ... }`.

## SetTrainLineLocoColorModeCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainLineId`: game type `TrainLineId`.
  JSON hint: `int`.
- `mode`: game type `LocoColorMode`.
  JSON hint: `string`.
  Additional metadata: `{"values": ["SameAsLine", "NoOverride", "Custom"]}`.

## SetTrainLineLocoCustomColorCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainLineId`: game type `TrainLineId`.
  JSON hint: `int`.
- `color`: game type `TrainLineColor`.
  JSON hint: `{ primary: { r: int, g: int, b: int, a?: int } | ..., secondary: { r: int, g: int, b: int, a?: int } | ..., trainColor: int | ... }`.

## SetTrainNetworkColorApplicationCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `applyLineColorToTrains`: game type `bool`.

## SetTrainNetworkColorCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `color`: game type `TrainLineColor`.
  JSON hint: `{ primary: { r: int, g: int, b: int, a?: int } | ..., secondary: { r: int, g: int, b: int, a?: int } | ..., trainColor: int | ... }`.

## SetTrainNetworkLocoColorModeCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `mode`: game type `LocoColorMode`.
  JSON hint: `string`.
  Additional metadata: `{"values": ["SameAsLine", "NoOverride", "Custom"]}`.

## SetTrainNetworkLocoCustomColorCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `networkId`: game type `TrainNetworkId`.
  JSON hint: `int`.
- `color`: game type `TrainLineColor`.
  JSON hint: `{ primary: { r: int, g: int, b: int, a?: int } | ..., secondary: { r: int, g: int, b: int, a?: int } | ..., trainColor: int | ... }`.

## SetTrainSchedulePriority

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItemId`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `priority`: game type `int`.
- `rootId`: game type `EntityId`.
  JSON hint: `int`.

## SetTrainScheduleSkipIfCannotArriveCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItemId`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `skipIfCannotArrive`: game type `bool`.

## SetTrainScheduleSkipIfHighFuelCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItemId`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `skipIfFuelHigherThan`: game type `Percent`.
  JSON hint: `number (0.5 is 50%)`.

## SetTrainScheduleSkipIfNextCanArriveCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItemId`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `skipIfNextCanArrive`: game type `bool`.

## SetTrainStationTrainLimitCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `trainLimit`: game type `int`.

## SetTrainTrackBufferTurnaroundCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

Sets AllowsTurnaround of a buffer.

### Constructor 1

- `bufferId`: game type `EntityId`.
  JSON hint: `int`.
- `allowsTurnaround`: game type `bool`.

## SetVehicleDepotTargetZone

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleDepotId`: game type `EntityId`.
  JSON hint: `int`.
- `zoneId`: game type `LogisticsZoneId?`.
  JSON hint: `int or null`.
  Default: `null`.

## SetVehicleLogisticsZoneCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `zoneId`: game type `LogisticsZoneId?`.
  JSON hint: `int or null`.
  Default: `null`.
- `truckId`: game type `EntityId`.
  JSON hint: `int`.

## SetWagonProductFilterCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.
- `wagonIndex`: game type `int`.
- `subCarIndex`: game type `int`.
- `productId`: game type `ProductProto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.

## ShipayardSetFuelSliderStepCmd

Namespace: `Mafi.Core.Buildings.Shipyard`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `shipyardId`: game type `EntityId`.
  JSON hint: `int`.
- `importStep`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.
  Negative if undefined.
- `exportStep`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.
  Negative if undefined.

## ShipyardDiscardProductCmd

Namespace: `Mafi.Core.Buildings.Shipyard`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `shipyardId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## ShipyardMakePrimaryCmd

Namespace: `Mafi.Core.Buildings.Shipyard`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `shipyardId`: game type `EntityId`.
  JSON hint: `int`.

## ShipyardSetRepairingCmd

Namespace: `Mafi.Core.Buildings.Shipyard`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `isRepairing`: game type `bool`.

### Constructor 2

- `shipyardId`: game type `EntityId`.
  JSON hint: `int`.
- `isRepairing`: game type `bool`.

## ShipyardToggleAutoRepairCmd

Namespace: `Mafi.Core.Buildings.Shipyard`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `shipyardId`: game type `EntityId`.
  JSON hint: `int`.

## ShipyardToggleUnloadPriorityCmd

Namespace: `Mafi.Core.Buildings.Shipyard`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `shipyardId`: game type `EntityId`.
  JSON hint: `int`.

## ShipyardToggleWorksPauseCmd

Namespace: `Mafi.Core.Buildings.Shipyard`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

### Constructor 2

- `shipyardId`: game type `EntityId`.
  JSON hint: `int`.

## ShipyardWorldEntityConstructionToggle

Namespace: `Mafi.Core.Buildings.Shipyard`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `shipyardId`: game type `EntityId`.
  JSON hint: `int`.
- `worldEntityIdToConstruct`: game type `EntityId`.
  JSON hint: `int`.

## SkipScheduleItemCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.

## SorterToggleProductCmd

Namespace: `Mafi.Core.Factory.Sorters`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `sorterId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## SortingPlantSetBlockedProductAlertCmd

Namespace: `Mafi.Core.Buildings.OreSorting`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `sortingPlantId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `isAlertEnabled`: game type `bool`.

## StackerTowerSetDumpRadiusCmd

Namespace: `Mafi.Core.Factory.Transports`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `radiusLeft`: game type `RelTile1i?`.
  JSON hint: `int or null`.
  Default: `null`.
- `radiusRight`: game type `RelTile1i?`.
  JSON hint: `int or null`.
  Default: `null`.

## StackerTowerSetFullAlertActiveCmd

Namespace: `Mafi.Core.Factory.Transports`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `active`: game type `bool`.

## StackerTowerSetMaxSegmentsCmd

Namespace: `Mafi.Core.Factory.Transports`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `segmentsCount`: game type `int`.

## StartDeconstructionOfStaticEntityCmd

Namespace: `Mafi.Core.Entities.Static.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `reason`: game type `EntityRemoveReason`.
  JSON hint: `string`.
  Additional metadata: `{"values": ["Remove", "Collapse"]}`.
- `isAreaRemove`: game type `bool`.
  Default: `false`.
  True when this deconstruction is part of an area removal (bulldozing a region). Used so that a waypoint in the area also clears the rail line under it instead of leaving the plain replacement track an individual delete would.

## StorageAddAllowedTruckGroupCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `truckProtoId`: game type `Proto.ID`.
  JSON hint: `string`.

## StorageAlertSetEnabledCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `isEnabled`: game type `bool`.
- `isAbove`: game type `bool`.

## StorageAlertSetThresholdCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `value`: game type `Percent`.
  JSON hint: `number (0.5 is 50%)`.
- `isAbove`: game type `bool`.

## StorageDisableLogisticsToggleCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `isInput`: game type `bool`.
- `isDisabled`: game type `bool`.

## StorageRemoveAllowedTruckGroupCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `truckProtoId`: game type `Proto.ID`.
  JSON hint: `string`.

## StorageSetProductCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## StorageSetSliderStepCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

Sets the sliders of a storage. Steps above MAX_STEPS are clamped to it when the command is processed.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `importStep`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.
  Negative if undefined.
- `exportStep`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.
  Negative if undefined.
- `transportFrom`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.
  Negative if undefined.
- `transportUntil`: game type `int?`.
  JSON hint: `int or null`.
  Default: `null`.
  Negative if undefined.

### Constructor 2

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `importUntil`: game type `Percent?`.
  JSON hint: `number (0.5 is 50%) or null`.
  Default: `null`.
- `exportFrom`: game type `Percent?`.
  JSON hint: `number (0.5 is 50%) or null`.
  Default: `null`.
- `transportFrom`: game type `Percent?`.
  JSON hint: `number (0.5 is 50%) or null`.
  Default: `null`.
  Negative if undefined.
- `transportUntil`: game type `Percent?`.
  JSON hint: `number (0.5 is 50%) or null`.
  Default: `null`.
  Negative if undefined.

## ToggleConstructionPriorityCmd

Namespace: `Mafi.Core.Entities.Static.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## ToggleContractCmd

Namespace: `Mafi.Core.World.Contracts`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `contractId`: game type `Proto.ID`.
  JSON hint: `string`.

## ToggleDefaultLogisticsMode

Namespace: `Mafi.Core.Entities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## ToggleEnabledCmd

Namespace: `Mafi.Core.Entities`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## ToggleEnforceAssignedVehiclesForEntityCmd

Namespace: `Mafi.Core.Buildings.Storages`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `storageId`: game type `EntityId`.
  JSON hint: `int`.
- `isEnforced`: game type `bool`.

## ToggleFuelStationTrucksAllowedToRefuelCmd

Namespace: `Mafi.Core.Buildings.FuelStations`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `fuelStationId`: game type `EntityId`.
  JSON hint: `int`.

## ToggleFullBufferNotificationCmd

Namespace: `Mafi.Core.Buildings.Farms`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `farmId`: game type `EntityId`.
  JSON hint: `int`.

## ToggleLoadUnloadTrainScheduleItemCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItemId`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `isUnload`: game type `bool`.
- `disable`: game type `bool`.

## ToggleLogisticsZoneConstructionCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `zoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.
- `constructionZoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.

## ToggleMechGeneratorAutoBalanceCmd

Namespace: `Mafi.Base.Prototypes.Machines.PowerGenerators`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## TogglePartialTrucksLoadCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## ToggleRocketCountdownMuteCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `launchPadId`: game type `EntityId`.
  JSON hint: `int`.

## ToggleScrapTrainAtNearestDepotCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.

## ToggleSpaceStationCrewEnabledCmd

Namespace: `Mafi.Core.SpaceProgram`. Advertised result: `bool`.

No description advertised.

### Constructor 1

No parameters advertised.

## ToggleStaticEntityConstructionCmd

Namespace: `Mafi.Core.Entities.Static.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## ToggleTrainPausedCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `trainId`: game type `TrainId`.
  JSON hint: `int`.

## ToggleTrainStationAllowedFuelCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `rootStationId`: game type `EntityId`.
  JSON hint: `int`.
- `fuelId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## ToggleTrainStationModuleLoadUnloadCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `load`: game type `bool?`.
  JSON hint: `bool or null`.
  Default: `null`.

## ToggleTrainStationStorageLinkCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `storageId`: game type `EntityId`.
  JSON hint: `int`.

## ToggleVehicleScrapCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.

## TradeDockToggleUnloadPriorityCmd

Namespace: `Mafi.Core.Buildings.Cargo`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `tradeDockId`: game type `EntityId`.
  JSON hint: `int`.

## TrainContainsDepartConditionEditCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItemId`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `rootId`: game type `EntityId`.
  JSON hint: `int`.
- `conditionIndex`: game type `int`.
- `useInferiorToInsteadOfSuperiorTo`: game type `bool?`.
  JSON hint: `bool or null`.
  Default: `null`.
- `mode`: game type `TrainContainsDepartCondition.ComparisonMode?`.
  JSON hint: `string or null`.
  Default: `null`.
  Additional metadata: `{"values": ["AllProducts", "AnyProduct", "SpecificProduct"]}`.
- `percent`: game type `Percent?`.
  JSON hint: `number (0.5 is 50%) or null`.
  Default: `null`.
- `productId`: game type `ProductProto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.
- `productIdSpecified`: game type `bool`.
  Default: `false`.
  Whether to interpret the Product field being null as clear or unset.
- `isSimplified`: game type `bool?`.
  JSON hint: `bool or null`.
  Default: `null`.

## TrainDurationDepartConditionEditCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `scheduleItem`: game type `TrainScheduleItemId`.
  JSON hint: `{ trainLineId: int, scheduleIndex: int }`.
- `rootId`: game type `EntityId`.
  JSON hint: `int`.
- `conditionIndex`: game type `int`.
- `delay`: game type `Duration?`.
  JSON hint: `int or null`.
  Default: `null`.

## TrainStationFuelSetFuelCmd

Namespace: `Mafi.Base.Prototypes.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `primaryFuelId`: game type `ProductProto.ID?`.
  JSON hint: `string or null`.
  Default: `null`.
  null to clear

## TrainStationModuleClearProductCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `moduleId`: game type `EntityId`.
  JSON hint: `int`.

## TrainStationModuleQuickRemoveProductCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `moduleId`: game type `EntityId`.
  JSON hint: `int`.

## TrainStationModuleSetProductCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `moduleId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.

## TruckConstructionRuleSetCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `truckId`: game type `Proto.ID`.
  JSON hint: `string`.
- `zoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.
- `rule`: game type `TruckConstructionRule`.
  JSON hint: `string`.
  Additional metadata: `{"values": ["None", "OnlyIfOthersCannotReach", "Forbid"]}`.

## TruckJobsAllowCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `truckId`: game type `Proto.ID`.
  JSON hint: `string`.
- `zoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.

## TruckJobsForbidCmd

Namespace: `Mafi.Core.Vehicles`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `truckId`: game type `Proto.ID`.
  JSON hint: `string`.
- `zoneId`: game type `LogisticsZoneId`.
  JSON hint: `int`.

## TryTransformEntityCmd

Namespace: `Mafi.Core.Entities.Static.Commands`. Advertised result: `bool`.

Tries to rotate / flip entity in place. Only applicable to non-constructed ghosts.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `rotate`: game type `bool`.
- `flip`: game type `bool`.

## UnassignVehicleCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `EntityId`.
  JSON hint: `int`.

## UnassignVehicleFromEntityCmd

Namespace: `Mafi.Core.Vehicles.Commands`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `vehicleId`: game type `DynamicEntityProto.ID`.
  JSON hint: `string`.
- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `count`: game type `int`.
  Default: `1`.
- `zoneToAssign`: game type `LogisticsZoneId?`.
  JSON hint: `int or null`.
  Default: `null`.

## UpdateTrainStationArrivalRuleCmd

Namespace: `Mafi.Core.Trains`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `stationId`: game type `EntityId`.
  JSON hint: `int`.
- `productId`: game type `ProductProto.ID`.
  JSON hint: `string`.
- `threshold`: game type `Percent`.
  JSON hint: `number (0.5 is 50%)`.

## WellPumpAlertSetEnabledCmd

Namespace: `Mafi.Core.Factory.Machines`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `wellPumpId`: game type `EntityId`.
  JSON hint: `int`.
- `isEnabled`: game type `bool`.

## WorldMapEntityCancelRepairCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## WorldMapEntityStartRepairCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## WorldMapEntityUpgradeCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.

## WorldMapSettlementAdoptPopsCmd

Namespace: `Mafi.Core.World`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `entityId`: game type `EntityId`.
  JSON hint: `int`.
- `popsCount`: game type `int`.

## ZipperSetForceEvenInputsCmd

Namespace: `Mafi.Core.Factory.Zippers`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `zipperId`: game type `EntityId`.
  JSON hint: `int`.
- `forceEvenInputs`: game type `bool`.

## ZipperSetForceEvenOutputsCmd

Namespace: `Mafi.Core.Factory.Zippers`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `zipperId`: game type `EntityId`.
  JSON hint: `int`.
- `forceEvenOutputs`: game type `bool`.

## ZipperSetPriorityPortsCmd

Namespace: `Mafi.Core.Factory.Zippers`. Advertised result: `bool`.

No description advertised.

### Constructor 1

- `zipperId`: game type `EntityId`.
  JSON hint: `int`.
- `portName`: game type `char`.
  JSON hint: `string of one character`.
- `isPrioritized`: game type `bool?`.
  JSON hint: `bool or null`.
  Default: `null`.
  Acts like toggle if null.
