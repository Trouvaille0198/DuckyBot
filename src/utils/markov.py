import os
import random
import re
import jieba


class Markov():
    def __init__(self, n: int = 1, path: str = '', text_type='English'):
        """
        构建马尔科夫链
        :param n: 阶数, 前缀单词的个数
        :param path: 文本路径
        :param text_type: 文本语言
        """
        self.path = path
        self.type = text_type
        self.n = n
        self.txt = self.get_path()
        self.words = self.text_procession()
        self.words_dict = self.analyze()

    def get_path(self):
        """
        封装保存路径
        """
        path = os.path.join(os.getcwd(), self.path+'.txt')
        if os.path.exists(path):
            with open(path) as txt:
                return txt.read()
        else:
            return ''

    def text_procession(self) -> list:
        """
        文本脏数据处理、分词
        :return: 分词列表
        """
        path = os.path.join(os.getcwd(), self.path+'_segmentation.txt')
        if os.path.exists(path):
            with open(path) as file_obj:
                text = file_obj.read()
                words = text.split(' ')
            return words
        else:
            text = self.txt.replace('\n', ' ').replace(
                '[', ' ').replace(']', ' ')
            r = '[-*#\"\'\\()%“‘’”、（）|=\d<>《》/]+'
            text = re.sub(r, '', text)
            if self.type == 'English':
                for symbol in [',', '.', ':', ';', '?', '!']:
                    text = re.sub('[{}]+'.format(symbol), ' '+symbol+' ', text)
                words = [word.lower().strip()
                         for word in text.split() if not word.isspace()]
            else:
                words = [word.strip()
                         for word in jieba.cut(text) if not word.isspace()]
            return words

    def save_segmentation(self):
        """
        保存分词结果
        """
        path = os.path.join(os.getcwd(), self.path+'_segmentation.txt')
        if not os.path.exists(path):
            with open(path, 'w') as file_obj:
                for word in self.words:
                    file_obj.write(word+' ')

    def analyze(self) -> dict:
        """
        统计后缀词频
        """
        words_dict = {}
        count = len(
            self.words)//self.n if self.n != 1 else len(self.words)//self.n-1

        print('Start analyzing')
        for i in range(count):
            n_words = tuple([self.words[i+j] for j in range(self.n)])
            if n_words not in words_dict:
                words_dict[n_words] = {}

            words_dict[n_words][self.words[i+self.n]] = words_dict[n_words].get(self.words[i+self.n], 0)+1
        return words_dict

    def save_dict(self):
        """
        以字典格式保存后缀词频
        """
        with open(self.path+'_dict_{}.txt'.format(str(self.n)), 'w') as file_obj:
            for key, value in self.words_dict.items():
                for word in key:
                    file_obj.write(word+' ')
                file_obj.write('\n')
                for _key, _value in value.items():
                    file_obj.write('\t\t'+_key+': '+str(_value)+'\n')

    def word_frequency_sum(self, fre_dict: dict) -> int:
        """
        统计后缀总数
        """
        sum = 0
        for word, value in fre_dict.items():
            sum += value
        return sum

    def fetch_suffix(self, fre_dict: dict) -> str:
        """
        按词频概率选取后缀
        :param fre_dict: 单个前后缀字典
        :return: 后缀
        """
        rand_int = random.randint(1, self.word_frequency_sum(fre_dict))
        for word, value in fre_dict.items():
            rand_int -= value
            if rand_int <= 0:
                return word

    def generate(self, length: int = 100, cur_word: str = ''):
        """
        生成随机文本
        :param length: 文本字数
        :param cur_word: 文首词
        :return: 随机文本
        """
        chain = ''
        if not cur_word:
            cur_word = random.choice(list(self.words_dict.keys()))
        else:
            for words_tuple in self.words_dict.keys():
                if cur_word == words_tuple[0]:
                    cur_word = words_tuple
            if not isinstance(cur_word, tuple):  # 若指定单词不存在, 还是在文本中随机寻取
                cur_word = random.choice(list(self.words_dict.keys()))

        print('Start generating')
        for i in range(length):
            for word in cur_word:
                chain += word
                if self.type == 'English':
                    chain += ' '

            # 舍去前缀
            cur_word = self.fetch_suffix(self.words_dict[cur_word])
            key = []
            for words_tuple in self.words_dict.keys():
                if cur_word == words_tuple[0]:
                    key.append(words_tuple)
            cur_word = random.choice(key)

        return chain

    def generate_one_sentence(self):
        cur_word = random.choice(list(self.words_dict.keys()))
        chain = ''
        print('Start generating')
        while True:
            for word in cur_word:
                chain += word
                if chain.endswith(('。', '？', '~', '吗', '啊')) and len(chain) > 10:
                    break
            else:
                # 舍去前缀
                cur_word = self.fetch_suffix(self.words_dict[cur_word])
                key = []
                for words_tuple in self.words_dict.keys():
                    if cur_word == words_tuple[0]:
                        key.append(words_tuple)
                cur_word = random.choice(key)
                continue
            break
        return chain


if __name__ == '__main__':
    eng_mar = Markov(2, r'experiment3\data\whitefang')
    eng_mar.save_dict()
    eng_mar.save_segmentation()

    print(eng_mar.generate(200, "i"))

    # chi_mar = Markov(2, r'experiment3\data\围城', text_type='Chinese')
    # chi_mar.save_segmentation()
    # print(chi_mar.generate(length=2000))
    # with open(r'experiment3\data\wow.txt', 'w') as file_obj:
    #     text = chi_mar.generate(length=20000)
    #     text = text.replace('。', '。\n')
    #     file_obj.write(text + '\n')
    #     print('saved')
