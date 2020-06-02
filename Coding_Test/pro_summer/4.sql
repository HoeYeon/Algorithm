SELECT game_users.id                     "USER_ID"
         ,COUNT(DISTINCT purchases.item) "PURCHASE_COUNT"
         ,SUM(NVL(characters.price,0))        "TOTAL_PRICE"
FROM  game_users
          LEFT OUTER JOIN purchases ON
          game_users.id = purchases.user_id
          LEFT OUTER JOIN characters ON
          purchases.item = characters.name
GROUP BY game_users.id
ORDER BY game_users.id