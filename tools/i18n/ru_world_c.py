# -*- coding: utf-8 -*-
# Русские описания настроек worldserver.conf — часть C (остаток, включая семейство AuctionHouseBot.*).
WORLD_C = {
    'AllowTrackBothResources': '1 — разрешить одновременное отслеживание двух ресурсов (например, маны и энергии) на панели.',
    'PlayerStart.AllReputation': '1 — выдать новым персонажам максимальную репутацию со всеми фракциями (для тестов).',
    'PlayerStart.AllSpells': '1 — выдать новым персонажам все заклинания (для тестов).',
    'PlayerStart.MapsExplored': '1 — отметить все карты как исследованные у новых персонажей.',
    'PlayerStart.String': 'Стартовая точка для новых персонажей (строка из таблицы playerstart). Пусто — стандартная.',
    'HonorPointsAfterDuel': 'Количество очков чести, которое получает победитель дуэли.',
    'ResetDuelCooldowns': '1 — сбрасывать все перезарядки заклинаний после окончания дуэли.',
    'ResetDuelHealthMana': '1 — восстанавливать здоровье и ману игроков после окончания дуэли.',
    'AlwaysMaxWeaponSkill': '1 — всегда считать навык владения оружием максимальным (для тестов).',
    'PvPToken.Enable': '1 — включить выдачу PvP-жетонов за победы в PvP.',
    'PvPToken.MapAllowType': 'Типы карт, на которых выдаются PvP-жетоны (битовая маска).',
    'PvPToken.ItemID': 'ID предмета PvP-жетона, который выдаётся как награда.',
    'PvPToken.ItemCount': 'Количество PvP-жетонов, выдаваемых за одно убийство игрока.',
    'NoResetTalentsCost': '1 — сброс талантов бесплатный.',
    'Guild.AllowMultipleGuildMaster': '1 — разрешить в гильдии несколько глав (гильдмастеров).',
    'ShowKickInWorld': '1 — показывать всему миру сообщение, когда игрок кикнут с сервера.',
    'ShowMuteInWorld': '1 — показывать всему миру сообщение о муте игрока.',
    'ShowBanInWorld': '1 — показывать всему миру сообщение о бане игрока.',
    'RecordUpdateTimeDiffInterval': 'Интервал (в миллисекундах) записи времени обновления мира в лог (для диагностики лагов).',
    'MinRecordUpdateTimeDiff': 'Минимальная задержка обновления мира (в миллисекундах), которая записывается в лог.',
    'LevelReq.Trade': 'Минимальный уровень для торговли с другими игроками.',
    'LevelReq.Auction': 'Минимальный уровень для использования аукционного дома.',
    'LevelReq.Mail': 'Минимальный уровень для отправки почты.',
    'PlayerDump.DisallowPaths': 'Пути, по которым запрещено сохранять дампы персонажей (PlayerDump).',
    'PlayerDump.DisallowOverwrite': '1 — запретить перезапись существующего файла дампа персонажа.',
    'UI.ShowQuestLevelsInDialogs': '1 — показывать уровень квеста в диалоговом окне.',
    'Calculate.Creature.Zone.Area.Data': '1 — вычислять зону и район для существ при запуске (дольше запуск, точнее данные).',
    'Calculate.Gameoject.Zone.Area.Data': '1 — вычислять зону и район для игровых объектов при запуске.',
    'NoGrayAggro.Above': 'Уровень, выше которого серые (слабые) мобы не нападают на игрока.',
    'NoGrayAggro.Below': 'Уровень, ниже которого серые (слабые) мобы не нападают на игрока.',
    'PreventRenameCharacterOnCustomization': '1 — запретить смену имени персонажа при изменении внешности.',
    'Creature.CheckInvalidPosition': '1 — проверять и исправлять неверные позиции существ при загрузке.',
    'GameObject.CheckInvalidPosition': '1 — проверять и исправлять неверные позиции игровых объектов при загрузке.',
    'LegacyBuffEnabled': '1 — включить устаревшие баффы для совместимости со старыми клиентами.',
    'pbot': 'Настройка модуля ботов игроков (playerbot): базовый режим работы ботов.',
    'pbotall': 'Настройка модуля ботов игроков: включить ботов для всех аккаунтов.',
    'pbotasl': 'Настройка модуля ботов игроков: автоматически входить ботами в мир при запуске.',
    'pbot_hp': 'Настройка модуля ботов игроков: процент здоровья, при котором бот использует лечение.',

    'AuctionHouseBot.Update.Interval': 'Интервал (в минутах) обновления аукционного бота.',
    'AuctionHouseBot.Seller.Enabled': '1 — включить бота-продавца аукционного дома (выставляет лоты).',
    'AuctionHouseBot.Alliance.Items.Amount.Ratio': 'Множитель количества лотов бота для аукциона Альянса.',
    'AuctionHouseBot.Horde.Items.Amount.Ratio': 'Множитель количества лотов бота для аукциона Орды.',
    'AuctionHouseBot.Neutral.Items.Amount.Ratio': 'Множитель количества лотов бота для нейтрального аукциона.',
    'AuctionHouseBot.MinTime': 'Минимальное время жизни лота бота на аукционе (в минутах).',
    'AuctionHouseBot.MaxTime': 'Максимальное время жизни лота бота на аукционе (в минутах).',
    'AuctionHouseBot.Items.Vendor': '1 — выставлять предметы, которые продаются у торговцев.',
    'AuctionHouseBot.Items.Loot': '1 — выставлять предметы, выпадающие из добычи.',
    'AuctionHouseBot.Items.Misc': '1 — выставлять прочие предметы, не попавшие в другие категории.',
    'AuctionHouseBot.Bind.No': '1 — выставлять предметы, не привязанные к персонажу.',
    'AuctionHouseBot.Bind.Pickup': '1 — выставлять предметы, привязанные при подборе.',
    'AuctionHouseBot.Bind.Equip': '1 — выставлять предметы, привязанные при надевании.',
    'AuctionHouseBot.Bind.Use': '1 — выставлять предметы, привязанные при использовании.',
    'AuctionHouseBot.Bind.Quest': '1 — выставлять предметы, связанные с квестами.',
    'AuctionHouseBot.LockBox.Enabled': '1 — выставлять запертые сундуки (шкатулки).',
    'AuctionHouseBot.ItemsPerCycle.Boost': 'Число лотов за цикл в режиме ускоренного наполнения аукциона.',
    'AuctionHouseBot.ItemsPerCycle.Normal': 'Число лотов за цикл в обычном режиме.',
    'AuctionHouseBot.BuyPrice.Seller': 'Цена покупки у продавца в процентах от базовой цены предмета.',
    'AuctionHouseBot.BidPrice.Min': 'Минимальная стартовая ставка (в процентах от цены выкупа).',
    'AuctionHouseBot.BidPrice.Max': 'Максимальная стартовая ставка (в процентах от цены выкупа).',
    'AuctionHouseBot.Alliance.Price.Ratio': 'Множитель цен бота для аукциона Альянса.',
    'AuctionHouseBot.Horde.Price.Ratio': 'Множитель цен бота для аукциона Орды.',
    'AuctionHouseBot.Neutral.Price.Ratio': 'Множитель цен бота для нейтрального аукциона.',
    'AuctionHouseBot.ItemsPerCycle.Boost': 'Число лотов за цикл в режиме ускоренного наполнения аукциона.',
    'AuctionHouseBot.Items.ItemLevel.Min': 'Минимальный уровень предмета (ilvl) для выставления ботом.',
    'AuctionHouseBot.Items.ItemLevel.Max': 'Максимальный уровень предмета (ilvl) для выставления ботом.',
    'AuctionHouseBot.Items.ReqLevel.Min': 'Минимальный требуемый уровень персонажа для предметов бота.',
    'AuctionHouseBot.Items.ReqLevel.Max': 'Максимальный требуемый уровень персонажа для предметов бота.',
    'AuctionHouseBot.Items.ReqSkill.Min': 'Минимальный требуемый навык для предметов бота.',
    'AuctionHouseBot.Items.ReqSkill.Max': 'Максимальный требуемый навык для предметов бота.',
    'AuctionHouseBot.Class.Misc.Mount.ReqLevel.Min': 'Минимальный требуемый уровень для ездовых животных (маунтов), выставляемых ботом.',
    'AuctionHouseBot.Class.Misc.Mount.ReqLevel.Max': 'Максимальный требуемый уровень для ездовых животных, выставляемых ботом.',
    'AuctionHouseBot.Class.Misc.Mount.ReqSkill.Min': 'Минимальный требуемый навык для ездовых животных, выставляемых ботом.',
    'AuctionHouseBot.Class.Misc.Mount.ReqSkill.Max': 'Максимальный требуемый навык для ездовых животных, выставляемых ботом.',
    'AuctionHouseBot.Class.Glyph.ReqLevel.Min': 'Минимальный требуемый уровень для символов (глифов), выставляемых ботом.',
    'AuctionHouseBot.Class.Glyph.ReqLevel.Max': 'Максимальный требуемый уровень для символов (глифов), выставляемых ботом.',
    'AuctionHouseBot.Class.Glyph.ItemLevel.Min': 'Минимальный уровень предмета для символов (глифов), выставляемых ботом.',
    'AuctionHouseBot.Class.Glyph.ItemLevel.Max': 'Максимальный уровень предмета для символов (глифов), выставляемых ботом.',
    'AuctionHouseBot.Class.TradeGood.ItemLevel.Min': 'Минимальный уровень предмета для товаров ремесла, выставляемых ботом.',
    'AuctionHouseBot.Class.TradeGood.ItemLevel.Max': 'Максимальный уровень предмета для товаров ремесла, выставляемых ботом.',
    'AuctionHouseBot.Class.Container.ItemLevel.Min': 'Минимальный уровень предмета для контейнеров (сумок), выставляемых ботом.',
    'AuctionHouseBot.Class.Container.ItemLevel.Max': 'Максимальный уровень предмета для контейнеров (сумок), выставляемых ботом.',
    'AuctionHouseBot.forceIncludeItems': 'Список ID предметов, которые бот обязательно выставляет на аукцион (через запятую).',
    'AuctionHouseBot.forceExcludeItems': 'Список ID предметов, которые бот никогда не выставляет на аукцион (через запятую).',
    'AuctionHouseBot.Buyer.Enabled': '1 — включить бота-покупателя аукционного дома (покупает лоты игроков).',
    'AuctionHouseBot.Buyer.Alliance.Enabled': '1 — включить бота-покупателя на аукционе Альянса.',
    'AuctionHouseBot.Buyer.Horde.Enabled': '1 — включить бота-покупателя на аукционе Орды.',
    'AuctionHouseBot.Buyer.Neutral.Enabled': '1 — включить бота-покупателя на нейтральном аукционе.',
    'AuctionHouseBot.Buyer.ChanceFactor': 'Общий множитель шанса покупки лота ботом.',
    'AuctionHouseBot.Class.Misc.Mount.ReqLevel.Min': 'Минимальный требуемый уровень для ездовых животных, выставляемых ботом.',
}

# Группы, которые повторяются для каждого класса предметов или качества.
_CLASSES = {
    'Consumable': 'расходуемых предметов', 'Container': 'контейнеров (сумок)', 'Weapon': 'оружия',
    'Gem': 'самоцветов', 'Armor': 'брони', 'Reagent': 'реагентов', 'Projectile': 'снарядов',
    'TradeGood': 'товаров ремесла', 'Generic': 'прочих предметов', 'Recipe': 'рецептов',
    'Quiver': 'колчанов', 'Quest': 'квестовых предметов', 'Key': 'ключей', 'Misc': 'разных предметов',
    'Glyph': 'символов (глифов)',
}
_QUALITY = {
    'Gray': 'серых (плохих)', 'White': 'белых (обычных)', 'Green': 'зелёных (необычных)',
    'Blue': 'синих (редких)', 'Purple': 'фиолетовых (эпических)', 'Orange': 'оранжевых (легендарных)',
    'Yellow': 'жёлтых (артефактов)',
}
for _c, _cn in _CLASSES.items():
    WORLD_C['AuctionHouseBot.Class.%s' % _c] = '1 — выставлять на аукцион предметы категории: %s.' % _cn
    WORLD_C['AuctionHouseBot.Class.%s.Allow.Zero' % _c] = '1 — разрешить выставлять предметы категории %s без стоимости (бесплатные).' % _cn
    WORLD_C['AuctionHouseBot.Class.%s.Price.Ratio' % _c] = 'Множитель цены для категории: %s.' % _cn
    WORLD_C['AuctionHouseBot.Class.RandomStackRatio.%s' % _c] = 'Шанс (в процентах) выставить стак предметов категории: %s.' % _cn
for _q, _qn in _QUALITY.items():
    WORLD_C['AuctionHouseBot.Items.Amount.%s' % _q] = 'Количество выставляемых ботом предметов качества: %s.' % _qn
    WORLD_C['AuctionHouseBot.Items.%s.Price.Ratio' % _q] = 'Множитель цены для предметов качества: %s.' % _qn
    WORLD_C['AuctionHouseBot.Buyer.Baseprice.%s' % _q] = 'Базовая цена, которую бот-покупатель считает нормой для предметов качества: %s.' % _qn
    WORLD_C['AuctionHouseBot.Buyer.ChanceMultiplier.%s' % _q] = 'Множитель шанса покупки бота для предметов качества: %s.' % _qn
WORLD_C['AuctionHouseBot.Items.Vendor'] = '1 — выставлять предметы, которые продаются у торговцев.'
WORLD_C['AuctionHouseBot.Items.Gray.Price.Ratio'] = 'Множитель цены для серых (плохих) предметов.'
WORLD_C['AuctionHouseBot.Items.Amount.Gray'] = 'Количество выставляемых серых (плохих) предметов.'
WORLD_C['AuctionHouseBot.Class.Misc.ItemLevel.Min'] = 'Минимальный уровень предмета для разных предметов, выставляемых ботом.'
WORLD_C['AuctionHouseBot.Class.Misc.ItemLevel.Max'] = 'Максимальный уровень предмета для разных предметов, выставляемых ботом.'
WORLD_C['AuctionHouseBot.Class.Misc.Mount.ReqLevel.Max'] = 'Максимальный требуемый уровень для ездовых животных, выставляемых ботом.'
