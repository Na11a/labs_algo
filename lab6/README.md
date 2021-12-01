# Algorithms part 3 Lab 4 wchain
## Task
![task image](https://github.com/thefreekley/Lab4-Algo3/blob/dev/task.png)

---

	
## words.py
##Words
### def counter
1.Перебирає посортований ліст слів якій був заданий в in файлі, визиває функцію count_chain та підраховує максимальний ланцюжок із слів

```python
      def counter(self,visible = False):
        if(visible):print('-----------------------CHAIN-----------------------')
        for word in self.list_words:
            len_chain = self.count_chain(word,visible)
            if len_chain > self.max_chain:
                self.max_chain = len_chain
                self.best_word = word
        if (visible): print('---------------------------------------------------')
```
### def count_chain
2. Цикл забирає по одній букві із заданого в  counter слові і,перебираючи слово, алгоритм шукає в словнику  self.chain_words слово яке збігається із можливим новоутвореним словом.
У випадку якщо в любій комбінації букв такого слова немає, ми вказуємо в словнику до цього слова що максимальна довжина ланцюга із слів з цим 
словом буде сягати 2. Якщо ж слово є, алгоритм бере це слово, через словник дізнається яка максимальна можлива довжина ланцюга з цим словом і якщо це самий найкращий варіант
серед інших можливих слів, ця довжина присвоюється як нова довжина ланцюга із цим слова.
```python
         def count_chain(self,word,visible):
        len_chain = 1
        past_word =''

        for index in range(0, len(word)):
            possible_word = word[:index] + word[index + 1:]
            if possible_word in self.chain_words:
                if len_chain < self.chain_words[possible_word]:
                    len_chain =  self.chain_words[possible_word]
                    past_word = possible_word

        self.example[word] = past_word
        if visible :self.visible(word)
        self.chain_words[word] = len_chain + 1
        return len_chain
```


---
# Іnstalation
## Для реквестів:git clone https://github.com/thefreekley/Lab4-Algo3.git
## Для запуску: python main.py
