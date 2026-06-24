# WC-2026-cli
A command-line tool to explore, search, and filter FIFA World Cup 2026 match data — by team, group, stage, or date.
## Data Source
Match data from [openfootball/worldcup.json](https://github.com/openfootball/worldcup.json)
(CC0 1.0 — public domain).


## Current Data Displaying Styles 
1. Fixture info display                                                                                   
        # ╔══════════════════════════════════════════════╗
        # ⚽ Curaçao  vs  Ivory Coast              
        # 🏆 Matchday 15 | Group E
        # 📅 26/06/2026  🕐 01:30 IST
        # 📍 Philadelphia
        # 🟢 Upcoming
        # ╚══════════════════════════════════════════════╝

2. Matches on same Date display 
        # 📅 Matches on 26/06/2026
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 🕐 01:30 IST  |  Curaçao vs Ivory Coast        [Group E | Philadelphia]
        # 🕐 01:30 IST  |  Ecuador vs Germany            [Group E | New York/New Jersey]
        # 🕐 04:30 IST  |  Japan vs Sweden               [Group F | Dallas]
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3. Matches by round display
        # 🏆 Matchday 15
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 📅 26/06/2026  🕐 01:30 IST  |  Curaçao vs Ivory Coast     [Group E]
        # 📅 26/06/2026  🕐 04:30 IST  |  Japan vs Sweden             [Group F]
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4. A teams match schedule display
        #   🏆 Matches for Argentina
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        #   📅 17/06/2026  🕐 07:30 IST  |  Argentina vs Algeria    [Matchday 6 | Kansas City]
        #   📅 23/06/2026  🕐 00:30 IST  |  Argentina vs Austria    [Matchday 12 | Dallas]
        #   📅 28/06/2026  🕐 07:30 IST  |  Jordan vs Argentina     [Matchday 17 | Dallas]
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
