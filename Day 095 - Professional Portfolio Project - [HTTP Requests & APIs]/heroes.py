heroes_dict = {1: 'Anti-Mage', 2: 'Axe', 3: 'Bane', 4: 'Bloodseeker', 5: 'Crystal Maiden', 6: 'Drow Ranger',
               7: 'Earthshaker', 8: 'Juggernaut', 9: 'Mirana', 10: 'Morphling', 11: 'Shadow Fiend',
               12: 'Phantom Lancer', 13: 'Puck', 14: 'Pudge', 15: 'Razor', 16: 'Sand King', 17: 'Storm Spirit',
               18: 'Sven', 19: 'Tiny', 20: 'Vengeful Spirit', 21: 'Windranger', 22: 'Zeus', 23: 'Kunkka', 25: 'Lina',
               26: 'Lion', 27: 'Shadow Shaman', 28: 'Slardar', 29: 'Tidehunter', 30: 'Witch Doctor', 31: 'Lich',
               32: 'Riki', 33: 'Enigma', 34: 'Tinker', 35: 'Sniper', 36: 'Necrophos', 37: 'Warlock', 38: 'Beastmaster',
               39: 'Queen of Pain', 40: 'Venomancer', 41: 'Faceless Void', 42: 'Wraith King', 43: 'Death Prophet',
               44: 'Phantom Assassin', 45: 'Pugna', 46: 'Templar Assassin', 47: 'Viper', 48: 'Luna',
               49: 'Dragon Knight', 50: 'Dazzle', 51: 'Clockwerk', 52: 'Leshrac', 53: "Nature's Prophet",
               54: 'Lifestealer', 55: 'Dark Seer', 56: 'Clinkz', 57: 'Omniknight', 58: 'Enchantress', 59: 'Huskar',
               60: 'Night Stalker', 61: 'Broodmother', 62: 'Bounty Hunter', 63: 'Weaver', 64: 'Jakiro', 65: 'Batrider',
               66: 'Chen', 67: 'Spectre', 68: 'Ancient Apparition', 69: 'Doom', 70: 'Ursa', 71: 'Spirit Breaker',
               72: 'Gyrocopter', 73: 'Alchemist', 74: 'Invoker', 75: 'Silencer', 76: 'Outworld Devourer', 77: 'Lycan',
               78: 'Brewmaster', 79: 'Shadow Demon', 80: 'Lone Druid', 81: 'Chaos Knight', 82: 'Meepo',
               83: 'Treant Protector', 84: 'Ogre Magi', 85: 'Undying', 86: 'Rubick', 87: 'Disruptor',
               88: 'Nyx Assassin', 89: 'Naga Siren', 90: 'Keeper of the Light', 91: 'Io', 92: 'Visage', 93: 'Slark',
               94: 'Medusa', 95: 'Troll Warlord', 96: 'Centaur Warrunner', 97: 'Magnus', 98: 'Timbersaw',
               99: 'Bristleback', 100: 'Tusk', 101: 'Skywrath Mage', 102: 'Abaddon', 103: 'Elder Titan',
               104: 'Legion Commander', 105: 'Techies', 106: 'Ember Spirit', 107: 'Earth Spirit', 108: 'Underlord',
               109: 'Terrorblade', 110: 'Phoenix', 111: 'Oracle', 112: 'Winter Wyvern', 113: 'Arc Warden',
               114: 'Monkey King', 119: 'Dark Willow', 120: 'Pangolier', 121: 'Grimstroke', 123: 'Hoodwink',
               126: 'Void Spirit', 128: 'Snapfire', 129: 'Mars', 135: 'Dawnbreaker', 136: 'Marci', 137: 'Primal Beast'}

heroes_img = {1: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/antimage.png?',
              2: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/axe.png?',
              3: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/bane.png?',
              4: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/bloodseeker.png?',
              5: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/crystal_maiden.png?',
              6: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/drow_ranger.png?',
              7: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/earthshaker.png?',
              8: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/juggernaut.png?',
              9: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/mirana.png?',
              10: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/morphling.png?',
              11: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/nevermore.png?',
              12: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/phantom_lancer.png?',
              13: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/puck.png?',
              14: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/pudge.png?',
              15: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/razor.png?',
              16: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/sand_king.png?',
              17: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/storm_spirit.png?',
              18: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/sven.png?',
              19: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/tiny.png?',
              20: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/vengefulspirit.png?',
              21: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/windrunner.png?',
              22: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/zuus.png?',
              23: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/kunkka.png?',
              25: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/lina.png?',
              26: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/lion.png?',
              27: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/shadow_shaman.png?',
              28: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/slardar.png?',
              29: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/tidehunter.png?',
              30: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/witch_doctor.png?',
              31: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/lich.png?',
              32: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/riki.png?',
              33: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/enigma.png?',
              34: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/tinker.png?',
              35: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/sniper.png?',
              36: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/necrolyte.png?',
              37: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/warlock.png?',
              38: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/beastmaster.png?',
              39: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/queenofpain.png?',
              40: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/venomancer.png?',
              41: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/faceless_void.png?',
              42: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/skeleton_king.png?',
              43: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/death_prophet.png?',
              44: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/phantom_assassin.png?',
              45: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/pugna.png?',
              46: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/templar_assassin.png?',
              47: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/viper.png?',
              48: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/luna.png?',
              49: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/dragon_knight.png?',
              50: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/dazzle.png?',
              51: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/rattletrap.png?',
              52: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/leshrac.png?',
              53: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/furion.png?',
              54: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/life_stealer.png?',
              55: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/dark_seer.png?',
              56: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/clinkz.png?',
              57: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/omniknight.png?',
              58: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/enchantress.png?',
              59: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/huskar.png?',
              60: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/night_stalker.png?',
              61: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/broodmother.png?',
              62: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/bounty_hunter.png?',
              63: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/weaver.png?',
              64: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/jakiro.png?',
              65: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/batrider.png?',
              66: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/chen.png?',
              67: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/spectre.png?',
              68: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/ancient_apparition.png?',
              69: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/doom_bringer.png?',
              70: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/ursa.png?',
              71: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/spirit_breaker.png?',
              72: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/gyrocopter.png?',
              73: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/alchemist.png?',
              74: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/invoker.png?',
              75: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/silencer.png?',
              76: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/obsidian_destroyer.png?',
              77: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/lycan.png?',
              78: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/brewmaster.png?',
              79: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/shadow_demon.png?',
              80: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/lone_druid.png?',
              81: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/chaos_knight.png?',
              82: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/meepo.png?',
              83: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/treant.png?',
              84: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/ogre_magi.png?',
              85: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/undying.png?',
              86: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/rubick.png?',
              87: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/disruptor.png?',
              88: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/nyx_assassin.png?',
              89: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/naga_siren.png?',
              90: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/keeper_of_the_light.png?',
              91: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/wisp.png?',
              92: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/visage.png?',
              93: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/slark.png?',
              94: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/medusa.png?',
              95: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/troll_warlord.png?',
              96: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/centaur.png?',
              97: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/magnataur.png?',
              98: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/shredder.png?',
              99: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/bristleback.png?',
              100: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/tusk.png?',
              101: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/skywrath_mage.png?',
              102: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/abaddon.png?',
              103: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/elder_titan.png?',
              104: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/legion_commander.png?',
              105: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/techies.png?',
              106: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/ember_spirit.png?',
              107: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/earth_spirit.png?',
              108: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/abyssal_underlord.png?',
              109: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/terrorblade.png?',
              110: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/phoenix.png?',
              111: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/oracle.png?',
              112: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/winter_wyvern.png?',
              113: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/arc_warden.png?',
              114: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/monkey_king.png?',
              119: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/dark_willow.png?',
              120: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/pangolier.png?',
              121: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/grimstroke.png?',
              123: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/hoodwink.png?',
              126: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/void_spirit.png?',
              128: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/snapfire.png?',
              129: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/mars.png?',
              135: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/dawnbreaker.png?',
              136: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/marci.png?',
              137: 'https://api.opendota.com/apps/dota2/images/dota_react/heroes/primal_beast.png?'}
