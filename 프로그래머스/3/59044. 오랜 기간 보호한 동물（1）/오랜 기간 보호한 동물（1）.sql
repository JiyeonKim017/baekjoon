-- 풀이
# 아직 입양 못 간 (ins엔 있지만 outs엔 없는)  -> 
# 보호소 가장 오래 있던 동물 3마리
# 보호 시작일 순 정렬

-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I LEFT OUTER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3