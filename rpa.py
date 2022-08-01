# -*- coding: utf-8 -*-
"""
RPA Workflow / main application

@author: python-rpa-dev

Date        Author          Info
-------------------------------------------------------------------------------
2022.06.20  python-rpa-dev  Initial Version
2022.06.29  python-rpa-dev  Set loglevel with environment variable RPA_LOGLEVEL
                            see https://powerfulpython.com/blog/nifty-python-logging-trick/
2022.06.29  python-rpa-dev  Add checksum so we can use versioning for data collection etc.

"""

import logging
from pyrpa.lib_config import load_config
from pyrpa.lib_rpa import Robotic_Process_Automation
from pyrpa.lib_secv import gen_checksum
import os
import argparse

logger = logging.getLogger(__name__)


def first_screen():
    """
    for the first scan we allow multiple tries to the
    loading of the initial screen
    imp_pos = find_scaled_image('logo_nexters.png', tries = 10, sleep = 2)
    logger.info('(X/Y) %s:%s (W/H) %s:%s', imp_pos[0].left, imp_pos[0].top, imp_pos[0].width, imp_pos[0].height)

    Step: find nexters logo to lookup browser window
    img_pos, scale = find_and_click('logo_nexters.png', tries = 10, sleep = 2)
    # logger.info('image position %s', img_pos)
    """
    rpa.wait_and_click(['logo_nexters.png'], max_wait=20)  # check for loading screen and ads

    rpa.press('esc', presses=3)  # exit promotion screen

def server_44():
    """
    ----------------------------------------------------------------------
    Step: Change to Server 44
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_server.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_server_change.png'], confidence=0.9)

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_server_down.png'], max_wait=20)

           if rpa.end_of_queue_state():
               rpa.wait_and_click(['btn_server_44.png'], max_wait=1)
               rpa.wait_and_click(['btn_server_select.png'])

        rpa.restore_queue('start_loop')

def server_51():
    """
    ----------------------------------------------------------------------
    Step: Change to Server 51
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_server.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_server_change.png'], confidence=0.9)

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_server_up.png'], max_wait=20)

           if rpa.end_of_queue_state():
               rpa.wait_and_click(['btn_server_51.png'], max_wait=1)
               rpa.wait_and_click(['btn_server_select.png'])

        rpa.restore_queue('start_loop')       
  
def server_90():
    """
    ----------------------------------------------------------------------
    Step: Change to Server 90
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_server.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_server_change.png'], confidence=0.9)

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_server_up.png'], max_wait=20)

           if rpa.end_of_queue_state():
               rpa.wait_and_click(['btn_server_90.png'], max_wait=1)
               rpa.wait_and_click(['btn_server_select.png'])

        rpa.restore_queue('start_loop')       

def daily_bonus():
    """
    ----------------------------------------------------------------------
    Step: get daily bonus
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_daily_bonus.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_daily_bonus_collect.png'], max_wait=5)

    rpa.press('esc', presses=5, interval=0.5)

def chest():
    """
    ----------------------------------------------------------------------
    Step: open chest
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_chest2.png', 'btn_chest3.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_chest_open.png'], max_wait=5)

    rpa.press('esc', presses=5, interval=0.5)


def daily_quests():
    """
    ----------------------------------------------------------------------
    Step: cleanup daily quests
    ----------------------------------------------------------------------
    """

    rpa.wait_and_click(['btn_daily_quests.png'])

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_quest_complete3.png'], max_wait=5)

    rpa.press('esc', presses=5, interval=0.5)


def airship():
    """
    ----------------------------------------------------------------------
    Step: get all airship tasks
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_airship.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['gift_valkyrie.png'])

        if rpa.end_of_queue_state():
            rpa.press('esc', presses=1)

        rpa.wait_and_click(['btn_expeditions_rd.png'])

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_with_rd.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_airship_start.png'])

                if rpa.end_of_queue_state():
                    rpa.wait_and_click(['btn_airship_auto.png'])
                    rpa.wait_and_click(['btn_airship_start2.png'])

                # need to set queue state to start of loop
                rpa.restore_queue('start_loop')

            rpa.press('esc', presses=1)

        rpa.press('esc', presses=5, interval=0.5)

def arena():
    """
    ----------------------------------------------------------------------
    Step: 1st fight in arena
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_arena.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_kattegat.png','btn_kattegat2.png','btn_arena_skoll.png'])

        if rpa.end_of_queue_state():
            rpa.press('esc')
            rpa.wait_and_click(['btn_arena_refresh.png'])

            rpa.restore_queue('start_loop')

    rpa.wait_and_click(['btn_arena_attack.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_arena_battle.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_arena_pause.png'], max_wait=20)

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_arena_skip_battle.png'])
            
    rpa.press('esc', presses=3, interval=0.5)

def arena2():
    """
    ----------------------------------------------------------------------
    Step: 2nd fight in arena
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_arena.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_kattegat.png','btn_kattegat2.png','btn_arena_skoll.png'])

        if rpa.end_of_queue_state():
            rpa.press('esc')
            rpa.wait_and_click(['btn_arena_refresh.png'])

            rpa.restore_queue('start_loop')

    rpa.wait_and_click(['btn_arena_attack.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_arena_battle.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_arena_pause.png'], max_wait=20)

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_arena_skip_battle.png'])
            
    rpa.press('esc', presses=3, interval=0.5)

def grand_arena():
    """
    ----------------------------------------------------------------------
    Step: 1 fight in grand arena
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_grand_arena.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_grand_arena_battle.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_kattegat.png','btn_kattegat2.png','btn_arena_skoll.png'])

        if rpa.end_of_queue_state():
            rpa.press('esc')
            rpa.wait_and_click(['btn_grand_arena_refresh.png'])

            rpa.restore_queue('start_loop')

    
    

    rpa.wait_and_click(['btn_grand_arena_attack.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_grand_arena_next.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_grand_arena_next.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_grand_arena_battle2.png'])

                if rpa.end_of_queue_state():
                     rpa.wait_and_click(['btn_grand_arena_pause.png'], max_wait=20)

                     if rpa.end_of_queue_state():
                         rpa.wait_and_click(['btn_grand_arena_skip.png'])

    rpa.press('esc', presses=3, interval=0.5)
       
def send_presents():
    """
    ----------------------------------------------------------------------
    Step: get all airship tasks
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_gifts.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_gifts_send.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_gifts_send_presents.png'], max_wait=5)

            rpa.press('esc', presses=1)

        rpa.press('esc', presses=3, interval=0.5)


def outland():
    """
    ----------------------------------------------------------------------
    Step: get all outland challenges
    """
    rpa.wait_and_click(['btn_outland.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_outland_reward_rd.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_outland_chests.png'])
            rpa.wait_and_click(['btn_outland_open2.png'])
            rpa.wait_and_click(['btn_outland_exit.png'])
            rpa.wait_and_click(['btn_outland_next.png'])

            rpa.restore_queue('start_loop')

    rpa.wait_and_click(['btn_outland_exit.png'])

    rpa.press('esc', presses=5, interval=0.5)

def mail():
    """
    ----------------------------------------------------------------------
    Step: get all mails
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_mail.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_mail_collect_all.png'], max_wait=15)

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_mail_collect_all2.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_mail_show_all.png'], max_wait=15)

        rpa.press('esc', presses=5, interval=0.5)


def tower():
    """
    ----------------------------------------------------------------------
    Step: get all tower chests (without emeralds)
    """
    rpa.wait_and_click(['btn_tower.png'])

    rpa.save_queue('start_loop')

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_tower_instclear.png'])

        if rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_tower_ch_chests.png'])

        rpa.restore_queue('start_loop')

        while rpa.end_of_queue_state():
           rpa.wait_and_click(['btn_tower_chest.png', 'btn_tower_chest_2.png', 'btn_tower_chest_3.png'], confidence =0.7)
        
           if rpa.end_of_queue_state():
               rpa.wait_and_click(['btn_tower_open.png'])

               if rpa.end_of_queue_state():
                   rpa.wait_and_click(['btn_tower_proceed.png'])
    
    rpa.press('esc', presses=1) # End of tower

    rpa.wait_and_click(['btn_tower_skull.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_tower_exch_skull_coins.png'])

        if rpa.end_of_queue_state():
            rpa.press('esc', presses=1) # Exit collecting coins

    rpa.wait_and_click(['btn_tower_points.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_tower_points_collect.png'])
    
        if rpa.end_of_queue_state():
            rpa.press('esc', presses=1) # Exit collecting points


    rpa.press('esc', presses=5, interval=0.5) # Exit collecting points

def dungeon():
    """
    ----------------------------------------------------------------------
    Step: get oracle cards
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_dungeon.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_dungeon_portal.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_oracle_rd.png'])

            while rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_oracle_claim.png'])

            rpa.wait_and_click(['btn_outland_exit.png'])

        rpa.press('esc', presses=2, interval=0.5)

def divination_cards():
    """
    ----------------------------------------------------------------------
    Step: Use all divination cards
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_dungeon.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_dungeon_portal.png'])

        while rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_divination_battle.png','btn_divination_attack.png','btn_divination_fate.png','btn_divination_savepoint.png','btn_divination_collect.png'], max_wait=15)

        rpa.press('esc', presses=6, interval=0.5)

        
    

def tournament():
    """
    ----------------------------------------------------------------------
    Step: Raid tournament
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_titan_valley.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_tournament.png'])

        rpa.save_queue('start_loop')

        while rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_tournament_raid.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_tournament_raid2.png'])

                if rpa.end_of_queue_state():
                    rpa.wait_and_click(['btn_tournament_ok.png'])

                    if rpa.end_of_queue_state():
                        rpa.wait_and_click(['btn_tournament_claim.png'])
                   

                # need to set queue state to start of loop
        rpa.restore_queue('start_loop')

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_tournament_chest.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_tournament_claim2.png'])

                
    rpa.press('esc', presses=4, interval=0.5)

        

def altar():
    """
    ----------------------------------------------------------------------
    Step: Open Titan Artifact Sphere
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_titan_valley.png'])

    if rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_altar.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_altar_sphere.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_altar_exit.png'])

        rpa.press('esc', presses=5, interval=0.5)

def asgard():
    """
    # ----------------------------------------------------------------------
    # Step: Asgard
    # ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_asgard.png'])

    if rpa.end_of_queue_state():
        # Substep: Cradle of the Stars

        rpa.wait_and_click(['btn_asgard_seer.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_asgard_seer_open.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_outland_exit.png'])

            rpa.press('esc', presses=1)

    # Substep: Guild Raid

    rpa.wait_and_click(['btn_asgard_guild_raid.png'])

    rpa.save_queue('start_loop')

    while rpa.end_of_queue_state():
        rpa.wait_and_click(['btn_asgard_guild_raid_sk1.png'])

        if rpa.end_of_queue_state():
            rpa.wait_and_click(['btn_asgard_guild_raid_start.png'])

            if rpa.end_of_queue_state():
                rpa.wait_and_click(['btn_asgard_guild_raid_battle.png'])

                # wait for auto battle button
                rpa.wait_for_image(['btn_battle_auto.png'], max_wait=15)

                if rpa.end_of_queue_state():
                    rpa.press('esc', presses=1)

                    rpa.wait_and_click(['btn_asgard_guild_raid_skip.png'])
                    rpa.wait_and_click(['btn_asgard_guild_raid_ok.png'])

            rpa.restore_queue('start_loop')

    rpa.restore_queue('start_loop')

    # while rpa.end_of_queue_state():
    #     rpa.wait_and_click(['btn_asgard_guild_raid_sk2.png', 'btn_asgard_guild_raid_sk3.png'])

    #     while rpa.end_of_queue_state():
    #         rpa.wait_and_click(['btn_asgard_guild_raid_start.png'])

    #         while rpa.end_of_queue_state():
    #             rpa.wait_and_click(['btn_asgard_guild_raid_next.png', 'btn_asgard_guild_raid_battle.png', 'btn_asgard_guild_raid_next2.png'])

    #         rpa.save_queue('start_fights')

    #         while rpa.end_of_queue_state():
    #             # wait for auto battle button
    #             rpa.wait_for_image(['btn_battle_auto.png'], max_wait=15)

    #             if rpa.end_of_queue_state():
    #                rpa.press('esc', presses=1)

    #                rpa.wait_and_click(['btn_asgard_guild_raid_skip.png'])

    #                while rpa.end_of_queue_state():
    #                    rpa.wait_and_click(['btn_asgard_guild_raid_ok.png','btn_asgard_guild_raid_next2.png'])

    #                rpa.restore_queue('start_fights')

    #         rpa.restore_queue('start_loop')

    # after we finished all the steps
    rpa.press('esc', presses=3, interval=0.5)


def switch_to_guild():
    """
    ----------------------------------------------------------------------
    Step: switch to guild plane
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_guild.png'])

    # wait until  new plane is displayed
    if rpa.end_of_queue_state():
        rpa.wait_for_image(['btn_to_city.png'], max_wait=30)


def switch_to_city():
    """
    ----------------------------------------------------------------------
    Step: switch to city plane
    ----------------------------------------------------------------------
    """
    rpa.wait_and_click(['btn_to_city.png'])

    # wait until  new plane is displayed
    if rpa.end_of_queue_state():
        rpa.wait_for_image(['btn_guild.png'], max_wait=30)


class CustomLogRecord(logging.LogRecord):
    """ Improve log output for source file and line number """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.origin = f"{self.filename}:{self.lineno}"

def main(ini_file, profile, checksum):
    """ main routine """
    global rpa

    logger.info('RPA client version: %s', checksum)

    app_cfg = load_config(ini_file)
#   tmp_dir = app_cfg['Environment']['tmp_dir']

    rpa = Robotic_Process_Automation(
        name='herowars',
        tmp_dir=app_cfg['Environment']['tmp_dir'],
        scale=float(app_cfg['Environment']['scale']),
        max_wait=float(app_cfg['Environment']['max_wait'])
        )

    # set_tmp_dir(app_cfg['Environment']['tmp_dir'])
    # set_def_scale(float(app_cfg['Environment']['scale']))
    # set_def_max_wait(float(app_cfg['Environment']['max_wait']))

    # init_queue()

    #first_screen()
    #chest()
    #daily_quests()
    #airship()
    #send_presents()
    #outland()
    #mail()
    #switch_to_guild()
    #dungeon()
    #asgard()
    #switch_to_city()
    #daily_quests()

    # repeatable steps, switched to ini file configuration
    for module in app_cfg[profile]["run_daily"].strip().split("\n"):
        globals()[module]()

if __name__ == "__main__":
    RPA_LOGLEVEL = os.environ.get('RPA_LOGLEVEL', 'DEBUG').upper()

    app_chksum = gen_checksum('rpa.py')

    # parse parameters
    parser = argparse.ArgumentParser(description='HW Robot Client')
    parser.add_argument('--version' , action='version', version='%(prog)s rel 1.0.0 (' + app_chksum[0:8] + ')')
    parser.add_argument('--ini-file', required=True, help='Initial parameters file')
    parser.add_argument('--profile', required=True, help='RPA Profile (RPA_<namer>)')
    args = parser.parse_args()

    # setup logging capabilities
    logging.setLogRecordFactory(CustomLogRecord)
    logging.basicConfig(
        format='%(asctime)s [%(origin)-20s] %(levelname)-5s - %(funcName)-20s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S',
        level=RPA_LOGLEVEL
        )

    main(args.ini_file, args.profile, app_chksum)
