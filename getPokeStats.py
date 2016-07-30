import argparse
from pgoapi import pgoapi

parser = argparse.ArgumentParser()
parser.add_argument("login_name")
parser.add_argument("password")
parser.add_argument("service", help="ptc or google")
parser.add_argument("lat")
parser.add_argument("long")
args = parser.parse_args()

pokemon_list = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","NidoranF","Nidorina","Nidoqueen","NidoranM","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
move_list = {'0': 'MOVE_UNSET','1': 'THUNDER_SHOCK','2': 'QUICK_ATTACK','3': 'SCRATCH','4': 'EMBER','5': 'VINE_WHIP','6': 'TACKLE','7': 'RAZOR_LEAF','8': 'TAKE_DOWN','9': 'WATER_GUN','10': 'BITE','11': 'POUND','12': 'DOUBLE_SLAP','13': 'WRAP','14': 'HYPER_BEAM','15': 'LICK','16': 'DARK_PULSE','17': 'SMOG','18': 'SLUDGE','19': 'METAL_CLAW','20': 'VICE_GRIP','21': 'FLAME_WHEEL','22': 'MEGAHORN','23': 'WING_ATTACK','24': 'FLAMETHROWER','25': 'SUCKER_PUNCH','26': 'DIG','27': 'LOW_KICK','28': 'CROSS_CHOP','29': 'PSYCHO_CUT','30': 'PSYBEAM','31': 'EARTHQUAKE','32': 'STONE_EDGE','33': 'ICE_PUNCH','34': 'HEART_STAMP','35': 'DISCHARGE','36': 'FLASH_CANNON','37': 'PECK','38': 'DRILL_PECK','39': 'ICE_BEAM','40': 'BLIZZARD','41': 'AIR_SLASH','42': 'HEAT_WAVE','43': 'TWINEEDLE','44': 'POISON_JAB','45': 'AERIAL_ACE','46': 'DRILL_RUN','47': 'PETAL_BLIZZARD','48': 'MEGA_DRAIN','49': 'BUG_BUZZ','50': 'POISON_FANG','51': 'NIGHT_SLASH','52': 'SLASH','53': 'BUBBLE_BEAM','54': 'SUBMISSION','55': 'KARATE_CHOP','56': 'LOW_SWEEP','57': 'AQUA_JET','58': 'AQUA_TAIL','59': 'SEED_BOMB','60': 'PSYSHOCK','61': 'ROCK_THROW','62': 'ANCIENT_POWER','63': 'ROCK_TOMB','64': 'ROCK_SLIDE','65': 'POWER_GEM','66': 'SHADOW_SNEAK','67': 'SHADOW_PUNCH','68': 'SHADOW_CLAW','69': 'OMINOUS_WIND','70': 'SHADOW_BALL','71': 'BULLET_PUNCH','72': 'MAGNET_BOMB','73': 'STEEL_WING','74': 'IRON_HEAD','75': 'PARABOLIC_CHARGE','76': 'SPARK','77': 'THUNDER_PUNCH','78': 'THUNDER','79': 'THUNDERBOLT','80': 'TWISTER','81': 'DRAGON_BREATH','82': 'DRAGON_PULSE','83': 'DRAGON_CLAW','84': 'DISARMING_VOICE','85': 'DRAINING_KISS','86': 'DAZZLING_GLEAM','87': 'MOONBLAST','88': 'PLAY_ROUGH','89': 'CROSS_POISON','90': 'SLUDGE_BOMB','91': 'SLUDGE_WAVE','92': 'GUNK_SHOT','93': 'MUD_SHOT','94': 'BONE_CLUB','95': 'BULLDOZE','96': 'MUD_BOMB','97': 'FURY_CUTTER','98': 'BUG_BITE','99': 'SIGNAL_BEAM','100': 'X_SCISSOR','101': 'FLAME_CHARGE','102': 'FLAME_BURST','103': 'FIRE_BLAST','104': 'BRINE','105': 'WATER_PULSE','106': 'SCALD','107': 'HYDRO_PUMP','108': 'PSYCHIC','109': 'PSYSTRIKE','110': 'ICE_SHARD','111': 'ICY_WIND','112': 'FROST_BREATH','113': 'ABSORB','114': 'GIGA_DRAIN','115': 'FIRE_PUNCH','116': 'SOLAR_BEAM','117': 'LEAF_BLADE','118': 'POWER_WHIP','119': 'SPLASH','120': 'ACID','121': 'AIR_CUTTER','122': 'HURRICANE','123': 'BRICK_BREAK','124': 'CUT','125': 'SWIFT','126': 'HORN_ATTACK','127': 'STOMP','128': 'HEADBUTT','129': 'HYPER_FANG','130': 'SLAM','131': 'BODY_SLAM','132': 'REST','133': 'STRUGGLE','134': 'SCALD_BLASTOISE','135': 'HYDRO_PUMP_BLASTOISE','136': 'WRAP_GREEN','137': 'WRAP_PINK','200': 'FURY_CUTTER_FAST','201': 'BUG_BITE_FAST','202': 'BITE_FAST','203': 'SUCKER_PUNCH_FAST','204': 'DRAGON_BREATH_FAST','205': 'THUNDER_SHOCK_FAST','206': 'SPARK_FAST','207': 'LOW_KICK_FAST','208': 'KARATE_CHOP_FAST','209': 'EMBER_FAST','210': 'WING_ATTACK_FAST','211': 'PECK_FAST','212': 'LICK_FAST','213': 'SHADOW_CLAW_FAST','214': 'VINE_WHIP_FAST','215': 'RAZOR_LEAF_FAST','216': 'MUD_SHOT_FAST','217': 'ICE_SHARD_FAST','218': 'FROST_BREATH_FAST','219': 'QUICK_ATTACK_FAST','220': 'SCRATCH_FAST','221': 'TACKLE_FAST','222': 'POUND_FAST','223': 'CUT_FAST','224': 'POISON_JAB_FAST','225': 'ACID_FAST','226': 'PSYCHO_CUT_FAST','227': 'ROCK_THROW_FAST','228': 'METAL_CLAW_FAST','229': 'BULLET_PUNCH_FAST','230': 'WATER_GUN_FAST','231': 'SPLASH_FAST','232': 'WATER_GUN_FAST_BLASTOISE','233': 'MUD_SLAP_FAST','234': 'ZEN_HEADBUTT_FAST','235': 'CONFUSION_FAST','236': 'POISON_STING_FAST','237': 'BUBBLE_FAST','238': 'FEINT_ATTACK_FAST','239': 'STEEL_WING_FAST','240': 'FIRE_FANG_FAST','241': 'ROCK_SMASH_FAST',}

pokeapi = pgoapi.PGoApi()
login_name = args.login_name
password = args.password
service = args.service
lat = args.lat
long = args.long

pokeapi.login(service, login_name, password, float(lat), float(long), 10)
pokeapi.get_inventory()
request = pokeapi.create_request()
request.get_inventory()
response = request.call()
items = response['responses']['GET_INVENTORY']['inventory_delta']['inventory_items']

print("Nickname, Species, CP, Attack IV, Defense IV, Stamina IV, Percent, Move 1, Move 2")
for item in items:
    if 'pokemon_data' in item['inventory_item_data']:
        # Eggs are treated as pokemon by Niantic.
         if 'is_egg' not in item['inventory_item_data']['pokemon_data']:
            pokedata = item['inventory_item_data']['pokemon_data']
            attack_IV = pokedata.get('individual_attack', 0)
            defense_IV = pokedata.get('individual_defense', 0)
            stamina_IV = pokedata.get('individual_stamina', 0)
            percent = float(attack_IV + defense_IV + stamina_IV)/45. * 100.
            percent = "%.2f" % percent
            cp = str(pokedata.get('cp', 0))
            species = pokemon_list[int(pokedata.get('pokemon_id', 0))-1]
            nickname = pokedata.get('nickname', 'no_nickname')
            move1 = pokedata.get('move_1', 0)
            move2 = pokedata.get('move_2', 0)
            move1 = move_list[str(move1)].replace("_FAST","")
            move2 = move_list[str(move2)]
            print("%s,%s,%s,%s,%s,%s,%s,%s,%s" %(nickname, species, cp, str(attack_IV), str(defense_IV), str(stamina_IV), str(percent), move1, move2))         
