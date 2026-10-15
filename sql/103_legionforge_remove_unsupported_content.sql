-- =====================================================================
-- LEGIONFORGE 7.3.5.26124 - [103] remove unsupported higher-expansion loot.
-- The listed SpellEffect records originate from BfA-era custom client data;
-- the Legion server has no verified source loot tables for them. They are
-- disabled for players, creatures and pets (flags 1|2|4 plus deprecated
-- marker 8, total 15); no invented items are rewarded.
-- The deprecated marker also lets LootMgr skip its "missing spell loot"
-- validation for these deliberately disabled spells.
-- Expansion-only disenchant IDs 180..185 were copied from unrelated rows in
-- an earlier workaround. Delete those fabricated rows; C++ ignores DB2
-- disenchant rows newer than Legion so these items do not receive guessed loot.
-- Safe to run repeatedly.
-- =====================================================================
DELETE FROM `spell_loot_template`
 WHERE `Entry` IN (253113, 253116, 253117, 253118, 253125, 253132, 253135, 253138, 253141, 253144, 253149, 253156, 253157, 253158, 253159, 253160, 253161, 253162, 253165, 253168, 253171, 253174, 253177, 253180, 253183, 253186, 253187, 253188, 253190, 253191, 253192, 255457, 255458, 255459, 255610, 256164, 256217, 256218, 256219, 256220, 256221, 256223, 256245, 256246, 256247, 256248, 256249, 256308, 256323, 256611, 256613, 256622, 256748, 256749, 256750);

DELETE FROM `disenchant_loot_template`
 WHERE `Entry` BETWEEN 180 AND 185;

-- The Magmaw script handles cast spell 88253; 88287 is its damage spell and has no
-- matching DUMMY effect hook. Replace any stale misbinding from the world DB.
DELETE FROM `spell_script_names`
 WHERE `ScriptName` = 'spell_magmaw_massive_crash';
INSERT INTO `spell_script_names` (`spell_id`, `ScriptName`)
VALUES (88253, 'spell_magmaw_massive_crash');

INSERT INTO `disables` (`sourceType`, `entry`, `flags`, `params_0`, `params_1`, `comment`) VALUES
(0, 253113, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253116, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253117, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253118, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253125, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253132, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253135, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253138, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253141, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253144, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253149, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253156, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253157, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253158, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253159, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253160, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253161, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253162, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253165, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253168, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253171, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253174, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253177, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253180, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253183, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253186, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253187, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253188, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253190, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253191, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 253192, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 255457, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 255458, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 255459, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 255610, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256164, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256217, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256218, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256219, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256220, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256221, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256223, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256245, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256246, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256247, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256248, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256249, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256308, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256323, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256611, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256613, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256622, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256748, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256749, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled'),
(0, 256750, 15, '', '', 'LegionForge: unsupported BfA loot spell disabled')
ON DUPLICATE KEY UPDATE
  `flags` = VALUES(`flags`),
  `params_0` = '',
  `params_1` = '',
  `comment` = VALUES(`comment`);

-- Post-checks: all counts should be zero.
SELECT 'Unsupported spell loot templates remain' AS `check`, COUNT(*) AS `remaining`
  FROM `spell_loot_template` WHERE `Entry` IN (253113, 253116, 253117, 253118, 253125, 253132, 253135, 253138, 253141, 253144, 253149, 253156, 253157, 253158, 253159, 253160, 253161, 253162, 253165, 253168, 253171, 253174, 253177, 253180, 253183, 253186, 253187, 253188, 253190, 253191, 253192, 255457, 255458, 255459, 255610, 256164, 256217, 256218, 256219, 256220, 256221, 256223, 256245, 256246, 256247, 256248, 256249, 256308, 256323, 256611, 256613, 256622, 256748, 256749, 256750)
UNION ALL
SELECT 'Unsupported spells missing disable rows', COUNT(*)
  FROM `disables` WHERE `sourceType`=0 AND `entry` IN (253113, 253116, 253117, 253118, 253125, 253132, 253135, 253138, 253141, 253144, 253149, 253156, 253157, 253158, 253159, 253160, 253161, 253162, 253165, 253168, 253171, 253174, 253177, 253180, 253183, 253186, 253187, 253188, 253190, 253191, 253192, 255457, 255458, 255459, 255610, 256164, 256217, 256218, 256219, 256220, 256221, 256223, 256245, 256246, 256247, 256248, 256249, 256308, 256323, 256611, 256613, 256622, 256748, 256749, 256750) AND (`flags` & 15) <> 15
UNION ALL
SELECT 'Fabricated disenchant templates 180-185 remain', COUNT(*)
  FROM `disenchant_loot_template` WHERE `Entry` BETWEEN 180 AND 185
UNION ALL
SELECT 'Magmaw script has a wrong spell binding', COUNT(*)
  FROM `spell_script_names` WHERE `ScriptName`='spell_magmaw_massive_crash' AND `spell_id`<>88253;
