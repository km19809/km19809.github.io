# NEIS 전송용 학생 사진 이름 변경기
## 설명
NEIS 전송을 위해 JPG파일 이름을 일괄 변경하는 프로그램입니다.
모든 동작은 개인정보 보호를 위해 사용자 측에서 처리됩니다.

## 이용 방법
1. 학생 이름과 출석번호가 담긴 엑셀 파일을 준비하고 항목을 지정하세요.
2. 이름 순으로 정렬된 사진을 업로드하세요. 서버로 전송되진 않습니다.
3. 변환을 누르면 이름을 일괄 변경하여 ZIP 파일로 저장합니다.

## 주의사항
- 학생 이름과 출석번호에는 빈 칸이 없어야 합니다.
- 사진은 어떤 이름이든 무관하지만, 반드시 출석번호에 맞게 정렬되어 있어야 합니다.
- 정렬에는 사전순, 대소문자 무시, 자연순 (1,2,3, ... ,11, 21, 31, ... 순) 정렬하나 Windows의 동작과 다를 수 있습니다.

## 사용 기술
- xlsx: XLSX 파일 읽기
- fflate: ZIP 작성
- GPT5.6: 웹 페이지 제작

## 고지사항
모든 클라이언트 측 코드는 비공개 Rust 코드를 ChatGPT를 사용하여 번역하여 작성했습니다.
`neis-renamer`의 모든 코드는, 그리고 neis-renamer 범위에 한정하여, MIT 라이선스를 따릅니다.

## LICENSE
This software was generated with AI assistance.

To the extent that I hold any copyright in this software, I dedicate it to the public domain under The Unlicense.

You may freely use, modify, delete, redistribute, or commercially exploit it without attribution or permission.