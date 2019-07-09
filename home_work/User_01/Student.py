class Student(object):

    def __init__(self, name, age, score_list):
        self.name = name
        self.age = age
        self.score_list = score_list

    def get_name(self):
        return ('student name:%s' % (self.name))

    def get_max_score(self):
        self.score_list.sort()

        return ('name:{},  Max score:{}'.format(self.name, self.score_list[2]))
    def get_min_score(self):
        self.score_list.sort(reverse=True)#降序排序
        return ('name:{},  Min score:{}'.format(self.name, self.score_list[2]))

    def get_avg_score(self):
        score_sum = 0
        for i in range(0, len(self.score_list)):
            score_sum += self.score_list[i]
        return ('name:{}, Average score:{}'.format(self.name, round(score_sum / len(self.score_list))))
s=Student('NAME',12,[90,91,92])
print(s.get_max_score())
print(s.get_min_score())
print(s.get_avg_score())