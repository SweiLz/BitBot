
class Count21(object):
    def __init__(self):
        self.list_count = []
        self.win_list = [1,5,9,13,17,21]

    def user(self, list_user=None):
        ret_list = []
        if list_user == None:
            ret_list = [1]
        else:
            self.list_count += list_user
            print(">>",list_user)
            # print("##", self.list_count)
            num = ((self.list_count[-1]+3)//4)*4+1-self.list_count[-1]
            if num>3:
                num=1
            # print("$$", num)
            ret_list = list(range(self.list_count[-1]+1,self.list_count[-1]+num+1))
            # print(">>>>>>>>", ret_list)
            # print("count:",len(self.list_count)%3+1)
            # ret_list = [4]
        
        self.list_count += ret_list
        print("<<", ret_list)
        # print("##", self.list_count)

        return ret_list 

# game = Count21()
# game.user([1,2])
# game.user([6,7])
# # game.user([8,9])
# game.user([10,11])
# game.user([14])
# game.user([18,19,20])
# game.run([1,2,3])
# print(list(range(1,22)))

    
