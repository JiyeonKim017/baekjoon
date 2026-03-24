SET @hour := -1; -- 변수 선언 (0부터 시작하기 위해 -1로 초기화)

SELECT 
    (@hour := @hour + 1) AS HOUR,
    (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;