-- 코드를 입력하세요
SELECT B.user_id,B.nickname
,concat(B.city,' ',B.street_address1,' ',B.street_address2) AS 전체주소
,concat(LEFT(tlno,3), '-', MID(tlno,4,4),'-', RIGHT(tlno,4)) AS 전화번호
FROM used_goods_board A join used_goods_user B ON A.writer_id = B.user_id
GROUP BY writer_id
HAVING count(writer_id) >= 3
ORDER BY B.user_id DESC