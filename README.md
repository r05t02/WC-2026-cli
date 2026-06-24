# WC-2026-cli
A command-line tool to explore, search, and filter FIFA World Cup 2026 match data — by team, group, stage, or date.

## Data Source
Match data from [openfootball/worldcup.json](https://github.com/openfootball/worldcup.json) (CC0 1.0 — public domain).

## Current Data Displaying Styles

### 1. Fixture info display
```text
 ╔══════════════════════════════════════════════╗
   ⚽ Argentina  vs  Austria
   🏆 Matchday 12  |  Group J
   📅 22/06/2026  🕐  22:30 IST
   📍 Dallas (Arlington)
   🔴 Upcoming match
 ╚══════════════════════════════════════════════╝
```

### 2. Matches on same Date display
```text
   📅 Matches on 25/06/2026

   ──────────────────────────────────────────────────────────────────
   🕐 00:30 IST | Switzerland vs Canada          Group B  Matchday 14  Vancouver
   🕐 00:30 IST | Bosnia & Herzegovina vs Qatar  Group B  Matchday 14  Seattle
   🕐 03:30 IST | Scotland vs Brazil             Group C  Matchday 14  Miami
   🕐 06:30 IST | Czech Republic vs Mexico       Group A  Matchday 14  Mexico City
   ──────────────────────────────────────────────────────────────────
```

### 3. Matches by round display
```text
  🏆  Matchday 4

 ────────────────────────────────────────────────
  📅 14/06/2026  🕐 22:30 IST | Germany vs Curaçao
  📅 15/06/2026  🕐 01:30 IST | Netherlands vs Japan
  📅 15/06/2026  🕐 04:30 IST | Ivory Coast vs Ecuador
 ────────────────────────────────────────────────
```

### 4. Team match schedule display
```text
   🏆 Brazil Fixtures

 ─────────────────────────────────────────────────────────────────────
  📅 14/06/2026  🕐 03:30 IST | Brazil vs Morocco    Matchday 3   New York/NJ
  📅 20/06/2026  🕐 06:00 IST | Brazil vs Haiti       Matchday 9   Philadelphia
  📅 25/06/2026  🕐 03:30 IST | Scotland vs Brazil    Matchday 14  Miami
 ─────────────────────────────────────────────────────────────────────
```