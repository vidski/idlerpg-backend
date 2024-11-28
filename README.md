Apps
- skills
  - eg mining, woodcutting, fishing
- actions
  - eg fishing for fish X or mine for ore Y
- equipment
    - eg pickaxe, axe, fishing rod 
- inventory
  - items
- market
  - buy/sell items
- pets
- quests
- stats
  - eg amount of fish caught, amount of ore mined


endpoints:
- getUser
  - returns user state


- stopAction
  - stops current action
  - returns user state
- startAction
  - starts action
    - actionId: string
    - skillId: string
      - amount: number
  - returns user state


- equipItem
  - equips item
    - itemId: string
    - equipmentId: string
    - amount: number
- unequipItem
  - unequips item
    - equipmentId: string


- claimQuest
  - claims quest reward
    - questId: string
  - returns user state


- buyMerchantItem
  - buys item from merchant
    - itemId: string
    - quantity: number
  - returns OK (zustand increase item in inventory)


- getGuilds
  - returns guilds
- joinGuild
- leaveGuild
- createGuild
- getGuild


- getLeaderboards


- time
    - returns current server time