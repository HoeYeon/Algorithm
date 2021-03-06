-- 코드를 입력하세요
SELECT MERCHANTS.ID, MERCHANTS.NAME
FROM MERCHANTS
INNER JOIN CARD_USAGES
ON MERCHANTS.ID = CARD_USAGES.MERCHANT_ID
WHERE CARD_USAGES.CATEGORY = '결제'
GROUP BY MERCHANTS.ID
HAVING COUNT(NAME) > 3
ORDER BY MERCHANTS.ID