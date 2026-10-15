-- LEGIONFORGE 7.3.5.26124 - [102] Final cleanup of verified orphan data.
-- Unsupported BfA loot spells and copied disenchant rows are removed/disabled
-- by sql/103_legionforge_remove_unsupported_content.sql. No substitute drops
-- or guessed loot tables are inserted by this file.
-- Target: WORLD database. Idempotent (safe to re-run).
-- =====================================================================

-- ---------------------------------------------------------------------
-- [102-1] spell_loot_template: "Entry N isn't spell id (random item
-- creating) and not referenced from loot, and thus useless."
-- These Entries are NOT spells at all -> the row is dead weight -> DELETE
-- is the correct remedy here.
-- ---------------------------------------------------------------------
DELETE FROM `spell_loot_template`
 WHERE `Entry` IN (263148, 263149, 263150, 263151, 263152, 263153, 263154);

-- ---------------------------------------------------------------------
-- [102-2] reference_loot_template: "Entry N isn't reference id and not
-- referenced from loot, and thus useless." Same reasoning -> DELETE.
-- ---------------------------------------------------------------------
DELETE FROM `reference_loot_template`
 WHERE `Entry` IN (210020, 210021, 210022, 210023, 210024, 210025,
                   210026, 210027, 210028, 210029);

-- ---------------------------------------------------------------------
-- [102-4] achievement_reward rows with neither a title nor an item reward
-- ("does not contain title or item reward data. Ignored."). The core skips
-- them at every boot; the rows are unusable as they stand.
-- ---------------------------------------------------------------------
-- Column names verified against AchievementMgr.cpp:
--   SELECT entry, title_A, title_H, item, sender, subject, text, mailTemplate
--   FROM achievement_reward
DELETE FROM `achievement_reward`
 WHERE `entry` IN (13, 2398, 3636, 4400, 5863, 6131, 7853,
                   8820, 9496, 10058, 10741, 11210, 11211, 11848)
   AND COALESCE(`title_A`, 0) = 0
   AND COALESCE(`title_H`, 0) = 0
   AND COALESCE(`item`, 0) = 0;

-- ---------------------------------------------------------------------
-- [102-5] gossip_menu 11061 points at a non-existing TextId 15442.
-- Re-point it to the first text id that really exists for this menu, and
-- drop the row only if there is no usable text at all.
-- ---------------------------------------------------------------------
SET @lf_fallback_text := (SELECT MIN(`ID`) FROM `npc_text` WHERE `ID` > 0);

UPDATE `gossip_menu`
   SET `TextId` = @lf_fallback_text
 WHERE `MenuId` = 11061
   AND `TextId` = 15442
   AND @lf_fallback_text IS NOT NULL
   AND NOT EXISTS (SELECT 1 FROM `npc_text` n WHERE n.`ID` = 15442);

DELETE FROM `gossip_menu`
 WHERE `MenuId` = 11061
   AND `TextId` = 15442
   AND @lf_fallback_text IS NULL;

-- ---------------------------------------------------------------------
-- [102-6] Creature 130758 has UNIT_NPC_FLAG_SPELLCLICK but no spellclick
-- data (the core strips the flag at every boot). Strip it in the DB so the
-- warning disappears and the template matches the actual behaviour.
-- UNIT_NPC_FLAG_SPELLCLICK = 0x01000000 = 16777216.
-- ---------------------------------------------------------------------
UPDATE `creature_template`
   SET `npcflag` = `npcflag` & ~16777216
 WHERE `entry` = 130758
   AND (`npcflag` & 16777216) <> 0
   AND NOT EXISTS (SELECT 1 FROM `npc_spellclick_spells` s WHERE s.`npc_entry` = 130758);

-- =====================================================================
-- Intentionally NOT touched (cosmetic / safe):
--   * "areatrigger ... wrong spawn mask ... unsupported difficulty modes"
--     - the core already indexes spawnMasks by map id
--       (AreaTriggerDataStore.cpp); changing live masks could break
--       difficulty-specific triggers.
--   * SmartAIMgr "Kill Credit / creature summon" notices - they describe
--     normal script data, not broken rows.
--   * WaypointMovementGenerator "doesn't have waypoint path id" - a few
--     spawns reference empty paths; they simply stand still.
--   * BfA/test dungeon templates outside this Legion-only release are removed
--     only when their exact IDs are identified in SQL 100/103; no guessed IDs.
-- =====================================================================
