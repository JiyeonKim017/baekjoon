-- 풀이
# OUTS 테이블엔 있는데, INS 테이블엔 없는 값 찾기.
# OUTS를 기준으로 INS를 붙여와 INS 정보가 없다면 O.ID와 O.NAME 출력
    # ?? - SQL에서 없으면을 어떻게 확인하지? 

-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O LEFT OUTER JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL