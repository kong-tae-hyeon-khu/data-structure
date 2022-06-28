# list is linear relationship (선형 관계, 1차원)
# Unsorted List : 자료의 순서나 관계없이 저장.
class UnsortedList:

    def __init__(self) : 
        self.list = ["Empty" * 100]  # Append , Del 과 같은 함수를 이용하지 않고 구현
        self.length = 0
        self.current_pos = -1
        self.max_items = 100 # 저장할 수 있는 자료의 최대 갯수.

    def Insert_item(self, item) :
        if self.length == self.max_items :
            print("List is Full !")
            return
        
        self.list[self.length] = item
        self.length += 1


    def Delete_item(self, item) :
        # 간단하게 파이썬 메소드를 이용할 수도 있다.
        last_item_index = self.length - 1
        for i in range(0, self.length) :
            if self.list[i] == item :
                # 마지막 원소로 대체
                self.list[i] = self.list[last_item_index]
                self.length -= 1 # 길이 줄이기.
                print("삭제 완료.")
                return
        print("삭제할 원소가 없습니다.")
    