class Solution(object):
    def letterCombinations(self, digits):
        # 빈 digits가 들어왔을 때
        if not digits:
            return []
        
        # 딕셔너리화
        num2str_list = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        num2str_dic = {str(i): num2str_list[i] for i in range(10)}
        
        # 변수 설정
        self.results = []
        self.digits = digits
        self.num2str_dic = num2str_dic

        # BT 시작
        self._BT(0, "")
        return self.results

    # BT 함수: 현재 위치, 현재 만든 문자열
    def _BT(self, c_i, c_str):
        # 종료 조건 : 현재 digits의 index가 마지막일 때 
        if c_i == len(self.digits):
            # 결과 저장하고 종료
            self.results.append(c_str)
            return
        
        # 현재 숫자의 문자들 가져오기
        c_digit = self.digits[c_i]
        p_chars = self.num2str_dic[c_digit]
        
        for char in p_chars:
            # 문자 추가하고 탐색
            c_str += char
            self._BT(c_i + 1, c_str)
            # 되돌리기: 추가했던 문자 제거
            c_str = c_str[:-1]
