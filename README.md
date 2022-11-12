# Сортировка с помощью деревьев: АВЛ, красно-чёрное, Splay

### Описание

В данном репозитории находится код Python-программы, предоставляющей возможность наглядно сравнить 3 алгоритма
сортировки с использованием различных деревьев:

- Сортировка с использованием AVL-дерева
- Сортировка с использованием Красно-чёрного дерева
- Сортировка с использованием Splay-дерева.

Программа предоставляет возможность сравнить все 3 алгоритма на массивах, имеющих размер n, все элементы которых
находятся в диапазоне [w, q] и находятся в одном из следующих состояний:

- Находятся в хаотичном порядке
- Отсортированы по неубыванию
- Отсортированы по невозрастанию.

![Пример работы](Example.png?raw=true)

### Проведённые эксперименты

Были проведены следующие эксперименты:

- **Эксперимент 1**:  
  Демонстрирует, что в неотсортированном массиве псевдослучайных чисел лучше всего себя показывает алгоритм сортировки,
  использующий Красно-чёрное дерево. Splay-дерево (и тем более АВЛ) оказываются ощутимо хуже при увеличении числа
  элементов n.
  ![Эксперимент 1](Experiment_1.png?raw=true)


- **Эксперимент 2**:  
  Демонстрирует, что в отсортированном по возрастанию массиве псевдослучайных чисел быстрее всего работает сортировка на
  Splay-дереве. Второй по скорости становится сортировка на Красно-чёрном дереве, а АВЛ-сортировка - самая медленная.
  ![Эксперимент 2](Experiment_2.png?raw=true)


- **Эксперимент 1.3**:  
  Ещё раз подтверждает результаты, полученные при проведении эксперимента 2, но уже если массив отсортирован по
  убыванию.
  ![Эксперимент 3](Experiment_3.png?raw=true)

Выводы:

- Сортировку АВЛ-деревом целесообразно использовать только при небольшом количестве элементов
- Если заранее известно, что массив не отсортирован, будет выгоднее применить сортировку Красно-чёрным деревом
- Если же заранее известно об отсортированности массива по возрастанию/убыванию, целесообразнее использование
  сортировки Splay-деревом.

### Источники:

- АВЛ-дерево:
    - https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lec06_code.zip
    - https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec06_orig.pdf
    - https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-6-avl-trees-avl-sort/
    - [Просто о поворотах](https://translated.turbopages.org/proxy_u/en-ru.ru.1bd900c1-633c4683-b5fcc6e4-74722d776562/https/www.freecodecamp.org/news/avl-tree-insertion-rotation-and-balance-factor/)

- Красно-чёрное дерево:
    - https://blog.boot.dev/python/red-black-tree-python/
- Splay-дерево:
    - http://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/

Сопутствующая информация:

- https://progler.ru/blog/krasnoe-chernoe-derevo-protiv-dereva-avl